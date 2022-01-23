import os
import time

list =[]
for adress, dirs, files in os.walk("C:\\Users\Admin\Desktop\sample"):
    for file in files:
        full =os.path.join(adress,file)
        #if ".txt" in full:
        if time.time() - os.path.getctime(full) < 86400:
            list.append(full)
print(list)
