from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import CreateView

from .forms import RegisterForm

from blogapp.views import BasicView
# Create your views here.




class LoginView(BasicView,View):
    def get(self,request):
        context = {
            'categories':self.category(),
            'tags':self.tag(),
        }
        return render(request,'login.html', context)
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class RegisterView(BasicView,CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context