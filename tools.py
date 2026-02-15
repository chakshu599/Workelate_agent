def create_specs(topic):
    # Logic to simulate writing a spec
    return f"Technical specifications for {topic} generated."

def analyze_market_data(input_data):
    # Logic to simulate data processing
    return f"Analysis complete for: {input_data}. Metrics: 85% growth potential."

def finalize_task(summary):
    return f"Project Finalized: {summary}"

# Map of available tools for the LLM
TOOL_MAP = {
    "create_specs": create_specs,
    "analyze_market_data": analyze_market_data,
    "finalize_task": finalize_task
}