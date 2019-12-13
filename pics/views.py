from django.http import HttpResponse
import datetime as dt


def welcome(request):
    return HttpResponse('Galla.me pics')



