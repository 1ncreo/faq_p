from rest_framework import serializers
from django.core.cache import cache
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def get_question(self, obj):
        lang = self.context.get('request').query_params.get('lang', 'en')
        cache_key = f'faq_question_{obj.id}_{lang}'

        cached = cache.get(cache_key)
        if cached:
            return cached

        if lang == 'hi':
            result = obj.question_hi or obj.question
        else:
            result = obj.question

        cache.set(cache_key, result, timeout=3600)
        return result

    def get_answer(self, obj):
        lang = self.context.get('request').query_params.get('lang', 'en')
        cache_key = f'faq_answer_{obj.id}_{lang}'

        cached = cache.get(cache_key)
        if cached:
            return cached

        if lang == 'hi':
            result = obj.answer_hi or obj.answer
        else:
            result = obj.answer

        cache.set(cache_key, result, timeout=3600)
        return result
