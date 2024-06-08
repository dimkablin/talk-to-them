
import os
import gpt4all

class LLM:
    def __init__(self, model_name, model_folder='llm/models'):
        self.model_path = os.path.join(model_folder, model_name)
        self.model = self.load_model(self.model_path)
    
    def load_model(self, model_path):
        # Здесь загрузка модели с использованием gpt4all
        try:
            model = gpt4all.load_model(model_path, device='cuda')
            return model
        except Exception as e:
            print(f"Error loading model from {model_path}: {e}")
            return None

    def call(self, prompt):
        if self.model is None:
            print("Model is not loaded.")
            return None

        try:
            response = self.model.generate(prompt)
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return None
