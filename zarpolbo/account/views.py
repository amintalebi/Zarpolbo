from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from account.forms import RegisterForm
from django.contrib.auth.views import login as django_login_view


def register_view(request):
    # Should not be logged in
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            if User.objects.filter(username=username).count() != 0:
                form.add_error('username', 'A user with this username already exists.')
            else:
                User.objects.create_user(username=username, email=email, password=password, first_name=name)
                return redirect('/account/login/')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


class LoginView(FormView):
    success_url = '/'
    form_class = AuthenticationForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)

        return super(LoginView, self).form_valid(form)


@login_required(login_url='/account/login/')
def logout_view(request):
    logout(request)
    return redirect('/')
