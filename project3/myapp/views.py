from django.shortcuts import render
from .models import Django_Table
from .forms import Django_form

# Create your views here.
def index(request):
    os = Django_Table.objects.all()
    return render(request,'index.html',{'data':os})

def form_data(request):
    if request.method =="POST":
        f = Django_form(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = Django_form()
    return render(request,'forms.html',{'form':f})
