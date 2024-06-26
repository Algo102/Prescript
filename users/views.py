from django.contrib.auth.views import PasswordResetDoneView
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from users.forms import UserCreationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/custom_password_reset_done.html'


# from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
#
# class CustomPasswordResetView(PasswordResetView):
#     template_name = 'registration/password_reset_form.html'
#     email_template_name = 'registration/password_reset_email.html'
#     subject_template_name = 'registration/password_reset_subject.txt'