from transformers import pipeline

# Load the text generator
generator = pipeline("text-generation", model="gpt2")

# Start the story
prompt = input("type the beginning of your story: ")

story = prompt

for _ in range(5):
    # Generate a continuation
    result = generator(prompt, num_return_sequences=1, pad_token_id=generator.tokenizer.eos_token_id)
    text = result[0]['generated_text']

    # Add to the story
    story += " " + text
    print("\nStory so far:\n", text)

    # Ask user what happens next
    user_input = input("\nWhat happens next? (Describe or type 'end' to end the story): ")

    if user_input.lower() == "end":
        break

    # New prompt includes the user’s direction
    prompt = text + " " + user_input

print("\nFinal Story:\n")
print(story)
