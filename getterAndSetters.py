class Study:
    def __init__(self):
        self._age = 0

    def get_age(self):
        print("getter method called")
        return self._age

    def set_age(self, a):
        print("setter method called")
        self._age = a

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


mark = Study()

mark.age = 10

print(mark.age)


class Geeks:
    def __init__(self):
        self._age = 0

    # using property decorator
    @property
    def age(self):
        print("getter method called")
        return self._age

    @age.setter
    def age(self, a):
        if a < 18:
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


mark = Geeks()

mark.age = 19

print(mark.age)
