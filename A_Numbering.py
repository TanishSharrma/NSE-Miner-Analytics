group_size = 5
blank = 1
start = 1
end = 246

filex = open("A_Temp.txt", "r+")
temp = ""
res = ""
for q in range (group_size+blank):
    temp += "\n"

for i in range(start, end+1):
    res += str(i)+ temp

filex.write(res)
filex.close()