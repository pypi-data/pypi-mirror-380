import os
import requests
import json
import random
from dotenv import load_dotenv


class NeuralAPI:
    def __init__(self):
        self.openrouter_url = "https://openrouter.ai/api/v1/chat/completions"

        # Загружаем переменные из .env файла
        load_dotenv()

        # Берем ключ из переменных окружения или используем демо
        self.api_key = os.getenv('OPENROUTER_API_KEY', 'sk-or-v1-demo-key')

        if self.api_key == 'sk-or-v1-demo-key':
            print("⚠️  Используется демо-ключ. Для полной функциональности установи OPENROUTER_API_KEY в .env файле")

    def ask_neural_guess(self, history, max_number):
        """Спрашиваем нейросеть о следующем предположении"""

        prompt = f"""
        Мы играем в игру "Угадай число". 
        Диапазон чисел: от 1 до {max_number}
        История предыдущих попыток: {history}

        Ты - умный алгоритм, который угадывает числа. 
        На основе истории предыдущих попыток предложи следующее число для угадывания.
        Верни ТОЛЬКО число, без каких-либо пояснений.
        """

        try:
            response = requests.post(
                url=self.openrouter_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                data=json.dumps({
                    "model": "google/gemini-flash-1.5",  # Бесплатная модель
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.7
                })
            )

            if response.status_code == 200:
                result = response.json()
                guess_text = result['choices'][0]['message']['content'].strip()
                guess = self.extract_number(guess_text, max_number)
                return guess
            else:
                print(f"❌ Ошибка API: {response.status_code}")
                return self.fallback_guess(history, max_number)

        except Exception as e:
            print(f"❌ Ошибка: {e}")
            return self.fallback_guess(history, max_number)

    def extract_number(self, text, max_number):
        """Извлекаем число из текста ответа нейросети"""
        try:
            import re
            numbers = re.findall(r'\d+', text)
            if numbers:
                guess = int(numbers[0])
                if 1 <= guess <= max_number:
                    return guess
        except:
            pass

        return random.randint(1, max_number)

    def fallback_guess(self, history, max_number):
        """Запасной алгоритм если нейросеть не работает"""
        if not history:
            return max_number // 2

        available_numbers = list(range(1, max_number + 1))
        for guess, _ in history:
            if guess in available_numbers:
                available_numbers.remove(guess)

        return random.choice(available_numbers) if available_numbers else random.randint(1, max_number)