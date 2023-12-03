from django.shortcuts import render

# Create your views here.
def Index(request):
   a = "My name is Khan"
   b = ['ABC',35,"Thane",3434343]
   return render(request,'index.html',{'data':a,'data1':b})

def About(request):
   return render(request,'about.html')
