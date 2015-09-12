# coding: utf-8

#--------------//////////----------------------


#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 06/08/2015

#--------------//////////----------------------

"""grimorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin, auth
from grimorio.core.views import HomepageViews, NewuserViews, SucessuserView, ContactViews, AboutViews, CharacterView, ExitView, NewcharacterViews, CharacterdetailView, NewmagicViews, MagiadetailView

urlpatterns = [
    url(r'^$', HomepageViews.as_view(), name='homepage'),
    url(r'^logout/$', ExitView.as_view(), name='sair'),
    url(r'^newuser/$', NewuserViews.as_view(), name='newuser'),
    url(r'^newuser/(?P<pk>[\w_-]+)$', SucessuserView.as_view(), name='cadastro-sucesso'),
    url(r'^newcharacter/$', NewcharacterViews.as_view(), name='newcharacter'),
    url(r'^contatos/$', ContactViews.as_view(), name='contatos'),
    url(r'^sobre/$', AboutViews.as_view(), name='sobre'),
    url(r'^personagens/(?P<pk>[\w_-]+)$', CharacterView.as_view(), name='personagens'),
    url(r'^grimorio/(?P<pk>[\w_-]+)$', CharacterdetailView.as_view(), name='detail-character'),
    url(r'^newmagic/$', NewmagicViews.as_view(), name='newmagic'),
    url(r'^magicdetail/(?P<pk>[\w_-]+)$', MagiadetailView.as_view(), name='magicdetail'),
    url(r'^admin/', include(admin.site.urls)),
]
