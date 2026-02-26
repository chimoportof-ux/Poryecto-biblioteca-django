"""
URL configuration for django_final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from bookManager import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),

    path('signup/', views.signupuser, name='signupuser'),

    path('login/', views.loginuser, name='loginuser'),

    path('logout/', views.logoutuser, name='logoutuser'),

    path('bookList/', views.bookList, 
    name="bookList"),

    path('book/<int:id>/', views.details, name='book-detail-page'),

    path('categoryList/', views.categoryList, 
    name="categoryList"),

    path('categoryBooks<int:id>', views.categoryBooks, name='categoryBooks'),

    path('createBook/', views.create_book, 
    name="createBook"),

    path('books/<int:id>/delete/', views.delete_book, name='deleteBook'),

    path('books/<int:id>/modify/', views.modify_book, name='modifyBook'),

    path('createCategory/', views.create_category, 
    name="createCategory"),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
