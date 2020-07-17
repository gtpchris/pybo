from django.urls import path

# from bookmark.views import BookmarkLV, BookmarkDV
from bookmark import views

import logging
logger = logging.getLogger(__name__)

app_name = 'bookmark'

urlpatterns = [

    # class-based views
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    # path('blog/', base_views.BookmarkLV, name='BookmarkLV'),
    # path('blog/<int:pk>/', base_views.BookmarkDV, name='BookmarkDV'),

    # Example: /bookmark/add/
    path('add/', views.BookmarkCreateView.as_view(), name='add'),

    # Example: /bookmark/change/
    path('change/', views.BookmarkChangeLV.as_view(), name='change'),

    # Example: /bookmark/99/update/
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),

    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'),
]

