questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

def greeting():
    print("Привет! Предлагаю проверить свои знания английского! Наберите 'ready', чтобы начать!")

def start_game():
    score = 0
    total_questions = len(questions)

    for i in range(total_questions):
        user_answer = input(questions[i] + " ")
        if user_answer.lower() == answers[i]:
            print("Ответ верный!")
            score += 1
        else:
            print("Неправильно. Правильный ответ:", answers[i])

    percentage = (score / total_questions) * 100
    print("Вот и все! Вы ответили на", score, "вопросов из", total_questions, "верно, это", percentage, "процентов.")

def main():
    greeting()
    user_input = input()
    if user_input.lower() == "ready":
        start_game()
    else:
        print("Кажется, вы не хотите играть. Очень жаль.")

main()

