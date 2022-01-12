import random
import math
train_len=int(input("enter"))
man_spd=int(input("enter"))
train_time=int(input("enter"))
rs=(train_len/train_time)*18/5
train_spd=rs+man_spd
print("train speed:",train_spd)