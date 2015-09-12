# coding: utf-8

#--------------//////////----------------------


#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 06/08/2015

#--------------//////////----------------------

from django.test import TestCase
from grimorio.core.models import Userc, Character, Spells
from django.db import IntegrityError

import datetime
"""
class UsercTest(TestCase):
    def setUp(self):
        self.obj =  Userc(
            name='Tork',
            login='Tork',
            password='1Ed56',
            email='tork@tork.com',
            created_at=datetime.datetime.now(),
        )

    def test_create(self):
        'Subscription must have name, loguin, password, email'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_unicode(self):
        self.assertEqual(u'Tork', unicode(self.obj))


class UsercUniqueTest(TestCase):
    def setUp(self):
        'Create a first entry to force the colision'
        Userc.objects.create(
            name='Tork',
            login='Tork',
            password='1Ed56',
            email='tork@tork.com',
            created_at=datetime.datetime.now(),
        )

    def test_create(self):
        'loguin, password, email must be unique'
        self.obj =  Userc(
            name='Tork',
            login='Tork',
            password='1Ed56',
            email='tork@tork.com',
            created_at=datetime.datetime.now(),
        )
        self.assertRaises(IntegrityError, self.obj.save)
"""
class SpellsTest(TestCase):
    def setUp(self):
        self.obj =  Spells(
            name='Bola de Fogo',
            execution='Ação Padrão',
            nivel=3,
            reach='30m',
            duration='Instantânea',
            resistence='Reflexos',
            descriptors='Fogo',
            livro='Manual Básico',
            page=156,
            tipe='Arcano',
            description='Uma das mais famosas magias deataque, a bola de fogo cria uma poderosa explosão de chamas. Você aponta o dedo e dispara uma pequena pedra fl amejante, que explode quando atinge o local escolhido, causando 6d6 pontos de dano.'
        )

    def test_create(self):
        'Subscription must have name, execution, nivel, reach, duration, resistence, descriptors, livro, page, tipe, description'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_unicode(self):
        self.assertEqual(u'Bola de Fogo', unicode(self.obj))


class SpellsUniqueTest(TestCase):
    def setUp(self):
        'Create a first entry to force the colision'
        Spells.objects.create(
            name='Bola de Fogo',
            execution='Ação Padrão',
            nivel=3,
            reach='30m',
            duration='Instantânea',
            resistence='Reflexos',
            descriptors='Fogo',
            livro='Manual Básico',
            page=156,
            tipe='Arcano',
            description='Uma das mais famosas magias deataque, a bola de fogo cria uma poderosa explosão de chamas. Você aponta o dedo e dispara uma pequena pedra fl amejante, que explode quando atinge o local escolhido, causando 6d6 pontos de dano.'
        )

    def test_create(self):
        'name, execution, nivel, reach, duration, resistence, descriptors, livro, page, tipe, description must be unique'
        self.obj =  Spells(
            name='Bola de Fogo',
            execution='Ação Padrão',
            nivel=3,
            reach='30m',
            duration='Instantânea',
            resistence='Reflexos',
            descriptors='Fogo',
            livro='Manual Básico',
            page=156,
            tipe='Arcano',
            description='Uma das mais famosas magias deataque, a bola de fogo cria uma poderosa explosão de chamas. Você aponta o dedo e dispara uma pequena pedra fl amejante, que explode quando atinge o local escolhido, causando 6d6 pontos de dano.'
        )
        self.assertRaises(IntegrityError, self.obj.save)


class CharacterTest(TestCase):
    def setUp(self):
        self.obj =  Character(
            name='Zezinho',
            PM=16,
            descricao='O Pedreiro')

    def test_create(self):
        'Subscription must have name,PM, descrição'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_unicode(self):
        self.assertEqual(u'Bola de Fogo', unicode(self.obj))

