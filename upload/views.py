from django.http import HttpResponse
from django.shortcuts import render
from upload import mynet as mnet
import os
# Create your views here.
def home_view(request, *args, **kwargs):
    data = 'data from home_view'
    context = {
        'data': data
    }
    return render(request, 'upload/upload.html', context)


def form_view(request):
    if request.method == "GET":
        ip = ''
        username = ''
        password = ''
        #myfile = []
        cmdlist = []
        result = ''
    if request.method == "POST":
        ip = request.POST.get('ip')
        username = request.POST.get('username')
        password = request.POST.get('password')
        #myfile = request.POST.get('myfile')
        #cmdlist = request.POST.get('cmdlist')
        #cwd = os.getcwd()  # Get the current working directory (cwd)
        #myfile = os.listdir('/Users/shaun/dev/netmiko_django/netmiko_django/static') # Get all the files in that directory
        #myfile = ['hello.txt', 'hello.1.txt', 'hello.2.txt', 'hello.3.txt']
        cmdlist = [ 'exit', 'sho ip inter brief', 'show ver', 'show flash:']
        x = mnet.my_netmiko(ip, username, password, cmdlist)
        result = x.main()
        print(ip)
        print(result)
    context = {
        'ip': ip,
        'username': username,
        'password': password,
        #'myfile': myfile,
        'cmdlist': cmdlist,
        'result': result
    }
    return render(request, 'upload/form.html', context)
