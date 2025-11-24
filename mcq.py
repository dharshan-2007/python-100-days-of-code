class Question:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer


class mcq:
    def __init__(self,q_list):
        self.mark=0
        self.q_no=0
        self.q_list=q_list
    def next_question(self):
        cur_question=self.q_list[self.q_no]
        self.q_no+=1
        user_ans=input(f"Q.{self.q_no} {cur_question.question} (True/False): ")
        if(user_ans==cur_question.answer):
            print("Answer is correct")
            self.mark+=1
        else:
            print("Answer is wrong")
    def totalMark(self):
        return  f"{self.mark}/{len(self.q_list)}"

facts_list = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "Humans can breathe underwater without any equipment.", "answer": "False"},
    {"text": "The Great Wall of China is visible from space.", "answer": "False"},
    {"text": "Sharks are mammals.", "answer": "False"},
    {"text": "Lightning never strikes the same place twice.", "answer": "False"},
    {"text": "Honey never spoils.", "answer": "True"},
    {"text": "An octopus has three hearts.", "answer": "True"},
    {"text": "Bananas are berries.", "answer": "True"},
    {"text": "Goldfish have a memory span of only three seconds.", "answer": "False"},
    {"text": "The Eiffel Tower can grow taller in summer.", "answer": "True"}
]

question_bank=[]
for dict_ in facts_list:
    question_bank.append(Question(dict_["text"],dict_["answer"]))

quiz=mcq(question_bank)
while(quiz.q_no<len(question_bank)):
    quiz.next_question()

print("Your mark is: ",quiz.totalMark())