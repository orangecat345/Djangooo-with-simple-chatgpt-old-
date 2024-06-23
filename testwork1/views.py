from django.http import HttpResponse
def user(request):
    return HttpResponse("Hello, world. You're at the polls index.")
from django.shortcuts import render     #render函数用于将模板文件和数据进行渲染
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from .models import station
# from .models import data
# # Create your views here.

# """
# 试图函数定义的基本要求
#     1.第一个参数是HttpRequest对象(通过命名的request)
#          request包含了浏览器的请求信息
#     2.必须返回一个HttpResponse对象(或者子类对象)
#          HttpResponse对象包含了响应浏览器的内容



#     视图函数的使用流程：
#     1. 在应用中的views.py文件中定义视图函数
#     2. 配置路由
#         1. 在项目中的urls.py文件中关联应用中的urls.py文件
#         from django.contrib import admin
#         from django.urls import path,include,re_path

#         urlpatterns = [
#             path("admin/", admin.site.urls),
#             #将应用中的urls.py文件中的urlpatterns列表中的元素添加到项目中的urlpatterns列表中
#             path('news/',include('news.urls')),
#             re_path(r'^news/',include('news.urls'))
# ]
#         2. 在应用中创建urls.py文件并在urls.py文件中定义路由信息
#            from django.urls import path

#            from news.views import index
#            urlpatterns = [
#                 path('index',index)
#             ]
# """

# #定义视图函数
# from .models import newsinfo

# def index(request):
#     res='这是新闻首页'
#     return HttpResponse(res)


# #在视图函数中使用模型类
# def newslist(request):
#     newsinfos=newsinfo.objects.all()      #查询所有的新闻信息  等同于select * from newsinfo
#     result=''
#     for news in newsinfos:
#         title='<h1>{}<h1>'.format(news.title)
#         result+=title
#     return HttpResponse(result)



# '''
# 模板的配置和使用
#     1. 在应用中创建templates文件夹并在settings.py文件中配置模板文件的路径
#     2. 在templates文件夹中创建html文件
#     3. 在应用中的views.py文件中定义视图函数,并返回render函数的返回值
#     4. 在应用中的urls.py文件中定义路由信息
#     5. 配置路由访问规则


# '''




# #在视图函数中使用模板文件
# def newslist2(request):
#     newsinfos=newsinfo.objects.all()      #查询所有的新闻信息  等同于select * from newsinfo
#     item=newsinfos[1]
#     info={                           #定义一个字典，用于存储数据，字典的键名要和模板文件中的变量名一致，必须是字典类型
#         'title':item.title,
#         'content':item.content,
#         'b_data':item.b_data,
#         'read':item.read
#     }


#     #render函数的第一个参数是HttpRequest对象
#     #render函数的第二个参数是模板文件的路径
#     #render函数的第三个参数是字典类型的数据
#     return render(request,'list.html',info)


# # def newslist3(request):
# #     newsinfos=newsinfo.objects.all()      #查询所有的新闻信息  等同于select * from newsinfo
# #     item=newsinfos[2]
# #     info={                           #定义一个字典，用于存储数据，字典的键名要和模板文件中的变量名一致，必须是字典类型
# #         'title':item.title,
# #         'content':item.content,
# #         'b_data':item.b_data,
# #         'read':item.read
# #     }


# #     #render函数的第一个参数是HttpRequest对象
# #     #render函数的第二个参数是模板文件的路径
# #     #render函数的第三个参数是字典类型的数据
# #     return render(request,'222.html',info)

# def stations(request):
#     stations=station.objects.all()
#     return render(request,'stations.html',{'stations':stations})

# def datas(request,stations_id):
#     # 获取特定站点的详细信息
#     selected_station = station.objects.get(id=stations_id)
    
#     # 获取与特定站点相关的所有数据
#     station_data = data.objects.filter(station=selected_station)
#     return render(request,'data.html',{'data':station_data,'station':selected_station})


# # views.py
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json


# from openai import OpenAI
# # 设置 OpenAI API 密钥
# apikey = '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'  # 替换为你的实际 API 密钥

# client = OpenAI(
#   api_key=apikey,
# )

# @csrf_exempt  # 仅为示例，请根据实际情况安全配置
# def solve_question(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         question = data.get('question', '')

#         chat_response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "user", "content": question},
#             ],
#         )
#         print(chat_response)
# #         # 提取 chat_response 中的一些信息
# #         response_data = {
# #             'id': chat_response.id,
# #             'object': chat_response.object,
# #             'created': chat_response.created,
# #              # 添加其他需要的属性...
# #         }

# # # 将提取的信息转换为 JSON 字符串
# #         json_response = json.dumps(response_data)

# #         return JsonResponse({'answer': json_response})


#         print('Received question:', question)

#         # 在这里进行问题解答的逻辑，示例中直接返回问题的反转作为答案
#         answer = question[::-1]

#         return JsonResponse({'answer': answer})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})


def main(request):
    return render(request, 'static/html/main.html')  
# yourapp/views.py
from django.shortcuts import render

def your_custom_view(request):
    return render(request, '222.html')  # 更新这里的模板文件名


# def main(request):
    # return render(request, 'static/html/main.html')  # 更新这里的模板文件名


def Login(request):
    if (request.method=="GET"):
        return render(request, 'static/html/Login.html')  # 更新这里的模板文件名
    if (request.method == 'POST'):
        jason_str=request.body
        abdict=json.loads(jason_str)
        print(abdict)
        sys.stdout.flush()
        if request.session["verification_code"]!=abdict["verification_code"]:
            return HttpResponse(json.dumps({
                "status": 400,
                "result": "验证码错误"}))
        usr=models.user.objects.filter(name=abdict["username"])
        if usr.exists():
            usr=usr[0]
            if models.user.objects.filter(name=abdict["username"],password=abdict["password"]):
                request.session["username"]=abdict["username"]
                request.session["password"]=abdict["password"]
                # request.session["cookie"]=abdict["cookie"]
                if int(usr.cookie)==0:
                    models.chat_history.objects.filter(user_id_id=usr.id).update(content1="",content2="",content3="")
                if int(models.user.objects.filter(name=abdict["username"])[0].cookie)==3:
                    models.chat_history.objects.filter(user_id_id=usr.id).update(content1="")
                if int(models.user.objects.filter(name=abdict["username"])[0].cookie)==1:
                    models.chat_history.objects.filter(user_id_id=usr.id).update(content2="")
                if int(models.user.objects.filter(name=abdict["username"])[0].cookie)==2:
                    models.chat_history.objects.filter(user_id_id=usr.id).update(content3="")
                request.session["chat_history_pointer"]=(int(models.user.objects.filter(name=abdict["username"])[0].cookie)%3+1).__str__()
                models.user.objects.filter(name=abdict["username"]).update(cookie=(int(models.user.objects.filter(name=abdict["username"])[0].cookie)%3+1).__str__())

                return HttpResponse(json.dumps({
                "status": 200,
                "result": "成功"}))
            else:
                return HttpResponse(json.dumps({
                "status": 200,
                "result": "密码错误"}))
        else:
            return HttpResponse(json.dumps({
                "status": 200,
                "result": "用户名不存在"}))
import sys
def register(request):
    return render(request, 'static/html/Register.html')  # 更新这里的模板文件名
import json
def check_email_password(request):
    if (request.method == 'POST'):
        jason_str=request.body
        abdict=json.loads(jason_str)
        print(abdict)
        sys.stdout.flush()
        #用户名被使用
        if models.user.objects.filter(name=abdict["username"]):
            return HttpResponse(json.dumps({
                "status": 400,
                "result": "email_hasbeen_registered"}))
        if abdict["username"]!='' and abdict["password1"]==abdict["password2"] and abdict["password1"]!='' and "@" in abdict["username"] and "." in abdict["username"] and len(abdict["password1"])>=6 and len(abdict["password1"])<=16:
            if len(abdict["username"])>=3 and len(abdict["username"])<=100:
                dbsave(request)
                return HttpResponse(json.dumps({
                "status": 200,
                "result": "成功"}))
            else:
                return HttpResponse(json.dumps({
                "status": 400,
                "result": "邮箱长度不符合要求"}))
        else:
            return HttpResponse(json.dumps({
                "status": 400,
                "result": "邮箱或密码不符合要求"}))

from django.urls import path
from sqlchat import models
def dbsave(request):
    jason_str=request.body
    abdict=json.loads(jason_str)
    #将数据保存到数据库中，先获取数据库中id最大的数据，然后将id+1，然后将数据保存到数据库中
    models.user.objects.create(id=models.user.objects.latest('id').id+1,name=abdict["username"],
                               email=abdict["username"],password=abdict["password1"],
                               start_time=models.user.objects.latest('id').start_time,
                                 end_time=models.user.objects.latest('id').end_time,
                                 cookie="0",
                                superuser="普通用户",
                                money_left=5.0
                                 )
    models.chat_history.objects.create(user_id_id=models.user.objects.latest('id').id)
    return "ok"
def register_process(request):
    print(request.body.decode('utf-8'),request.session["verification_code"])
    jason_str=request.body
    abdict=json.loads(jason_str)
    sys.stdout.flush()
    if request.session["verification_code"]!=abdict["verification_code"]:
        return HttpResponse(json.dumps({
                "status": 400,
                "result": "验证码错误"}))
    # # print
    # username=request.GET.get('username')
    # password=request.GET.get('password')#这里的password是一个列表包括两个值
    # verification_code=request.GET.get('verification_code')
    # sys.stdout.flush()
    # if password[0]!=password[1]:
    #     return HttpResponse('两次密码不一致！')
    return check_email_password(request)
import random
from PIL import Image, ImageFont, ImageDraw


def get_code():
    mode = 'RGB'
    bg_width = 180 #这个是验证码那个框框的宽度
    bg_height = 30 #这个是验证码那个框框的高度
    bg_size = (bg_width, bg_height)
    bg_color = (255, 255, 255)
    ttf_path = 'testwork1/static/images/cambriab.ttf'
    img = Image.new(mode, bg_size, bg_color)
    draw = ImageDraw.Draw(img, mode)
    font = ImageFont.truetype(ttf_path, 20)#这个俺也没懂

    # generate text
    letters = get_letters()
    for index, text in enumerate(letters):
        x = 35 * index + 10 #这个好像是调那个字符间距的
        y = 0
        draw.text((x, y), text, get_rdmcolor(), font)

    # blur the background
    for i in range(100): #这个是设置干扰线的,数值越大,干扰的越厉害
        x = random.randint(0, bg_width)
        y = random.randint(0, bg_height)
        fill = get_rdmcolor()
        draw.point((x, y), fill)
    return img, letters


def get_letters(): #这个就是从下面这些字母里去随机4个出来
    base = '1234567890abcdefghijklmnopqrstuvwxyz'#ABCDEFGHIJKLMNOPQRSTUVWXYZ
    result = []
    for i in range(5): #这个是4位,应该改更多位,那么上面的参数还要调试,不然显示有问题
        result.append(random.choice(base))
    return result


def get_rdmcolor():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

from io import BytesIO
def verification_code(request):
    img, letters = get_code()
    request.session['verification_code'] = ''.join(letters)#将验证码保存到session中
    fp = BytesIO()#BytesIO()方法用于创建一个BytesIO对象，然后用这个对象的write方法写入一些bytes
    img.save(fp, 'png')
    return HttpResponse(fp.getvalue(), content_type='image/png')#getvalue()方法用于获得写入后的str




def user_name(request):
    if (request.method == 'POST'):
        jason_str=request.body
        abdict=json.loads(jason_str)
        print(abdict)
        sys.stdout.flush()
        if request.session.get("username")==None:
            return HttpResponse(json.dumps({
                "status": 200,
                "result": "未登录",}))
        #在数据库中比对用户名
        # try:
        #     a=request.session[user_name]
        # except:
        #     return HttpResponse(json.dumps({
        #         "status": 200,
        #         "result": "1未登录",}))
        
        tempmodels=models.user.objects.filter(name=request.session["username"])
        if tempmodels.exists():
            print(tempmodels)
            sys.stdout.flush()
            return HttpResponse(json.dumps({
                "status": 200,
                "result": request.session["username"],
                "money":tempmodels[0].money_left,
                "superuser":tempmodels[0].superuser,
                })) 
        else:
            return HttpResponse(json.dumps({
                "status": 200,
                "result": "用户未登录"}))
def log_out(request):
    if (request.method == 'POST'):
        jason_str=request.body
        abdict=json.loads(jason_str)
        print(abdict)
        sys.stdout.flush()
        #在数据库中比对用户名
        if models.user.objects.filter(name=request.session["username"]).exists():
            del request.session["username"]
            del request.session["password"]
            del request.session["chat_history_pointer"]
            return HttpResponse(json.dumps({
                "status": 200,
                "result": "成功"})) 
        else:
            return HttpResponse(json.dumps({
                "status": 200,
                "result": "用户未登录"}))
def get_history(request):
    if (request.method == 'POST'):
        jason_str=request.body
        abdict=json.loads(jason_str)
        if request.session.get("username")==None:
            return HttpResponse(json.dumps({
                "status": 200,
                "result": "未登录",}))
        # try:
        #     a=request.session[user_name]
        #     # 如果session过期，会抛出异常
        # except:
        #     return HttpResponse(json.dumps({
        #         "status": 200,
        #         "result": "1未登录",}))
        
        print(abdict)
        sys.stdout.flush()
        #在数据库中比对用户名
        if models.user.objects.filter(name=request.session["username"]).exists():
            #设置session,拥有同一个session的聊天记录被记录在一起?如何判断session没过期?在session中记录用户名
            tempmodels=models.chat_history.objects.filter(user_id=models.user.objects.filter(name=request.session["username"])[0].id)
            if tempmodels.exists():
                #按时间排序
                # tempmodels=tempmodels.order_by('generar_time'
                # print(tempmodels[0])
                # sys.stdout.flush()
                cookpoint=int(models.user.objects.filter(name=request.session["username"])[0].cookie)
                if cookpoint==1:
                    return HttpResponse(json.dumps({
                    "status": 200,
                    "result": "成功",
                    "history1":tempmodels[0].content1,
                    "history2":tempmodels[0].content2,
                    "history3":tempmodels[0].content3,
                    "space":"1",
                    }))
                if cookpoint==2:
                    return HttpResponse(json.dumps({
                    "status": 200,
                    "result": "成功",
                    "history1":tempmodels[0].content1,
                    "history2":tempmodels[0].content2,
                    "history3":tempmodels[0].content3,
                    "space":"2",
                    }))
                    
                if cookpoint==3:
                    return HttpResponse(json.dumps({
                    "status": 200,
                    "result": "成功",
                    "history1":tempmodels[0].content1,
                    "history2":tempmodels[0].content2,
                    "history3":tempmodels[0].content3,
                    "space":"3",
                    }))     
                # 发生系统逻辑错误   
                if cookpoint>=4:
                    return HttpResponse(json.dumps({
                    "status": 400,
                    "result": "系统逻辑错误",
                    }))
                
            else:
                return HttpResponse(json.dumps({
                    "status": 200,
                    "result": "用户未登录",}))
        else:
            return HttpResponse(json.dumps({
                "status": 200,
                "result": "用户不存在",}))
    else:
        return HttpResponse(json.dumps({
                "status": 400,
                "result": "错误请求",}))