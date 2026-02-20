from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="microsoft/DialoGPT-small"
)

def get_response(user_input):
    response = chatbot(
        user_input,
        max_length=80,
        num_return_sequences=1,
        pad_token_id=50256,
        do_sample=True,
        temperature=0.8
    )

    generated_text = response[0]["generated_text"]

    # Remove input only if it appears at beginning
    if generated_text.startswith(user_input):
        bot_reply = generated_text[len(user_input):].strip()
    else:
        bot_reply = generated_text.strip()

    if bot_reply == "":
        bot_reply = "Hmm... tell me more about that."

    return bot_reply
