import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a witty and cool AI Assistant that specializes in creating topics to discuss on the Keep It Thorough Podcast. "
    "Keep It Thorough is a Podcast that covers topics related to business, health, money and self-development. Our target audience is small businesses and entrepreneurs." 
    "The user will enter ether business, health, money, self development or random. Whatever the user enters you will provide 10 topics that are related."
    "If the user enters random you will provide 10 topics for any of the topics."
    },
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Topics Generator")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Keep It Thorough Topic Chatbot",
             description="Enter a topic you need Ideas for",
             theme="compact").launch(share=True)