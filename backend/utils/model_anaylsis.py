import json
import matplotlib.pyplot as plt

def find_average():
    with open("100test.json") as f:
        data = json.load(f)
    model_times = {
        "OPENAI_GPT4o MC": [],
        "OPENAI_GPT4o Simple": [],
        "OPENAI_GPT3.5-Turbo MC": [],
        "OPENAI_GPT3.5-Turbo Simple": []
    }

    # grabbed the fail rates of each model
    model_fails = {
        "OPENAI_GPT4o MC": 0,
        "OPENAI_GPT4o Simple": 0,
        "OPENAI_GPT3.5-Turbo MC": 0,
        "OPENAI_GPT3.5-Turbo Simple": 0
    }
    for res in data['results']:
        model_times[res['name']].extend(res['times'])
        model_fails[res['name']] = res['testPassFailCounts']['Response time is less than 15s']['fail']
    avg_times = {model: (sum(times) / len(times))/1000 for model, times in model_times.items()}
    
    # idk if this the best way of doing this lmaoo
    categories = list(model_times.keys())
    averages = list(avg_times.values())
    fails = list(model_fails.values())
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(categories))
    width = 0.35
    
    bars1 = ax.bar([i - width/2 for i in x], averages, width, label='Average Time',)

    bars2 = ax.bar([i + width/2 for i in x], fails, width, label='Fail Count ( Took more than 15 seconds :( )')
    
    ax.set_xlabel("Model")
    ax.set_ylabel("Time (seconds) / Fail Count")
    ax.set_title("Model Performance")
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45, ha='right')
    ax.legend()
    
    # grouped bar chart?? maybe idk probably the best way to visualize it
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height,
                f'{height:.2f}', ha='center', va='bottom')
    
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height,
                f'{int(height)}', ha='center', va='bottom')
    
    fig.tight_layout()
    plt.show()

find_average()