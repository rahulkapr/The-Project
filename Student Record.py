#create any program
class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=40:
            print(f"Name:{self.name}\nMarks:{self.marks}\nResult:Passed")

        else:
            print(f"Name:{self.name}\nMarks:{self.marks}\nResult:Failed")

a=Students("iyerhoewirui",20)
a.result()               

                    