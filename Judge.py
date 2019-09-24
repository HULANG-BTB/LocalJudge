import os
import time
import random
from subprocess import *

def getJudgeFile() :
    cnt_dir = os.getcwd()
    file_list = os.listdir(cnt_dir);
    in_file = []
    out_file = []
    judge_file = []
    for item in file_list:
        name = os.path.splitext(item)[0]
        ext = os.path.splitext(item)[1][1:]
        if ext == "in" :
            in_file.append(name)
        elif ext == "out":
            out_file.append(name)
    for item in in_file:
        if item in out_file:
            judge_file.append(item)
    return judge_file

def judge(file_list):
    ns = 0
    for name in file_list:
        print("正在测试： " + name)
        stdin_file = open(name + ".in", "r")
        stdout_file = open(name + ".out", "r")
        time_begin = time.time()
        process = Popen("std.exe", shell=True, stdin=stdin_file, stdout=PIPE, stderr=STDOUT)
        time_end = time.time()
        time_cost = time_end - time_begin
        print("测试点： " + name + " 测试完成， 时间: " + format(time_cost,'.4f'))
        stdout_context = stdout_file.read().strip()
        myout_context = str(process.stdout.read(), encoding = "utf8").strip()
        if stdout_context == myout_context :
            print("通过")
            ns += 1
        else:
            print("\033[31m未通过")
            print("=====================")
            print("标准输出：")
            print(""+stdout_context)
            print("你的输出：")
            print(""+myout_context)
            print("=====================\033[32m")
        stdin_file.close()
        stdout_file.close()
    return ns
        
if __name__ == "__main__" :
    os.system("color 2")
    file_list = getJudgeFile()
    all = len(file_list)
    print("获取到测试点数目：" + str(all))
    ac = judge(file_list)
    print("测试点总数：" + str(all) + "通过：" + str(ac))
    os.system("pause")
    
