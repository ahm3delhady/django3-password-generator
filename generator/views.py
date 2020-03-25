from django.shortcuts import render
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    # Don't forget to add the CSRF token in the future to implement the refresh with the same features.

    the_password = ''
    length = int(request.GET.get('length', 12))
    characters = list(ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(ascii_uppercase))

    if request.GET.get('numbers'):
        characters.extend(list(digits))

    if request.GET.get('special'):
        characters.extend(list(punctuation))

    for x in range(length):
        the_password += choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'generator/about.html')


    