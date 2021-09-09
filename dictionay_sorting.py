dict1={5:25,2:4,10:5,8:64,1:1,7:49}
print(sorted(dict1.items(),key=lambda kv:(kv[1],kv[0])))
print(sorted(dict1.items(),key=lambda kv:(kv[0],kv[1])))

