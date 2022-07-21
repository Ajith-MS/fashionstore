"""fashionstore URL Configuration

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
from fashionapi import views
from posts import views as pview
from store import views as proview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/',views.HelloWorldView.as_view()),
    path('goodmorning/',views.GoodMorningView.as_view()),
    path('goodevening/',views.GoodEveningView.as_view()),
    path('goodnight/',views.GoodNightView.as_view()),
    path('ajith/',views.Nameview.as_view()),
    path('varapuzha/',views.placeview.as_view()),
    path('greetings/',views.GreetingsView.as_view()),
    path('operations/cube/',views.CubeView.as_view()),
    path('operations/factorial/',views.FactorialView.as_view()),
    path('operations/wordcount/',views.WordCountView.as_view()),
    path('social/posts/',pview.PostView.as_view()),
    path('social/posts/<int:pid>/',pview.PostDetailView.as_view()),
    path('fashion/store/',proview.ProductView.as_view()),
    path('fashion/store/<int:pid>/',proview.ProductDetailView.as_view()),
    path('social/posts/likes/<int:pid>/',pview.AddLikeView.as_view()),
]
