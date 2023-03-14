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
            succes = forms.save()
            return redirect('read-user', succes.id)
    else:
        forms = UserForms()
    return render(request, 'interface/create.html', {'form': forms})

def read(request, id):
    user = User.objects.get(id=id)
    tag = User.objects.all()
    value = tag.values().get(id=id)
    print(value)
    return render(request, 'interface/read.html', {
        'user': value,
        'name': user,
        })

def update(request):
    user = User.objects.all()
    return render(request, 'interface/update.html', {'user': user})

def update_user(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        forms = UserForms(request.POST, instance=user)
        if forms.is_valid():
            succes = forms.save()
            return redirect('read-user', succes.id)
    else:
        forms = UserForms(instance=user)
    return render(request, 'interface/update_user.html', {
        'form': forms,
        'user': user,
        })

def delete(request):
    user = User.objects.all()
    return render(request, 'interface/delete.html', {'user': user})

def delete_user(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect('main')
    return render(request, 'interface/delete_user.html', {'user': user})