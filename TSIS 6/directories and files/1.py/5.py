list = ["Apple ","Banana ","Milk ","Salmon"]
f = open("products.txt","w")
f.writelines(list)
f.close()