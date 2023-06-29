class Students:
    def __init__(self, name, major, roll_no, cgpa):
        self.name = name
        self.major = major
        self.roll_no = roll_no
        self.cgpa = cgpa

    def is_pass(self):
        if self.cgpa > 5:
            print("pass")
        else:
            print("fail")


class Chef:
    def make_chicken(self):
        print("makes chicken")

    def make_pulaav(self):
        print("makes pulaav")

    def make_nonveg(self):
        print("makes non veg")


# inheritence
chef = Chef()
chef.make_chicken()
chef.make_pulaav()
chef.make_nonveg()


class Chinese_Chef(Chef):
    def make_chinese(self):
        print("makes chinese")


chinese_chef = Chinese_Chef()
chinese_chef.make_chinese()
chinese_chef.make_nonveg()
