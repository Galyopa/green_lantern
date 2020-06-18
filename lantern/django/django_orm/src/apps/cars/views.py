from django.views.generic import ListView

from apps.cars.models import Car
from apps.dealers.models import Dealer


class CarsListView(ListView):
    model = Car
    template_name = 'cars_list.html'
    context_object_name = 'cars'
    paginate_by = 10
    queryset = Car.objects.all()


class DealersCarListView(ListView):
    model = Dealer
    template_name = 'dealers.html'
    context_object_name = 'dealers'
    paginate_by = 10

    def get_queryset(self):
        if self.kwargs:
            return Dealer.objects.all().filter(user_ptr_id=int(self.kwargs.get('pk')))
        else:
            return Dealer.objects.all()
