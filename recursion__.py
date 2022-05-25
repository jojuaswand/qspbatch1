def disp(i=0):
    if i < 5:
        print("hello world")
        i += 1
        disp(i)

disp()
