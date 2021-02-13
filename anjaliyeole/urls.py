from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('update-interaction/', views.updateInteractions, name='update-interaction'),
    path('update-achievement/', views.updateAchievement, name='update_achievement'),

]