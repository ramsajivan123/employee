"""
URL configuration for employee_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from employees.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('logout',logout_page,name='logout'),
    path('dashboard',admin_dashboard,name='dashboard'),
    path('add_recoards',add,name='add_recoards'),
    path('view_recoards',view_employee,name='view_recoards'),
    path('edit_recoards',edit_employee,name='edit_recoards'),
    path('about_page',about,name='about_page'),
    path('feedback',feedback_form,name='feedback_page'),
    path('view_feedback',view_feedback,name='view_feedback'),
    path('edit_action/<int:id>',edit_form,name='edit_action'),
    path('delete_action/<int:id>',del_action,name='delete_action'),
    path('change_password',change_pass,name='change_password'),
    path('footer_page',footer,name='footer_page'),
    path('gallery',photos,name='gallery')

]

urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) # this code is show media file in view records