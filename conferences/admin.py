from django.contrib import admin

# Register your models here.
from conferences.models import ConferenceType, Category
from conferences.models import Place, Conference, Feedback


class ConferenceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ConferenceType, ConferenceTypeAdmin)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Conference)
admin.site.register(Feedback)
