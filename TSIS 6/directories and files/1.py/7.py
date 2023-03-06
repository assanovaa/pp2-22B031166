with open("test.txt") as my_file:
    with open("out.txt","w") as another_file:
        for x in my_file:
            another_file.write(x)