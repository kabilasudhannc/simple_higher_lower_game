from art import logo, vs
from game_data import data
import random
from replit import clear

score = 0


def calc_score():
    global score
    return score + 1


def format_questions(questions):
    question_1 = f"Compare A: {questions['A']['name']}, a {questions['A']['description']}, from {questions['A']['country']}."
    question_2 = f"Against B: {questions['B']['name']}, a {questions['B']['description']}, from {questions['B']['country']}."
    return question_1, question_2


def get_questions():
    questions = {}
    questions['A'] = random.choice(data)
    questions['B'] = random.choice(data)
    return questions


def next_questions(questions):
    questions['A'] = questions['B']
    questions['B'] = random.choice(data)
    return questions


def play_game():
    global score
    global questions
    clear()
    print(logo)
    questions = next_questions(questions)

    if score != 0:
        print(f"You're right! Current score: {score}")

    formated_questions = format_questions(questions)

    print(f"{formated_questions[0]}")
    print(vs)
    print(f"{formated_questions[1]}")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == 'A':
        if questions[choice]['follower_count'] > questions['B']['follower_count']:
            score = calc_score()
            play_game()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")

    else:
        if questions[choice]['follower_count'] > questions['A']['follower_count']:
            score = calc_score()
            play_game()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")


questions = get_questions()
play_game()
