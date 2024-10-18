from question_model import Question
from data import question_data, video_game_question_data
from quiz_brain import Quiz

question_bank = []
choice = input("Select a quiz (original or video games): ").lower()
if choice == "original":
    answer_valid = True
    for quest in question_data:
        question_bank.append(Question(quest["text"], quest["answer"]))

elif choice == "video games":
    answer_valid = True
    for quest in video_game_question_data["results"]:
        question_bank.append(Question(quest["question"], quest["correct_answer"]))

else:
    answer_valid = False
    print("Invalid answer.")


# print(question_bank_video_games[0].text)

if answer_valid:
    quizz = Quiz(question_bank)
    # quizz.next_question()

    while quizz.still_has_questions():
        quizz.next_question()

    quizz.final_score()