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