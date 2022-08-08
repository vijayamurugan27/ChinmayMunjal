import unittest
import employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = employee.Employee("raghu", 'ram', 5000)
        emp_2 = employee.Employee("sundhar", "pitchai", 10000)

        self.assertEqual(emp_1.email, 'raghu.ram@email.com')        
        self.assertEqual(emp_2.email, 'sundhar.pitchai@email.com')

        emp_1.first = 'pranav'
        emp_2.first = 'ganesh'

        self.assertEqual(emp_1.email, 'pranav.ram@email.com')        
        self.assertEqual(emp_2.email, 'ganesh.pitchai@email.com')

        emp_1.last = 'gopi'
        emp_2.last = 'raju'

        self.assertEqual(emp_1.email, 'pranav.gopi@email.com')        
        self.assertEqual(emp_2.email, 'ganesh.raju@email.com')

    def test_fullname(self):
        emp_1 = employee.Employee("raghu", 'ram', 5000)
        emp_2 = employee.Employee("sundhar", "pitchai", 10000)

        self.assertEqual(emp_1.fullname, 'raghu .ram')        
        self.assertEqual(emp_2.fullname, 'sundhar .pitchai')

        emp_1.first = 'pranav'
        emp_2.first = 'ganesh'

        self.assertEqual(emp_1.fullname, 'pranav .ram')        
        self.assertEqual(emp_2.fullname, 'ganesh .pitchai') 

        emp_1.last = 'gopi'
        emp_2.last = 'raju'

        self.assertEqual(emp_1.fullname, 'pranav .gopi')        
        self.assertEqual(emp_2.fullname, 'ganesh .raju')
    

    def test_apply_raise(self):
        emp_1 = employee.Employee("raghu", 'ram', 5000)
        emp_2 = employee.Employee("sundhar", "pitchai", 10000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 7500)
        self.assertEqual(emp_2.pay, 15000)
        

        # setup and teardown methods for making multiple and long test procedures
        # if we are 100 of test , it will be a pain to maintain. it would be nice. could create these from scratch. 
        # in one place, and reuse them for every test.
        #for this only we are going for setup and teardown method.
        # first one a function;  def setUp():  second one def tearDown(): here we are using only camel case.
        # def setUp(): this code will runbefore every test, and the teradown method will run after every single test.
        # if we want to create these two employee details nefore every single tests. 
        # we can passs it in the def setUp() method.





        
