from django.urls import include
from django.conf.urls import url
from BRMapp2 import views

urlpatterns =[
    url('newBook',views.newBook),
    url('add',views.add),
    url('viewBooks',views.viewBooks),
    url('editBook',views.editBook),
    url('deleteBook',views.deleteBook),
    url('edit',views.edit),
    url('searchForm',views.SearchForm),
    url('search',views.search)
]
