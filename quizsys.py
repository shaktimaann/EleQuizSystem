import random
import os
import csv
from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options  # Tuple of 4 options
        self.answer = answer    # Correct answer (A/B/C/D)


class Player:
    def __init__(self, name):
        self.name = name
        self.score_history = []


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.asked = set()  # set → avoid repeated questions

    def ask_question(self, q: Question):
        print("\n-----------------------------------")
        print(q.text)
        for opt in q.options:
            print(opt)

        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == q.answer:
            print("✔ Correct!")
            self.score += 1
        else:
            print(f"✘ Incorrect! Correct answer is {q.answer}")

    def start(self):
        print("\n===== DIGITAL ELECTRONICS QUIZ STARTED =====")

        # Shuffle questions for random order
        random.shuffle(self.questions)

        for q in self.questions:
            if q.text not in self.asked:
                self.asked.add(q.text)
                self.ask_question(q)

        print("\n===== QUIZ FINISHED =====")
        print(f"Your Score: {self.score}/{len(self.questions)}")

        return self.score


def load_questions_from_file(filename):
    """Reads questions from a text file and returns a list of Question objects"""
    questions = []

    if not os.path.exists(filename):
        print("❌ Question file not found!")
        return questions

    with open(filename, "r") as file:
        lines = file.read().split("\n")

    for line in lines:
        if line.strip() == "":
            continue
        # Format → Question|A)|B)|C)|D)|Correct
        parts = line.split("|")

        if len(parts) != 6:
            continue

        q_text = parts[0]
        options = (parts[1], parts[2], parts[3], parts[4])
        answer = parts[5].strip()

        questions.append(Question(q_text, options, answer))

    return questions


def save_results(player_name, score):
    """Save the result into a CSV file compatible with Excel."""
    filename = "quiz_results.csv"
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Player", "Score", "Date"])

        writer.writerow([player_name, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])


def analyze_performance(player: Player):
    scores = player.score_history

    if len(scores) == 0:
        print("\nNo previous performance data available.")
        return

    avg_score = sum(scores) / len(scores)
    print("\n===== PERFORMANCE ANALYSIS =====")
    print(f"Previous Scores: {scores}")
    print(f"Average Score: {avg_score:.2f}")

    if avg_score > 7:
        print("Excellent understanding of Digital Electronics!")
    elif avg_score > 4:
        print("Good performance, needs improvement in some areas.")
    else:
        print("Needs more practice!")


def main():
    print("===== DIGITAL ELECTRONICS QUIZ SYSTEM =====")
    name = input("Enter your name: ")

    player = Player(name)

    while True:
        # Load questions from external file
        questions = load_questions_from_file("questions.txt")

        if not questions:
            print("No questions available! Add questions to 'questions.txt'")
            break

        quiz = Quiz(questions)
        score = quiz.start()

        player.score_history.append(score)
        save_results(player.name, score)

        analyze_performance(player)

        again = input("\nDo you want to play another round? (y/n): ").lower()
        if again != "y":
            break

    print("\nThank you for playing the quiz!")

if __name__ == "__main__":
    main()