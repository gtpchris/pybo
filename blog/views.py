from django.views.generic import ListView, DetailView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic import DayArchiveView, TodayArchiveView

from blog.models import Post

import logging
logger = logging.getLogger(__name__)

#--- ListView
class PostLV(ListView):
    logger.info("blog PostLV() 진입")
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


#--- DetailView
class PostDV(DetailView):
    model = Post


#--- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True


class PostMAV(MonthArchiveView):
    logger.info('PostMAV 진입1')
    model = Post
    date_field = 'modify_dt'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

