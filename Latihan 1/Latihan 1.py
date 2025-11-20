# Latihan 1 – Dictionary daftar kontak
kontak = {
    "Ari": "081267889",
    "Dina": "087677776",
}
# Tampilkan kontaknya Ari
print("Kontak Ari:", kontak["Ari"])
# Tambah kontak baru
kontak["Riko"] = "087654544"
print("\nSetelah tambah kontak Riko:")
print(kontak)
# Ubah kontak Dina
kontak["Dina"] = "088999776"
print("\nSetelah ubah kontak Dina:")
print(kontak)
# Tampilkan semua Nama
print("\nSemua Nama:")
for nama in kontak.keys():
    print(nama)
# Tampilkan semua Nomor
print("\nSemua Nomor:")
for nomor in kontak.values():
    print(nomor)
# Tampilkan daftar Nama dan Nomornya
print("\ndaftar Nama dan Nomor:")
for nama, nomor in kontak.items():
    print(nama, ":", nomor)
# Hapus kontak Dina
del kontak["Dina"]
print("\nSetelah hapus Dina:")
print(kontak)
