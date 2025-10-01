from .ai_api import NeuralAPI


class NeuralGuesser:
    def __init__(self, max_number=100, use_real_ai=True):
        self.max_number = max_number
        self.min_guess = 1
        self.max_guess = max_number
        self.guesses = 0
        self.history = []  # [(guess, feedback), ...]

        # Настоящая нейросеть через API
        self.use_real_ai = use_real_ai
        if use_real_ai:
            self.ai = NeuralAPI()

    def smart_guess(self):
        """Умное предположение - либо от нейросети, либо бинарный поиск"""
        self.guesses += 1

        if self.use_real_ai and self.ai:
            # Используем настоящую нейросеть
            guess = self.ai.ask_neural_guess(self.history, self.max_number)
        else:
            # Используем бинарный поиск
            if self.min_guess <= self.max_guess:
                guess = (self.min_guess + self.max_guess) // 2
            else:
                guess = random.randint(1, self.max_number)

        return guess

    def add_feedback(self, feedback, last_guess):
        """Обновляем историю и диапазон"""
        self.history.append((last_guess, feedback))

        # Обновляем для бинарного поиска (на случай если нейросеть ошибается)
        if feedback == '+':
            self.min_guess = max(self.min_guess, last_guess + 1)
        elif feedback == '-':
            self.max_guess = min(self.max_guess, last_guess - 1)

    def start_game(self):
        """Запускает игру с настоящей нейросетью"""
        print(f"🔮 Vibe Binary с НЕЙРОСЕТЬЮ угадает число от 1 до {self.max_number}!")
        print("Правила: + (мое число БОЛЬШЕ), - (мое число МЕНЬШЕ), = (угадал)")

        if self.use_real_ai:
            print("💫 Режим: НАСТОЯЩАЯ НЕЙРОСЕТЬ через API")
        else:
            print("⚡ Режим: Локальный бинарный поиск")

        print("─" * 50)

        self.guesses = 0
        self.history = []
        self.min_guess = 1
        self.max_guess = self.max_number

        while True:
            guess = self.smart_guess()
            print(f"🤔 Нейросеть предполагает: {guess}")

            feedback = input("Твой ответ (+, -, =): ").strip()

            while feedback not in ['+', '-', '=']:
                print("❌ Только +, - или =!")
                feedback = input("Твой ответ (+, -, =): ").strip()

            if feedback == '=':
                print(f"🎉 Нейросеть угадала за {self.guesses} попыток!")
                break

            self.add_feedback(feedback, guess)

            if self.min_guess > self.max_guess:
                print("🤨 Кажется, ты где-то ошибся с ответами...")
                break


def neural_guess_number(max_number=100, use_real_ai=True):
    """Функция для угадывания числа с нейросетью"""
    game = NeuralGuesser(max_number, use_real_ai)
    game.start_game()


def neural_guess_c(max_number=100):
    """Чистая версия с нейросетью"""
    game = NeuralGuesser(max_number, use_real_ai=True)
    game.start_game()