from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    #create an instance
    form = UserCreationForm()
    return render(request, 'users/register.html', {'FORMvariableTHIS': form})