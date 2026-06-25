from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('main-page-1/', views.main_page_1, name='main_page_1'),
    path('main-page-2/', views.main_page_2, name='main_page_2'),
    path('main-page-3/', views.main_page_3, name='main_page_3'),

    path('generator/gen-page-1/', views.gen_page_1, name='gen_page_1'),
    path('generator/gen-page-2/', views.gen_page_2, name='gen_page_2'),
    path('generator/gen-page-3/', views.gen_page_3, name='gen_page_3'),

    path('generator/news/news-page-1/', views.news_page_1, name='news_page_1'),
    path('generator/news/news-page-2/', views.news_page_2, name='news_page_2'),
    path('generator/news/news-page-3/', views.news_page_3, name='news_page_3'),

    path('users/', views.users_list, name='users_list'),
    path('users/info/', views.users_info, name='users_info'),
    path('users/info/detail/', views.users_info_detail, name='users_info_detail'),
]