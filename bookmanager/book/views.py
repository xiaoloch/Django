from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    # return HttpResponse('OK')
    context={"name1":"西游记", "name2":"三国演义"}
    return render(request,"book/index.html",context=context)

