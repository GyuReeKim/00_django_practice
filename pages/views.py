from django.shortcuts import render
from .models import Page

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    myname = request.GET.get('myname')
    myage = request.GET.get('myage')

    page = Page()
    page.myname = myname
    page.myage = myage
    page.save()
    return render(request, 'create.html')

def index(request):
    pages = Page.objects.all()
    context = {
        'pages': pages,
    }
    return render(request, 'index.html', context)

def detail(request, page_id):
    page = Page.objects.get(id=page_id)
    context = {
        'page': page,
    }
    return render(request, 'detail.html', context)

def delete(request, page_id):
    page = Page.objects.get(id=page_id)
    page.delete()
    return render(request, 'delete.html')

def edit(request, page_id):
    page = Page.objects.get(id=page_id)
    context = {
        'page': page,
    }
    return render(request, 'edit.html', context)

def update(request, page_id):
    myname = request.GET.get('myname')
    myage = request.GET.get('myage')

    page = Page.objects.get(id=page_id)
    page.myname = myname
    page.myage = myage
    page.save()
    return render(request, 'update.html')