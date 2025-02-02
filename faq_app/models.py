from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor support
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_hi = models.TextField(blank=True, null=True)  # Hindi translation
    answer_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer)

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question