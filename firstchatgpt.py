import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an English professor that helps and rate undergraduate first year papers in college"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Prof Gu")

demo.launch(share=True)