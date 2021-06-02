def testing(var1, var2, var3):
    listlist = var1, var2, var3
    for data in listlist:
        if data == ' ':
            listlist.remove()



if __name__ == '__main__':
    q1 = 'hallo'
    q2 = 3
    q3 = 'miep'

    testing(q1, q2, q3)
