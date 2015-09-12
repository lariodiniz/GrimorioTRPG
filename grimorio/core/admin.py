# coding: utf-8

#--------------//////////----------------------


#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 15/06/2015

#--------------//////////----------------------



from django.contrib import admin

from grimorio.core.models import Character, Spells, Reach, Duration, Descriptors, Tipe, Book


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('user','name','PM','descricao')

class SpellsAdmin(admin.ModelAdmin):
    list_display = ('name','execution','nivel','reach','duration','resistence','descriptors','book','page','tipe','description')

class ReachAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DurationAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DescriptorsAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TipeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Character, CharacterAdmin)
admin.site.register(Spells, SpellsAdmin)
admin.site.register(Reach, ReachAdmin)
admin.site.register(Duration, DurationAdmin)
admin.site.register(Descriptors, DescriptorsAdmin)
admin.site.register(Tipe, TipeAdmin)
admin.site.register(Book, BookAdmin)

