from django.shortcuts import render, HttpResponse, redirect

from app01 import models
# Create your views here.
def index(request):
    data_list_all = models.book_info.objects.order_by("-rating_nums")
    data_list_all = data_list_all.values("book_name","author","book_img").distinct()
    data_list_all1 = data_list_all[0:12]
    data_list_all2 = data_list_all[12:24]
    data_list_all3 = data_list_all[24:36]
    data_list_literature = models.book_info.objects.all()
    data_list_literature1 = data_list_literature[0:12]
    data_list_literature2 = data_list_literature[12:24]
    data_list_literature3 = data_list_literature[24:36]

    queryset = {
        "data_list_all1": data_list_all1,
        "data_list_all2": data_list_all2,
        "data_list_all3": data_list_all3,
        "data_list_literature1":data_list_literature1,
        "data_list_literature2":data_list_literature2,
        "data_list_literature3":data_list_literature3,
    }
    return render(request,"user.html",queryset)