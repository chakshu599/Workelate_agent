from state_manager import load_state, save_state
from brain import get_next_action
from tools import TOOL_MAP

def run_agent():
    state = load_state()
    
    while state['current_step_idx'] < 5: # Limit steps for safety
        print(f"--- Step {state['current_step_idx']} ---")
        
        # 1. THINK
        decision = get_next_action(state)
        print(f"Reasoning: {decision['reasoning']}")
        
        # 2. ACT
        tool_to_call = TOOL_MAP.get(decision['tool'])
        result = tool_to_call(decision['input'])
        
        # 3. UPDATE STATE
        state['decision_history'].append({
            "step": state['current_step_idx'],
            "reasoning": decision['reasoning'],
            "result": result
        })
        state['current_step_idx'] += 1
        save_state(state)
        
        if decision['tool'] == "finalize_task":
            break

if __name__ == "__main__":
    run_agent()