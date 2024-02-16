from django.shortcuts import render


def home(request):
    return render(request, 'item/home.html')
