"""
Fungsi mengambil parameter uang
"""
def kembalian(uang):
    print("Total   : Rp{}".format(uang))
    """
    Membuat himpunan yang berisi kumpulan nominal kembalian
    """
    nominal_kembalian = [200,500,1000,2000,5000,
    10000,20000,50000,100000]
    """
    Membuat himpunan kosong untuk solusi.
    """
    himpunan_solusi={}
    """
    Membuat iterasi dari panjang himpunan nominal_kembalian hingga
    ke nol
    """
    i = len(nominal_kembalian)-1

    """
    Selama i masih lebih sama dengan nol maka lakukan operasi
    dimana mencari angka terbesar dalam nominal_kembalian yang
    lebih kecil dibandingkan variable uang. Jika kandidat dalam
    nominal kembalian lebih kecil daripada varible uang, maka masukan
    kandidat kedalam himpunan solusi dan kurangi uang dengan kandidat tersebut.
    Jika uang tersebut 0, maka print hasil.
    """
    while(i>=0):
        while(uang>=nominal_kembalian[i]):
            uang-=nominal_kembalian[i]
            if(nominal_kembalian[i] not in himpunan_solusi):
                himpunan_solusi[nominal_kembalian[i]]=1
            else:
                himpunan_solusi[nominal_kembalian[i]]+=1
        i-=1
    print("Kembali : ",end="\n")
    for solusi,jumlah in himpunan_solusi.items():
        print("Rp{} : {} lembar".format(solusi,jumlah))
"""
Driver untuk memasukan uang.
"""
if __name__ == '__main__':
    uang = 3500
    kembalian(uang)