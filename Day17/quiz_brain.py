class Quiz:

    def __init__(self, q_bank):
        self.number = 0
        self.bank = q_bank
        self.correct_answers = 0
        # self.questions_left = True

    # def still_has_questions(self):
    #     if self.number < len(self.bank):
    #         pass
    #     else: self.questions_left = False

    def still_has_questions(self):
        return self.number < len(self.bank)

    def check_answer(self, answer, q_answer):
        if answer == q_answer.answer:
            self.correct_answers += 1
            print(f"That's correct! ({self.correct_answers}/{self.number})")
        else:
            print(f"You missed it. ({self.correct_answers}/{self.number})")

    def next_question(self):
        question = self.bank[self.number]
        self.number += 1
        answer = input(f"Q.{self.number}: {question.text} (True/False): ").title()
        self.check_answer(answer, question)

    def final_score(self):
        print("You have completed the quiz!")
        print(f"Your final score is {self.correct_answers}/{self.number}.")