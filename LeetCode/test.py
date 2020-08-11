class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        n = 3
        def test(n):
            if n == 0:
                print(0)
            else:
                print(n)
                test(n - 1)
        test(n)
        return self.name
    def test(n):
        if n == 0:
            print(0)
        else:
            print(n)
            Student.test(n-1)

a = Student('a')
a.get_name()

b = Student('b')
b.get_name()

Student.test(3)
