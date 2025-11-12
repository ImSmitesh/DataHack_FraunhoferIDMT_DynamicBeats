def generate_skating_music_prompt(moves_json):
    """Generate a detailed music prompt from figure skating moves"""
    
    move_descriptions = {
        "3Axel": "powerful and dramatic with strong brass accents and building tension",
        "2Axel": "energetic and dynamic with crisp percussion and ascending melodies",
        "FlyCamelSpin4": "graceful and flowing with smooth strings and elegant harmonies",
        "FlyingSpin": "light and airy with floating melodies",
        "CamelSpin": "smooth and lyrical with gentle orchestration"
    }
    
    # Build the prompt
    prompt_parts = ["Epic orchestral figure skating program music with"]
    
    for i, move in enumerate(moves_json):
        move_name = move["move"]
        time = move["mean_time"]
        
        description = move_descriptions.get(
            move_name, 
            "expressive and athletic movement"
        )
        
        prompt_parts.append(f"{description} at {int(time)} seconds")
        
        if i < len(moves_json) - 1:
            prompt_parts.append(",")
    
    return " ".join(prompt_parts)

# Usage
moves_data = [
    {"move": "3Axel", "start_time": 16.67, "end_time": 33.33, "mean_time": 25.0},
    {"move": "FlyCamelSpin4", "start_time": 33.33, "end_time": 50.0, "mean_time": 41.5},
    {"move": "2Axel", "start_time": 66.67, "end_time": 83.33, "mean_time": 75.0},
    {"move": "FlyCamelSpin4", "start_time": 83.33, "end_time": 100.0, "mean_time": 91.5},
    {"move": "3Axel", "start_time": 100.0, "end_time": 116.67, "mean_time": 108.0}
]

prompt = generate_skating_music_prompt(moves_data)
print(prompt)
```

## Output:
```
Epic orchestral figure skating program music with powerful and dramatic with strong brass accents and building tension at 25 seconds, graceful and flowing with smooth strings and elegant harmonies at 41 seconds, energetic and dynamic with crisp percussion and ascending melodies at 75 seconds, graceful and flowing with smooth strings and elegant harmonies at 91 seconds, powerful and dramatic with strong brass accents and building tension at 108 seconds 