#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import datetime
import schedule
import time
import os

success = 0
fail = 0

def tryRequestQuestion():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('tryRequestQuestion time :',ts)

    global success
    global fail
    r = requests.get('')
    if (r.status_code == 200 and r.json()['code'] == 0):
        success += 1
    else:
        fail += 1
        print("retry request...")
        tryRequestQuestion()

def startTask():
    print("startTask pid: ", os.getpid())

    #清空任务
    schedule.clear()
    #创建一个按 分钟 间隔执行任务
    schedule.every(60).seconds.do(tryRequestQuestion)
    while True:
        schedule.run_pending()
        time.sleep(1)

startTask()

