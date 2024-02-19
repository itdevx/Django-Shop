from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib import messages
from Account.forms import UserSignUpForm


class SignInView(View):
    template_name = 'sign-in.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(request, 'Sign-in Successfuly!')
            return redirect('product:index')
        else:
            messages.error(request, 'username or password has not found!')
            
        
        return render(request, self.template_name)


class SignUpView(CreateView):
    template_name = 'sign-up.html'
    # success_url = reverse_lazy('product:index')
    form_class = UserSignUpForm
    success_message = 'Sign-up Successfuly!'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Sign-up has bin Successfuly!')
            return redirect('product:index')
        return super().form_valid(form)

class SignOutRequest(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Sign-Out successfuly!')
        return redirect('product:index')