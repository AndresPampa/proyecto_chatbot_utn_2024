# from dotenv import load_dotenv
import os
#OpenAI
from openai import OpenAI
#Gemini
import google.generativeai as genai
#Graphics
import gradio as gr


class ChatbotGemini:

    def __init__(self):
        self.iniciarBot()


    def iniciarBot(self):
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=GOOGLE_API_KEY)
        genai.GenerationConfig(temperature=0.4)
        self.model = genai.GenerativeModel('models/gemini-pro').start_chat(history=[])
    

    def respuestas(self, pregunta, conversacion):
        respuesta = self.model.send_message(pregunta)
        conversacion.append((pregunta, respuesta.text))
        return "", conversacion
    

    #Parte visual de gradio
    def launch_gradio(self):
        with gr.Blocks(title="Chatbot-UTN", theme='HaleyCH/HaleyCH_Theme') as demo:
            chatbot = gr.Chatbot()
            question = gr.Textbox(label="Que quieres preguntarme")
            clear = gr.ClearButton([question, chatbot])
            question.submit(self.respuestas, [question, chatbot], [question, chatbot])

        demo.launch(debug=True)

if __name__ == "__main__":
    try:
        gc = ChatbotGemini()
        gc.launch_gradio()
    except Exception as e:
        print(f"Se rompio... por {e}")
        exit()