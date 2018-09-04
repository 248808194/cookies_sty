from django.shortcuts import render,redirect

# Create your views here.
USER_DIC = {
    'zhoutao':{'password':'123123'},
    'jack':{'password':'123123'},
}

from django.urls import reverse
def san(request,*args,**kwargs):
    v = reverse('test1',args=(30,'asdf'))
    print(v)
    print(args,kwargs)
    return  render(request,'3.html')


def auth(func): #用户认证装饰器 func = index ,return func前做一些判断
    def inner(request,*args,**kwargs):
        v = request.COOKIES.get('username')
        if not v:
            return redirect('/a/login')
        return func(request,*args,**kwargs)
    return inner


@auth
def index(request):
    v = request.COOKIES.get('username')
    return render(request,'index.html',{'username':v})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(type(p))
        u_dic = USER_DIC.get(u)
        print(u,p,u_dic)
        if not u_dic: #用户不存在
            return render(request,'login.html')

        if u_dic['password'] == p: #用户名密码都匹配redirect index
            res = redirect('/a/index')
            res.set_cookie('username',u)
            return res
        else:
            return redirect('/a/login')

LIST = []
for i in range(100):
    LIST.append(i)

from a.pange_auto import Page
def user_list(request):
    current_page = request.GET.get('p',1)

    current_page = int(current_page)
    print(current_page)
    val = request.COOKIES.get('per_page_count',10)
    print(val)
    val = int(val)

    page_obj = Page(current_page,len(LIST),val)

    date = LIST[page_obj.start:page_obj.end]
    page_str = page_obj.page_str("4")

    return render(request,'4.html',{'li':date,'page_str': page_str})


def simpletag(request):
    return render(request,'3.html')


