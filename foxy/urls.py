"""foxy URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from auth import views as auth_view
from social import views as social_view

urlpatterns = [
    path('admin/', admin.site.urls),



    #auth
    path("login/", auth_view.Login.as_view(), name = "login"),
    path("logout/", auth_view.Logout.as_view(), name = "logout"),
    path("signup/", auth_view.Signup.as_view(), name = "signup"),

    #social
    path("profile/", social_view.Profile.as_view(), name = "profile"),
    path("post/", social_view.Post.as_view()),
    path("", social_view.Wall.as_view(), name = "home"),
    #like
    path("post/<int:pk>/like", social_view.PostLike.as_view()),
    #comment
    path("post/<int:pk>/comment", social_view.PostComment.as_view())
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)