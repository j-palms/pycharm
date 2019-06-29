def up_low(string):
    for i in string:
        u = 0
        l = 0
        if i == i.upper:
            u += 1
        else:
            l += 1
    print ("The string contains:{} upper case and {} lower case letters!".format(u,l))
    return [u,l]

a = up_low("Hallo Ich Kann Zaehlen")
print (a)
print (10)
