# coding: utf-8

#--------------//////////----------------------


#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 06/08/2015

#--------------//////////----------------------

from django.test import TestCase
from grimorio.core.models import Userc

class AboutTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/sobre/')
    def test_get(self):
        'GET / must return status code 200.'
        self.assertEqual(200, self.resp.status_code)
        #self.assertTemplateUsed(response)

class ContactTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/contatos/')
    def test_get(self):
        'GET / must return status code 200.'
        self.assertEqual(200, self.resp.status_code)
        #self.assertTemplateUsed(response)

class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    def test_get(self):
        'GET / must return status code 200.'
        self.assertEqual(200, self.resp.status_code)
        #self.assertTemplateUsed(response)

class NewuserTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/newuser/')
    def test_get(self):
        'GET / must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

class SucessuserViewTest(TestCase):
    def setUp(self):
        s = Userc.objects.create(
            name='Tork',
            loguin='Tork',
            password='1Ed56',
            email='tork@tork.com',
        )
        self.resp = self.client.get('/newuser/%d' %s.pk)

    def test_get(self):
        'GET /newuser/1 should return status 200.'
        self.assertEqual(200, self.resp.status_code)
