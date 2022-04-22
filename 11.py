gz = 4
import pickle
class Tovar:
    name = None
    amout = None
    price = None


f = open('bAZ1.txt', 'r', encoding='utf-8')
S = []
while True:
    x = f.readline()
    if not x:
        break
    s = Tovar()
    x = x.split(' ', 3)
    s.name = x[0]
    s.amout = x[2]
    s.price = x[1]
    S.append(s)
f2 = open('bAZ2.dat', 'wb')
pickle.dump(S, f2)
f.close()
f2.close()
while True:
    n = int(input())
    f3 = open('bAZ2.dat', 'rb')
    B = pickle.load(f3)
    if n == 1:
        for i in range(gz):
            print(B[i].name, B[i].price, B[i].amout)
        f3.close()
    elif n == 2:
        sfz = input()
        xz = []
        for i in B:
            print(sfz, i.name)
            if sfz == i.name:
                zxc = input().split(' ', 3)
                i.name = zxc[0]
                i.amout = zxc[2]
                i.price = zxc[1]
                f3.close()
            xz.append(i)
        f4 = open('bAZ2.dat', 'wb')
        pickle.dump(xz, f4)
        f4.close()
    elif n == 3:
        a = []
        z = []
        for i in B:
            b = []
            b.append(i.name)
            b.append(i.price)
            b.append(i.amout)
            z.append(b)
            a.append(int(i.price))
        a.sort()
        sz = []
        for i in a:
            izx = Tovar()
            for ix in range(len(z)):
                if i == int(z[ix][1]):
                    izx.name = z[ix][0]
                    izx.amout = z[ix][2]
                    izx.price = z[ix][1]
                    sz.append(izx)
        f3.close()
        f4 = open('bAZ2.dat', 'wb')
        pickle.dump(sz, f4)
        f4.close()
    elif n == 4:
        a = []
        z = []
        for i in B:
            b = []
            b.append(i.name)
            b.append(i.price)
            b.append(i.amout)
            z.append(b)
            a.append(i.name)
        a.sort()
        sz = []
        for i in a:
            izx = Tovar()
            c = []
            for ix in range(len(z)):
                if i == z[ix][0]:
                    if i not in c:
                        izx.name = z[ix][0]
                        izx.amout = z[ix][2]
                        izx.price = z[ix][1]
                        sz.append(izx)
                        c.append(i)
                    else:
                        l = c.index(i)
                        c.pop(l)
        f3.close()
        f4 = open('bAZ2.dat', 'wb')
        pickle.dump(sz, f4)
        f4.close()
    elif n == 5:
        f4 = open('bAZ3.txt', 'w')
        for i in range(gz):
            f4.write(B[i].name + ' ')
            f4.write(B[i].price + ' ')
            f4.write(B[i].amout + '\n')
        f4.close()
    elif n == 6:
        sfz = input()
        xz = []
        for i in B:
            if sfz == i.name:
                print(i.name,i.amout,i.price)
                i.price = zxc[1]
                break
                f3.close()
