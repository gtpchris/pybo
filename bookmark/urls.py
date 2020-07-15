from django.urls import path

from bookmark.views import BookmarkLV, BookmarkDV
import logging
logger = logging.getLogger(__name__)

app_name = 'bookmark'

urlpatterns = [

    # class-based views
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
    # path('blog/', base_views.BookmarkLV, name='BookmarkLV'),
    # path('blog/<int:pk>/', base_views.BookmarkDV, name='BookmarkDV'),
]

