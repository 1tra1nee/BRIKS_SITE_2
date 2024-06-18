"""psy1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import index_page
from myapp.views import disciplines_page
from myapp.views import abitur_page
from myapp.views import contacts_page
from myapp.views import science_page
from myapp.views import experts_page
from myapp.views import materials_page
#from myapp.views import login_page
from myapp import views                                        #Добавил пути для авторизации 14:49
from myapp.views import registerMod #from . import views       #Добавил блок для модалки авторизации 22:49
#from myapp.views import RegisterUser                           #Добавил блок для модалки авторизации 23:44


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('disciplines/', disciplines_page),
    path('abitur/', abitur_page),
    path('contacts/', contacts_page),
    path('science/', science_page),
    path('teachers/', experts_page),
    path('materials/', materials_page),
    path('loginMe/', registerMod),
    path('login/', views.LoginView.as_view(), name='login'),             #Добавил пути для авторизации 14:49
    path('logout/', views.LogoutView.as_view(), name='logout'),          #Добавил пути для авторизации 14:49
    path('register/', views.RegisterView.as_view(), name='register'),    #Добавил пути для авторизации 14:49
    #path('registerMod/', RegisterUser.as_view(), name="registerMod"),    #Добавил блок для модалки авторизации 22:49
    #path('accounts', include("django.contrib.auth.urls"))
    # path('login/', views.loginUser, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    # path('register/', views.registerUser, name="register"),
    #path('profile/<str:username>/', views.userProfile, name="user-profile"),
    # path('account/', views.userAccount, name="account"),
    # path('edit-account/', views.editAccount, name="edit-account"),

]
