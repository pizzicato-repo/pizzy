from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import DetailView, ListView
from .models import *

def home(request):
    return HttpResponse('You are at home')

class ProfileView(DetailView):
    model = Teatcher

    def get(request, id):
        print( 'id  ', id)
        return render(request, self.template_name, {})