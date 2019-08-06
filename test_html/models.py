from django.db import models


# Create your models here.
class Drug_type(models.Model):
    '''
    药品类型
    '''
    types = models.CharField(max_length=20, verbose_name='药品类型')

    class Meta:
        db_table = 'drug_type'


class Drug_role(models.Model):
    '''
    药品作用
    '''
    role = models.CharField(max_length=20, verbose_name='药品作用')

    class Meta:
        db_table = 'drug_role'


class House_room(models.Model):
    """
    房间表
    """
    room_num = models.IntegerField(verbose_name='房间号码')

    class Meta:
        db_table = 'house_room'


class Department(models.Model):
    """
    部门表
    """
    d_name = models.CharField(max_length=20, verbose_name='部门称号')
    superior = models.ForeignKey('Department', null=True, blank=True, on_delete=models.CASCADE, verbose_name='上级')

    class Meta:
        db_table = 'department'


class Subject(models.Model):
    """
    科室
    """
    sub_name = models.CharField(max_length=20, verbose_name='科室')
    for_dep = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所属部门')

    class Meta:
        db_table = 'subject'


class User_info(models.Model):
    """
    挂号信息表
    """
    sex = (
        ('男', 0),
        ('女', 1)
    )
    user_name = models.CharField(max_length=20, verbose_name='用户名')
    user_sex = models.IntegerField(choices=sex, verbose_name='性别')
    user_age = models.IntegerField(verbose_name='年龄')
    user_phone = models.IntegerField(verbose_name='联系方式')
    id_numer = models.CharField(verbose_name='身份证号', max_length=18)
    social = models.CharField(max_length=30, verbose_name='社保卡')
    password = models.CharField(max_length=50,verbose_name='密码')

    class Meta:
        db_table = 'user_info'


class Staff(models.Model):
    """
    职工表基本信息
    """
    staff_sex = (
        ('男', 0),
        ('女', 1)
    )
    staff_num = models.CharField(max_length=30, verbose_name='工号')
    staff_age = models.IntegerField(verbose_name='年龄')
    staff_sex = models.IntegerField(choices=staff_sex, verbose_name='职工性别')
    staff_phone = models.IntegerField(verbose_name='手机号')
    staff_education = models.CharField(max_length=30, verbose_name='学历')
    staff_eailm = models.EmailField(max_length=30, verbose_name='邮箱')
    staff_hiredate = models.DateTimeField(auto_now_add=True, verbose_name='入职时间')
    password = models.CharField(max_length=50,verbose_name='密码')

    class Meta:
        db_table = 'staff'


class Position(models.Model):
    """
    职位表
    """
    pos = models.CharField(max_length=30, verbose_name='职位')

    class Meta:
        db_table = 'position'


class Staff_info(models.Model):
    """
    职工表
    """
    id = models.AutoField(primary_key=True)
    for_staff = models.ForeignKey(to='Staff', to_field='id', on_delete=models.CASCADE, verbose_name='职员信息表的外键')
    for_pos = models.ForeignKey(to='Position', on_delete=models.CASCADE, to_field='id', verbose_name='职位表的外键')
    for_dep = models.ForeignKey(to='Department', on_delete=models.CASCADE, to_field='id', verbose_name='部门表的外键')
    for_sub = models.ForeignKey(to='Subject', to_field='id', on_delete=models.CASCADE, verbose_name='科室表的外键', null=True)
    for_house = models.ForeignKey(to='House_room', to_field='id', on_delete=models.CASCADE, verbose_name='房间表的外键',null=True)
    waiter_people_num = models.IntegerField(verbose_name='最大的服务人数')

    class Meta:
        db_table = 'staff_info'


class Drug(models.Model):
    '''
    药品表
    '''
    drug_name = models.CharField(max_length=20,verbose_name='药品名称')
    for_type = models.ForeignKey('Drug_type',on_delete=models.CASCADE,verbose_name='药品类别')
    for_role = models.ForeignKey('Drug_role',on_delete=models.CASCADE,verbose_name='药品作用')
    drug_introduce = models.CharField(max_length=250,verbose_name='药品简介')
    drug_number = models.IntegerField(verbose_name='药品数量')
    drug_pirce = models.FloatField(verbose_name='药品价格')
    class Meta:
        db_table = 'drug'


class Drug_put_in(models.Model):
    """
    药品入库记录表
    """
    for_drug=models.ForeignKey(to='Drug',on_delete=models.CASCADE,verbose_name='药物id')
    in_date = models.DateTimeField(auto_now_add=True,verbose_name='入库时间')
    for_staff = models.ForeignKey(to='Staff_info',on_delete=models.CASCADE,verbose_name='负责职工id')

    class Meta:
        db_table = 'drug_put_in'

class Drug_put_out(models.Model):
    """
    药品出库记录
    """
    for_drug = models.ForeignKey(to='Drug', on_delete=models.CASCADE, verbose_name='药物id')
    out_date = models.DateTimeField(auto_now_add=True,verbose_name='出库时间')
    for_user = models.ForeignKey(to='User_info',on_delete=models.CASCADE,verbose_name='用户表外键')
    for_med = models.ForeignKey(to='Medical_records',on_delete=models.CASCADE,verbose_name='就诊记录外键')
    for_staff = models.ForeignKey(to='Staff_info',on_delete=models.CASCADE,verbose_name='职工表医生外键')

    class Meta:
        db_table = 'drug_put_out'


class Registered(models.Model):
    """
    挂号记录
    """
    for_user = models.ForeignKey(to='User_info',on_delete=models.CASCADE,verbose_name='用户表外键')
    for_sub = models.ForeignKey(to='Subject', to_field='id', on_delete=models.CASCADE, verbose_name='科室表的外键', null=True)
    for_staff = models.ForeignKey(to='Staff_info',on_delete=models.CASCADE,verbose_name='职工表医生外键')
    datatime = models.DateTimeField(auto_now_add=True,verbose_name='挂号时间')
    yes_or_no = models.BooleanField(verbose_name='是否就诊',default=False)
    yes_or_no_manay = models.BooleanField(verbose_name='是否缴费',default=False)

    class Meta:
        db_table = 'registered'


class Medical_records(models.Model):
    """
    就诊记录表
    """
    for_user = models.ForeignKey(to='User_info',on_delete=models.CASCADE,verbose_name='用户表外键')
    for_staff = models.ForeignKey(to='Staff_info',on_delete=models.CASCADE,verbose_name='职工表医生外键')
    for_res = models.ForeignKey(to='Registered',on_delete=models.CASCADE,verbose_name='挂号表外键')
    suggest = models.CharField(max_length=30,verbose_name='就诊建议')
    hospitalization= models.BooleanField(verbose_name='是否住院',default=False)

    class Meta:
        db_table = 'medical_records'

class pay_items(models.Model):
    '''
    收费项目管理
    '''
    pro_name = models.CharField(max_length=50,verbose_name='收费项目')
    pro_price = models.IntegerField(verbose_name='金额')
    pro_data = models.DateTimeField(auto_now_add=True,verbose_name='穿件日期')

    class Meta:
        db_table='pay_items'


class Records_drug(models.Model):
    '''
    就诊药物
    '''
    for_user = models.ForeignKey(to='User_info',on_delete=models.CASCADE,verbose_name='用户表外键')
    for_drug = models.ForeignKey(to='Drug',on_delete=models.CASCADE,verbose_name='药物表外键')
    price = models.FloatField(verbose_name='单价')
    number = models.IntegerField(verbose_name='药品数量')
    yes_or_no = models.BooleanField(verbose_name='是否缴费',default=False)

    class Meta:
        db_table = 'records_drug'

class Records_pro(models.Model):
    '''
    就诊项目
    '''
    for_rec = models.ForeignKey('Medical_records',on_delete=models.CASCADE,verbose_name='就诊记录ID')
    for_pro = models.ForeignKey('pay_items',on_delete=models.CASCADE,verbose_name='收费项目外键')
    price = models.IntegerField(verbose_name='价格')
    yes_or_no = models.BooleanField(verbose_name='是否缴费',default=False)

    class Meta:
        db_table = 'records_pro'

class Pay_cost(models.Model):
    """
    缴费记录
    """
    for_user = models.ForeignKey(to='User_info',on_delete=models.CASCADE,verbose_name='用户表外键')
    project = models.CharField(max_length=30,verbose_name='缴费项目')
    data = models.DateTimeField(auto_now_add=True,verbose_name='缴费时间')

    class Meta:
        db_table = 'pay_cost'


class Hospitl_records(models.Model):
    """
    入住记录
    """
    for_user = models.ForeignKey(to='User_info',on_delete=models.CASCADE,verbose_name='用户表外键')
    for_house = models.ForeignKey(to='House_room', to_field='id', on_delete=models.CASCADE, verbose_name='房间表的外键')
    for_care = models.ForeignKey(to='Staff_info',on_delete=models.CASCADE,verbose_name='职工表护工外键')
    for_med = models.ForeignKey(to='Medical_records', on_delete=models.CASCADE, verbose_name='就诊记录外键')
    data = models.DateTimeField(auto_now_add=True,verbose_name='入院时间')
    dates_num = models.IntegerField(verbose_name="住院天数")
    bed = models.IntegerField(verbose_name="床位号")
    yes_or_no = models.BooleanField(verbose_name='是否缴费',default=False)
    is_whether = models.BooleanField(verbose_name='是否出院',default=False)
    cash = models.IntegerField(verbose_name='缴纳押金')

    class Meta:
        db_table = 'hospitl_records'


class Medical_zhi(models.Model):
    """
    治疗记录
    """
    for_user = models.ForeignKey(to='User_info',on_delete=models.CASCADE,verbose_name='用户表外键')
    for_drug = models.ForeignKey(to='Drug',on_delete=models.CASCADE,verbose_name='药品表外键')
    use_number = models.IntegerField(verbose_name='所需数量')
    sent_number = models.IntegerField(verbose_name='已给数量')
    for_care = models.ForeignKey(to='Staff_info',on_delete=models.CASCADE,verbose_name='职工表外键')

    class Meta:
        db_table = 'medical_zhi'
