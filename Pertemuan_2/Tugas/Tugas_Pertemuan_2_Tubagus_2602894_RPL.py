jumlah_peserta = int(input("Masukkan jumlah peserta seminar: "))
biaya_sewa_tempat = int(input("Masukkan biaya sewa tempat (Rp): "))
biaya_dokumentasi = int(input("Masukkan biaya dokumentasi (Rp): "))

# ================= A. Biaya Konsumsi =================
harga_konsumsi = int(35000)  # rupiah / paket
persen_cadangan_konsumsi = int(10)  # persen

cadangan_konsumsi = int(jumlah_peserta * persen_cadangan_konsumsi / 100)
if jumlah_peserta * persen_cadangan_konsumsi / 100 > cadangan_konsumsi:
    cadangan_konsumsi += 1

jumlah_konsumsi = int(jumlah_peserta + cadangan_konsumsi)
total_biaya_konsumsi = int(jumlah_konsumsi * harga_konsumsi)

print(f"A. Perhitungan Biaya Konsumsi")
print(f"- Jumlah konsumsi yang disediakan (termasuk cadangan): {jumlah_konsumsi} paket")
print(f"- Total biaya konsumsi: Rp {total_biaya_konsumsi}")

# ============= B. Kebutuhan Cetak Sertifikat ==========
lembar_per_rim = int(500)  # lembar / rim
harga_per_rim = int(65000)  # rupiah / rim
persen_cadangan_sertifikat = int(5)  # persen

cadangan_sertifikat = int(jumlah_peserta * persen_cadangan_sertifikat / 100)
if jumlah_peserta * persen_cadangan_sertifikat / 100 > cadangan_sertifikat:
    cadangan_sertifikat += 1

jumlah_sertifikat = int(jumlah_peserta + cadangan_sertifikat)
jumlah_lembar = int(jumlah_sertifikat)

jumlah_rim = int(jumlah_lembar / lembar_per_rim)
if jumlah_lembar / lembar_per_rim > jumlah_rim:
    jumlah_rim += 1

total_biaya_kertas = int(jumlah_rim * harga_per_rim)

print(f"\nB. Perhitungan Kebutuhan Cetak Sertifikat")
print(f"- Jumlah sertifikat yang perlu dicetak: {jumlah_sertifikat} lembar")
print(f"- Jumlah lembar kertas yang dibutuhkan: {jumlah_lembar} lembar")
print(f"- Perkiraan jumlah rim kertas yang diperlukan: {jumlah_rim} rim")
print(f"- Total biaya pembelian kertas: Rp {total_biaya_kertas}")

# ============= C. Biaya Pendaftaran Peserta ==========
persen_dana_cadangan = int(10)  # persen

total_biaya_acara = int(total_biaya_konsumsi + total_biaya_kertas + biaya_sewa_tempat + biaya_dokumentasi)
dana_cadangan = int(total_biaya_acara * persen_dana_cadangan / 100)
total_dana_dikumpulkan = int(total_biaya_acara + dana_cadangan)
biaya_per_peserta = int(total_dana_dikumpulkan / jumlah_peserta)

print(f"\nC. Perhitungan Biaya Pendaftaran Peserta")
print(f"- Total biaya penyelenggaraan acara: Rp {total_biaya_acara}")
print(f"- Besar dana cadangan: Rp {dana_cadangan}")
print(f"- Total dana yang harus dikumpulkan: Rp {total_dana_dikumpulkan}")
print(f"- Biaya pendaftaran per peserta: Rp {biaya_per_peserta}")