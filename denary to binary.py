def main():
    a=input("Write number you want to convert to binary: ")
    if a=="":
        print("Number wasn't inserted")
        main()
    else:
        a=int(a)
        s=""
        while a>=2:
            s=s+str(a%2)
            a=a//2
        s=s+"1"

        print(s[::-1])
        main()
main()