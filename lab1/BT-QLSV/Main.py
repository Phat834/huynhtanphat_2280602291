from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("================================Menu================================")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien boi ID")
    print("3. Xoa sinh vien boi ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat chuong trinh")
    print("====================================================================")

    try:
        key = int(input("Nhap lua chon cua ban: "))
        if key < 0 or key > 7:
            raise ValueError 
    except ValueError:
        print("\nLỗi, không hợp lệ, xin nhập lại!")
        continue  

    if key == 1:
        print("\n1. Them sinh vien")
        qlsv.nhapSV()
        print("Them sinh vien thanh cong")

    elif key == 2:
        if qlsv.soluongSinhVien() > 0:
            print("\n2. Cap nhat thong tin sinh vien")
            id = int(input("Nhap ID: ")) 
            qlsv.updateSV(id)
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 3:
        if qlsv.soluongSinhVien() > 0:
            print("\n3. Xoa sinh vien")
            id = int(input("Nhap ID: "))  
            if qlsv.deleteByID(id):
                print("\nXoa thanh cong sinh vien co id =", id)
            else:
                print("\nSinh vien co ID {} khong ton tai".format(id))
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 4:
        if qlsv.soluongSinhVien() > 0:
            print("\n4. Tim kiem sinh vien theo ten")
            ten = input("Nhap ten sinh vien: ")
            searchResult = qlsv.findByName(ten)
            qlsv.ShowSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 5:
        if qlsv.soluongSinhVien() > 0:
            print("\n5. Sap xep sinh vien theo diem trung binh")
            qlsv.sortByDiemTB()
            qlsv.ShowSinhVien(qlsv.listSinhVien) 
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 6:
        if qlsv.soluongSinhVien() > 0:
            print("\n6. Sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.ShowSinhVien(qlsv.listSinhVien)
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 7:
        if qlsv.soluongSinhVien() > 0:
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.ShowSinhVien(qlsv.listSinhVien)
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 0:
        print("\n0. Thoat chuong trinh")
        break
