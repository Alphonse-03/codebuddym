from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from mainprocess.models import Profile,C,Cpp,Java,Python,ConnectRequest,Message
import random 
from django.db.models import Q
# Create your views here.
flag=True
def home(request):
    if request.user.is_authenticated:
        n=request.user
      
        i=Profile.objects.filter(username=n).first().intrest
        m=Profile.objects.filter(username=n).first().marks
  
        if i=='' or m==0:
          
            return redirect("timeline")
        else:
            return redirect("profile")
    else:
        return render(request,"base.html")

def timeline(request):
    n=request.user
    i=Profile.objects.filter(username=n).first().intrest

    m=Profile.objects.filter(username=n).first().marks
    if i =='':
        if request.method=="POST":
            choice=request.POST['choice']
          
            Profile.objects.filter(username=n).update(intrest=choice) 
            return redirect("test")
        return render(request,"code/choice.html")
    if m==0:
        return redirect("test")
    return render(request,"base.html")

def test(request):
    n=request.user
    if Profile.objects.filter(username=n).first().marks == 0:
        choice=Profile.objects.filter(username=n).first().intrest
        if choice=='C++':
            que=Cpp.objects.all()
        if choice=='C':
            que=C.objects.all()
        if choice=='Java':
            que=Java.objects.all()
        if choice=='Python':
            que=Python.objects.all()
        
        
        questions=[]
        un=['a','b','c','d','e','f','g','h','i','j']

        for q in que:
            if q not in questions:
                questions.append(q)
            else:
                continue
        sampling = random.sample(questions, 10)

        print(sampling)

        correctAnswers=[]
        for j in sampling:
              
                correctAnswers.append(j.ans)


        print(sampling)

      

        d = dict(zip(un,sampling))
      
        answers=[]
        if request.method=="POST":
            answers.append(request.POST['a'])    
            answers.append(request.POST['b'])
            answers.append(request.POST['c'])
            answers.append(request.POST['d'])
            answers.append(request.POST['e'])
            answers.append(request.POST['f'])
            answers.append(request.POST['g'])
            answers.append(request.POST['h'])
            answers.append(request.POST['i'])
            answers.append(request.POST['j'])      
    
            marks=0
            print(answers)
            
            for i in range(0,10):
                if correctAnswers[i]==answers[i]:
                    marks=marks+1
            category=""
            if marks == 10:
                category="Legendary"
            elif marks>=8 and marks<=9:
                category="Titan"
            elif marks>=6 and marks<=7:
                category="Champion"
            elif marks>=4 and marks<=5:
                category="Gold"
            elif marks>=2 and marks<=3:
                category="Silver"
            elif marks>=0 and marks<=1:
                category="Bronze"
            
            Profile.objects.filter(username=n).update(marks=marks,category=category)
            return redirect("profile")

        return render(request,"code/test.html",{'questions':d,'a':1})

def loginhandle(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse("something went wrong")

def logouthandle(request):
    logout(request)
    return redirect("/")

def registerhandle(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1 == pass2:
            userr=User.objects.create_user(username,email,pass1)
           
            userr.first_name=fname
            userr.last_name=lname
            userr.save()
            profile=Profile(name=fname,email=email,username=username)
            profile.save()
            return redirect("/")
    
    else:
            return HttpResponse("404-something went wrong")

def profile(request):
    username=request.user
    marks=Profile.objects.filter(username=username).first().marks
    intrest=Profile.objects.filter(username=username).first().intrest
    email=Profile.objects.filter(username=username).first().email
    category=Profile.objects.filter(username=username).first().category
    n=Profile.objects.filter(username=username).first().name
    param={
        'name':n,
        'username':username,
        'marks':marks,
        'intrest':intrest,
        'email':email,
        'category':category,
    }
    return render(request,"code/profile.html",param)

def buddylist(request):
    username=request.user
    category=Profile.objects.filter(username=username).first().category
    intrest=Profile.objects.filter(username=username).first().intrest

    not_to_be_included_list=[]

    accepted_list=[]
    list_of_profile=[]
    
    #pending list
    not_to_be_included=ConnectRequest.objects.filter(Q(sender__username__icontains=username)).filter(status="Pending")

    #accepted list
    liss=ConnectRequest.objects.filter(sender__username__icontains=username).filter(status="Accepted")
    liss2=ConnectRequest.objects.filter(receiver__username__icontains=username).filter(status="Accepted")

    for receivers in liss:
        accepted_list.append(receivers.receiver)

    for senders in liss2:
        accepted_list.append(senders.sender)


    #receiver is a foreign key so i am using it for connecting it to the Profile model so that i can iterate the 
    #informations from the Profile model
    for receivers in not_to_be_included:
        not_to_be_included_list.append(receivers.receiver)
    all_profile=Profile.objects.filter(category=category).filter(intrest=intrest).exclude(username=username)

    #typecasting the query set of "all_profile" to a list

    list_of_profile=list(all_profile)

    actual_list=set(list_of_profile)-set(not_to_be_included_list)-set(accepted_list)

    pending_list=not_to_be_included_list
  
    return render(request,"code/buddylist.html",{'buddy':actual_list,'pendinglist':pending_list})

def budprofile(request,slug):
    bud=Profile.objects.filter(username=slug).first()
    
    return render(request,"code/budprofile.html",{'bud':bud})

def sendrequest(request,receiver):
    receiver_user = Profile.objects.get(username=receiver)
    sender=request.user
    sender_user=Profile.objects.get(username=sender.username)
    obj,created=ConnectRequest.objects.get_or_create(sender=sender_user,
        receiver=receiver_user,
        status="Pending"
    )
    return redirect("buddylist")

def requestlist(request):
    connectionlist=ConnectRequest.objects.all()
    receiver=request.user.username
    cList=[]
    for connection in connectionlist:
        if connection.receiver.username == receiver and connection.status=="Pending":
            cList.append(connection.sender.username)

    return render(request,"code/pendinglist.html",{'connectionlist':cList})

def declinerequest(request,slug):
    sender=slug
    receiver=request.user.username
    cl=ConnectRequest.objects.all()
    idn=0
    for c in cl:
        if c.receiver.username==receiver and c.sender.username==slug:
            idn=c.idno

    ConnectRequest.objects.filter(idno=idn).delete()
    return redirect("requestlist")


def cancelrequest(request,slug):
    sender=request.user.username
    receiver=slug

    cl=ConnectRequest.objects.all()
    idn=0
    for c in cl:
        if c.receiver.username==receiver and c.sender.username==sender:
            idn=c.idno

    ConnectRequest.objects.filter(idno=idn).delete()
    return redirect("buddylist")


def acceptrequest(request,slug):
    sender=slug
    receiver=request.user.username
   
    #cl=ConnectRequest.objects.all()
    # idn=0
    # for c in cl:
    #     if c.receiver.username==receiver and c.sender.username==slug:
    #         idn=c.idno
   
    ConnectRequest.objects.filter(Q(sender__username__icontains=sender)).filter(Q(receiver__username__icontains=receiver)).update(status="Accepted")
    

    
    return redirect("requestlist")



def friendlist(request):
    username=request.user.username

    liss=ConnectRequest.objects.filter(sender__username__icontains=username).filter(status="Accepted")
    liss2=ConnectRequest.objects.filter(receiver__username__icontains=username).filter(status="Accepted")

    accepted_list=[]

    for receivers in liss:
        accepted_list.append(receivers.receiver)

    for senders in liss2:
        accepted_list.append(senders.sender)

    return render(request,"code/friendlist.html",{'accepted_list':accepted_list})


def chatting(request,receiver):
    sender=request.user
    params=["messagemessagemessagemessagemessagemessagemessagemessagemessagemessagemessage",
        "dsyhbs sf hufesdsdnv fdbvjnfvn vnv sd bdfv fv nsd v nfdvn nvjdsvndfi fb ",
        "sdvin usfnvfefdnn fnmfbjkfbm   dfb njdfb  xifbjcn  fcbfdl kdfbnkdmzelbnbij bfkvcn"
    ]
    return render(request,"code/message.html",{"message":params,"receiver":receiver})


def message(request,receiver):
    print("in the message")
    if request.method=="POST":
        
        mess=request.POST['message']
        receiver_user = Profile.objects.get(username=receiver)
        sender=request.user
        sender_user=Profile.objects.get(username=sender.username)
    
        thread=Message(sender=sender_user,receiver=receiver_user,mess=mess)

        thread.save()
    return redirect("message")