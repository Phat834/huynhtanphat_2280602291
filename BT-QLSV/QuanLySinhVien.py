from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        MaxId = 1
        if self.soluongSinhVien() > 0:
            MaxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if MaxId < sv._id:
                    MaxId = sv._id
            MaxId += 1
        return MaxId

    def soluongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSV(self):
        id = self.generateID()
        ten = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap nganh hoc: ")
        diemtb = float(input("Nhap diem trung binh: "))
        sv = SinhVien(id, ten, sex, major, diemtb)
        self.listSinhVien.append(sv)
        self.xeploaiHocLuc(sv)

    def updateSV(self, id):
        sv = self.findById(id)
        if (sv != None):
           
            ten = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh: ")
            major = input("Nhap nganh hoc: ")
            diemtb = float(input("Nhap diem trung binh: ")) 

 
            sv._ten = ten
            sv._sex = sex
            sv._major = major
            sv._diemtb = diemtb
            self.xeploaiHocLuc(sv)
        else:
                print("Sinh vien co ID: {} khong ton tai".format(id))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._major, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemtb, reverse=False)

    def findById(self, id):
        for sv in self.listSinhVien:
            if sv._id == id:
                return sv
        return None

    def findByName(self, keyword):
        listSV = []
        for sv in self.listSinhVien:
            if keyword.upper() in sv._ten.upper():
                listSV.append(sv)
        return listSV  
    def deleteByID(self, id):
        sv = self.findById(id)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xeploaiHocLuc(self, sv: SinhVien):
        if sv._diemtb >= 8:
            sv._hocluc = "Gioi"
        elif sv._diemtb >= 6.5:
            sv._hocluc = "Kha"
        elif sv._diemtb >= 5:
            sv._hocluc = "Trung Binh"
        else:
            sv._hocluc = "Yeu"

    def ShowSinhVien(self, listSV):
        print("{:<5} {:<15} {:<10} {:<12} {:<10} {:<10}"
              .format("ID","Ten","Gioi Tinh","Nganh Hoc","Diem TB","Hoc Luc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<5} {:<15} {:<10} {:<12} {:<10.2f} {:<10}"
                      .format(sv._id, sv._ten, sv._sex, sv._major, sv._diemtb, sv._hocluc))
            print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
