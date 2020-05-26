import requests
import random
import os
import re
import time
from uuid import uuid4
from tkinter import*
window=Tk()
window.title("爬取彼岸图网图片")
#window.iconbitmap("tc.ico")

headers={
    'Referer':' https://www.acg-pixiv.com/index.html',
   'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
    }
#sjs=random.randint(0,3)
##sjs=0
##print(sjs)
##if sjs ==0:
##    proxies = {
##        "http": "60.191.11.229:3128"
##    }
##elif sjs==1:
##    proxies = {
##        "http": "https://169.254.171.233:2121"
##    }
##信息
dl=requests.session
dl.headers=headers
def one():
    gh=1
    hz(gh)
def two():
    gh=2
    hz(gh)
def three():
    gh=3
    hz(gh)
def four():
    gh=4
    hz(gh)
def five():
    gh=5
    hz(gh)
def six():
    gh=6
    hz(gh)
def seven():
    gh=7
    hz(gh)
def eight():
    gh=8
    hz(gh)
def nine():
    gh=9
    hz(gh)
def ten():
    gh=10
    hz(gh)
def sy():
    gh=11
    hz(gh)
def sr():
    gh=12
    hz(gh)

def hz(sj):
    print(sj)
    global ljl
    if sj==1:
        ljl='http://pic.netbian.com/4kfengjing/'
    elif sj==2:
        ljl='http://pic.netbian.com/4kmeinv/'
    elif sj==3:
        ljl='http://pic.netbian.com/4kyouxi/'
    elif sj==4:
        ljl='http://pic.netbian.com/4kdongman/'
    elif sj==5:
        ljl='http://pic.netbian.com/4kyingshi/'
    elif sj==6:
        ljl='http://pic.netbian.com/4kmingxing/'
    elif sj==7:
        ljl='http://pic.netbian.com/4kqiche/'
    elif sj==8:
        ljl='http://pic.netbian.com/4kdongwu/'
    elif sj==9:
        ljl='http://pic.netbian.com/4krenwu/'
    elif sj==10:
        ljl='http://pic.netbian.com/4kmeishi/'
    elif sj==11:
        ljl='http://pic.netbian.com/4kzongjiao/'
    elif sj==12:
        ljl='http://pic.netbian.com/4kbeijing/'

def anj():
    ks(ljl)
##    lj="1"
##    ks(lj)
##    print(lj)

#按键
Label(window,text="选择类型:").grid(row=0,column=0)
Button(window,text="风景",width=5,command=one).grid(row=0,column=2,sticky=W,padx=5,pady=5)
Button(window,text="美女",width=5,command=two).grid(row=0,column=4,sticky=W,padx=5,pady=5)
Button(window,text="游戏",width=5,command=three).grid(row=0,column=6,sticky=W,padx=5,pady=5)
Button(window,text="动漫",width=5,command=four).grid(row=0,column=8,sticky=W,padx=5,pady=5)
Button(window,text="影视",width=5,command=five).grid(row=2,column=2,sticky=W,padx=5,pady=5)
Button(window,text="明星",width=5,command=six).grid(row=2,column=4,sticky=W,padx=5,pady=5)
Button(window,text="汽车",width=5,command=seven).grid(row=2,column=6,sticky=W,padx=5,pady=5)
Button(window,text="动物",width=5,command=eight).grid(row=2,column=8,sticky=W,padx=5,pady=5)
Button(window,text="人物",width=5,command=nine).grid(row=4,column=2,sticky=W,padx=5,pady=5)
Button(window,text="美食",width=5,command=ten).grid(row=4,column=4,sticky=W,padx=5,pady=5)
Button(window,text="宗教",width=5,command=sy).grid(row=4,column=6,sticky=W,padx=5,pady=5)
Button(window,text="背景",width=5,command=sr).grid(row=4,column=8,sticky=W,padx=5,pady=5)
Label(window,text="张数:").grid(row=10,column=0)
e1=Entry(window,text=0,width=4)
e1.grid(row=10,column=2,padx=1,pady=2)
def download(url):
    html=requests.get(url)
    #print(html)
    #print(type(html.content))
    str2=str(html.content,encoding="gbk")
    #print(str2)
    #str1=str(html.content)
    #print(type(str1))
    #print(str1)
    fblj=re.findall('/uploads/allimg.+.jpg" d',str2)
    #print(fblj)
    print("正在运行！耐心等待！不能爬太快会封ip!所以请等待！")
    xiazai(fblj)
def xiazai(fblj):      #下载图片
    for lj in fblj:
        lj=lj[:48]
        lj2=lj[:44]
        name=lj2[27:]
        #print(lj)
        print("本来只需要3秒一张！唉")
        zurl="http://pic.netbian.com"
        hclj=zurl+lj
        #print(hclj)
        wj2=requests.get(hclj)
        #print(wj2.content)
        filename='彼岸图网\\图片'
        if not os.path.exists(filename):
            os.makedirs(filename)
        with open('./{}/{}.jpg'.format(filename,name),'wb') as f:
            sjtime =5
            f.write(wj2.content)
            time.sleep(10)
            f.close()
            jc='./{}/{}.jpg'.format(filename,name)
            print(jc)
            if not os.path.exists(jc):
                f.write(wj2.content)
                time.sleep(sjtime)
                f.close()
                time.sleep(10)
        time.sleep(10)
def ks(ljl):
        #print(ljl)
        zsz=e1.get()
        #print(zsz)
        #print(type(zsz))
        #下载页数计算
        print("正在运行！耐心等待！")
        if zsz=="":
            zsz=21
            qz=requests.get(ljl)
            #print(qz)
            utf=str(qz.content,encoding='gbk')

        else:
            zsz=int(zsz)
            #print(zsz)
            #print(type(zsz))
            ds=int(zsz/21)
            #print(type(ds))
            #print(ds)
            pd=True
            aj=0
            while(pd):
                aj=int(aj)
                aj +=1
                #print(aj)
                if aj%ds==0:
                    pd=False
                    #print("结束")
                elif aj==1:
                    #print("数字一")
                    qz=requests.get(ljl)
                    #print(qz)
                    utf=str(qz.content,encoding='gbk')
                elif aj>1:
                    aj=str(aj)
                    qmin='index_'
                    hmin='.html'
                    quanmin=ljl+qmin+aj+hmin
                    #print(quanmin)
                    qz=requests.get(quanmin)
                    #print(qz)
                    utf=str(qz.content,encoding='gbk')
                time.sleep(300)

                

##        f =open("彼岸图网\\图片\\1.txt")
##        utf=f.read()
        #print(utf)
        #获取网址
        zzz=re.findall('tupian/2.+.html',utf)
        #print(zzz)
        for fjz in zzz:
            #zzc =fjz[:17]
            zzc = fjz.split('target="_blank"><img src="/uploads/allimg',20)
            #print(zzc)
            #print(fjz)
            for fjzz in zzc:
                zzzz=re.findall('tupian/.+.html',fjzz)
                #print(zzzz)
                for wd in zzzz:
                    #print(wd)
                    yb='http://pic.netbian.com/'
                    newlj=yb+wd
                    #print(newlj)
                    download(newlj)

                time.sleep(30)
                
##            for fjz2 in zzzz:
##                #print(fjz2)
 ##            #download(newlj)
##            time.sleep(5)
##        time.sleep(8)

Button(window,text="开始",width=5,command=anj).grid(row=12,column=2,padx=2,pady=5)
Label(window,text="©青春进行时").grid(row=13,column=0)
##    for ljd in fblj:
##        print(ljd)
#    bs2=bytes.decode(str1)
##    print(bs2)
#url="http://pic.netbian.com/tupian/22146.html"
#url="http://pic.netbian.com/tupian/24700.html"
#url="http://pic.netbian.com/e/search/result/?searchid=9957"
#url="http://pic.netbian.com/tupian/23354.html"
#download(url)
################http://pic.netbian.com/downpic.php?id=24700&classid=68
mainloop()
