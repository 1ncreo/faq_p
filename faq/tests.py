from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        self.assertEqual(faq.get_translated_question('hi'), faq.question_hi)

class FAQAPITest(TestCase):
    def test_faq_list(self):
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, 200)