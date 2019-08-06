from django.shortcuts import render

# Create your views here.
# 首页
def index(request):
    return render(request,'index.html')


# 挂号信息管理
def registration_index(request):
    return render(request,'registration/index.html')


# 住院办理
def hospital_index(request):
    return render(request,'hospital/index.html')


# 住院结算
def hospital_account(request):
    return render(request,'hospital/account.html')


# 在院发药
def hospital_dispensing(request):
    return render(request,'hospital/dispensing.html')


# 药品管理
def medicine_index(request):
    return render(request,'medicine/index.html')

# 检查收费项目登记
def hospital_charge2(request):
    return render(request,'hospital/charge2.html')

# 收费项目管理
def hospital_charge(request):
    return render(request,'hospital/charge.html')

# 门诊医生管理
def doctor_index(request):
    return render(request,'doctor/index.html')

# 用户管理
def User_index(request):
    return render(request,'User/index.html')

# 角色管理
def Role_index(request):
    return render(request,'Role/index.html')

# 资源管理
def Resource_index(request):
    return render(request,'Resource/index.html')

# 密码管理
def User_password(request):
    return render(request,'User/password.html')


