class car(object):
    def __init__(self, model, color, company, speed_limit):
           self.color = color
           self.company = company
           self.speed_limit = speed_limit 
           self.model = model

    def setGrade(self, course, grade):
          self.grades[course] = grade
    def start(self):
          print(self.color)

abcd = car("anything", "red","audi",80)
print(abcd.start())
print(abcd.model)
