from gpt4all import GPT4All

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

with model.chat_session():
    user_input = input("You: ")
    response = model.generate(user_input, max_tokens=512)
    print("Bot:", response)
