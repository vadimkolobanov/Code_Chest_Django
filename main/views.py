from django.shortcuts import render


def index(request):
    '''Главная страница сайта'''
    return render(request, 'main/index.html')


def main(request):
    '''Основная страница'''
    return render(request, 'main/main.html')