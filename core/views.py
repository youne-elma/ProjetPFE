from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def annonce(request):
    return render(request, 'core/annonce.html')


def SearchNote(request):
    return render(request, 'core/SearchNote.html')
