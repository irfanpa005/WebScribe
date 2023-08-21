from django.contrib import admin
from . models import Note, Tutorial

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','noteowner')
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.noteowner:
            obj.noteowner = request.user
        obj.save()

admin.site.register(Note, NoteAdmin)
admin.site.register(Tutorial)