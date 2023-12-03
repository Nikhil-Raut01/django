from django.shortcuts import render,HttpResponse

# Create your views here.

def Home(request):
   a = 'Welcome To Django Class'
   return HttpResponse(a)


def about(request):
   return HttpResponse('Welcome To About Page')

def Contact(request):
   data = {'name':'ABC','age':34,'city':'Thane'}
   return HttpResponse(data['city'])
