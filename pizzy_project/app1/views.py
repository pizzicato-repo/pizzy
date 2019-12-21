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

login_required_m = megit log thod_decorator(login_required)
class ProfileViegit pullw(View): # TODO ? RedirectView

    @login_required_m
    def get(self, request):

        isTeatcher = Teatcher.objects.filter(user=request.user).count() > 0

        if isTeatcher :
            teatcher = Teatcher.objects.get(user=request.user)
            lboxes = LearnBox.objects.filter(owner=teatcher)
            
            return render(request, "app1/teatcher_detail.html", {'lboxes' : lboxes})
        else:
            return render(request, "app1/student_detail.html", {})

login_required_m = method_decorator(login_required)
class LB_create(CreateView):
    model = LearnBox
    fields = ['libelle', 'description', 'discipline']
    success_url = reverse_lazy('app1:profile')
    success_message = "LearnBox crée"

    def form_valid(self, form):
        teatcher = Teatcher.objects.get(user=self.request.user)
        form.instance.owner = teatcher
        return super(CreateLBView, self).form_valid(form)


login_required_m = method_decorator(login_required)
class LB_detail(DetailView):
    model = LearnBox

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['book_list'] = Book.objects.all()
    #     return context