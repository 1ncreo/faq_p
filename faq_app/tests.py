import pytest
from django.urls import reverse
from rest_framework import status
from .models import FAQ

@pytest.fixture
def faq_instance(db):
    return FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework."
    )

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture(autouse=True)
def setup_cache():
    from django.core.cache import cache
    cache.clear()
    yield
    cache.clear()

@pytest.mark.django_db
class TestFAQ:
    def test_translation_creation(self, faq_instance):
        assert faq_instance.question_hi is not None
        assert faq_instance.answer_hi is not None

    def test_translation_retrieval(self, faq_instance):
        assert faq_instance.get_translated_question('hi') == faq_instance.question_hi
        assert faq_instance.get_translated_question('en') == faq_instance.question

    def test_api_list(self, api_client):
        url = reverse('faq-list-create')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_language_switch(self, api_client, faq_instance):
        url = reverse('faq-list-create')
        response_hi = api_client.get(f"{url}?lang=hi")
        response_en = api_client.get(f"{url}?lang=en")
        assert response_hi.status_code == status.HTTP_200_OK
        assert response_en.status_code == status.HTTP_200_OK
