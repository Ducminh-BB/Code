n = int(input("nhap thang "))
if n > 8 and n % 2:
    print("30 ngay")
elif n > 8 and n // 2:
    print("31 ngay")
if 2 < n <= 8 and n % 2:
    print("31 ngay")
elif 2 < n <= 8 and n // 2:
    print("30 ngay")
if 0 < n <= 2:
    print("28 hoac 31 ngay")


