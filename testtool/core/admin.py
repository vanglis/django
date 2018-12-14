'''
Created on 2016-04-18
Author: xiaohanfei
'''
from django.contrib import admin
from .models import Php,Java,UpdateAccount
from django.conf import settings
import logging
import subprocess,os,re
import time

# Register your models here.


class PhpAdmin(admin.ModelAdmin):
    list_display = ('branchname','environment_type','environment_num','author','add_time')
    actions = ['delete_branch']

    def delete_branch(self, request, queryset):
        branchname = queryset.get().branchname   #分支名
        environment_type = queryset.get().environment_type #环境类型
        environment_num = queryset.get().environment_num #环境编号

        if environment_num == 0 or environment_num == 1:
            game_dir = '/data/httpd/game/'+environment_type
        else:
            game_dir = '/data/httpd/game'+str(environment_num)+'/'+environment_type
        #判断当前环境是否指向当前分支
        os.chdir(game_dir)
        cmd = "git branch"
        r_all = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
        r_all = r_all.stdout.readlines()
        now_branchname_list = []
        for r_each in r_all:
            now_branchname = r_each.decode()[2:-1]
            sign = r_each.decode()[0:1]
            now_branchname_list.append(now_branchname)
            if now_branchname == branchname:
               if sign == '*': 
                  msg = "当前分支正在使用，无法删除"
               else:
                  cmd = 'git branch -D '+branchname
                  r = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
                  queryset.delete()
                  msg = branchname+'：分支已删除'
                  logging.debug(msg)
        logging.debug(now_branchname_list)
        if branchname not in now_branchname_list:  
            msg = "当前分支不存在，无需删除"
        self.message_user(request, msg)
        return
    delete_branch.short_description = "删除当前分支"

class JavaAdmin(admin.ModelAdmin):
    list_display = ('branchname','branch_type','author','add_time')
    actions = ['delete_branch']

    def delete_branch(self, request, queryset):
        branchname = queryset.get().branchname
        branch_type = queryset.get().branch_type
        game_dir = '/data/appsystem/apps'
        os.chdir(game_dir)
        if branchname == 'master':
           branchname_key = branch_type
           cmd = "rm -rf "+branchname_key+".*"
           logging.debug(cmd)
           subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
           queryset.delete()
           msg = branchname+'：分支已删除'
        else:  
           branchname_key = re.search(r'[^/]+$', branchname).group(0)
           cmd = "find . -name '*"+branchname_key+"*'"
           r_all = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
           r_all = r_all.stdout.readlines()
           logging.debug(r_all)
           for r_each in r_all:
               cmd = "rm -rf "+r_each.decode()
               logging.debug(cmd)
               subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
           queryset.delete()    
           msg = branchname+'：分支已删除' 
        self.message_user(request, msg)      
        return
    delete_branch.short_description = "删除当前分支"

class UpdateAccountAdmin(admin.ModelAdmin):
    list_display = ('login_name','amount_type','amount','author','add_time')

#admin.site.register([Php,Java])
admin.site.register(Php,PhpAdmin)
admin.site.register(Java,JavaAdmin)
admin.site.register(UpdateAccount,UpdateAccountAdmin)
admin.site.disable_action('delete_selected')#删除默认动作