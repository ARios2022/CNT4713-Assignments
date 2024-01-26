import socket

class Assignment2:
    # Task 1: Constructor
    def __init__(self, year):
        self.year = year

    # Task 2: Age
    def tellAge(self, currentYear):
        age = currentYear - self.year
        print(f'Your age is {age}')

    # Task 3: List
    def listAnniversaries(self):
        anniversaries = [(i+1)*10 for i in range((2022-self.year)//10)]
        return anniversaries

    # Task 4: String Manipulation
    def modifyYear(self, n):
        year_str = str(self.year)
        first_part = year_str[:2] * n
        second_part = ''.join([year_str[i] for i in range(len(year_str)) if i % 3 == 1 or i % 3 == 2])
        return first_part + second_part

    # Task 5: Loop and Conditional statements
    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
        if not string[0].islower():
            return False
        if sum(c.isdigit() for c in string) != 1:
            return False
        return True

    # Task 6: Socket
    @staticmethod
    def connectTcp(host, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.close()
            return True
        except:
            return False
