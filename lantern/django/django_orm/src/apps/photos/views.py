from django.urls import reverse_lazy
from django.views.generic import FormView


from apps.photos.forms import PhotosForm


class PhotoView(FormView):
    template_name = 'add_photo_to_car_form.html'
    form_class = PhotosForm
    success_url = reverse_lazy('success_page_url')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
