from django.urls import path
from test_html import views

urlpatterns = [
    path('', views.index, name='index'),
    # 资源管理
    path('Resource_index/', views.Resource_index, name='Resource_index'),
    # 密码管理
    path('User_password/', views.User_password, name='User_password'),
    # 角色管理
    path('Role_index/', views.Role_index, name='Role_index'),
    # 用户管理
    path('User_index/', views.User_index, name='User_index'),
    # 门诊医生管理
    path('doctor_index/', views.doctor_index, name='doctor_index'),
    # 收费项目管理
    path('hospital_charge/', views.hospital_charge, name='hospital_charge'),
    # 检查收费项目登记
    path('hospital_charge2/', views.hospital_charge2, name='hospital_charge2'),
    # 药品管理
    path('medicine_index/', views.medicine_index, name='medicine_index'),
    # 在院发药
    path('hospital_dispensing/', views.hospital_dispensing, name='hospital_dispensing'),
    # 住院结算
    path('hospital_account/', views.hospital_account, name='hospital_account'),
    # 住院办理
    path('hospital_index/', views.hospital_index, name='hospital_index'),
    # 挂号信息管理
    path('registration_index/', views.registration_index, name='registration_index'),
]
