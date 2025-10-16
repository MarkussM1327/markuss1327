import os
os.system('cls')
dict={
    0:7,
    1:4,
    2:5,
    3:8,
    4:1,
    5:2,
    6:9,
    7:0,
    8:3,
    9:6
}
a=input("Enter a number - ").strip()

if a.len()<2:
    print(dict[a])

