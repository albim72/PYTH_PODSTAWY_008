f= open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()

f= open("dane.txt","a",encoding="utf-8")
f.write("\nTomasz,60")
f.close()

f= open("info.txt","w",encoding="utf-8")
f.write("to jest ważna informacja: 1133")
f.close()
