from django.shortcuts import render
from .models import Image,Category,location
from django.http import Http404

def welcome(request):
    title='welcome to Galla.me'
    my_images=Image.objects.all()
    return render(request,'all-images/first.html',{"title":title,"my_images":my_images})

def image(request,image_id):
    try:
        images=Image.objects.get(id=image_id)
    except DoesNotExsist:
        raise Http404()
    return render(request,"all-images/image.html",{"images":images})

def search_category(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})

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


