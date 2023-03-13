from django.shortcuts import render, redirect
from .models import User
from .forms import UserForms


def main(request):
    users = User.objects.all()
    return render(request, 'interface/index.html', {'users': users})

def create(request):
    if request.method == 'POST':
        forms = UserForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('main')
    else:
        forms = UserForms()
    return render(request, 'interface/create.html', {'form': forms})

def read(request, id):
    user = User.objects.get(id=id)
    tag = User.objects.all()
    value = tag.values()[id-1]
    # print(tag.values()[id-1])
    return render(request, 'interface/read.html', {'user': value})