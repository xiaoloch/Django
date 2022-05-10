from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View

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

def set_cookie(request):
    name = request.GET['username']
    response = HttpResponse('It is done!')
    response.set_cookie('name',name,max_age=60*60)
    response.set_cookie('passwd', "Daliancxl")
    return response

def get_cookie(request):
    name = request.COOKIES['name']
    return HttpResponse(name)

def del_cookie(request):
    response = HttpResponse('See see if cookie is deleted')
    response.delete_cookie('name')
    return response

def set_session(request):
    # 1.模拟获取用户信息
    username = request.GET.get('username')

    # 2. 设置session信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username

    return HttpResponse("set_session")

def get_session(request):
    # user_id = request.session['user_id']
    # username = request.session['username']
    # content = '{},{}'.format(user_id,username)
    # request.session.clear()
    # request.session.flush()
    request.session.set_expiry(3600)
    return HttpResponse('flushed')

class login(View):
    def get(self,request):
        return HttpResponse('get get get')
    def post(self,request):
        return HttpResponse('post post post')

