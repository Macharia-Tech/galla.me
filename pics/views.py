from django.shortcuts import render
from .models import Image,Category,location
from django.http import Http404

# Create your views here.
def start(request):
    title='welcome to Galla.me'
    images=Image.London()
    return render(request,'all-images/first.html',{"title":title,"images":images})

def image(request,image_id):
    try:
        images=Image.objects.get(id=image_id)
    except DoesNotExsist:
        raise Http404()
    return render(request,"all-images/image.html",{"images":images})

def search_category(request):
    search_term=request.GET.get("category")
    searched_categories=Image.search(search_term)
    return render (request,'all-images/search.html',{"searched_categories":searched_categories})

def london(request):
    location=Image.London()
    return render (request,'all-images/location.html',{"location":location})

def amsterdam(request):
    location=Image.Amsterdam()
    return render (request,'all-images/location1.html',{"location":location})

def southafrica(request):
    location=Image.SouthAfrica()
    return render (request,'all-images/location2.html',{"location":location})
    
def nairobi(request):
    location=Image.Nairobi()
    return render (request,'all-images/location3.html',{"location":location})
