from django.shortcuts import render
from django.http import HttpResponse

# ========== MAIN PAGE ==========
def main_page_1(request):
    return HttpResponse("<h1>Main Page 1</h1><p>Добро пожаловать на главную страницу 1</p>")

def main_page_2(request):
    return HttpResponse("<h1>Main Page 2</h1><p>Добро пожаловать на главную страницу 2</p>")

def main_page_3(request):
    return HttpResponse("<h1>Main Page 3</h1><p>Добро пожаловать на главную страницу 3</p>")

# ========== GENERATOR ==========
def gen_page_1(request):
    return HttpResponse("<h1>Generator Page 1</h1><p>Страница генератора 1</p>")

def gen_page_2(request):
    return HttpResponse("<h1>Generator Page 2</h1><p>Страница генератора 2</p>")

def gen_page_3(request):
    return HttpResponse("<h1>Generator Page 3</h1><p>Страница генератора 3</p>")

# ========== GENERATOR/NEWS ==========
def news_page_1(request):
    return HttpResponse("<h1>News Page 1</h1><p>Новостная страница 1</p>")

def news_page_2(request):
    return HttpResponse("<h1>News Page 2</h1><p>Новостная страница 2</p>")

def news_page_3(request):
    return HttpResponse("<h1>News Page 3</h1><p>Новостная страница 3</p>")

# ========== USERS ==========
def users_list(request):
    return HttpResponse("<h1>Users List</h1><p>Список пользователей</p>")

def users_info(request):
    return HttpResponse("<h1>Users Info</h1><p>Информация о пользователях</p>")

def users_info_detail(request):
    return HttpResponse("<h1>Users Info Detail</h1><p>Детальная информация о пользователе</p>")