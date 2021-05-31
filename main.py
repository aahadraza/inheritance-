'''
Inheritance is a way of creating a new class from an existing class.
'''
class employess:
    company = "google"

    def showdetail(self):
        print("this is an employee")
class programmer(employess):
    languages = "python"
    #company = "youtube  "

    def getlanguage(self):
        print(f"the language is {self.languages}")
    def showdetail(self):
        print("this is an programmer")
e = employess()
e.showdetail()
p = programmer()
p.showdetail()
print(p.company)
