import gradio as gr
from main import LLM
from nlp.env import llm_port

# Инициализация модели
model_name = "saiga-q2_K.gguf"  # Укажите имя модели
llm = LLM(model_name)

# Функция для Gradio интерфейса
def generate_response(prompt):
    response = llm(prompt)
    return response

# Создание Gradio интерфейса
iface = gr.Interface(
    fn=generate_response,
    inputs=gr.inputs.Textbox(lines=2, placeholder="Введите ваш запрос здесь"),
    outputs="text",
    title="GPT-4 Interface",
    description="Интерфейс для генерации текста с использованием GPT-4 модели",
)

# Запуск Gradio интерфейса
if __name__ == "__main__":
    iface.launch(server_name="127.0.0.1", server_port=llm_port)
