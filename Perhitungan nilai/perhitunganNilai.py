print("Aplikasi Menghitung Nilai")
print("-"*30)

# Nilai UTS
# Ngeprint pertanyaan di terminal, terus akhirnya pake "end=""" supaya inputnya gak muncul di line baru
print("Nilai UTS : ",end="")
# Pake input untuk pengguna masukin nilai
nuts=int(input())
# Nilai yang udah dimasukin, dikaliin sesuai ketentuan dari soal terus di masukin di variable nilai_uts
nilai_uts=0.25*nuts

# Nilai UAS
# Ngeprint pertanyaan di terminal, terus akhirnya pake "end=""" supaya inputnya gak muncul di line baru
print("Nilai UAS : ",end="")
# Pake input untuk pengguna masukin nilai
nuas=int(input())
# Nilai yang udah dimasukin, dikaliin sesuai ketentuan dari soal terus di masukin di variable nilai_uas
nilai_uas=0.30*nuas

# Nilai praktikum
# Ngeprint pertanyaan di terminal, terus akhirnya pake "end=""" supaya inputnya gak muncul di line baru
print("Nilai PRAKTIKUM : ",end="")
# Pake input untuk pengguna masukin nilai
prak=int(input())
# Nilai yang udah dimasukin, dikaliin sesuai ketentuan dari soal terus di masukin di variable nilai_prak
nilai_prak=0.30*prak

# Nilai tugas
# Ngeprint pertanyaan di terminal, terus akhirnya pake "end=""" supaya inputnya gak muncul di line baru
print("Nilai TUGAS : ",end="")
# Pake input untuk pengguna masukin nilai
tgs=int(input())
# Nilai yang udah dimasukin, dikaliin sesuai ketentuan dari soal terus di masukin di variable nilai_prak
nilai_tgs=0.15*tgs

# Ngehitung total nilai buat nanti ditentuin nilai akhirnya apa
# Jumlahin nilai_uts+nilai_uas+nilai_prak+nilai_tgs terus masukin ke variable nilai_akhir
nilai_akhir=nilai_uts+nilai_uas+nilai_prak+nilai_tgs
print('-'*30)
# Ngeprint total nilai di layar pake format print(f"{}") dimana di dalam kurung siku itu masukin variable
# yang mau diprint
print(f"Total Nilai : {nilai_akhir}")
# Bikin varible kosong nah(Disini nanti yang diganti jadi A, AB, dst)
nah=""

# Logika aplikasinya
# Kalo nuts atau nuas atau prak diisi kosong sama pengguna maka
# otomatis nilainya E
if(nuts==0) or (nuas==0) or (prak==0):
    nah="E"
elif(nilai_akhir>=80 and nilai_akhir<=100): #Kalo nilainya lebih besar sama dengan 80 dan lebih kecil sama dengan 100, nilai akhir==A
    nah="A"
elif(nilai_akhir>=75 and nilai_akhir<80): #Kalo nilainya lebih besar sama dengan 75 dan lebih kecil dari 80, nilai akhir==AB
    nah="AB"
elif(nilai_akhir>=65 and nilai_akhir<75): #Kalo nilainya lebih besar sama dengan 65 dan lebih kecil dari 75, nilai akhir==B
    nah="B"
elif(nilai_akhir>=50 and nilai_akhir<65): #Kalo nilainya lebih besar sama dengan 50 dan lebih kecil dari 65, nilai akhir==BC
    nah="BC"
elif(nilai_akhir>=40 and nilai_akhir<50): #Kalo nilainya lebih besar sama dengan 40 dan lebih kecil dari 50, nilai akhir==C
    nah="C"
elif(nilai_akhir>=30 and nilai_akhir<40): #Kalo nilainya lebih besar sama dengan 30 dan lebih kecil dari 40, nilai akhir==D
    nah="D"
elif(nilai_akhir<30): #Kalo nilainya lebih kecil dari 30, nilai akhir==E
    nah="E"
# Ngeprint nilai akhir
print(f"Nilai akhir : {nah}")
