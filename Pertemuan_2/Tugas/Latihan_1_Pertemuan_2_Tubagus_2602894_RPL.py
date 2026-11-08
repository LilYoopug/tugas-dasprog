nama_user = str(input("Masukkan nama Anda: "))
tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
tahun_sekarang = 2026 #jika ingin fleksibel tanpa manual mengisi tahun bisa menggunakan library date
usia = int(tahun_sekarang - tahun_lahir)

print(f"Selamat datang, {nama_user}! Umur Anda sekarang adalah {usia} tahun.")