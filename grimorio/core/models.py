# coding: utf-8

#--------------//////////----------------------


#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 06/08/2015

#--------------//////////----------------------

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

import datetime

class Reach(models.Model):
    name=models.CharField(_('Nome'), max_length=100, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Alcance')
        verbose_name_plural = _(u'Alcances')

class Duration(models.Model):
    name=models.CharField(_('Nome'), max_length=100, unique=True)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Duração')
        verbose_name_plural = _(u'Durações')

class Descriptors(models.Model):
    name=models.CharField(_('Nome'), max_length=100, unique=True)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Descritor')
        verbose_name_plural = _(u'Descritores')

class Tipe(models.Model):
    name=models.CharField(_('Nome'), max_length=100, unique=True)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Tipo')
        verbose_name_plural = _(u'Tipos')

class Book(models.Model):
    name=models.CharField(_('Nome'), max_length=100, unique=True)
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Livro')
        verbose_name_plural = _(u'Livros')

class Spells(models.Model):
    name=models.CharField(_('Nome'), max_length=250, unique=True)
    execution=models.CharField(_(u'Execução'), max_length=100)
    nivel=models.IntegerField(_('Nivel da Magia'))
    reach=models.ForeignKey('Reach', verbose_name=_('Alcance'), blank=True)
    target=models.CharField(_('Alvo'), max_length=250)
    duration=models.ForeignKey('Duration', verbose_name=_(u'Duração'), blank=True)
    resistence=models.CharField(_('Teste de Resistencia'), max_length=100)
    descriptors=models.ForeignKey('Descriptors', verbose_name=_(u'Descritores'), blank=True)
    book=models.ForeignKey('Book', verbose_name=_(u'Livros'), blank=True)
    page=models.IntegerField(_('Pagina'))
    tipe=models.ForeignKey('Tipe', verbose_name=_(u'Tipo'), blank=True)
    description=models.TextField(_(u'Descrição'), blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = _(u'Magia')
        verbose_name_plural = _(u'Magias')

    def get_absolute_url(self):
        return reverse('magicdetail', kwargs={'pk': self.pk})


class Character(models.Model):
    user = models.ForeignKey(User,verbose_name=_('Usuarios'), blank=True)
    name=models.CharField(_('Nome'), max_length=100)
    PM=models.IntegerField(_('PM MAX'))
    spells=models.ManyToManyField('Spells', verbose_name=_('Magias'), blank=True)
    descricao=models.CharField(_(u'Descrição'), max_length=250)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Personagen')
        verbose_name_plural = _(u'personagens')

    def get_absolute_url(self):
        return reverse('detail-character', kwargs={'pk': self.pk})
