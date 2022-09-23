def image(width, length):
    count = 1
    list = []
    list1 = []
    while count <= width:
        list.append("*")
        count += 1
    list1.append(list)
    count = 1
    count1 = length - 2
    s = ["*"]
    while count < width - 1:
        s.append(" ")
        count+=1
    s.append("*")
    while count1 > 0:
        list1.append(s)
        count1 -= 1
    list1.append(list)
    for i in list1:
        print(''.join(i))
image(5,5)
