class Human():
    def __init__(self, name,age,birthday, sex, ):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.sex = sex
        self.friends = []

    def __str__(self):
        return 'Name: {} Age: {} Birthday: {} Sex: {} Friends: {}'.format(self.name, self.age, self.birthday, self.sex, self.friends)

    def __add__(self, other):
        if(isinstance(other,Human)):
            if not other in self.friends:
                self.friends.append(other)
                other.friends.append(self)
                return self

    def __sub__(self, other):
        if(isinstance(other,Human)):
            if other in self.friends:
                # self.friends = [friend for friend in self.friends if friend != other]
                # other.friends = [friend for friend in other.friends if friend != self]
                self.friends.remove(other)
                other.friends.remove(self)

    def __mod__(self, other):
        return other in self.friends

    def __truediv__(self, other):
        return [friend.sex for friend in self.friends].count(other)

    def set_age (self, age):
        self.age = age

    def greet(self):
        print('My name is: {}. I am {} years old'.format(self.name, self.age))

    def add_friend(self, friend):
        self.friends.append(friend)

    def get_zodiac_sign(self):
        birthday = self.birthday
        zodiac_sign = ''
        [date, month] = birthday.split('.')

        if int(month) == 12:
	        zodiac_sign = 'Sagittarius' if (int(date) < 22) else 'Capricorn'
        elif int(month) == 1:
	        zodiac_sign = 'Capricorn' if (int(date) < 20) else 'Aquarius'
        elif int(month) == 2:
	        zodiac_sign = 'Aquarius' if (int(date) < 19) else 'Pisces'
        elif int(month) == 3:
	        zodiac_sign = 'Pisces' if (int(date) < 21) else 'Aries'
        elif int(month) == 4:
	        zodiac_sign = 'Aries' if (int(date) < 20) else 'Taurus'
        elif int(month) == 5:
	        zodiac_sign = 'Taurus' if (int(date) < 21) else 'Gemini'
        elif int(month) == 6:
	        zodiac_sign = 'Gemini' if (int(date) < 21) else 'Cancer'
        elif int(month) == 7:
	        zodiac_sign = 'Cancer' if (int(date) < 23) else 'Leo'
        elif int(month) == 8:
	        zodiac_sign = 'Leo' if (int(date) < 23) else 'Virgo'
        elif int(month) == 9:
	        zodiac_sign = 'Virgo' if (int(date) < 23) else 'Libra'
        elif int(month) == 10:
	        zodiac_sign = 'Libra' if (int(date) < 23) else 'Scorpio'
        elif int(month) == 11:
	        zodiac_sign = 'scorpio' if (int(date) < 22) else 'Sagittarius'
        return zodiac_sign


h1 = Human('Borinkata', 21, '25.08', 'm')
print(h1)