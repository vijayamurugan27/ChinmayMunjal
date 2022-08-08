from pprint import pprint
from turtle import title
from django.test import TestCase
from app1.models import Post

from model_bakery import baker
from pprint import pprint

from django.contrib.auth.models import User

class TestNew(TestCase):
    def setUp(self):
        self.post = baker.make('app1.Post')
        pprint(self.post.__dict__)
        
    def test_model_str(self):
        title = Post.objects.create(title = "Django Testing")
        content = Post.objects.create(content = "This is Some Content")
        self.assertEqual(str(title), "Django Testing")