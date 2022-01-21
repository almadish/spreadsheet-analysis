# place your code to clean up the data file below.
import os

f = open("data.csv", "r")
save_path = 'data'
path = os.path.join(save_path, "clean_data.csv")
csv_file = open(path, "w")

s = f.readline()

while "DBN" not in s:
    s = f.readline()
s = s.split(",")
s[-1] =  s[-1][:-1]
s.extend(["Num of AP Exams Failed\n"])
s = ",".join(s)
csv_file.write(s)

s = f.readline()

while True:
    if s != "":
        s = s.split(",")
        if s[-3] == "s" or s[-3] == "s" or s[-1] == "s\n":
            s = f.readline()
            continue
        else:
            s[-1] =  s[-1][:-1]
            s.extend([str(int(s[-2])-int(s[-1]))+"\n"])
            s = ",".join(s)
            csv_file.write(s)
            s = f.readline()
    else:
        break

csv_file.close()
'''
s[-1] =  s[-1][:-1]

while True:
    if s != "":
        s = s.split(",")
        for i in range(len(s)):
            if s[i] == "s" or s[i] == "s\n":
                s[i] = "#N/A"
        if s[-2] == "#N/A" or s[-1] == "#N/A":
            s.extend(["#N/A"])
            s = ",".join(s) + "\n"
        else:
            s[-1] =  s[-1][:-1]
            s.extend([str(int(s[-2])-int(s[-1]))+"\n"])
            s = ",".join(s)
        csv_file.write(s)
        s = f.readline()
    else:
        break
'''








