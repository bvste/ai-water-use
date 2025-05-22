# AI Water Usage Estimator Based on Prompt Text

def estimate_water_usage(prompt, liters_per_prompt=0.519):
    global bottles
    """
    Estimate water usage based on prompt length.
    Longer prompts slightly increase compute, so we scale liters based on char.
    """
    avg_chars = 100  # Assume 100 characters = normal-sized prompt
    prompt_length = len(prompt)
    
    scaling_factor = prompt_length / avg_chars
    estimated_liters = scaling_factor * liters_per_prompt
    bottles = estimated_liters
    
    return estimated_liters

# === Shell Loop ===
print("AI Prompt Water Usage Estimator")
print("Type 'exit' to quit.\n")

while True:
    user_prompt = input("Enter your AI prompt: ")
    
    if user_prompt.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break
    
    water_used = estimate_water_usage(user_prompt)
    
    print(f"Estimated water used: {water_used:.4f} liters")
    print(f"This is about {(bottles/0.5):.2f} bottles of 500 ml water.\n")
