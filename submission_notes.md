# WorkElate AI Internship - Stateful Execution Agent

##  Overview
I have built a stateful reasoning agent designed to operate as an autonomous "worker" rather than a simple chatbot. The system follows a **Reasoning → Action → Memory** loop, ensuring that every step is logged and the progress is persistent.

---

##  Architecture & Systems Thinking
The project is built with strict modularity to demonstrate an "operational layer" approach:

1.  **State Manager (`state_manager.py`):** Handles persistence. I chose a JSON-based state file (`state.json`) to allow the agent to survive crashes or manual interruptions.
2.  **The Brain (`brain.py`):** Encapsulates the reasoning logic. While currently using a mock reasoning engine for local demonstration, it is architected to be swapped with an LLM via a single function update.
3.  **The Tools (`tools.py`):** A collection of discrete functions the agent can invoke.
4.  **The Loop (`main.py`):** The central controller that coordinates between thinking and acting.

---

##  Meta-Commentary (The "Final Task" Requirements)

### 1. What confused me?
The primary challenge was deciding the level of granularity for the "Memory." I initially considered storing every raw interaction, but I decided to store a structured `decision_history`. This ensures the agent has a "Reasoning Trace" without cluttering the context window with redundant data.

### 2. What would I change about the task?
If given more time, I would implement **Multi-Agent Validation**. Specifically, a "Reviewer Agent" that monitors the "Worker Agent." Before any tool execution is finalized, the Reviewer would verify the output against the original objective to minimize hallucinations or logic drifts.

### 3. What blocker ate the most time?
Handling **State Corruption**. During testing, I encountered `JSONDecodeError` when the script was interrupted exactly during a write operation or when the file was empty. I solved this by implementing a robust `load_state` function that validates file integrity and falls back to a default state if necessary, ensuring the agent never crashes on startup.

---

##  Execution & Testing
- **Stateful Resume:** I verified that killing the process mid-run and restarting it allows the agent to resume from the exact step it left off (e.g., resuming from Step 2 instead of starting over).
- **Traceability:** The terminal output and `state.json` both capture the `reasoning` field, proving the agent isn't just executing code but following a planned logic path.

---

##  How to Run
1. Ensure you have Python 3.12+ installed.
2. Run `python main.py`.
3. Observe the `state.json` file updating in real-time.
