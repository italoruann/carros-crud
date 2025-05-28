

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import CarModelForm
from .models import Car, CarInventory


@method_decorator(cache_page(60 * 15), name='dispatch')
class CarsHomeView(ListView):
    model = Car
    template_name = 'index.html'
    context_object_name = 'home'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inventory'] = CarInventory.objects.first()
        return context

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(Q(model__icontains=search) | Q(brand__name__icontains=search) | Q(factory_year__icontains=search))
        return cars


class NewCarCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    
class CarUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    
    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'