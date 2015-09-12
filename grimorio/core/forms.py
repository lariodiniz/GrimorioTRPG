# coding: utf-8

#--------------//////////----------------------


#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 06/08/2015

#--------------//////////----------------------

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from grimorio.core.models import Character, Spells


class SpellsForm(forms.ModelForm):

    class Meta:
        model= Spells
        fields = '__all__'

class UsercForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password')

    def __init__(self, *args, **kwargs):
        self.base_fields['username'].help_text = ''
        self.base_fields['password'].widget = forms.PasswordInput()

        self.base_fields['username'].label =_('Login')

        super(UsercForm, self).__init__(*args, **kwargs)


    def get_absolute_url(name):
        return reverse('personagens', kwargs={'name': name})

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')

    confirm_the_password=forms.CharField(label=_('Confirme a Senha'), max_length=30, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        print self.base_fields

        self.base_fields['password'].help_text = '<br/>Informe uma senha segura'
        self.base_fields['username'].help_text = '<br/>Somente letras, dígitos e @/./+/-/_.'

        self.base_fields['password'].widget = forms.PasswordInput()

        self.base_fields['username'].label =_('Login')
        self.base_fields['first_name'].label =_('Nome')
        self.base_fields['last_name'].label =_('Sobre Nome')
        self.base_fields['email'].label =_('Email')
        self.base_fields['password'].label =_('Senha')

        super(UserForm, self).__init__(*args, **kwargs)


    def clean_confirm_the_password(self):
        if self.cleaned_data['confirm_the_password'] != self.data['password']:
            raise forms.ValidationError('Confirmacao da senha nao confere!')
        return self.cleaned_data['confirm_the_password']

    def save(self, commit=True):
        usuario = super(UserForm, self).save(commit=False)
        usuario.set_password(self.cleaned_data['password'])
        if commit:
            usuario.save()
        return usuario

class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields =['name','PM','descricao']


