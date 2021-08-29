from django.shortcuts import render
from BRMapp2.forms import NewBookForm
from BRMapp2 import models
from django.http import HttpResponse,HttpResponseRedirect

def newBook(request):
    form = NewBookForm()
    res = render(request,"BRMapp2/new_book.html",{"form":form})
    return res
def add(request):
    if request.method=='POST': #Request will accesses here
        form = NewBookForm(request.POST) # when request send,that requested data will access here
        book = models.Book() #now we are going to add data our in database
        book.title = form.data['title'] #'title' means whatever we are 'filled form' that filled values are access here
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save() #now data will save in tabel
    s="Record stored<br><a href='/BRMapp2/view-books'>View All Books</a>"
    return HttpResponse(s)

def viewBooks(request):
    books = models.Book.objects.all() #if we are sending data on table,then always we have to use 'model class'
    res = render(request,BRMapp2/view_books.html,{'books':books})
    return res

def editBook(request):
    book = models.Book.objects.get(id=request.GET['bookid'])
    fields = {'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form = NewBookForm(initial=fields)
    res = render(request,"BRMapp2/edit_book.html",{'form':form,'book':book})
    return res
def edit(request):
    if request.method=="POST":
        form = NewBookForm(request.POST)
        book = models.Book()
        book.id = request.POST['bookid']
        book.title = form.data['title']
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save()
    return HttpResponseRedirect("BRMapp2/view-books")

def deleteBook(request):
    bookid = request.GET['bookid'] #when we clicked on delete button then that all data will access here...
    book = models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect("BRMapp2/view-books")

def SearchForm(request):
    form = searchbook()
    res = render(request,"BRMapp2/search_book.html",{'form':form})
    return res
def search(request):
    # if request.method=='POST'
    form = SearchForm(request.POST)
    books = models.Book.object.filter(title=form.data['title'])
    res = render(request,"BRMapp2/search_book.html",{'form':form, 'books':books})
    return res
