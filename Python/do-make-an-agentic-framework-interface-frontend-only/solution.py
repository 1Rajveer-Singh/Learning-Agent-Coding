import abc
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class AgentState:
    """Represents the current snapshot of the agent's memory and context."""
    messages: List[Dict[str, str]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

class AgentInterface(abc.ABC):
    """
    Abstract Base Class defining the contract for a frontend-only agentic framework.
    This interface ensures that any agent implementation remains decoupled from 
    backend execution logic, focusing purely on state management and UI interaction.
    """

    @abc.abstractmethod
    def render(self, state: AgentState) -> Any:
        """Transforms the current agent state into a frontend-renderable format."""
        pass

    @abc.abstractmethod
    def handle_user_input(self, input_text: str) -> AgentState:
        """Processes user interaction and returns the updated state."""
        pass

class SimpleChatAgent(AgentInterface):
    """A concrete implementation of a frontend-focused chat agent."""

    def __init__(self, name: str):
        self.name = name
        self.state = AgentState()

    def render(self, state: AgentState) -> Dict[str, Any]:
        """Returns a JSON-serializable representation for frontend components."""
        return {
            "agent_name": self.name,
            "history": state.messages,
            "status": "ready"
        }

    def handle_user_input(self, input_text: str) -> AgentState:
        """Updates internal state based on user input."""
        self.state.messages.append({"role": "user", "content": input_text})
        # Logic for frontend-only state transition
        self.state.messages.append({"role": "assistant", "content": f"Echo: {input_text}"})
        return self.state