from time import time

start_time = time()

for i in range(0, 100000):
    print(i)

end_time = time()
elapsed = end_time - start_time



start_time1 = time()
my_list = [0] * 100000
for i in my_list:
    print(i)

end_time1 = time()
elapsed1 = end_time1 - start_time1  

print(elapsed)
print(elapsed1)