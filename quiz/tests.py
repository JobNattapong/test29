from django.test import TestCase
from django.urls import resolve
from quiz.views import index
import datetime
from django.utils import timezone
from quiz.models import Question, Choice

class IndexTest(TestCase):
    def test_root_index(self):
        fonnd = resolve('/quiz/')
        self.assertEqual(fonnd.func, index)

    def test_user_index_template(self):
        response = self.client.get('/quiz/')
        self.assertTemplateUsed(response, 'quiz/index.html')
