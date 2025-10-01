import random


class NeuralGuesser:
    def __init__(self, max_number=100, use_real_ai=True):
        self.max_number = max_number
        self.min_guess = 1
        self.max_guess = max_number
        self.guesses = 0
        self.use_real_ai = use_real_ai

        # Пытаемся импортировать нейросеть, но не падаем при ошибке
        self.ai = None
        if use_real_ai:
            try:
                from .ai_api import NeuralAPI
                self.ai = NeuralAPI(silent_mode=True)
            except ImportError:
                # Если зависимости не установлены, используем локальный алгоритм
                self.use_real_ai = False

    def smart_guess(self):
        self.guesses += 1

        if self.use_real_ai and self.ai:
            try:
                # Пытаемся использовать нейросеть
                guess = self.ai.ask_neural_guess(
                    [(g, f) for g, f in self.history],
                    self.max_number
                )
                return guess
            except Exception:
                # Если нейросеть сломалась, переключаемся на локальный алгоритм
                self.use_real_ai = False

        # Локальный бинарный поиск
        if self.min_guess <= self.max_guess:
            return (self.min_guess + self.max_guess) // 2
        else:
            return random.randint(1, self.max_number)

    def add_feedback(self, feedback, last_guess):
        self.history.append((last_guess, feedback))

        if feedback == '+':
            self.min_guess = max(self.min_guess, last_guess + 1)
        elif feedback == '-':
            self.max_guess = min(self.max_guess, last_guess - 1)

    def start_game(self):
        print(f"🔮 Vibe Binary угадает число от 1 до {self.max_number}!")

        # Тихая проверка доступности нейросети
        mode = "НЕЙРОСЕТЬ" if self.use_real_ai else "локальный алгоритм"
        print(f"💫 Режим: {mode}")

        print("Правила: + (БОЛЬШЕ), - (МЕНЬШЕ), = (угадал)")
        print("─" * 50)

        self.guesses = 0
        self.history = []
        self.min_guess = 1
        self.max_guess = self.max_number

        while True:
            guess = self.smart_guess()
            print(f"🤔 Предположение: {guess}")

            feedback = input("Твой ответ (+, -, =): ").strip()

            while feedback not in ['+', '-', '=']:
                print("❌ Только +, - или =!")
                feedback = input("Твой ответ (+, -, =): ").strip()

            if feedback == '=':
                print(f"🎉 Угадал за {self.guesses} попыток!")
                break

            self.add_feedback(feedback, guess)


def neural_guess_number(max_number=100, use_real_ai=True):
    """Функция, которая никогда не падает"""
    try:
        game = NeuralGuesser(max_number, use_real_ai)
        game.start_game()
    except Exception as e:
        # Аварийный fallback - запускаем без нейросети
        print("⚠️  Переключаемся на локальный режим...")
        game = NeuralGuesser(max_number, use_real_ai=False)
        game.start_game()


def neural_guess_c(max_number=100):
    """Тихая версия без лишних сообщений"""
    game = NeuralGuesser(max_number, use_real_ai=True)
    game.start_game()