import abc
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class Message:
    """Represents a unit of communication within the agentic framework."""
    role: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

class Tool(abc.ABC):
    """Abstract base class for tools that agents can utilize."""
    @abc.abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        pass

class Agent(abc.ABC):
    """Abstract base class defining the interface for an autonomous agent."""
    
    @abc.abstractmethod
    def step(self, messages: List[Message]) -> Message:
        """Processes input messages and returns a single response."""
        pass

class Orchestrator:
    """Manages the lifecycle and interaction between agents and tools."""
    
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.history: List[Message] = []

    def register_agent(self, name: str, agent: Agent) -> None:
        self.agents[name] = agent

    def run_turn(self, agent_name: str, input_text: str) -> Message:
        """Executes a single turn for a specific agent."""
        if agent_name not in self.agents:
            raise ValueError(f"Agent {agent_name} not found.")
        
        msg = Message(role="user", content=input_text)
        self.history.append(msg)
        
        response = self.agents[agent_name].step(self.history)
        self.history.append(response)
        return response