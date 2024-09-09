from django.shortcuts import redirect, render

from .models import event_details
from .forms import eventform
# Create your views here.
def index(request):
    data = event_details.objects.all()
    context = {
        "event_data":data
    }
    return render(request,'index.html',context)
    
def base(request):
    return render(request,"base.html")

def detail(request,id):
    context = {
        "data": event_details.objects.get(id=id)
    }
    return render(request,"detail.html",context)

def add(request):
    form = eventform(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form":form
    }
    return render(request,"add.html",context)