# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 06/08/2015

#--------------//////////----------------------


from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from grimorio.core.forms import CharacterForm, UserForm, UsercForm, CharacterForm, SpellsForm
from grimorio.core.models import Character, Spells



class AboutViews(TemplateView):
    template_name = 'core/sobre.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'usuario': self.request.user.username})

class ContactViews(TemplateView):
    template_name = 'core/contatos.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'usuario': self.request.user.username})

class HomepageViews(View):
    template_name = 'core/index.html'
    form_class = UsercForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/personagens/%d' %request.user.pk)
        else:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/personagens/%d' %user.pk)
            else:
                #Usuario Broqueado aqui
                pass
        else:
            form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

class ExitView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')


class NewuserViews(View):
    template_name = 'core/newuser.html'
    form_class = UserForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/personagens/%d' %request.user.pk)
        else:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/newuser/%s' %obj.pk)

        return render(request, self.template_name, {'form': form})


class NewcharacterViews(View):
    template_name = 'core/newcharacter.html'
    form_class = CharacterForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/personagens/%d' %request.user.pk)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/personagens/%d' %request.user.pk)

        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewcharacterViews, self).dispatch(*args, **kwargs)

class SucessuserView(DetailView):
    model = User
    template_name = 'core/cadastrosucess.html'

    def get_context_data(self, **kwargs):
        context = super(SucessuserView, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user.username
        return context

class CharacterView(ListView):
    template_name = 'core/personagens.html'


    def get_queryset(self):
        return Character.objects.filter(user=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(CharacterView, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user.username
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CharacterView, self).dispatch(*args, **kwargs)

class CharacterdetailView(DetailView):
    template_name = 'core/detailpersonagem.html'
    model = Character

    def get_context_data(self, **kwargs):
        context = super(CharacterdetailView, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user.username
        context['contador'] = [0,1,2,3,4,5,6,7,8,9]
        context['personagens'] = Character.objects.filter(user=self.request.user.pk)

        return context
    def post(self, request, *args, **kwargs):
        return super(CharacterdetailView, self).dispatch(*args, **kwargs)


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CharacterdetailView, self).dispatch(*args, **kwargs)

class NewmagicViews(View):
    template_name = 'core/newmagic.html'
    form_class = SpellsForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponseRedirect('/personagens/%d' %request.user.pk)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/personagens/%d' %request.user.pk)

        return render(request, self.template_name, {'form': form})

class MagiadetailView(ListView):
    template_name = 'core/magiapersonagem.html'

    def get_queryset(self):
        a= int(str(self.request.path).split('/')[2])
        return Spells.objects.filter(nivel=int(a))

    def get_context_data(self, **kwargs):
        print self.request.POST
        context = super(MagiadetailView, self).get_context_data(**kwargs)
        context['usuario'] = self.request.user.username
        context['personagens'] = Character.objects.filter(user=self.request.user.pk)
        context['nivel_magia'] = str(self.request.path).split('/')[2]
        return context

    def post(self, request, *args, **kwargs):
        form = request.POST

        try:
            obj= Character.objects.get(pk=int(form["Personagen"].split(' - ')[0]))
            spel= Spells.objects.get(name=form["Magia"].split(' - ')[0])
            obj.spells.add(spel)
            return HttpResponseRedirect('/grimorio/%d' %obj.pk)
        except:
            return HttpResponseRedirect('/magicdetail/%d' %int(str(request.path).split('/')[2]))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MagiadetailView, self).dispatch(*args, **kwargs)