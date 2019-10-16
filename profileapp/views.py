from django.shortcuts import render
from .models import reg,sreg1,exam12,events,faculty,departments,student,data
import random
from django import template
from random import randint
from django.core.mail import send_mail
from django.http import HttpResponse

def f1(request):
    return render(request,'reg.html')
def f2(request):
    if request.method=="POST":
        a1=request.POST['name']
        a2=request.POST['sub']
        a3=request.POST['dep']
        a4=request.POST['qua']
        a5=request.POST['exp']
        a6=request.POST['email']
        v7=randint(123456,456789)
        a7=reg(name=a1,subject=a2,depart=a3,qualification=a4,exp=a5,email=a6,id=v7)
        a7.save()
        sub='userisd'
        msg=str(v7)
        gh=a6
        send_mail(sub,msg,'kirananaparthi8@gmail.com',[gh])
        return render(request,'reg.html')
def f3(request):
    return render(request,'sign.html')
def f4(request):
    if request.method=="POST":
        a8=request.POST['sub1']
        a9=request.POST['em']
        a10=reg.objects.filter(subject=a8,email=a9)
        noti=data.objects.all()
        for h in noti:
            mr=h.data
        return render(request,'noti.html',{'mh':mr})
def f5(request):
    return render(request,'studentreg.html')
def f6(request):
    if request.method=="POST":
        a11=request.POST['name1']
        a12=request.POST['branch']
        a13=request.POST['year']
        a14=request.POST['email1']
        v8=randint(123,456)
        student=sreg1(sname=a11,sbranch=a12,syear=a13,semail=a14,id=v8)
        student.save()
        sub='userisd'
        msg=str(v8)
        mk=a14
        send_mail(sub,msg,'kirananaparthi8@gmail.com',[mk])
        return render(request,'studentreg.html')
def f7(request):
    return render(request,'sign1.html')
def f8(request):
    if request.method=="POST":
        a15=request.POST['id']
        a16=request.POST['branch']
        a10=sreg1.objects.filter(id=a15,sbranch=a16)
        return render(request,'noti.html')
def f9(request):
    return render(request,'exam.html')
def f10(request):
    if request.method=="POST":
        s1=request.POST['sele']
        s2=request.POST['yar']
        if s1=="ece" :
            d1=exam12.objects.filter(departments=s1,year=s2)
            for d in d1:
                k=d.exam
                l=d.date
            all=sreg1.objects.filter(sbranch=s1,syear=s2)
            for d in all:
                s=d.semail
                sub="pnv"
                msg="exam name:"+k+"\n""date:"+str(d)
                send_mail(sub,msg,'kirananaparthi8@gmail.com',[s])
            return render(request,'exam.html',{'m':d1})
        elif s1=="eee":
            d1=exam12.objects.filter(departments=s1,year=s2)
            for d in d1:
                k=d.exam
                l=d.date
            all=sreg1.objects.filter(sbranch=s1,syear=s2)
            for d in all:
                s=d.semail
                sub="pnv"
                msg="exam name:"+k+"\n""date:"+str(d)
                send_mail(sub,msg,'kirananaparthi8@gmail.com',[s])
            return render(request,'exam.html',{'m':d1})
        elif s1=="mech":
            d1=exam12.objects.filter(departments=s1,year=s2)
            for d in d1:
                k=d.exam
                l=d.date
            all=sreg1.objects.filter(sbranch=s1,syear=s2)
            for d in all:
                s=d.semail
                sub="pnv"
                msg="exam name:"+k+"\n""date:"+str(d)
                send_mail(sub,msg,'kirananaparthi8@gmail.com',[s])
            return render(request,'exam.html',{'m':d1})
        elif s1=="civil":
            d1=exam12.objects.filter(departments=s1,year=s2)
            for d in d1:
                k=d.exam
                l=d.date
            all=sreg1.objects.filter(sbranch=s1,syear=s2)
            for d in all:
                s=d.semail
                sub="pnv"
                msg="exam name:"+k+"\n""date:"+str(d)
                send_mail(sub,msg,'kirananaparthi8@gmail.com',[s])
            return render(request,'exam.html',{'m':d1})
        elif s1=="cse":
            d1=exam12.objects.filter(departments=s1,year=s2)
            for b in d1:
                j=b.exam
                d=b.date
            
            all=sreg1.objects.filter(sbranch=s1,syear=s2)
            for b in all:
                s=b.semail
                sub="PNV"
                msg="exam name:"+j+"\n"+"date:"+str(d)
                send_mail(sub,msg,'kirananaparthi8@gmail.com',[s])
            return render(request,'exam.html',{'m':d1})
                
        else:
            return render(request,'exam.html',{'msg':"nomatch"})
def f11(request):
    return render(request,'noti.html')
def f12(request):
    return render(request,'events.html')
def f13(request):
    if request.method=="POST":
        s1=request.POST['sele']
        s2=request.POST['yar']
        if s1=="ece" :
            d1=events.objects.filter(departments=s1,year=s2)
            return render(request,'events.html',{'m':d1})
        elif s1=="eee":
            d1=events.objects.filter(departments=s1,year=s2)
            return render(request,'events.html',{'m':d1})
        elif s1=="mech":
            d1=events.objects.filter(departments=s1,year=s2)
            return render(request,'events.html',{'m':d1})
        elif s1=="civil":
            d1=events.objects.filter(departments=s1,year=s2)
            return render(request,'events.html',{'m':d1})
        elif s1=="cse":
            d1=events.objects.filter(departments=s1,year=s2)
            return render(request,'events.html',{'m':d1})
        else:
            return render(request,'events.html',{'msg':"nomatch"})
def f14(request):
    return render(request,'faculty.html')
def f15(request):
    if request.method=="POST":
        s1=request.POST['sele']
        s2=request.POST['yar']
        if s1=="ece" :
            d1=faculty.objects.filter(departments=s1,year=s2)
            return render(request,'faculty.html',{'m':d1})
        elif s1=="eee":
            d1=faculty.objects.filter(departments=s1,year=s2)
            return render(request,'faculty.html',{'m':d1})
        elif s1=="mech":
            d1=faculty.objects.filter(departments=s1,year=s2)
            return render(request,'faculty.html',{'m':d1})
        elif s1=="civil":
            d1=faculty.objects.filter(departments=s1,year=s2)
            return render(request,'faculty.html',{'m':d1})
        elif s1=="cse":
            d1=faculty.objects.filter(departments=s1,year=s2)
            return render(request,'faculty.html',{'m':d1})
        else:
            return render(request,'faculty.html',{'msg':"nomatch"})
def f16(request):
    return render(request,'der.html')
def f17(request):
    if request.method=="POST":
        s1=request.POST['sele']
        s2=request.POST['yar']
        if s1=="ece" :
            d1=departments.objects.filter(departments=s1,year=s2)
            return render(request,'der.html',{'m':d1})
        elif s1=="eee":
            d1=departments.objects.filter(departments=s1,year=s2)
            return render(request,'der.html',{'m':d1})
        elif s1=="mech":
            d1=departments.objects.filter(departments=s1,year=s2)
            return render(request,'der.html',{'m':d1})
        elif s1=="civil":
            d1=departments.objects.filter(departments=s1,year=s2)
            return render(request,'der.html',{'m':d1})
        elif s1=="cse":
            d1=departments.objects.filter(departments=s1,year=s2)
            return render(request,'der.html',{'m':d1})
        else:
            return render(request,'der.html',{'msg':"nomatch"})
def f18(request):
    return render(request,'stu.html')
def f19(request):
    if request.method=="POST":
        s1=request.POST['sele']
        s2=request.POST['yar']
        if s1=="ece" :
            d1=student.objects.filter(departments=s1,year=s2)
            return render(request,'stu.html',{'m':d1})
        elif s1=="eee":
            d1=student.objects.filter(departments=s1,year=s2)
            return render(request,'stu.html',{'m':d1})
        elif s1=="mech":
            d1=student.objects.filter(departments=s1,year=s2)
            return render(request,'stu.html',{'m':d1})
        elif s1=="civil":
            d1=student.objects.filter(departments=s1,year=s2)
            return render(request,'stu.html',{'m':d1})
        elif s1=="cse":
            d1=student.objects.filter(departments=s1,year=s2)
            return render(request,'stu.html',{'m':d1})
        else:
            return render(request,'stu.html',{'msg':"nomatch"})
    


