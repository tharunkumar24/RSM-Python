import math
train_length = int(input("Enter length of the train:"))
train_speed = int(input("Enter the speed of the train:"))
man_speed = int(input("Enter the speed of the man:"))
relative_speed = train_speed + man_speed 
distance = train_length
r_s = relative_speed * 5/18
time = distance / r_s
print("Time taken for the train to cross:", time)
exit (0)