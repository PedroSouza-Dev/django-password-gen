from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):


    characters = list('abcdefghijklmnopqrstuvxwyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXWYZ')) #EXTENDER A LISTA DAS MINUSCULAS
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()-=+'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12)) # vai requisitar o tamanho pelo parametro name=length

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')

def who(request):
    return render(request, 'generator/who.html')

def contact(request):
    return render(request, 'generator/contact.html')