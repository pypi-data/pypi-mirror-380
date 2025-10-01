"""
Constraint application functionality for PyPSA networks.

Handles loading and applying custom constraints from the database.
"""

import logging
import pandas as pd
import numpy as np
from typing import Dict, Any, Optional, List

from pyconvexity.models import list_components_by_type, get_attribute

logger = logging.getLogger(__name__)


class ConstraintApplicator:
    """
    Handles loading and applying custom constraints to PyPSA networks.
    
    This class manages both pre-optimization constraints (applied to network structure)
    and optimization-time constraints (applied during solving via extra_functionality).
    """
    
    def apply_constraints(
        self,
        conn,
        network_id: int,
        network: 'pypsa.Network',
        scenario_id: Optional[int] = None,
        constraints_dsl: Optional[str] = None
    ):
        """
        Apply all constraints to the network.
        
        Args:
            conn: Database connection
            network_id: ID of the network
            network: PyPSA Network object
            scenario_id: Optional scenario ID
            constraints_dsl: Optional DSL constraints string
        """
        # Apply database constraints
        self._apply_database_constraints(conn, network_id, network, scenario_id)
        
        # Apply DSL constraints if provided
        if constraints_dsl:
            self._apply_dsl_constraints(network, constraints_dsl)
    
    def _detect_constraint_type(self, constraint_code: str) -> str:
        """
        Detect if constraint is network-modification or model-constraint type.
        
        Args:
            constraint_code: The constraint code to analyze
            
        Returns:
            "model_constraint" or "network_modification"
        """
        # Type 2 indicators (model constraints) - need access to optimization model
        model_indicators = [
            'n.optimize.create_model()',
            'm.variables',
            'm.add_constraints',
            'gen_p =',
            'constraint_expr =',
            'LinearExpression',
            'linopy',
            'Generator-p',
            'lhs <=',
            'constraint_expr =',
            'model.variables',
            'model.add_constraints'
        ]
        
        # Type 1 indicators (network modifications) - modify network directly
        network_indicators = [
            'n.generators.loc',
            'n.add(',
            'n.buses.',
            'n.lines.',
            'network.generators.loc',
            'network.add(',
            'network.buses.',
            'network.lines.'
        ]
        
        # Check for model constraint indicators first (more specific)
        if any(indicator in constraint_code for indicator in model_indicators):
            return "model_constraint"
        elif any(indicator in constraint_code for indicator in network_indicators):
            return "network_modification"
        else:
            # Default to network_modification for safety (existing behavior)
            return "network_modification"

    def _apply_database_constraints(
        self,
        conn,
        network_id: int,
        network: 'pypsa.Network',
        scenario_id: Optional[int]
    ):
        """Load and apply custom constraints from the database in priority order."""
        try:
            # Load all constraints for this network
            constraints = list_components_by_type(conn, network_id, 'CONSTRAINT')
            
            if not constraints:
                return
            
            # Load constraint attributes and filter active ones
            active_constraints = []
            model_constraints = []
            network_constraints = []
            
            for constraint in constraints:
                try:
                    # Get constraint attributes
                    is_active = get_attribute(conn, constraint.id, 'is_active', scenario_id)
                    priority = get_attribute(conn, constraint.id, 'priority', scenario_id)
                    constraint_code = get_attribute(conn, constraint.id, 'constraint_code', scenario_id)
                    
                    # Check if constraint is active
                    if is_active.variant == "Static":
                        # Extract boolean value from StaticValue
                        is_active_bool = False
                        if "Boolean" in is_active.static_value.data:
                            is_active_bool = is_active.static_value.data["Boolean"]
                        
                        if is_active_bool:
                            # Extract code value
                            code_val = ""
                            if constraint_code.variant == "Static":
                                if "String" in constraint_code.static_value.data:
                                    code_val = constraint_code.static_value.data["String"]
                            
                            # Extract priority value
                            priority_val = 0
                            if priority.variant == "Static":
                                if "Integer" in priority.static_value.data:
                                    priority_val = priority.static_value.data["Integer"]
                                elif "Float" in priority.static_value.data:
                                    priority_val = int(priority.static_value.data["Float"])
                            
                            constraint_dict = {
                                'id': constraint.id,
                                'name': constraint.name,
                                'priority': priority_val,
                                'code': code_val,
                                'constraint_code': code_val  # For compatibility
                            }
                            
                            # Detect constraint type and separate them
                            constraint_type = self._detect_constraint_type(code_val)
                            if constraint_type == "model_constraint":
                                model_constraints.append(constraint_dict)
                                logger.info(f"Detected model constraint: {constraint.name}")
                            else:
                                network_constraints.append(constraint_dict)
                                logger.info(f"Detected network constraint: {constraint.name}")
                        
                except Exception as e:
                    logger.warning(f"Failed to load constraint {constraint.name}: {e}")
                    continue
            
            if not model_constraints and not network_constraints:
                return
            
            logger.info(f"Constraint breakdown: {len(model_constraints)} model constraints, {len(network_constraints)} network constraints")
            
            # Apply network constraints first (they modify the network structure)
            if network_constraints:
                network_constraints.sort(key=lambda x: x['priority'])
                for constraint in network_constraints:
                    try:
                        logger.info(f"Executing network constraint '{constraint['name']}' (priority {constraint['priority']})")
                        
                        # Execute the constraint code in the normal Python environment
                        exec_globals = {
                            'n': network,
                            'network': network,
                            'pd': pd,
                            'np': np,
                        }
                        
                        # Execute the constraint code
                        exec(constraint['code'], exec_globals)
                        
                    except Exception as e:
                        error_msg = f"Failed to execute network constraint '{constraint['name']}': {e}"
                        logger.error(error_msg, exc_info=True)
                        # Continue with other constraints instead of failing the entire solve
                        continue
            
            # Apply model constraints (they need access to the optimization model)
            if model_constraints:
                self._apply_model_constraints(network, model_constraints)
                
        except Exception as e:
            logger.error(f"Failed to apply custom constraints: {e}", exc_info=True)
    
    def _apply_model_constraints(self, network: 'pypsa.Network', model_constraints: list):
        """
        Apply model constraints that need access to the optimization model.
        
        This creates the optimization model, applies constraints to it, and then
        replaces PyPSA's solve method to use the pre-constrained model.
        
        Args:
            network: PyPSA Network object
            model_constraints: List of model constraint dictionaries
        """
        try:
            logger.info(f"Applying {len(model_constraints)} model constraints...")
            
            # Create the optimization model (same as PyPSA would do internally)
            logger.info("Creating optimization model for constraint application...")
            model = network.optimize.create_model()
            logger.info(f"Created optimization model with {len(model.variables)} variable groups")
            
            # Sort constraints by priority
            sorted_constraints = sorted(model_constraints, key=lambda x: x['priority'])
            
            # Apply each model constraint
            for constraint in sorted_constraints:
                try:
                    constraint_code = constraint['constraint_code']
                    constraint_name = constraint['name']
                    
                    logger.info(f"Applying model constraint '{constraint_name}' (priority {constraint['priority']})")
                    
                    # Create execution environment with network, model, and utilities
                    exec_globals = {
                        'n': network,
                        'network': network,
                        'model': model,
                        'm': model,
                        'snapshots': network.snapshots,
                        'pd': pd,
                        'np': np,
                        'xr': __import__('xarray'),  # Import xarray for DataArray operations
                    }
                    
                    # Execute the constraint code
                    exec(constraint_code, exec_globals)
                    logger.info(f"Successfully applied model constraint '{constraint_name}'")
                    
                except Exception as e:
                    error_msg = f"Failed to apply model constraint '{constraint.get('name', 'unknown')}': {e}"
                    logger.error(error_msg, exc_info=True)
                    # Continue with other constraints instead of failing
                    continue
            
            # Store the constrained model for the solver to use
            # We'll replace PyPSA's solve_model method to use our pre-constrained model
            logger.info("Replacing PyPSA's solve method to use pre-constrained model...")
            
            # Store original methods
            original_optimize = network.optimize
            original_solve_model = original_optimize.solve_model
            
            # Create a wrapper that uses our pre-constrained model
            def constrained_solve_model(*args, **kwargs):
                """Use the pre-constrained model instead of creating a new one."""
                logger.info("Using pre-constrained model for solve...")
                return original_solve_model(model, *args, **kwargs)
            
            # Replace the solve_model method
            network.optimize.solve_model = constrained_solve_model
            
            logger.info(f"Successfully applied {len(model_constraints)} model constraints")
            
        except Exception as e:
            logger.error(f"Failed to apply model constraints: {e}", exc_info=True)
            # Don't re-raise - let the solve continue without constraints rather than fail completely
    
    def _apply_dsl_constraints(self, network: 'pypsa.Network', constraints_dsl: str):
        """
        Apply DSL constraints to the network.
        
        Args:
            network: PyPSA Network object
            constraints_dsl: DSL constraints string
        """
        try:
            logger.info("Applying DSL constraints")
            logger.debug(f"DSL Code: {constraints_dsl}")
            
            # Execute DSL constraints
            exec_globals = {
                'n': network,
                'network': network,
                'pd': pd,
                'np': np,
            }
            
            exec(constraints_dsl, exec_globals)
            
        except Exception as e:
            logger.error(f"Failed to apply DSL constraints: {e}", exc_info=True)
    
    def get_optimization_constraints(
        self,
        conn,
        network_id: int,
        scenario_id: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Get ALL active constraints for optimization-time application.
        The solver will determine which are model constraints vs network constraints.
        
        Args:
            conn: Database connection
            network_id: ID of the network
            scenario_id: Optional scenario ID
            
        Returns:
            List of all active constraints
        """
        try:
            # Load all constraints for this network
            constraints = list_components_by_type(conn, network_id, 'CONSTRAINT')
            
            if not constraints:
                return []
            
            # Load constraint attributes and filter active ones
            optimization_constraints = []
            for constraint in constraints:
                try:
                    # Get constraint attributes
                    is_active = get_attribute(conn, constraint.id, 'is_active', scenario_id)
                    priority = get_attribute(conn, constraint.id, 'priority', scenario_id)
                    constraint_code = get_attribute(conn, constraint.id, 'constraint_code', scenario_id)
                    
                    # Check if constraint is active
                    if is_active.variant == "Static":
                        # Extract boolean value from StaticValue
                        is_active_bool = False
                        if "Boolean" in is_active.static_value.data:
                            is_active_bool = is_active.static_value.data["Boolean"]
                        
                        if is_active_bool:
                            # Extract code value
                            code_val = ""
                            if constraint_code.variant == "Static":
                                if "String" in constraint_code.static_value.data:
                                    code_val = constraint_code.static_value.data["String"]
                            
                            # Extract priority value
                            priority_val = 0
                            if priority.variant == "Static":
                                if "Integer" in priority.static_value.data:
                                    priority_val = priority.static_value.data["Integer"]
                                elif "Float" in priority.static_value.data:
                                    priority_val = int(priority.static_value.data["Float"])
                            
                            optimization_constraints.append({
                                'id': constraint.id,
                                'name': constraint.name,
                                'priority': priority_val,
                                'constraint_code': code_val,  # Use consistent key name
                                'code': code_val  # Keep both for compatibility
                            })
                        
                except Exception as e:
                    logger.warning(f"Failed to load constraint {constraint.name}: {e}")
                    continue
            
            # Sort constraints by priority (lower numbers first)
            optimization_constraints.sort(key=lambda x: x['priority'])
            return optimization_constraints
            
        except Exception as e:
            logger.error(f"Failed to get optimization constraints: {e}", exc_info=True)
            return []
    
    def apply_optimization_constraints(
        self,
        network: 'pypsa.Network',
        snapshots,
        constraints: List[Dict[str, Any]]
    ):
        """
        Apply constraints during optimization (called via extra_functionality).
        
        Args:
            network: PyPSA Network object
            snapshots: Network snapshots
            constraints: List of constraint dictionaries
        """
        try:
            for constraint in constraints:
                try:
                    logger.info(f"Applying optimization constraint '{constraint['name']}' (priority {constraint['priority']})")
                    logger.debug(f"Code: {constraint['code']}")
                    
                    # Execute the constraint code with network and snapshots available
                    exec_globals = {
                        'net': network,
                        'network': network,
                        'n': network,
                        'snapshots': snapshots,
                        'pd': pd,
                        'np': np,
                    }
                    
                    # Execute the constraint code
                    exec(constraint['code'], exec_globals)
                    
                except Exception as e:
                    error_msg = f"Failed to execute optimization constraint '{constraint['name']}': {e}"
                    logger.error(error_msg, exc_info=True)
                    # Continue with other constraints instead of failing the entire solve
                    continue
                    
        except Exception as e:
            logger.error(f"Failed to apply optimization constraints: {e}", exc_info=True)
    
    def apply_optimization_constraint(
        self,
        network: 'pypsa.Network',
        snapshots,
        constraint: Dict[str, Any]
    ):
        """
        Apply a single optimization constraint during solve.
        
        Args:
            network: PyPSA Network object
            snapshots: Network snapshots
            constraint: Single constraint dictionary
        """
        try:
            logger.info(f"Applying optimization constraint '{constraint.get('name', 'unknown')}' (priority {constraint.get('priority', 0)})")
            logger.debug(f"Code: {constraint.get('code', '')}")
            
            # Execute the constraint code with network and snapshots available
            exec_globals = {
                'net': network,
                'network': network,
                'n': network,
                'snapshots': snapshots,
                'pd': pd,
                'np': np,
                'xr': __import__('xarray'),
            }
            
            # Execute the constraint code
            exec(constraint.get('code', ''), exec_globals)
            
        except Exception as e:
            error_msg = f"Failed to execute optimization constraint '{constraint.get('name', 'unknown')}': {e}"
            logger.error(error_msg, exc_info=True)
            raise  # Re-raise so solver can handle it