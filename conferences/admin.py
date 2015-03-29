from django.contrib import admin

# Register your models here.
from conferences.models import ConferenceType, Category, Place, Conference, Feedback

admin.site.register(ConferenceType)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Conference)
admin.site.register(Feedback)
