from django.core.cache import cache
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        faqs = cache.get(cache_key)
        if not faqs:
            faqs = FAQ.objects.all()
            for faq in faqs:
                faq.question = faq.get_translated_question(lang)
                faq.answer = faq.get_translated_answer(lang)
            cache.set(cache_key, faqs, timeout=60 * 15)  # Cache for 15 minutes
        return faqs