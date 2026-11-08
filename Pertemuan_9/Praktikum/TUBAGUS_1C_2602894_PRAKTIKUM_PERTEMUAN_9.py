# Nama : Tubagus Muhammad Ivan Syah Winata Kusuma
# Kelas : 1C
# Nim : 2602894

# def sapa():
#     print("Halo Gais")

# sapa()
# sapa()
# sapa()

# def luas_persegi(sisi):
#     return sisi * sisi

# print(luas_persegi(4))

# def telefun():
#     return "Halo Om"

# pesan = telefun()
# print(pesan)

# def miaw():
#     pass

# def nama_keturunan(nama):
#     print(nama + "Widodo")

# nama_keturunan("Joko")
# nama_keturunan("Gibran")
# nama_keturunan("Luhut")

# def pesan_mail(nama):
#     print(f"Halo, Yth Nasabah {nama} yang terhormat. Pinjaman anda Sebesar 5 juta sudah jatuh tempo")

# pesan_mail("owi")

# def nama_lengkap(ndepan, nbelakang):
#     print(ndepan + " " + nbelakang)

# nama_lengkap("James", "Bond")

# def sapa(name = "Kawan"):
#     print("Hello", name)

# sapa("Adit")
# sapa("Kaysan")
# sapa()
# sapa("Faza")

# def muda(*anak):
#     print("Paling muda " + anak[2])

# muda("Emil", "Tobias", "Linus")

# def total_angka(*angka):
#     total = 0
#     print(angka)
#     for i in angka:
#         total += num
#     return total

# print(total_angka(1,2,3,4,5))

##########################
## LATIHAN 1
##########################

### NO 1


# def fibonacci(n, a = 0, b = 1):
#     if n == 0:
#         print(a)
#         return
#     else:
#         print(a)
#         return fibonacci(n-1,b,a+b)

# fibonacci(int(input("Masukan jumlah iterasi fibonnaci : ")))

### NO 2

# def hitung_volume_tabung(jari_jari, tinggi_tabung):
#     luas_alas = 3.14 * jari_jari * jari_jari
#     volume = luas_alas * tinggi_tabung
#     return volume

# input_jari_jari = float(input("Masukkan jari-jari alas tabung: "))
# input_tinggi = float(input("Masukkan tinggi tabung: "))

# hasil_volume = hitung_volume_tabung(input_jari_jari, input_tinggi)
# print("Volume tabung adalah:", hasil_volume)

### NO 3

# input_angka = []

# def nilai_total(*angka):
#     total = sum(angka)
#     return total

# def nilai_rata_rata(*angka):
#     total = sum(angka)
#     jumlah_angka = len(angka)
#     rata_rata = total / jumlah_angka
#     return rata_rata

# jumlah_angka = int(input('Masukan jumlah angka nya: '))

# for i in range(jumlah_angka):
#     input_angka.append(int(input(f"Masukan Angka ke {i+1} : ")))
    
# print(f"Total : {nilai_total(*input_angka)}")
# print(f"Rata-rata : {nilai_rata_rata(*input_angka)}")

##########################
## LATIHAN 2
##########################

# jumlah_kesempatan = 3

# def kesempatan(password):
#    if password == "Latihan":
#         return True
#     else:
#         return False

# print("Login kedalam akun Anda \n")

# while jumlah_kesempatan != 0:
#     username = input("Usename: ")
#     password = kesempatan(input("Password: "))
#     if not password:
#         print("Password salah")
#         jumlah_kesempatan -= 1
#         if jumlah_kesempatan != 0:
#             print(f"Sisa kesempatan login {jumlah_kesempatan}x lagi")
#     else:
#         print("Login berhasil")
#        break
# else:
#    print("Kesempatan login Anda habis.")

##########################
## LATIHAN 3
##########################

# def hitung_detik_total(h, m, s):
#     return (h * 3600) + (m * 60) + s
# 
# 
# def dapatkan_selisih(j_awal, m_awal, d_awal, j_akhir, m_akhir, d_akhir):
#     detik_awal = hitung_detik_total(j_awal, m_awal, d_awal)
#     detik_akhir = hitung_detik_total(j_akhir, m_akhir, d_akhir)
# 
#     total_jeda = detik_akhir - detik_awal
# 
#     out_jam = total_jeda // 3600
#     sisa_waktu = total_jeda % 3600
#     out_menit = sisa_waktu // 60
#     out_detik = sisa_waktu % 60
# 
#     return out_jam, out_menit, out_detik
# 
# 
# print("=== Waktu Mulai ===")
# j_awal = int(input("Jam   : "))
# m_awal = int(input("Menit : "))
# d_awal = int(input("Detik : "))
# 
# print("=== Waktu Selesai ===")
# j_akhir = int(input("Jam   : "))
# m_akhir = int(input("Menit : "))
# d_akhir = int(input("Detik : "))
# 
# res_jam, res_menit, res_detik = dapatkan_selisih(
#     j_awal, m_awal, d_awal,
#     j_akhir, m_akhir, d_akhir
# )
# print(f"Selisihnya adalah {res_jam} jam - {res_menit} menit - {res_detik} detik")
