import random

quiz = {"A group of three powerful people.": "Triumvirate",
        " One who knows many languages": "Polyglot",
        "A person coming to a foreign land to settle": "Immigrant",
        "A name assumed by a writer or a false name": "Pseudonym",
        "The person who works for free": "Volunteer",
        "Life history written by oneself": "Autobiography",
        "The person who collects coins": "Numismatist",
        "A Government by the few": "Oligarchy",
        "Person who walks in sleep": "Somnambulist",
        "Fit to drink": "Potable"
        }
questions = 4
list = []
right_answers = 0
for i in quiz.keys():
    list.append(i)
while questions > 0:
    question = random.choice(list)
    print(question)
    answer = input("Enter the answer: ")
    if answer == quiz[question]:
        right_answers += 1
    questions -= 1
print(f"You answered right {right_answers} questions.")
