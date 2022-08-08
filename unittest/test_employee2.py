import unittest
import employee

  # setup and teardown methods for making multiple and long test procedures
        # if we are 100 of test , it will be a pain to maintain. it would be nice. could create these from scratch. 
        # in one place, and reuse them for every test.
        #for this only we are going for setup and teardown method.
        # first one a function;  def setUp():  second one def tearDown(): here we are using only camel case.
        # def setUp(): this code will runbefore every test, and the teradown method will run after every single test.
        # if we want to create these two employee details nefore every single tests. 
        # we can passs it in the def setUp() method.
        # to access all the instamce variables we have to add emp_1 as sef.emp_! and emp_2 as self.emp_2
        # setUp method is used to initiate all the initialise all the instance variables and the 
        # teardown method is used for delete all the datas stored in the variables.
        #  so that you have a clean slate for the next test.


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("\nsetUp")
        self.emp_1 = employee.Employee("raghu", 'ram', 5000)
        self.emp_2 = employee.Employee("sundhar", "pitchai", 10000)

    def tearDown(self):
        print("tearDown\n")
       
    def test_email(self):
        print("test_email")
        # emp_1 = employee.Employee("raghu", 'ram', 5000)
        # emp_2 = employee.Employee("sundhar", "pitchai", 10000)

        self.assertEqual(self.emp_1.email, 'raghu.ram@email.com')        
        self.assertEqual(self.emp_2.email, 'sundhar.pitchai@email.com')

        self.emp_1.first = 'pranav'
        self.emp_2.first = 'ganesh'

        self.assertEqual(self.emp_1.email, 'pranav.ram@email.com')        
        self.assertEqual(self.emp_2.email, 'ganesh.pitchai@email.com')

        self.emp_1.last = 'gopi'
        self.emp_2.last = 'raju'

        self.assertEqual(self.emp_1.email, 'pranav.gopi@email.com')        
        self.assertEqual(self.emp_2.email, 'ganesh.raju@email.com')

    def test_fullname(self):
        print("test_fullname")
        # emp_1 = employee.Employee("raghu", 'ram', 5000)
        # emp_2 = employee.Employee("sundhar", "pitchai", 10000)

        self.assertEqual(self.emp_1.fullname, 'raghu .ram')        
        self.assertEqual(self.emp_2.fullname, 'sundhar .pitchai')

        self.emp_1.first = 'pranav'
        self.emp_2.first = 'ganesh'

        self.assertEqual(self.emp_1.fullname, 'pranav .ram')        
        self.assertEqual(self.emp_2.fullname, 'ganesh .pitchai') 

        self.emp_1.last = 'gopi'
        self.emp_2.last = 'raju'

        self.assertEqual(self.emp_1.fullname, 'pranav .gopi')        
        self.assertEqual(self.emp_2.fullname, 'ganesh .raju')
    

    def test_apply_raise(self):
        print("test_apply_raise")
        # emp_1 = employee.Employee("raghu", 'ram', 5000)
        # emp_2 = employee.Employee("sundhar", "pitchai", 10000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 7500)
        self.assertEqual(self.emp_2.pay, 15000)
        

      




        
