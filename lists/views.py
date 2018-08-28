from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


def home_page(request):
    return render(request, 'lists/home.html')

def add_item(request, list_id):
    current_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=current_list)
    return redirect(f'lists/{current_list.id}/')

def view_list(request, list_id):
    current_list = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list': current_list})

def new_list(request):
    current_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=current_list)
    return redirect(f'lists/{current_list.id}/')
