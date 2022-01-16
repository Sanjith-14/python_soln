num = int(input());
for i in range(num):
    n = input();
    if(n.isdigit() is True):
        if(len(n)==10):
                if(int(n[0])>=7 and int(n[0])<=9):
                    print("YES");
                else:
                    print("NO");
        else:
            print("NO");
    else:
            print("NO");
