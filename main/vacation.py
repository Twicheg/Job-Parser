
class Vacation:
    '''Класс для создания и сравнения ваканский'''
    def __init__(self, id, vacation_name, link, payment, experience, snippet):
        self.id = id
        self.vacation_name = vacation_name
        self.link = link
        self.payment = payment
        self.experience = experience
        self.snippet = snippet

    def __le__(self, other):
        return self.payment < other.payment

    def __eq__(self, other):
        return self.payment == other.payment

    def __gt__(self, other):
        return self.payment > other.payment

    def __str__(self):
        return ''