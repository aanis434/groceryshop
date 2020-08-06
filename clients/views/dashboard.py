from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, TemplateView

from clients.forms import LoginClientForm


class IndexView(TemplateView):
    template_name = 'clients/index.html'


class LoginView(FormView):
    form_class = LoginClientForm
    template_name = 'clients/auth/login.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():

            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active and user.client:
                    login(request, user)

                    return HttpResponseRedirect('/admin/')
                else:
                    raise PermissionDenied()
            else:
                messages.error(request, "Login Failed! Enter the email and password correctly")
                return redirect('/admin/login')
        else:
            return render(request, self.template_name, {'form': form})
