
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView, UpdateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from account.forms import RegisterForm, UserInfoForm
from django.contrib.auth.views import login as django_login_view

from account.models import UserInfo


def register_view(request):
    # Should not be logged in
    if request.user.is_authenticated:
        return redirect('/cafe/')

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
    success_url = '/cafe/'
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
    return redirect('/cafe/')


def profile(request, username):
    template_name = 'account/profile.html'

    if User.objects.filter(username__contains=username).count() == 0:
        return redirect("/cafe/")
    else:
        user  = User.objects.filter(username__contains=username).first()

    context = {
        'user' : user
    }
    return render(request, template_name, context)


class UpdateUserInfoView(LoginRequiredMixin, UpdateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'account/edit_profile.html'
    success_url = '/cafe/'

    def get_object(self, queryset=None):
        if self.request.user.additionals.count() > 0:
            return self.request.user.additionals.all()[0]
        return None

class UserInfoView(LoginRequiredMixin, FormView):
    form_class = UserInfoForm
    template_name = 'account/edit_profile.html'

    def get_initial(self):
        initial = super(UserInfoView, self).get_initial()
        if self.request.user.additionals.count() > 0:
            user_info = self.request.user.additionals.all()[0]
            initial['name'] = user_info.name
            initial['email'] = user_info.email
            initial['password'] = user_info.password
        return initial

