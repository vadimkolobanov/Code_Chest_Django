from django.shortcuts import render


def index(request):
    '''Главная страница сайта'''
    return render(request, 'main/main.html')
