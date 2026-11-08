# Nama : Tubagus Muhammad Ivan Syah Winata Kusuma
# Kelas : 1C
# Nim : 2602894
jarak_tempuh = int(180) # kilometer
konsumsi_bbm = int(12) # kilometer / liter
harga_bbm = int(13000) # rupiah / liter

jumlah_bbm = int(jarak_tempuh / konsumsi_bbm)
biaya_bbm = int(jumlah_bbm * harga_bbm)

print(f"Untuk menempuh jarak {jarak_tempuh} km, Kita memerlukan:")
print(f"- Jumlah BBM: {jumlah_bbm} liter")
print(f"- Biaya BBM: Rp {biaya_bbm}")
