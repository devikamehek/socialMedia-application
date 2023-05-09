from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView,FormView,TemplateView,UpdateView,View,ListView,DetailView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy 

from myapp.forms import SignUpForm,SignInForm,ProfileEditForm,PostForm,CoverPicForm
from myapp.models import UserProfile,Posts,Comments


class SignUpView(CreateView):
    model=User
    form_class=SignUpForm
    template_name="register.html"
    success_url=reverse_lazy("signin")

    def form_valid(self, form):
        # return redirect("signin")
        messages.success(self.request,"Account has been Created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"Failed to create account")
        return super().form_invalid(form)


class SignInView(FormView):
    form_class=SignInForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            messages.error(request,"Invalid Credentials")
        return render(request,self.template_name,{"form":form})
    

class IndexView(CreateView,ListView):
    template_name="index.html"
    form_class=PostForm
    model=Posts
    context_object_name="posts"
    success_url=reverse_lazy("index")
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    

    


class ProfileEditView(UpdateView):
    model=UserProfile
    form_class=ProfileEditForm
    template_name="profile_edit.html"
    success_url=reverse_lazy("index")



def add_like_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    post_obj=Posts.objects.get(id=id)
    post_obj.liked_by.add(request.user)
    return redirect("index")

def add_comment_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    post_obj=Posts.objects.get(id=id)
    comment=request.POST.get("comment")
    user=request.user
    Comments.objects.create(user=user,post=post_obj,comment_text=comment)
    return redirect("index")



def remove_comment_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    comment_obj=Comments.objects.get(id=id)
    if request.user == comment_obj.user:
        comment_obj.delete()
        return redirect("index")
    else:
        messages.error(request,"Plz contact admin")
        return redirect("signin")
    


class ProfileDetail_view(DetailView):
    model=UserProfile
    template_name="profiledetail.html"
    context_object_name="profile"



def change_cover_pic_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    prof_obj=UserProfile.objects.get(id=id)
    form=CoverPicForm(instance=prof_obj,data=request.POST,files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect("profiledetail",pk=id)
    return redirect("index")
    


class ProfileListview(ListView):
    model=UserProfile
    template_name="profile-list.html"
    context_object_name="profiles"

    def get_queryset(self):
        return UserProfile.objects.exclude(user=self.request.user)

    # # change querry set
    # def get(self,request,*args,**kwargs):
    #     qs=UserProfile.objects.exclude(user=request.user)
    #     return render(request,self.template_name,{"profiles":qs})



def follow_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    profile_obj=UserProfile.objects.get(id=id)
    user_prof=UserProfile.objects.get(user=request.user)
    user_prof.following.add(profile_obj)
    user_prof.save()
    print(f'{request.user} is following {user_prof.following.all()}')
    return redirect("index")

def unfollow_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    profile_obj=UserProfile.objects.get(id=id)
    user_prof=UserProfile.objects.get(user=request.user)
    user_prof.following.remove(profile_obj)
    user_prof.save()
    print(f'{request.user} is following {user_prof.following.all()}')
    return redirect("index")



def post_delete_view(request,*args,**kwargs):
    post_id=kwargs.get("pk")
    post_obj=Posts.objects.get(id=post_id)
    post_obj.delete()
    return redirect("index")









