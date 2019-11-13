import random

class Question():
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
        pass
    pass

    def check_answer(self,answer):
        if self.answer == answer:
            return True
            pass
        else:
            return False
            pass
        return


class Quiz():
    def __init__(self):
        self.questions = []
        self.score = 0
        self.set_questions()
    
    def start(self):
        for q in self.questions:
            self.show_question(q)
            pass
        print(f"Your score : {self.score}")
        

    
    def show_question(self,q):
        print(q.question)
        for choice in q.choices:
            print(f"- {choice}")
            pass
        ans = input("Answer :")
        if q.check_answer(ans):
            self.score +=1
            print("CONGRATS! You are right!")
        else:
            print(f"You are wrong! The true answer is {q.answer}")
        pass

        


    def set_questions(self):
        for index in range(0,10):
            islem = self.get_islem()
            num1 = random.randint(1,11)
            num2 = random.randint(1,11)
            answer =self.get_answer(islem,num1,num2)
            q = Question(f"{num1} {islem} {num2}",[],str(answer))
            self.questions.append(q)
            pass    
    
    def get_answer(self,islem,num1,num2):
        if islem=="+":
            return str(num1+num2)
            pass
        elif islem == "-":
            return str(num1-num2)
            pass
        elif islem == "x":
            return str(num1*num2)
        elif islem == "/":
            return str(num1/num2)
        pass

        

    def get_islem(self):
        islem_int = random.randint(0,3)
        islem_str = ""
        if islem_int ==0:
            islem_str = "+"
            pass
        elif islem_int ==1:
            islem_str = "-"
            pass
        elif islem_int ==2:
            islem_str = "x"
            pass
        elif islem_int ==3:
            islem_str = "/"
            pass
        return islem_str
        pass
pass

q = Quiz()
q.start()
