# do make an agentic framework interface

## 💡 Overview & Approach
The agentic framework interface is designed using the **Strategy and Command patterns**. By utilizing Python's `abc` (Abstract Base Classes), we enforce a strict contract for `Agent` and `Tool` implementations, ensuring that any developer extending the framework adheres to the expected input/output signatures.

The `Orchestrator` acts as the central hub, maintaining the state of the conversation history and managing agent registration. This decoupled architecture allows for modularity, where agents can be swapped (e.g., switching from a ReAct agent to a Plan-and-Solve agent) without modifying the underlying orchestration logic.

## 📊 Complexity Analysis
- **Time Complexity**: O(N) per turn, where N is the number of messages in the history, assuming the agent's `step` function processes the history linearly.
- **Space Complexity**: O(M * L), where M is the number of messages and L is the average length of each message, representing the memory footprint of the conversation history.

## 🏢 Top Companies Asking This Problem
- OpenAI
- Anthropic
- Google (DeepMind)
- Meta (FAIR)
- Microsoft (Semantic Kernel team)

## 🚀 Key Features & Edge Cases Handled
- **Strict Interface Enforcement**: Uses `abc.abstractmethod` to prevent instantiation of incomplete agent logic.
- **State Management**: The `Orchestrator` maintains a centralized `history` list, ensuring consistency across multi-turn interactions.
- **Extensibility**: The `Tool` interface allows for arbitrary function execution, enabling agents to interact with external APIs, databases, or file systems.
- **Error Handling**: Includes basic validation for agent registration to prevent runtime lookup failures.