'''
Created on 2016-04-18
Author: xiaohanfei
'''
from django.db import models
import logging
import subprocess,os
from django.conf import settings
# 部署PHP环境
class Php(models.Model):
    branchname   = models.CharField(u'分支名称',max_length=200)
    TYPE_CHOICES = (
    (u'pc', u'pc'),
    (u'wap', u'wap'),
    (u'admin', u'admin'),
    (u'ios', u'ios'),
    )
    environment_type = models.CharField(u'环境类型',max_length=20,choices=TYPE_CHOICES)
    environment_num = models.IntegerField(u'环境编号',default=0)
    author  = models.CharField(u'部署作者',max_length=20)
    add_time = models.DateTimeField(u'添加时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __str__(self):
        return u'%s %s %s %s' % (self.branchname, self.author, self.environment_type , self.environment_num)

    class Meta:
        verbose_name = '部署PHP环境' #提供自述名显示
        verbose_name_plural = '部署PHP环境' #自述名复述形式
        ordering = ['-add_time']

    def save(self, *args, **kwargs):
        super(self.__class__, self).save(*args, ** kwargs) #将数据写入数据库  
        branchname = self.branchname
        environment_type = self.environment_type
        environment_num = self.environment_num
        if environment_num == 0 or environment_num == 1:
            game_dir = '/data/httpd/game/'+environment_type
        else:
            game_dir = '/data/httpd/game'+str(environment_num)+'/'+environment_type
        #判断当前环境是否指向当前分支
        os.chdir(game_dir)
        cmd = "git branch"
        r_all = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
        r_all = r_all.stdout.readlines()
        logging.debug(r_all)
        now_branchname_list = []
        for r_each in r_all:
            now_branchname = r_each.decode()[2:-1]
            sign = r_each.decode()[0:1]
            now_branchname_list.append(now_branchname)
            if now_branchname == branchname:
               if sign == '*': 
                  cmd = 'git pull'
                  subprocess.Popen('git checkout -- .',stdout=subprocess.PIPE,shell=True)
                  r = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
                  logging.debug(r.stdout.readlines())
               else:
                  os.chdir(settings.SCRIPT_URL)
                  cmd = 'nohup python php_checkout.py '+branchname+' '+game_dir+'&'
                  r = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
                  logging.debug(r)
        logging.debug(now_branchname_list)
        if branchname not in now_branchname_list:  
            os.chdir(settings.SCRIPT_URL)
            cmd = 'nohup python php_deploy.py '+branchname+' '+game_dir+'&'
            r = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
            logging.debug(r)
        return 


# 部署JAVA环境
class Java(models.Model):
    branchname   = models.CharField(u'分支名称',max_length=200)
    TYPE_CHOICES = (
    (u'GameSupport', u'GameSupport'),
    (u'GameGateway', u'GameGateway'),
    (u'GameAPI', u'GameAPI'),
    )
    branch_type = models.CharField(u'分支类型',max_length=20,choices=TYPE_CHOICES)
    author  = models.CharField(u'部署作者',max_length=20)
    add_time = models.DateTimeField(u'添加时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __str__(self):
        return u'%s %s %s' % (self.branchname,self.branch_type,self.author)

    class Meta:
        verbose_name = '部署JAVA环境' #提供自述名显示
        verbose_name_plural = '部署JAVA环境'
        ordering = ['-add_time'] #按照添加时间倒序排列

    def save(self, *args, **kwargs): 
        super(self.__class__, self).save(*args, ** kwargs)
        branchname = self.branchname
        branch_type = self.branch_type
        dir = '/home/www/'
        os.chdir(dir)
        cmd = 'sh git_deploy.sh '+branch_type+' '+branchname
        logging.debug(cmd)
        output = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).stdout.readlines()
        logging.debug(output)
        return

#更新测试环境帐户余
class UpdateAccount(models.Model):
    login_name   = models.CharField(u'用户名或游戏id',max_length=20)
    TYPE_CHOICES = (
    (u'1', u'挺豆'),
    (u'2', u'T点'),
    (u'3', u'T币'),
    (u'4', u'彩金'),
    )
    amount_type = models.CharField(u'金额类型',max_length=20,choices=TYPE_CHOICES)
    amount  = models.CharField(u'金额',max_length=20)
    author  = models.CharField(u'操作人',max_length=20)
    add_time = models.DateTimeField(u'添加时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __str__(self):
        return u'%s %s' % (self.login_name,self.author)

    class Meta:
        verbose_name = '更改测试账号余额'
        verbose_name_plural = '更改测试账号余额'
        ordering = ['-add_time']

    def save(self, *args, **kwargs): 
        super(self.__class__, self).save(*args, ** kwargs)
        login_name = self.login_name
        amount_type = self.amount_type
        amount = self.amount
        os.chdir(settings.SCRIPT_URL)
        cmd = 'python up_user_account.py '+login_name+' '+amount+' '+amount_type
        r = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
        logging.debug(cmd)
        logging.debug(r)
        return r