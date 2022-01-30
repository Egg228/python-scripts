import os
import time

list =[]
for adress, dirs, file in os.walk("C:\\Users\Admin\Desktop\sample"):
    for i in file: