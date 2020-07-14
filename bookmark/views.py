import logging
from django.views.generic import ListView, DetailView

from bookmark.models import Bookmark

logger = logging.getLogger(__name__)

class BookmarkLV(ListView):
    logger.info("BookmarkLV 진입")
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

