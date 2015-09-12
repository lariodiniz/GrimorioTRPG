# coding: utf-8

#--------------//////////----------------------


#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 06/08/2015

#--------------//////////----------------------

from django.test import TestCase
from grimorio.core.models import Userc

class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'core/index.html')

    def test_html(self):
        'Html must contain input controls.'

        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 4)

class NewuserTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/newuser/')

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'core/newuser.html')

    def test_html(self):
        'Html must contain input controls.'

        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)

class NewuserPostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Tork',
            loguin='Tork',
            password='1Ed56',
            email='tork@tork.com',
        )

        self.resp = self.client.post('/newuser/', data)

    def text_post(self):
        'Valid POST should redirect to /newuser/1/ '
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'Valid POST must be saved.'
        self.assertTrue(Userc.objects.exists())

class SucessuserViewTest(TestCase):
    def setUp(self):
        s = Userc.objects.create(
            name='Tork',
            loguin='Tork',
            password='1Ed56',
            email='tork@tork.com',
        )
        self.resp = self.client.get('/newuser/%d' %s.pk)

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'core/cadastrosucess.html')

    def test_html(self):
        'Html must contain input controls.'

        self.assertContains(self.resp, 'Tork')

class ContactViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/contatos/')

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'core/contatos.html')

class AboutViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/sobre/')

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'core/sobre.html')