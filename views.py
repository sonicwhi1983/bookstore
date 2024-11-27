from django.shortcuts import render, redirect, get_object_or_404 
from .models import Book 

def home(request): 
    book = Book.object.all() 
    return render(request,'home.html', {'book': book})

def add_book(request):
    if request.method == 'POST': 
        title = request.POST['title'] 
        author = request.POST['author'] 
        category = request.POST['category'] 
        price = request.POST['price'] 
        quantity = request.POST['quantity'] 
        Book.objects.create(title=title, author=author, category=category, price=price,quantity=quantity) 
        return redirect('home') 
    return render(request, 'add_book.html')

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('home') 
# Create your views here.
 