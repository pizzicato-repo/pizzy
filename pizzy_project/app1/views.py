from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View, DetailView, ListView, TemplateView, CreateView
from .models import *

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy

def home(request):
    return HttpResponse('You are at home')

class AccueilView(TemplateView):
    template_name = "app1/accueil.html"

login_required_m = method_decorator(login_required)
class ProfileView(View): # TODO ? RedirectView

    @login_required_m
    def get(self, request):

        isTeatcher = Teatcher.objects.filter(user=request.user).count() > 0

        if isTeatcher :
            return render(request, "app1/teatcher_detail.html", {})
        else:
            return render(request, "app1/student_detail.html", {})

login_required_m = method_decorator(login_required)
class CreateLBView(CreateView):
    model = LearnBox
    fields = ['libelle', 'description', 'discipline']
    success_url = reverse_lazy('app1:profile')
    success_message = "LearnBox crée"

    def form_valid(self, form):
        print( "self.request.user = ", self.request.user)

        teatcher = Teatcher.objects.filter(user=self.request.user)[0]
        print( "teatcher = ", self.request.user)
        form.instance.owner = teatcher
        return super(CreateLBView, self).form_valid(form)