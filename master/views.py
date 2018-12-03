from django.shortcuts import render
from django.views import generic
from .models import Company, Item


class MyView(generic.ListView):
    model = Item
    template_name = 'master/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Item.objects.filter(company=self.kwargs['pk'])


