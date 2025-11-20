# Program Input Nilai Mahasiswa
# Menggunakan Dictionary
data = {}
def header():
    print("Program Input Nilai")
    print("=====================")
def tabel():
    print("\nDaftar Nilai")
    print("====================================================================")
    print("| NO |   NIM   |   NAMA   | TUGAS | UTS | UAS | AKHIR |")
    print("====================================================================")
    if not data:
        print("|                          TIDAK ADA DATA                          |")
    else:
        no = 1
        for nim, isi in data.items():
            nama, tugas, uts, uas, akhir = isi
            print(f"| {no:2} | {nim:6} | {nama:8} |  {tugas:4} | {uts:3} | {uas:3} | {akhir:5.2f} |")
            no += 1
    print("====================================================================")
def tambah():
    print("\nTambah Data")
    nim = input("NIM     : ")
    nama = input("Nama    : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS   : "))
    uas = int(input("Nilai UAS   : "))
    akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
    data[nim] = [nama, tugas, uts, uas, akhir]
def ubah():
    print("\nUbah Data")
    nim = input("Masukkan NIM : ")
    if nim in data:
        nama = input("Nama Baru     : ")
        tugas = int(input("Nilai Tugas   : "))
        uts = int(input("Nilai UTS     : "))
        uas = int(input("Nilai UAS     : "))
        akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
        data[nim] = [nama, tugas, uts, uas, akhir]
        print("Data berhasil diubah!")
    else:
        print("Data tidak ditemukan!")
def hapus():
    print("\nHapus Data")
    nim = input("Masukkan NIM : ")
    if nim in data:
        del data[nim]
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")
def cari():
    print("\nCari Data")
    nim = input("Masukkan NIM : ")
    if nim in data:
        nama, tugas, uts, uas, akhir = data[nim]
        print("\nData ditemukan:")
        print("NIM   :", nim)
        print("Nama  :", nama)
        print("Tugas :", tugas)
        print("UTS   :", uts)
        print("UAS   :", uas)
        print("Akhir :", f"{akhir:.2f}")
    else:
        print("Data tidak ditemukan!")
# MAIN LOOP
while True:
    header()
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    pilihan = input("Pilih menu : ").lower()
    if pilihan == "l":
        tabel()
    elif pilihan == "t":
        tambah()
    elif pilihan == "u":
        ubah()
    elif pilihan == "h":
        hapus()
    elif pilihan == "c":
        cari()
    elif pilihan == "k":
        break
    else:
        print("Menu tidak tersedia!")
