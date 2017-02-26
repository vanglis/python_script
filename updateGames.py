#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015-09-09
Author: xiaohanfei
'''
import os
def updateWap(dir_wap):
    os.chdir(dir_wap)
    cmd1 = os.system('git checkout -- .')
    cmd2 = os.system('git pull')
    cmd3 = os.system('cp /data/httpd/game_config/gameHall/app/config.php ./app/')
    cmd4 = os.system('git fetch -p')
def updatePc(dir_pc):
    os.chdir(dir_pc)
    cmd1 = os.system('git checkout -- .')
    cmd2 = os.system('git pull')
    cmd3 = os.system('cp /data/httpd/game_config/gamepc/app/config.php ./app/')
    cmd4 = os.system('git fetch -p')
def updateAdmin(dir_admin):
    os.chdir(dir_admin)
    cmd1 = os.system('git checkout -- .')
    cmd2 = os.system('git pull')
    cmd3 = os.system('cp /data/httpd/game_config/youxi-admin/app/config.php ./app/')
    cmd4 = os.system('git fetch -p')
if __name__ == "__main__":
    for i in range(2,15):
       dir_wap = "/data/httpd/game"+str(i)+"/wap/"
       dir_pc = "/data/httpd/game"+str(i)+"/pc/"
       dir_admin = "/data/httpd/game"+str(i)+"/admin/"
       updateWap(dir_wap)
       print("wap更新完毕")
       updatePc(dir_pc)
       print("pc更新完毕")
       updateAdmin(dir_admin)
       print("admin更新完毕")
