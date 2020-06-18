from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.cars.views import CarsListView, DealersCarListView
from apps.photos.views import PhotoView

app_name = 'cars'

urlpatterns = [
    path('cars_list/', CarsListView.as_view(), name='cars_list'),
    path('cars_photo/', login_required(PhotoView.as_view()), name='cars_photo_url'),
    path('dealers_list/', DealersCarListView.as_view(), name='dealers_list_url'),
]
