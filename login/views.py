from django.shortcuts import render, redirect
from login import models
from django import forms


# Create your views here.
def user_list(request):
    """ 用户列表 """
    data_list = models.UserInfo.objects.all()
    return render(request, "user_list.html", {'data_list': data_list})


class UserForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo1
        fields = ["user_name", "user_pwd", "user_state"]
        # widgets = {
        #     "user_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
        #     "user_pwd": forms.TextInput(attrs={"class": "form-control", "placeholder": "密码"}),
        #     "user_state": forms.Select(attrs={"class": "form-control"})
        #
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_add(request):
    """添加用户信息"""
    # 获取前台表单填写的数据
    if request.method == 'GET':
        form = UserForm()
        return render(request, "user_add.html", {"form": form})

    # 以post提交的数据
    form = UserForm(data=request.POST)
    if form.is_valid():
        # 数据合法 保存到数据库
        print(form.cleaned_data)
        form.save()
        return redirect("/userinfo/list/")
    else:
        # 校验失败 显示错误信息
        return render(request, "user_add.html", {"form": form})
    #  context = {
    #      "state_choice": models.UserInfo.state_choices
    #  }
    # if request.method == 'GET':
    #     return render(request, "user_add.html", context)
    # user_name = request.POST.get("name")
    # user_pwd = request.POST.get("pwd")
    # user_state = request.POST.get("state")
    # # 将获取的数据添加到数据库
    # models.UserInfo.objects.create(user_name=user_name, user_pwd=user_pwd, user_state=user_state)
    # # 重定向到用户列表界面
    # return redirect("/userinfo/list")


# 删除用户信息
def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/userinfo/list")


    # nid = request.GET.get("nid")
    # models.UserInfo.objects.filter(id=nid).delete()
    # return redirect("/userinfo/list")


# 编辑用户信息
def user_edit(request, nid):
    if request.method == 'GET':
        row_obj = models.UserInfo.objects.filter(id=nid).first()
        form = UserForm(instance=row_obj)
        return render(request, "user_edit.html", {"form":form})

    row_obj=models.UserInfo.objects.filter(id=nid).first()
    form = UserForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/userinfo/list/")
    else:
        return render(request, "user_edit.html",{"form": form})

    # 根据nid获取当前行数据
    # if request.method == "GET":
    #     row_obj = models.UserInfo.objects.filter(id=nid).first()
    #     return render(request, "user_edit.html", {'row_obj': row_obj})
    # name = request.POST.get("name")
    # pwd = request.POST.get("pwd")
    # # pwds = request.POST.get("pwds")
    #
    # models.UserInfo.objects.filter(id=nid).update(user_name=name, user_pwd=pwd, user_state=1)
    # return redirect("/userinfo/list")


