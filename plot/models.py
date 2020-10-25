from django.db import models
from django.db.models import Model


# Create your models here.

# 做成什么样子

# 上传excel 文件
# 可以到看到上传的文件名和基本信息
# 和文件中包含的数据项


# 文件名 上传日期，  任务名
# 文件名是唯一的 文件一对多 到数据字段

# 数据字段
#  文件名 一级场景分类  二级场景分类 三级场景分类 用例编号，执行状态 执行结果 失败原因，备注

# 文件名  模块 成功率 失败率 大包版本


# 版本归档

# 文件名


class File(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    task_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:  # 自定义数据表名字
        db_table = "file"


class Item(models.Model):
    nid = models.AutoField(primary_key=True)
    case_name = models.CharField(max_length=64, unique=True)
    execute_status = models.CharField(max_length=64)  # 执行状态
    execute_result = models.CharField(max_length=64)  # 执行状态
    failed_reason = models.CharField(max_length=64)
    note = models.CharField(max_length=64)
    level_3 = models.ForeignKey(to='ModelMap', to_field='level_3', on_delete=models.CASCADE)
    file = models.ManyToManyField(to='File')

    def __str__(self):
        return self.case_name

    class Meta:  # 自定义数据表名字
        db_table = "item"


class ModelMap(models.Model):
    nid = models.AutoField(primary_key=True)
    level_1 = models.CharField(max_length=64)
    level_2 = models.CharField(max_length=64)

    level_3 = models.CharField(max_length=64,unique=True)
    def __str__(self):
        return self.level_1

    class Meta:  # 自定义数据表名字
        db_table = "modelmap"

# docker run -p 3306:3306 --name mysql8.0 -e MYSQL_ROOT_PASSWORD=123456 -d laradock_mysql