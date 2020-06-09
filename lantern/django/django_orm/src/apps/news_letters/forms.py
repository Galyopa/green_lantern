from django.forms import ModelForm

from apps.news_letters.models import NewsLetter


class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']
