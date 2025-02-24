sogiolam = float(input("Nhap so gio lam moi tuan: "))
luongtheogio = float(input("Nhap so luong lam theo gio: "))

giotieuchuan = 44
giovuotchuan = max (0, sogiolam - giotieuchuan)

thuclinh = giotieuchuan * luongtheogio + giovuotchuan * luongtheogio * 1.5

print(f"So tien thuc linh cua nhan vien: {thuclinh}")