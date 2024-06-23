
import os
from venv import logger
import openai

apikey=""
# 自己填
from openai import OpenAI
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  #修改请求头将openai的接口调用地址，由https://api.openai.com改成https://oneapi.xty.app即可使用。
  base_url="https://oneapi.xty.app/v1",
  api_key=apikey
)
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)
#创建一个对话程序，利用chatgpt构成代理
#循环接收用户输入，然后调用sendmsg函数
#用户输入从前端页面获取
#前端页面的内容通过url传递给后端
#后端通过url获取用户输入
#流式推送
from django.http import HttpResponse
#在res中返回前端页面，同时收集前端页面的输入
from django.shortcuts import render
from django.http import HttpResponse
import os,sys
ospath=os.path.split( os.path.realpath( sys.argv[0] ) )[0]#获取当前文件的路径
# print(ospath)
filepath=os.path.join(ospath,'testwork1\chat.html')#拼接路径
from django.http import StreamingHttpResponse


# class ChatView():
#     def post(self, request, *args, **kwargs):
       
#         # user_input = request.get('input', '')
#         user_input = request.POST.get('input', '')
#         chat_response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             stream=True,
#             messages=[
#                 {
#                     'role': 'user',
#                     'content': user_input,
#                 }
#             ]
#         )
        
#         def get_streaming_content(chat_response):
#             for chunk in chat_response:
#                 yield chunk.choices[0].delta.content
#         response = StreamingHttpResponse(get_streaming_content(chat_response), content_type='application/octet-stream')
#         return response
from django.http import StreamingHttpResponse
import json
from sqlchat import models
robot_response=str("")
class ChatView():
    def post(self, request, *args, **kwargs):
        jason_str=request.body
        abdict=json.loads(jason_str)
        user_input = abdict["input"]
        # Send user input to OpenAI GPT-3.5-turbo
        # model="gpt-3.5-turbo"
        model="get-4"
        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            stream=True,
            messages=[
                {"role": "user", "content": user_input},
            ],
        )
        robot_response=str("")#初始化机器人回复
        def event_stream():
            global robot_response
            for chunk in chat_response:
                global robot_response
                # print("test",chunk.choices[0].delta.content,robot_response)
                if (chunk.choices[0].finish_reason == 'stop'):
                    db_history_save(robot_response,user_input,request)
                    break
                robot_response+=chunk.choices[0].delta.content
                yield chunk.choices[0].delta.content
                #yield是一个生成器，每次调用next()方法时，会从上次yield语句暂停的地方继续执行
        
        response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
        print("test",response)
        sys.stdout.flush()
        #在返回之前合成聊天记录
        
        return response
def db_history_save(robot_response,user_input,request):
    robot_response = robot_response.encode('utf-8', errors='ignore').decode('utf-8')
    user_input = user_input.encode('utf-8', errors='ignore').decode('utf-8')
    # 执行统计并存储聊天记录,修改账户余额
    chat_history_list=models.chat_history.objects.filter(user_id_id= models.user.objects.filter(name=request.session["username"])[0].id)
    user_info=models.user.objects.filter(name=request.session["username"])
    # print("test robotresponse userinput",robot_response,user_input)
    sys.stdout.flush()
    if request.session["chat_history_pointer"]=="1":
        chat_history_list.update(content1=chat_history_list[0].content1+"\nyou:"+user_input+"\ngpt:"+robot_response,
        )   
    elif request.session["chat_history_pointer"]=="2":
        chat_history_list.update(content2=chat_history_list[0].content2+"\nyou:"+user_input+"\ngpt:"+robot_response,
        )
    elif request.session["chat_history_pointer"]=="3":
        chat_history_list.update(content3=chat_history_list[0].content3+"\nyou:"+user_input+"\ngpt:"+robot_response,
        )
    #如果聊天记录超过三条，则删除最早的一条聊天记录
    # 数据库中此用户的聊天记录为空，则创建一条新的聊天记录
a = ChatView()

import datetime
def res(request):
    # if request.cookies.get('csrftoken')!=
    if request.method == 'POST':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR') # 不使用代理获取ip
        print(ip)
        sys.stdout.flush()
        user_info=models.user.objects.filter(name=request.session["username"])
        if user_info.count()==0:
            #流式推送默认值"用户未登录"
            return StreamingHttpResponse("用户未登录", content_type='text/event-stream')
        # 执行统计并存储聊天记录,修改账户余额
        # print(user_info)
        user_info=user_info[0]
        models.user.objects.filter(name=request.session["username"]).update(money_left=user_info.money_left-0.1)
        #找到创建时间最早的聊天记录并覆盖
        return a.post(request)
    return render(request, 'static/html/chat01.html')
def cssres(request):
    return render(request, 'static/css/bootstrap.css')
def login(request):
    return render(request, 'static/html/login.html')

        
    
def maxa_b(a,b):
    if a>b:
        return b
    else:
        return a