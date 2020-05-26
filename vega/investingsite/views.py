from datetime import timezone

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import Stock


class IndexView(generic.ListView):
    template_name = 'investingsite/index.html'
    context_object_name = 'stock_list'

    def get_queryset(self):
        return Stock.objects.all()


class DetailView(generic.DetailView):
    model = Stock
    context_object_name = 'stock'
    template_name = 'investingSite/stockDetails.html'

    def get_queryset(self):
        return Stock.objects.filter(stock_id="MOWIOSL")

