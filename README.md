# Praktikum 5

**Nama:** Naziha Raiqi Aribino<br>
**Kelas:** TI.25.A2<br>
**NIM:** 312510232<br>
**Mata Kuliah:** Pengantar Pemrograman<br>

---

## <a id="latihan-1"></a>**LATIHAN 1 — Dictionary Daftar Kontak**

Latihan ini bertujuan untuk memahami dasar penggunaan **dictionary** dalam Python, seperti:

* Menambah data
* Menghapus data
* Mengubah data
* Mengakses key dan value
* Menampilkan seluruh data dalam dictionary

### **Penjelasan Program**

Program membuat sebuah dictionary bernama `kontak` berisi pasangan *nama* dan *nomor telepon*. Lalu dilakukan beberapa operasi:

1. Menampilkan nomor telepon milik *Ari*.
2. Menambah kontak baru bernama *Riko*.
3. Mengubah nomor telepon *Dina*.
4. Menampilkan semua nama.
5. Menampilkan semua nomor telepon.
6. Menampilkan semua nama beserta nomornya.
7. Menghapus kontak *Dina*.

### **Kode Program**

```python
kontak = {
    "Ari": "081267889",
    "Dina": "087677776",
}

print("Kontak Ari:", kontak["Ari"])

kontak["Riko"] = "087654544"
print("\nSetelah tambah kontak Riko:")
print(kontak)

kontak["Dina"] = "088999776"
print("\nSetelah ubah kontak Dina:")
print(kontak)

print("\nSemua Nama:")
for nama in kontak.keys():
    print(nama)

print("\nSemua Nomor:")
for nomor in kontak.values():
    print(nomor)

print("\nDaftar Nama dan Nomor:")
for nama, nomor in kontak.items():
    print(nama, ":", nomor)

del kontak["Dina"]
print("\nSetelah hapus Dina:")
print(kontak)
```

### **Kesimpulan**

Latihan ini mengajarkan bagaimana menggunakan dictionary untuk menyimpan data pasangan *key–value*. Dictionary sangat berguna karena mudah dimodifikasi dan diakses menggunakan *key* yang unik.

---

## <a id="tugas-praktikum"></a>**TUGAS PRAKTIKUM — Program Daftar Nilai Mahasiswa**

Program ini menampilkan data nilai mahasiswa dan memberikan menu untuk:

* **(T)** Tambah data
* **(U)** Ubah data
* **(H)** Hapus data
* **(L)** Lihat semua data
* **(C)** Cari data berdasarkan NIM
* **(K)** Keluar dari program

Program menggunakan dictionary dengan format:

```
{ NIM: [Nama, Tugas, UTS, UAS, NilaiAkhir] }
```

---

### **Flowchart Program (dalam bentuk teks / pseudo-flowchart)**

```
                ┌─────────────────────────┐
                │        MULAI            │
                └─────────────┬──────────┘
                              │
                    ┌─────────▼───────────┐
                    │  Tampilkan Menu     │
                    └─────────┬───────────┘
                              │
                ┌─────────────▼────────────────┐
                │ Input pilihan (L/T/U/H/C/K)  │
                └───────┬──────────┬──────────┘
                        │          │
     ┌──────────────────▼─┐    ┌───▼────────────────┐
     │ Pilihan = "L" ?    │    │ Pilihan = "T" ?     │
     └──────┬────────────┘    └───────┬─────────────┘
            │ YES                     │ YES
   ┌────────▼──────────┐     ┌────────▼──────────┐
   │ Tampilkan Tabel   │     │ Input Data Baru    │
   └────────┬──────────┘     └────────┬──────────┘
            │                           │
     ┌──────▼─────────┐       ┌────────▼──────────┐
     │ Kembali ke Menu│       │ Simpan ke Dict    │
     └─────────────────┘       └────────┬──────────┘
                                        │
                      (Proses sama untuk U/H/C)
                                        │
                              ┌─────────▼──────────┐
                              │ Pilihan = "K" ?     │
                              └─────────┬──────────┘
                                        │ YES
                              ┌─────────▼──────────┐
                              │       SELESAI       │
                              └──────────────────────┘
```

---

### **Penjelasan Program**

Program ini menggunakan *looping* `while True` sehingga menu akan terus muncul sampai pengguna memilih `K` (keluar). Setiap menu memanggil fungsi yang berbeda:

### **1. tambah()**

* Meminta input NIM, nama, nilai tugas, UTS, UAS.
* Menghitung nilai akhir dengan rumus:
  **Akhir = 30% Tugas + 35% UTS + 35% UAS**
* Menyimpan data ke dictionary.

### **2. ubah()**

* Mengubah data mahasiswa berdasarkan NIM.

### **3. hapus()**

* Menghapus entri data dari dictionary.

### **4. cari()**

* Menampilkan satu data mahasiswa berdasarkan NIM.

### **5. tabel()**

* Menampilkan seluruh data dalam bentuk tabel rapi seperti contoh soal.

---

## **Kode Program**

```python
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

while True:
    header()
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    pilihan = input("Pilih menu : ").lower()

    if pilihan == "l": tabel()
    elif pilihan == "t": tambah()
    elif pilihan == "u": ubah()
    elif pilihan == "h": hapus()
    elif pilihan == "c": cari()
    elif pilihan == "k": break
    else: print("Menu tidak tersedia!")
```

---

## **Kesimpulan Tugas Praktikum**

Melalui praktikum ini, mahasiswa dapat memahami bagaimana:

* Mengelola data menggunakan dictionary Python.
* Membuat program interaktif dengan menu.
* Menggunakan fungsi untuk modularisasi kode.
* Membuat tabel output yang rapi.
* Menghitung nilai akhir dengan rumus.

Program ini bermanfaat sebagai dasar untuk membuat aplikasi manajemen data yang lebih kompleks.
