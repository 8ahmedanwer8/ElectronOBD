# import sys 

# import time
# import json
# lst = [11,1,1,1,1,1,1,1,1,1]


# # # import obd
# # # connection = obd.OBD()
# # # response = connection.query(obd.commands.RPM)


# # # arg = sys.stdin.readlines()
# # # arg = json.dumps(arg)
# # c = 0
# # while c < 1000:
# # 	data = sys.stdin.readlines()
# # 	# if arg:
# # 	# 	export(arg)
# # 	data = 4
# # 	print(json.dumps(lst))
# # 	# print(data)
# # 	c = c +1 


# import sys, json
# import random 
# #Read data from stdin
# def read_in():
#     lines = sys.stdin.readlines()
#     return json.loads(lines[0])

# def main():
#     #get our data as an array from read_in()
#     lines = "no msg"

#     total_sum_inArray = 0
#     for item in lines:
#         total_sum_inArray += item
#     print ("lines",lines)
#     # print("random number: ", random.randint(0,500))
#     while True:
#         lines = sys.stdin.readlines()
#         lines = json.loads(lines[0])       
#         time.sleep(1)
#         print("random num: ",random.randint(0,10) )    
# main()

# # while True:
# #     main()
# #     time.sleep(1)
# #     print("random num: ",random.randint(0,10) )


import sys, json, time, random, select
import pandas as pd

#Read data from stdin
# def read_in():
#     lines = sys.stdin.readlines()
#     return json.loads(lines[0])

# def main():
#     print("begin")
#     c = 0

#     while c < 10000:
#         inp = int(input())    
#         print("input to python: ", inp)   
#         print([random.randint(1,100)])
#         c = c+1
#         if inp:
#             break


# main()


# for i in range(1,999):
#     time.sleep(0.3)
#     output = []
#     for data in range(1,104):
#         output.append(random.randint(10,90000))
#     print(json.dumps(output))
    # c=c+1
    # inp = json.loads(input())
    # inp = int(input())
    # if inp != 1:
    #     break

# labels = ['1','1','1','1','1','1','1','1','1','1',]
# def csv_exporter(labels, readings):
#     dictionary = dict(zip(labels, zip(*readings)))
#     df = pd.DataFrame(dictionary)
#     df.to_csv('export.csv', encoding='utf-8')
#     return df


# from threading import Thread
# c = 0
# data = []
# def main():
#     while True:
#         time.sleep(0.3)
#         output = []
#         for _ in range(1,42):
#             output.append(random.randint(1,10000000))
#             data.append(output)
#         print(json.dumps(output))
#         if c != 0:
#             csv_exporter(labels, data)
#             break
#     return

# inputListener = Thread(target = main)
# inputListener.daemon = True
# inputListener.start()
# d = 0
# while d<100:
#     inp = input()
#     if (inp):
#         c = 1
#     d = d + 1



#Code to test connection and OBD
import obd 
obd.logger.setLevel(obd.logging.DEBUG) # enables all debug information
ports = obd.scan_serial()      
if len(ports)>1:
    c = obd.OBD(ports[1])
else:
    c = obd.OBD(ports[0])

# c = obd.OBD()
d = 0 
for i in range(1,1000):
    r = c.query(obd.commands.RPM)
    print(r)
    d = d +1



