from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('blogs/',views.blogs,name='blogs'),
    path('category/<slug:slug>',views.category_request,name='category_request'),
    path('blogs/<slug:slug>',views.blogs_detail,name='blogs_detail'),
]


