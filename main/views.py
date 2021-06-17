from django.shortcuts import render, redirect
from .models import hero

# Create your views here.
def index(request):
    if request.method == 'GET':
        heros = hero.objects.all().order_by('-score')
        return render(request, 'main/index.html', {'heros':heros})
    else:
        name = request.POST.get('name')
        score = request.POST.get('score')
        newHero = hero.objects.create(name=name, score=score)
        newHero.save()
        return redirect('index')


