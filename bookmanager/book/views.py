from django.shortcuts import render,redirect
from django.http import JsonResponse


# Create your views here.
from django.http import HttpResponse
def index(request):
    # return HttpResponse('OK')
    context={"name1":"西游记", "name2":"三国演义"}
    return render(request,"book/index.html",context=context)

def GetUrl(request, para1, para2):
    print(para1, para2)
    param = request.GET
    site1= param.getlist('key')[0]
    site2= param.getlist('key')[1]
    return HttpResponse('%s %s是个好地方,其中 %s %s 尤其的好' % (para1, para2, site1, site2))

def register(request):
    # form = request.POST
    # print(form)
    # print(type(form))
    json_by = request.body
    print(json_by)
    print(type(json_by))
    json_str = json_by.decode()
    print(json_str)
    print(type(json_str))
    import json
    json_js = json.loads(json_str)
    print(json_js)
    print(type(json_js))
    return HttpResponse("OK")

def header(request):
    print(request.META)
    host = request.META['HTTP_HOST']
    print(request.method)
    return HttpResponse("%s %s" %(host,request.method))

def resp(request):
    response = HttpResponse('itcast python', status=400)
    response.status_code = 500
    return response

def json(request):
    response = [{"name":"xiaolong","age":35},{"name":"shuai","age":35}]
    return redirect("http://www.baidu.com")
    # return JsonResponse(response,safe=False)




