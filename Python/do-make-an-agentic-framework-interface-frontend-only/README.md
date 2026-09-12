# do make an agentic framework interface frontend only

## 💡 Overview & Approach
The goal is to create a decoupled, frontend-only interface for an agentic framework. By utilizing an Abstract Base Class (ABC), we enforce a strict contract that separates the "Agent Logic" (state transitions) from the "Rendering Logic" (UI representation). 

The approach uses a `State` pattern where the `AgentState` acts as the single source of truth. The `AgentInterface` ensures that any agent implementation provides a `render` method (to bridge data to UI frameworks like React or Vue) and a `handle_user_input` method (to manage state transitions). This design allows developers to swap agent behaviors without modifying the frontend rendering pipeline.

## 📊 Complexity Analysis
- **Time Complexity**: O(1) for state updates and rendering, assuming the message history is managed via an append-only structure. If history grows to size N, rendering is O(N).
- **Space Complexity**: O(N), where N is the number of messages stored in the `AgentState` history.

## 🏢 Top Companies Asking This Problem
- OpenAI (Internal tooling)
- Anthropic
- Vercel
- Meta (AI Studio teams)
- Microsoft (Semantic Kernel teams)

## 🚀 Key Features & Edge Cases Handled
- **Decoupling**: The interface is agnostic to the underlying LLM or backend service, making it ideal for local-first or browser-based AI agents.
- **State Immutability**: By using `dataclasses`, we encourage a functional approach to state management, preventing side effects during UI re-renders.
- **Extensibility**: New agent types (e.g., Task-oriented, Persona-based) can be added by simply inheriting from `AgentInterface` without refactoring existing UI components.