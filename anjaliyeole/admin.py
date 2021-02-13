from django.contrib import admin
from .models import About, Book, Award, Interaction, ContactMe, Achievement
# Register your models here.

admin.site.register(About)
admin.site.register(Interaction)
admin.site.register(Book)
#admin.site.register(Education)
#admin.site.register(AreasOfExpertise)
admin.site.register(Award)
admin.site.register(ContactMe)
admin.site.register(Achievement)

