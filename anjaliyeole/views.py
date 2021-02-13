from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import About, Book, Award, Interaction, ContactMe, Achievement
from .forms import Fill
import json

# Create your views here.

def index(request):
    about = About.objects.all()

    books = Book.objects.all()
    book1 = books[0]

    awards = Award.objects.all()

    interactions = Interaction.objects.all()

    if request.method == "POST" :
        form = Fill(request.POST)
        if form.is_valid():
            contactme = form.save(commit=False)
            contactme.save()
    else:
        form = Fill()


    achievementList = [ 'Certifications','Publications', 'Copyrights','Patents', 'Projects','Webinars','Articles']


    context = {
        'about': about,
        'books': books,
        'awards': awards,
        'book1': book1,
        'interactions': interactions,
        'form': form,
        'achievementList': achievementList
    }

    return render(request, 'index.html', context)


def updateInteractions(request):
    data = json.loads(request.body)
    category = data['category']

    interaction = Interaction.objects.get(category=category)
    content = interaction.content

    return JsonResponse(content, safe=False)


def updateAchievement(request):
    data = json.loads(request.body)
    category = data['category']

    achievements = Achievement.objects.get(category=category)

    content = achievements.content

    return JsonResponse(content, safe=False)