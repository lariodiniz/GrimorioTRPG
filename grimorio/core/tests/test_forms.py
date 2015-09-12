# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 07/08/2015

#--------------//////////----------------------

from django.test import TestCase
from grimorio.core.forms import UsercForm

class UsercForm_Test(TestCase):
    def test_has_fields(self):
        'Form must have 2 fields.'
        form = UsercForm()
        self.assertItemsEqual(['login','password'], form.fields)


