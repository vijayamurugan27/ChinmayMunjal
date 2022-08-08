# Why we are going for mocking
# consider a situation, for testing where we need to pull data from a website.
# during testing we can get data from website, 
# what if the website is down. During these cases we use mock.
import requests

class Employee:
    raise_amt = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} .{}'.format(self.first, self.last)
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad response!' 
    