from apps.news_letters.forms import NewsLetterForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class NewsLetterView(FormView):
    template_name = 'news_letters.html'
    form_class = NewsLetterForm
    success_url = reverse_lazy('success_page_url')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
