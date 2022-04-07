f=open("text.txt","r")
u=open("update_text.txt","w")
i=0
for x in f:
    i+=1
    u.write(str(i)+" "+x)
f.close()
u.close()