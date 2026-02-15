import time

def get_next_action(state):
    """
    Simulates an LLM reasoning process. 
    In a production environment, this would call OpenAI/Anthropic.
    """
    # Simulate 'thinking' time for the demo
    print("Agent is reasoning...")
    time.sleep(1.5) 
    
    idx = state['current_step_idx']
    plan = state['plan']
    
    # Logic to simulate autonomous decision making based on the plan
    if idx < len(plan):
        current_task = plan[idx]
        
        # Determine which tool to use based on the task name
        if "spec" in current_task.lower():
            tool = "create_specs"
        elif "metric" in current_task.lower() or "data" in current_task.lower():
            tool = "analyze_market_data"
        else:
            tool = "finalize_task"

        return {
            "reasoning": f"Based on the objective to '{state['objective']}', the next logical step is '{current_task}'. I will use the {tool} tool to execute this.",
            "tool": tool,
            "input": f"Simulated output for {current_task}"
        }
    else:
        return {
            "reasoning": "All steps in the initial plan have been executed. Objective met.",
            "tool": "finalize_task",
            "input": "Final Report: Dashboard project ready for deployment."
        }