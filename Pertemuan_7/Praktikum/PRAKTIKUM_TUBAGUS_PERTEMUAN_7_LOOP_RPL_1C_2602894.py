#Tubagus Muhammad Ivan Syah Winata Kusuma
#RPL 1C
#2602894

#PERTEMUAN 7 LOOP

#=====================================
#Soal 1
#Seorang mahasiswa membeli 5 buku dengan harga
#yang sama, yaitu Rp25.000 per buku. Hitung total
#biaya pembelian menggunakan perulangan.
#=====================================

# buku = 5
# harga = 25000
# total = 0

# for i in range(buku):
#     total += harga
#     print(f"Hitungan ke-{i+1} : {total}")

# print(f"Total Harga = {total}")

#=====================================
#Soal 2
#Dosen ingin memasukkan nilai 5 mahasiswa,
#kemudian menghitung rata-ratanya. (Menggunakan input dinamis)
#=====================================

# nilai = []

# for x in range(5):
#     nilai.append(int(input(f"Masukan nilai siswa ke-{x+1} :")))
    
# rata_rata = sum(nilai)/len(nilai)

# print(f"Rata rata nilai mahasiswa : {rata_rata}")

#=====================================
#Soal 3
#Program harus menghitung jumlah seluruh
#bilangan genap dari 0 sampai 20.
#=====================================

# total = 0

# for i in range(0, 21, 2):
#     total += i

# print(total)

#=====================================
#Soal 4
#Dosen memasukkan nilai 5 mahasiswa.
#Mahasiswa dinyatakan lulus jika nilainya minimal 65.
#Program menghitung jumlah mahasiswa yang lulus.
#=====================================

#Soal 4 V1

# lulus = 0
# jumlah_mahasiswa = 5

# for x in range(jumlah_mahasiswa):
#     nilai_siswa = int(input(f"Masukan nilai siswa ke-{x+1} :"))
#     if nilai_siswa >= 65:
#         lulus += 1

# print(f"Jumlah mahasiswa yang lulus : {lulus}")

#Soal 4 V2
# nilai = []
# lulus = 0
# jumlah_mahasiswa = 5

# for x in range(jumlah_mahasiswa):
#     nilai_siswa = int(input(f"Masukan nilai siswa ke-{x+1} :"))
#     nilai.append(nilai_siswa)


# for i in range(jumlah_mahasiswa):
#     print(f"Nilai Siswa ke-{i+1} : {nilai[i]}")
#     if nilai[i] >= 65:
#         lulus += 1
#         print("Lulus")
#     else:
#         print("Tidak Lulus")
    
# print(f"Jumlah mahasiswa yang lulus : {lulus}")











### LATIHAN PERCOBAAAN SAJA###
# jumlah_perulangan = 3

# for index in range(jumlah_perulangan):
#     print(f"Print ke-{index}")

# for index in range(1,6):
#     print(f"Print ke-{index}")

# for index in range(10,0,-1):
#     print(f"Print ke-{index}")
    
# for i in "Python":
#     print(f"Huruf:{i}")
    
# buah = ["apel","belimbing","ceri","durian"]

# for i in buah:
#     print(f"Buah : {i}")
    
# for i in range(len(buah)):
#     print(f"Buah : {buah[i]}")
    
# for i in range(-2,-10,-2):
#     print(f"Nilai:{i}")

# angka = 0
# while(angka < 8):
#     print(f"Angka sekarang : {angka}")
#     angka += 1

# angka = [1,2,3,4,5,6,7,8,9,10]

# for i in angka:
#     print(i)
#     if(i==3):
#         break

# angka = [1,2,3,4,5,6,7,8,9,10]

# for i in angka:
#     if(i==3):
#         continue
#     print(i)

# buah = ["apel","semangka","tomat"]
# angka = [1,2]

# for i in buah:
#     for j in angka:
#         print(i)
#         print(j)

# nested_list = [["apel","ceri"],[1,2]]

# for i in nested_list:
#     for j in i:
#         print(j)