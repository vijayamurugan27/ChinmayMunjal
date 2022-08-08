

from turtle import title
from django.test import TestCase
from app1.models import Post


from django.contrib.auth.models import User


class TestAppModels(TestCase):

    def test_model_str(self):
        title = Post.objects.create(title = "Django Testing")
        content = Post.objects.create(content = "content")
        self.assertEqual(str(title), "Django Testing")

    def test_model_str1(self):
        title = Post.objects.create(title = "Django Testing")
        content = Post.objects.create(content = "content")
        self.assertEqual(str(title), "Django Testing")

    def test_post_like_user(self):
        testuser = User.objects.create(username = 'testuser', password = '12345')
        testuser1 = User.objects.create(username = 'testuser1', password = '12345')
        title = Post.objects.create(title = "Django", content = "new Content")
        title.likes.set([testuser.pk, testuser1.pk])
        self.assertEqual(title.likes.count(), 2)

    