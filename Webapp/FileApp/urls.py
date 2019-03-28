from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
#from django.contrib.staticfiles import *

urlpatterns = [
    path('',PostListView.as_view(),name='file-home' ),
    path('user/<str:username>',UserPostListView.as_view(),name='user-file' ),
    #path('?q/<str:username>',BlogSearchListView.as_view(),name='blog_search_list_view' ),
    
    path('file/<int:pk>/',PostDetailView.as_view(),name='file-detail' ),
    path('file/new/',PostCreateView.as_view(),name='file-create' ),
    path('file/<int:pk>/update/',PostUpdateView.as_view(),name='file-update' ),
     path('file/<int:pk>/delete/',PostDeleteView.as_view(),name='file-delete' ),
     path('media/Files/<int:pk>',PostDeleteView.as_view(),name='file-delete' ),
    path('about/',views.About,name='file-about' ),
    path('search/',views.search,name='search' ),
    #path('Files/<str:file>',views.getfile,name='file' )

    #url(r'^search/', views.search, name="search")
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)