"""
ExosphereHost Python SDK

A distributed workflow execution framework for building scalable, stateful applications.

This package provides the core components for creating and executing distributed
workflows using a node-based architecture. The main components are:

- Runtime: Manages the execution environment and coordinates with the state manager
- BaseNode: Abstract base class for creating executable nodes
- Status constants: Define the various states in the workflow lifecycle

Example usage:
    from exospherehost import Runtime, BaseNode
    from pydantic import BaseModel

    class SampleNode(BaseNode):
        class Inputs(BaseModel):
            name: str

        class Outputs(BaseModel):
            message: str

        async def execute(self, inputs: Inputs) -> Outputs:
            print(inputs)
            return self.Outputs(message="success")

    runtime = Runtime(
        namespace="SampleNamespace", 
        name="SampleNode"
    )

    runtime.connect([SampleNode()])
    runtime.start()
"""

from ._version import version as __version__
from .runtime import Runtime
from .node.BaseNode import BaseNode
from .statemanager import StateManager
from .signals import PruneSignal, ReQueueAfterSignal
from .models import UnitesStrategyEnum, UnitesModel, GraphNodeModel, RetryStrategyEnum, RetryPolicyModel, StoreConfigModel, CronTrigger

VERSION = __version__

__all__ = ["Runtime", "BaseNode", "StateManager", "VERSION", "PruneSignal", "ReQueueAfterSignal", "UnitesStrategyEnum", "UnitesModel", "GraphNodeModel", "RetryStrategyEnum", "RetryPolicyModel", "StoreConfigModel", "CronTrigger"]
