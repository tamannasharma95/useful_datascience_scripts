data= input("Enter data: ")
f=open("data.txt",'a')
#if you want to append use "a" in place of w
f.write("\n")
f.write(data)
f.close()