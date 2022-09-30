"""blogpro URL Configuration

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
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name="main"),
    path('home',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('addblog',views.addblog,name='addblog'),
    path('contact',views.contact,name='contact'),
    path('single<int:id>',views.blogsingle,name='single'),
    path('pdfcreate<int:id>',views.pdfcreate,name='create'),
    path('Edit',views.Edit,name='Edit'),
    path('edit_blog<int:id>',views.edit_blog,name='edit_blog'),
    path('delete_blog<int:id>',views.delete_blog,name='delete_blog'),
    path('Contacts',views.Contacts,name='Contacts'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('s',views.signupform,name='signupform'),
    path('l',views.loginform,name='loginform'),
    path(r'^password/$', views.change_password, name='change_password'),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
