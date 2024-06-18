# from django.dispatch.dispatcher import receiver
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.urls import conf
# from .models import Profile
# from .forms import CustomUserCreationForm, ProfileForm
# from .utils import paginateProfiles, searchProfiles
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView          #Добавил блок для авторизации 14:49
from django.views.generic.edit import CreateView                     #Добавил блок для авторизации 14:49
from .models import User                                             #Добавил блок для авторизации 14:49
from django.contrib.auth.forms import UserCreationForm               #Добавил блок для авторизации 14:49

from django.shortcuts import render, redirect                        #Добавил блок для модалки авторизации 22:49
from django.contrib.auth.models import User                          #Добавил блок для модалки авторизации 22:49
from django.contrib.auth import login, authenticate                  #Добавил блок для модалки авторизации 22:49
from .mixins import DataMixin                                        #Добавил блок для модалки авторизации 23:44
from django.views.generic import CreateView                          #Добавил блок для модалки авторизации 23:44


def index_page(request):
    return render(request, 'index.html')

def disciplines_page(request):
    return render(request, 'disciplines.html')

def abitur_page(request):
    return render(request, 'abitur.html')

def contacts_page(request):
    return render(request, 'contact.html')

def science_page(request):
    return render(request, 'science.html')

def experts_page(request):
    return render(request, 'experts.html')

def materials_page(request):
    return render(request, 'materials.html')

def login_page(request):
    return render(request, 'loginMe.html')


def registerMod(request):                                                                                   #Добавил блок для модалки авторизации 22:49
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']
    #
    #     if password == confirm_password:
    #         try:
    #             user = User.objects.create_user(username=username, email=email, password=password)
    #             user.save()
    #             login(request, user)
    #             return redirect('home')  # Замените 'home' на нужный маршрут
    #         except:
    #             # Обработка ошибок регистрации
    #             pass
    return render(request, 'loginMe.html') #'registration_modal.html')                                                    #Добавил блок для модалки авторизации 22:49

# class RegisterUser(DataMixin, CreateView):                                                               #Добавил блок для модалки авторизации 23:44
#     form_class = UserCreationForm
#     template_name = 'templates/users/loginMe.html'
#     #success_url = reverse_lazy('')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         #c_def = self.get_context_data(title='Регистрация')
#         return dict(list(context.items())) #+ list(c_def.items()))                                         #Добавил блок для модалки авторизации 23:44

#Добавил classes для авторизации 14:49
class LoginView(LoginView):
    template_name = 'login.html'


class LogoutView(LogoutView):
    next_page = '/'


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/'


# def loginUser(request):
#     page = 'login'
#
#     if request.user.is_authenticated:
#         return redirect('users/profiles')
#
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'Такого пользователя нет в системе')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return redirect(request.GET['next'] if 'next' in request.GET else 'account')
#
#         else:
#             messages.error(request, 'Неверное имя пользователя или пароль')
#
#     return render(request, 'users/login_register.html')
#
#
# def logoutUser(request):
#     logout(request)
#     messages.info(request, 'Вы вышли из учетной записи')
#     return redirect('login')
#
#
# def registerUser(request):
#     page = 'register'
#     form = CustomUserCreationForm()
#
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#
#             messages.success(request, 'Аккаунт успешно создан!')
#
#             login(request, user)
#             return redirect('edit-account')
#
#         else:
#             messages.success(
#                 request, 'Во время регистрации возникла ошибка')
#
#     context = {'page': page, 'form': form}
#     return render(request, 'users/login_register.html', context)
#
# def profiles(request):
#     profiles, search_query = searchProfiles(request)
#     custom_range, profiles = paginateProfiles(request, profiles, 6)
#     context = {'profiles': profiles, 'search_query': search_query,
#                'custom_range': custom_range}
#     return render(request, 'users/profiles.html', context)
#
#
# def userProfile(request, username):
#     profile = Profile.objects.get(username=username)
#
#     main_skills = profile.skills.all()[:2]
#     extra_skills = profile.skills.all()[2:]
#
#     context = {'profile': profile, 'main_skills': main_skills,
#                "extra_skills": extra_skills}
#     return render(request, 'users/user-profile.html', context)
#
# def profiles_by_skill(request, skill_slug):
#     skill = get_object_or_404(Skill, slug=skill_slug)
#     profiles = Profile.objects.filter(skills__in=[skill])
#     context = {
#         "profiles": profiles
#     }
#
#     return render(request, "users/profiles.html", context)
#
# @login_required(login_url='login')
# def userAccount(request):
#     profile = request.user.profile
#
#     skills = profile.skills.all()
#     projects = profile.project_set.all()
#
#     context = {'profile': profile, 'skills': skills, 'projects': projects}
#     return render(request, 'users/account.html', context)
#
#
# @login_required(login_url='login')
# def editAccount(request):
#     profile = request.user.profile
#     form = ProfileForm(instance=profile)
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#
#             return redirect('account')
#
#     context = {'form': form}
#     return render(request, 'users/profile_form.html', context)


















