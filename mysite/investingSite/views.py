from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'investingSite/index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return HttpResponse("Put the list of top investments here")