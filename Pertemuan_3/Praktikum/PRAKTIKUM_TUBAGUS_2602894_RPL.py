# Tubagus Muhammad Ivan Syah Winata Kusuma - 2602894 - RPL - 1C
print("=========================================")
print("                Praktikum")
print("=========================================")

buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

print("1. Ganti item dengan nama “ceri” menjadi “cherry”")
print("Sebelum:", buah)
# Mengganti item dengan nama "ceri" menjadi "cherry"
buah[2] = "cherry"
print("Sesudah:", buah)


print("\n2. Tambahkan item dengan nama dan index yang ditentukan oleh User")
print("Sebelum:", buah)
# Menambahkan item dengan nama dan index yang ditentukan oleh User
index = int(input("Masukkan index: "))
nama = input("Masukkan nama buah: ")
buah.insert(index, nama)
print("Sesudah:", buah)


print("\n3. Urutkan item pada list sesuai dengan abjadnya")
print("Sebelum:", buah)
# Mengurutkan item pada list sesuai dengan abjadnya
buah.sort()
print("Sesudah:", buah)
