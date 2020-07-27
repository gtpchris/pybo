from django.urls import path

from psytest import views


app_name = 'psytest'

urlpatterns = [

    # Example: /psytest/
    path('', views.list, name='list'),

    # Example: /psytest/list
    path('list/', views.list, name='list'),

    # Example: /psytest/9/detail/
    path('<int:testsheet>/detail/', views.detail, name='detail'),

    # Example: /psytest/9/testDetail/detailList/
    path('<int:testsheet>/detail/detailList', views.detailList, name='detailList'),

    # Example: /psytest/9/testDetail/detailList/9
    path('<int:testsheet>/detail/detailList/<int:testCaseId>', views.testCase, name='testCase'),

]