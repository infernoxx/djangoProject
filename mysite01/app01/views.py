from django.shortcuts import render, HttpResponse, redirect

from app01.models import test02
# Create your views here.
def index(request):
    data_list = test02.objects.all()
    if request.method == "GET":
        nid = request.GET.get('nid')
        test02.objects.filter(id=nid).delete()
        return render(request,"user.html",{"datalist":data_list})



    name = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    test02.objects.create(name=name,password=pwd,age=age)


    return render(request,"user.html",{"datalist":data_list})