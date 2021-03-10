#!/usr/bin/env python3
# coding=utf-8
import os
import time,datetime
import sys

sys.path.append('/mnt/maillog/')
b = sys.path
from com.vpiaotong.database.MySQL import MySQL
conn = MySQL().GetConnect()
cursor = conn.cursor()
temporary = []


for root, dirs, files in os.walk('/logs/maillogs/', topdown=True):
    for name in files:
        file = os.path.join(root, name)
        price = file.split('/')
        server = price[3]#取上级目录名
        log_type1 = price[4].split('.')[0]#取的是文件名
        if log_type1 == 'smtpserver':
            cursor.execute("SELECT last_log_time from input_log_record  WHERE  server = (%s) and log_type = (%s)" ,(server,log_type1))
            last_record_time = cursor.fetchone()
            conn.commit()
            if last_record_time is None:  # 如果input_log_record1库中取到的时间值是否为空，如果为空赋值一个初始时间
                last_record_time = datetime.datetime.strptime("11/01/18 00:00:00", "%d/%m/%y %H:%M:%S")
                history_time = last_record_time  # 得到一个初始datetime格式的初始时间，用于判断读取文件的时间点
                cursor.execute("INSERT INTO input_log_record(`server`, `log_type`, `last_log_time`) VALUES (%s,%s,%s)",
                                (server, log_type1, history_time))
                conn.commit()
            else:  # 如果数据库不等于空，在数据库中拿到时间由于判断读取文件的时间点
                history_time = last_record_time[0]
                history_time.strftime("%Y-%m-%d %H:%M:%S")
            with open(file) as f:
                count=0
                for line in f:
                    file_lines = line.split()
                    if file_lines is  None or len(file_lines) < 8:
                        continue
                    try:
                        temp1 = (datetime.datetime.strptime(file_lines[4] + ' ' + file_lines[5],"%d/%m/%y %H:%M:%S"))
                    except Exception:continue
                    log_type = file_lines[6]
                    if history_time >= temp1:  #判断读取日志文件时间点位置，数据库时间是否大于等于原文件中时间
                         continue
                    else:
                        try:
                            log_time = time.strptime(file_lines[4] + ' ' + file_lines[5], "%d/%m/%y %H:%M:%S")
                        except Exception:continue
                        log_content = [str(i) for i in file_lines[8:]] #把句柄中的以列表的形式取值并转换成list
                        log_content = ' '.join(log_content).strip()#合成字符串
                        cursor.execute("INSERT INTO mail_smtp_log(`server`,`log_time`,`log_type`,`log_content`) VALUES (%s,%s,%s,%s)",(server,time.strftime('%Y-%m-%d %H:%M:%S',log_time ) ,log_type,log_content) )
                        count +=1
                    temporary = [server, log_type, log_time]
                    conn.commit()
            if len(temporary)!= 0:
                server2 = temporary[0]
                log_time2 =temporary[2]
                cursor.execute("UPDATE input_log_record SET server = (%s),log_type = (%s),last_log_time = (%s) WHERE log_type = (%s) and server = (%s)",
                                (server2, log_type1, time.strftime('%Y-%m-%d %H:%M:%S', log_time2),log_type1,server))
                conn.commit()
        else:
            continue
cursor.close()
os.system('nohup python3 /mnt/maillog/com/vpiaotong/mail/log/importMAILLET_log.py >> /logs/analy_start/importMAILLET_log.out  2>&1 &')

