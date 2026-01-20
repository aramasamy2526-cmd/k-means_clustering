temperatures = [32, 35, 30, 28, 33, 31, 29]
print(temperatures[0:4]) #Get first 4 days of temperature
print(temperatures[3:-1])#Get last 3 days of temperature
print(temperatures[-1::-1])#Reverse the temperature list
print(temperatures[-1::-2])#Get alternate day temperatures in reverse





for i in range(len(temperatures)):
    print(i, temperatures[i])




