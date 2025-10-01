from vibe_binary.ai_api import NeuralAPI


def test_neural_api():
    ai = NeuralAPI()

    # Тестируем на простом случае
    history = [(50, '-')]  # Пробовали 50, число меньше
    guess = ai.ask_neural_guess(history, 100)

    print(f"🎯 Нейросеть предложила: {guess}")

    if 1 <= guess <= 100:
        print("✅ API работает корректно!")
    else:
        print("❌ Проблема с API")


if __name__ == "__main__":
    test_neural_api()