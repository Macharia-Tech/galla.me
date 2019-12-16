from django.shortcuts import render
import datetime as dt


def welcome(request):
    return render(request,'welcome.html')

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})




