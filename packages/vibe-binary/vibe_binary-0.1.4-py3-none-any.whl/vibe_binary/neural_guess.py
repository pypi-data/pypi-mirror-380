import random


class NeuralGuesser:
    def __init__(self, max_number=100):
        self.max_number = max_number
        self.min_guess = 1
        self.max_guess = max_number
        self.guesses = 0
        self.history = []

    def smart_guess(self):
        """Умный бинарный поиск"""
        self.guesses += 1

        if self.min_guess <= self.max_guess:
            guess = (self.min_guess + self.max_guess) // 2
        else:
            # Если диапазон сломался, используем случайное число
            available = self.get_available_numbers()
            guess = random.choice(available) if available else random.randint(1, self.max_number)

        return guess

    def get_available_numbers(self):
        """Получить доступные числа на основе истории"""
        available = list(range(1, self.max_number + 1))

        for guess, feedback in self.history:
            if feedback == '+' and guess in available:
                available = [x for x in available if x > guess]
            elif feedback == '-' and guess in available:
                available = [x for x in available if x < guess]
            elif feedback == '=' and guess in available:
                available.remove(guess)

        return available

    def add_feedback(self, feedback, last_guess):
        """Обновляем диапазон на основе фидбэка"""
        self.history.append((last_guess, feedback))

        if feedback == '+':
            self.min_guess = max(self.min_guess, last_guess + 1)
        elif feedback == '-':
            self.max_guess = min(self.max_guess, last_guess - 1)

    def start_game(self, show_intro=True):
        """Запускает игру по угадыванию числа"""
        if show_intro:
            print(f"🔮 Vibe Binary угадает число от 1 до {self.max_number}!")
            print("Правила: + (твое число БОЛЬШЕ), - (твое число МЕНЬШЕ), = (угадал)")
            print("─" * 50)

        self.guesses = 0
        self.history = []
        self.min_guess = 1
        self.max_guess = self.max_number

        while True:
            guess = self.smart_guess()
            print(f"🤔 Мое предположение: {guess}")

            feedback = input("Твой ответ (+, -, =): ").strip()

            while feedback not in ['+', '-', '=']:
                print("❌ Неверный ввод! Используй только +, - или =")
                feedback = input("Твой ответ (+, -, =): ").strip()

            if feedback == '=':
                print(f"🎉 Ура! Я угадал число {guess} за {self.guesses} попыток!")
                return guess

            self.add_feedback(feedback, guess)

            if self.min_guess > self.max_guess:
                print("🤨 Кажется, ты где-то ошибся с ответами... Начинаем заново!")
                self.min_guess = 1
                self.max_guess = self.max_number


def neural_guess_number(max_number=100):
    """Функция для быстрого запуска игры в угадывание чисел"""
    guesser = NeuralGuesser(max_number)
    guesser.start_game()


def neural_guess_c(max_number=100):
    """Чистая версия без лишнего текста"""
    guesser = NeuralGuesser(max_number)
    guesser.start_game(show_intro=False)