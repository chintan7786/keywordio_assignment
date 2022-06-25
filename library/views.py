from atexit import register
from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import *
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
def index(request):
    books = Book.objects.all()

    context = {
        'books' : books
    }
    return render(request, 'library/index.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('account not active')
        else:
            print('someone tried to login and failed')
            print("username: {} and password: {}".format(username, password))
            return HttpResponse('invalid login details supplied')
    return render(request, 'library/login.html')


def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        username = request.POST['username']
        password = request.POST['password']
        print(user_name, username, password)

        group = Group.objects.get(name='student')

        user_object = User.objects.create_user(
            username = username,
            first_name = user_name,
            password = password
        )

        user_object.groups.add(group)
        print('added to student group')
        print('user created') if user_object else print('failed to create user')
        return redirect('user_login')

    return render(request, 'library/sign_up.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('logout_page')


def logout_page(request):
    return render(request, 'library/logout_page.html')


@allowed_users(allowed_roles=['admin'])
def create_book(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author = request.POST['author']
        print(book_name, author)

        book_object = Book.objects.create(
            book_name = book_name,
            author = author
        )

        print('Book created') if book_object else print('failed to create Book')
        return redirect('index')

    return render(request, 'library/create_book.html')


class DeletePost(DeleteView):
    model = Book
    template_name = 'library/delete_book.html'
    success_url = reverse_lazy('index')


@allowed_users(allowed_roles=['admin'])
def update_book(request, pk):
    book_object = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author = request.POST['author']
        book_object.book_name = book_name
        book_object.author = author
        book_object.save()
        print('value updated successfully')
        return redirect('index')
   
    print(book_object)
    context = {
        'book' : book_object
    }
    return render(request, 'library/update_book.html', context)
