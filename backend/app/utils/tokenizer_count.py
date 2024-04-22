"""
Created a quick script to help us later manage/estimate cost
"""

from datasets import load_dataset
from transformers import AutoTokenizer
import tiktoken


# Load the data sets. I used this example from hugging face
# if you find a better dataset/cheaper change this string
dataset = load_dataset("MicPie/unpredictable_studystack-com")

# only the columns that we care about
# maybe not task?
column_names = ["task", "input", "output"]

# Load the tokenizer for our model
tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")

total_tokens = 0
total_examples = 0

# iterate over the dataset and calculate token counts
for example in dataset["train"]:
    # Tokenize the text in the specified columns
    tokens = []
    for column_name in column_names:
        tokens.extend(tokenizer.encode(example[column_name]))
    
    total_tokens += len(tokens)
    total_examples += 1

# Print the results
print(f"Total tokens: {total_tokens}")
print(f"Total examples: {total_examples}")
print(f"Average tokens per example: {total_tokens / total_examples:.2f}")

# Cost per 1M tokens via OpenAI
total_cost = (total_tokens/1E6) * 6.00
print(f"Total Cost of Fine-Tuning Job: {total_cost}")