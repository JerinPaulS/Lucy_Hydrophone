import pandas as pd
import matplotlib.pyplot as plt
import math
from statistics import mean, stdev
import scipy.stats as stats
import pylab as pl

'''
def gaussian_transform(arr):

    u = mean(arr)
    sig = stdev(arr)
    fd = []
    a = 0
    pi = math.pi

    for i in arr:
        a = ((i - u) ** 2) / (2 * (sig ** 2))
        e = math.exp(-a)
        fd.append((1 / (sig * math.sqrt(2 * pi))) * e)

    return fd
'''

def convert_to_int(num):
    length = len(num)
    number = 0
    power_ten = length - 1
    for i in range(length):
        number = number + (int(num[i]) * 10 ** (power_ten))
        power_ten = power_ten - 1
    return number

def plot_graph(ys, Time, Comment, Temperature, Humidity, Sequence, num, N):
    x = []
    for i in range(num):
        x.append(i + 1)

    des = "Time: " + Time + ", Comment: " + Comment + ", Temperature: " + T + ", Sequence Number: " + S + ", Humidity: " + H + ", Total number of data points: " + N
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(des)
    plt.plot(x, ys)
    plt.show()

    ys.sort()
    fit = stats.norm.pdf(ys, mean(ys), stdev(ys))
    pl.plot(ys, fit, '-o')
    pl.hist(ys, density = True)
    pl.show()
    #y = gaussian_transform(ys)
    #plt.plot(ys, y)
    #plt.show()
    return 0

file = open('D:/Noise/Lucy.txt', 'r')
data = file.readlines()

req_data = []
description = []
points = []
flag = 0
count = 0
str = ""
Time = ""
Comment = ""
Temperature = 0.0
Humidity = 0.0
Sequence = 0
num_data_points = 0
num_instances = 0
Data_Points = []

for line in data:
    #print(line)
    for letter in line:
        flag = 0
        if letter == '\t' or letter == '\n' or letter == ' ':
            flag = 1
            req_data.append(str)

        else:
            str = str + letter

        if flag == 1:
            str = ""

flag = 0

for word in req_data:
    if word == "Data":
        flag = 1

    if flag == 1:
        points.append(word)

    else:
        description.append(word)

points = points[3 : ]

count = 0
dat = ""
processed_points = []
ys = []
indicator = 0

for point in points:
    if ':' in point:
        indicator = 1

    if indicator == 1:
        if len(point) < 8:
            dat = dat + point

        if len(point) == 8:
            processed_points.append(point)
            indicator = 0

        if len(dat) >= 6:
            processed_points.append(dat)
            dat = ""
            indicator = 0

    else:
        processed_points.append(point)

#print(processed_points)

for point in processed_points:
    if ':' in point:
        num_instances = num_instances + 1

print("Total number of instances are = ", num_instances)

#print(processed_points)

dcount = 0
ccount = 1
T = ""
S = ""
N = ""
H = ""

for point in processed_points:
    count = count + 1

    if ':' in point:
        Time = point
        count = 0
        if ccount == 1:
            if dcount > 0:
                plot_graph(ys, Time, Comment, T, H, S, num_data_points, N)
                ccount = 0
            dcount = dcount + 1
        ys = []

    if count == 1:
        Comment = point

    if count == 2:
        T = point
        Temperature = float(point)

    if count == 3:
        H = point
        Humidity = float(point)

    if count == 4:
        S = point
        Sequence = float(point)

    if count == 5:
        N = point
        num_data_points = int(point)

    if count > 5 and count < (num_data_points + 6):
        num_value = convert_to_int(point)
        ys.append(num_value)
        dcount = dcount + 1


#print(dcount)
#print(ys)
#print("\n\nTime: ", Time, "\nComment: ", Comment, "\nTemperature: ", Temperature, "\nSequence Number: ", Sequence, "\nHumidity: ", Humisity, "\nTotal number of data points: ", num_data_points)