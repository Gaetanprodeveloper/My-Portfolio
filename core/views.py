from django.shortcuts import render
from core.models import *
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        telephone=request.POST['telephone']
        message=request.POST['message']
        
        customer=Customer.objects.create(name=name,email=email,telephone=telephone,message=message)
        messages.success(request, 'Thank you for your message! I will get back to you soon')
        customer.save()
    
    return render(request,'index.html')
