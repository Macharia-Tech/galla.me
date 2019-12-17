from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^image/(\d+)',views.image,name='description'),
    url(r'^search/', views.search_category, name='search_category'),
    url(r'^London/',views.london,name='location'),
    url(r'^Amsterdam/',views.amsterdam,name='location1'),
    url(r'^SouthAfrica/',views.southafrica,name='location2'),
    url(r'^Nairobi/',views.nairobi,name='location3'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

