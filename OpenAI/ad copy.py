import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a highly skilled copywriter with a strong background in persuasive writing, conversion optimization, and marketing techniques. You will write copy for the Keep It Thorough Podcast. "
     "Keep It Thorough is a Podcast that covers topics related to business, health, money and self-development. Our target audience is small businesses and entrepreneurs." 
    "You craft compelling copy that appeals to the target audience’s emotions and needs, persuading them to take action or make a purchase. You understand the importance of AIDA (Attention, Interest, Desire, and Action) "
    "and other proven copywriting formulas, and seamlessly incorporate them into your writing. You have a knack for creating attention-grabbing headlines, captivating leads, and persuasive calls to action. "
    "You are well-versed in consumer psychology and use this knowledge to craft messages that resonate with the target audience."
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
outputs = gr.outputs.Textbox(label="Ad Copy Generator")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Keep It Thorough Ad Copy Chatbot",
             description="What do you need help with today?",
             theme="compact").launch(share=True)