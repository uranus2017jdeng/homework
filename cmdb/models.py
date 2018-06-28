
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class cmdb_ci(models.Model):
    id = models.BigIntegerField('id',primary_key=True)
    name = models.CharField('名称',max_length=255)
    parent_id = models.BigIntegerField('父Ci')

class cmdb_atrr(models.Model):
    ci_id = models.BigIntegerField('Ci_id')
    prop_id = models.BigIntegerField('属性id')
    label = models.CharField('标签',max_length=200)
    description = models.CharField('描述',max_length=200)
    validator = models.SmallIntegerField('验证器ID')
    sort = models.IntegerField('排序')
    is_required = models.SmallIntegerField('是否必填')
    is_search = models.SmallIntegerField('是否可搜索')
    show_type = models.SmallIntegerField('字段显示方式')
    is_unique = models.SmallIntegerField('唯一类型')
    is_delete = models.SmallIntegerField('是否删除')

class cmdb_ci_entity(models.Model):
    id = models.BigIntegerField('id',primary_key=True)
    ci_id = models.BigIntegerField('Ci_id')
    name = models.CharField('显示名',max_length=1024)
    unique_name = models.CharField('唯一名',max_length=1024)

class cmdb_attr_entity(models.Model):
    id = models.BigIntegerField('id',primary_key=True)
    ci_entity_id = models.ForeignKey(cmdb_ci_entity,null=True,on_delete=True)
    atrr_id = models.ForeignKey(cmdb_atrr,null=True,on_delete=True)



