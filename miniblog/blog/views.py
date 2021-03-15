from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
# Create your views here.
#home 

def home(request):
    posts=Post.objects.all()

    return render(request,'blog/home.html',{'posts':posts})



def about(request):
    return render(request,'blog/about.html')


def contact(request):
    return render(request,'blog/contact.html')


def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request,'blog/dashboard.html',{'fm':posts,'full':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations!! Your have become a member of CHAR BADH :) Now, Login please")
            user=form.save()
    else:
        form=SignUpForm()
    return render(request,'blog/signup.html',{'form':form})



def user_login(request):
   if not request.user.is_authenticated: 
       if request.method=="POST":
           fm=LoginForm(request=request,data=request.POST)
           if fm.is_valid():
               uname=fm.cleaned_data['username']
               upass=fm.cleaned_data['password']
               user=authenticate(username=uname,password=upass)
               if user is not None:
                   login(request,user)
                   messages.success(request,"You have been successfully login :)")
                   return HttpResponseRedirect('/dashboard/')
       else:
           fm=LoginForm()
       return render(request,'blog/login.html',{'form':fm})
   else:
        return HttpResponseRedirect('/dashboard/') 

    
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Post Added successfully !! ")
                return HttpResponseRedirect('/dashboard/')
        else:
            form=PostForm()  
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

   
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid:
                form.save()
                messages.success(request,"Post Updated successfully !!")
                return HttpResponseRedirect('/dashboard/')
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            messages.success(request,"Post Deleted successfully !!")
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')




