import logging
import math
import os
from time import time

from gpt4all import GPT4All
from env import DEVICE


class LLM:
    def __init__(self, model_name, model_path="models/"):
        self.model_name = model_name
        self.model_path = model_path
        self.device = DEVICE

        # try to load model
        try:
            self.model = self.load_model()
        except Exception as e:
            logging.exception(f"Ошибка инициализации модели: {self.model_name} в папке {self.model_path}")
            print(e.with_traceback())
    
    def load_model(self):
        # Здесь загрузка модели с использованием gpt4all
        try:
            model = GPT4All(
                model_name=self.model_name,
                model_path=self.model_path,
                allow_download=True,
                device=self.device,
                n_threads=6
            )
            return model
        except Exception as e:
            print(f"Error loading model from {self.model_name}: {e}")
            return None
    
    def stop_on_token_callback(self, token_id, token_string):
        # one sentence is enough:
        if '---' in token_string:
            return False
        else:
            return True

    def __call__(self, prompt):
        if self.model is None:
            print("Model is not loaded.")
            return None

        try:
            response = self.model.generate(
                prompt,
                max_tokens=128,
                n_batch=1,
                temp=0.01,
                callback=self.stop_on_token_callback
            )
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return None


if __name__ == "__main__":
    logging.info("Started gpt4all.")
    start_time = time()

    llm = LLM("saiga-q2_K.gguf")

    logging.info(f"Loaded model: {llm.model_name} within {time() - start_time} seconds.")
    
    with llm.model.chat_session("Тебя зовут Лина. Ты добрый и отзывчивый ассистент."):
        while True:
            prompt = str(input("User: "))
            start_time = time()
        
            if prompt == "exit":
                break

            response = llm(prompt)
            print(f"Bot [{(time()-start_time):.2f} sec]: {response}")
