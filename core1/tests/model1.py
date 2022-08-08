

from pprint import pprint
from turtle import title
from django.test import TestCase
from app1.models import Post

from model_bakery import baker
from pprint import pprint

from django.contrib.auth.models import User


class TestAppModels(TestCase):
                                    ###### method-1
    # def setUp(self):
    #     print('SetUp')
    #     testuser = User.objects.create(username = 'testuser', password = '12345')
    #     testuser1 = User.objects.create(username = 'testuser1', password = '12345')
    #     self.title = Post.objects.create(title = "Django", content = "new Content", slug = 'Django')
    #     self.title.likes.set([testuser.pk, testuser1.pk])
        
    # def test_model_str11(self):
    #     # print("1-Test")
    #     self.assertEqual(str(self.title), "Django")
    
    # def test_model_str2(self):
    #     # print("2-Test")
    #     self.assertEqual(str(self.title), "Django")

    # def test_absolute_url(self):
    #     self.title.slug = Post.objects.get(id=1)
    #     self.assertEqual("/Django/", self.title.slug.get_absolute_url())

    # # we have added self in the lines 15,16 and in 19


    #                         #####    method-2
    @classmethod
    def setUpTestData(cls):
        print('SetUp')
        testuser = User.objects.create(username = 'testuser', password = '12345')
        testuser1 = User.objects.create(username = 'testuser1', password = '12345')
        cls.title = Post.objects.create(title = "Django", content = "new Content", slug = 'Django')
        cls.title.likes.set([testuser.pk, testuser1.pk])
        
    def test_model_str11(self):
        # print("1-Test")
        self.assertEqual(str(self.title), "Django")
    
    def test_model_str2(self):
        # print("2-Test")
        self.assertEqual(str(self.title), "Django")

    def test_absolute_url(self):
        self.title.slug = Post.objects.get(id=1)
        self.assertEqual("/Django/", self.title.slug.get_absolute_url())

   
   

    #                         #####    method-3, not working
    # @classmethod
    # def setUpTestData(cls):
    #     print('SetUp')
    #     testuser = User.objects.create(username = 'testuser', password = '12345')
    #     testuser1 = User.objects.create(username = 'testuser1', password = '12345')
    #     cls.new = Post.objects.create(new = "Django", content = "new Content", slug = 'Django')
    #     cls.new.likes.set([testuser.pk, testuser1.pk])
        
    # def test_model_str11(self):
    #     # print("1-Test")
    #     self.assertEqual(str(self.new), "Django")
    
    # def test_model_str2(self):
    #     # print("2-Test")
    #     self.assertEqual(str(self.new), "Django")

    # def test_absolute_url(self):
    #     self.new.slug = Post.objects.get(id=1)
    #     self.assertEqual("/Django/", self.new.slug.get_absolute_url())

                        # ####          method-4 using baker

    class TestNew(TestCase):
        def setUp(self):
            self.post = baker.make('app1.Post')
            pprint(self.post.__dict__)
        
        def test_model_str(self):
            title = Post.objects.create(title = "Django Testing")
            content = Post.objects.create(content = "This is Some Content")
            self.assertEqual(str(title = "Django Testing"))