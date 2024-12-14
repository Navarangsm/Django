from django.shortcuts import render,redirect
from . forms import personForm
from . models import person

def signup(request):
    if request.method =='POST':
        form = personForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = personForm()
    return render(request,'person.html',{'form':form})

def user_list(request):
    users = person.objects.all()
    return render(request,'user_list.html',{'users':users})


