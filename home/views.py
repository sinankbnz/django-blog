from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from home.forms import MakePost
from home.models import Post



def index(request):
    post = {
        'post':Post .objects.all()
    }
    return render(request, 'index.html',post)
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


@login_required   
def make(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'make.html',{'form':MakePost()})

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('index')




def read(request, id):
    post = {
        'post':Post .objects.get(id=id)
    }
    return render(request, 'read.html',post)


def edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request, 'edit.html',{'form':MakePost(instance=post)})


def register(request):
    form = UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    return render(request,'register.html',{'form':form})

