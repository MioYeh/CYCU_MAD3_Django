from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from index import models
import qrcode
from django.contrib import auth 
import time
import os
from random import Random
from index.models import User


def hello_world(request):
    for x in User.objects.all():
        ttd = User.objects.get(id = x.id)
        ttd.img = "null"
        ttd.save()
    check_png = len(os.listdir('/Users/mio/CYCU_tt/templates/static/qrcode/'))
    if  check_png >= 2:
        os.remove('/Users/mio/CYCU_tt/templates/static/qrcode/qrcode.png')
        return render_to_response('../templates/index.html')
    else:
        return render_to_response('../templates/index.html')
    # return render_to_response('../templates/home.html')

def add(request):

    ra = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(24):
        ra+=chars[random.randint(0,length)]


    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )


    a = request.GET['Username']
    b = request.GET['Password']
    # get_m = models.User.objects.all()

    tt = User.objects.get(id = a)
    # m = tt.id
    tt.img = ra
    tt.save()

    qr.add_data(ra) ##give qrcode vlaue

    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("/Users/mio/CYCU_tt/templates/static/qrcode/qrcode.png") # 儲存圖片
    

    articles = open("/Users/mio/CYCU_tt/templates/static/qrcode/qrcode.png","rb").read()
    # for y in User.objects.all():
    #     td = User.objects.get(id = y.id)
    #     td.img = "error"
    #     td.save()
    return HttpResponse(articles ,content_type="image/png")
    # return render_to_response('../templates/home.html')
    # return HttpResponse(a + b)


def try_sleep(requests):
    time.sleep(5)
    return HttpResponse('jump')
    # return render_to_response('/Users/mio/CYCU_tt/templates/index.html')