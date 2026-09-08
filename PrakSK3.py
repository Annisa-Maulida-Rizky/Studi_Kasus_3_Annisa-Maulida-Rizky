Daftar_buku = ("Sistem Informasi", "Pengantar Ilmu Komputer", "Basis Data", "Psikologi Digital", "Digital ParenThink")
peminjaman= []

print ("menampilkan daftar buku: ")

for buku in Daftar_buku:
    print (buku)

while True:
    Pinjam_Buku = input("Mau meminjam buku apa? (Ketik selesai untuk berhenti): ")
    if Pinjam_Buku == "selesai": 
        break

    if Pinjam_Buku in Daftar_buku:
        print("Buku berhasil dipinjam!")
        peminjaman.append(Pinjam_Buku)

    else:
        print("Maaf buku tidak tersedia")

print("Daftar buku yang dipinjam: ")
for buku in peminjaman: 
    print("-", buku)

penghapusan = input ("Apakah anda ingin menghapus buku dari list?(ya/tidak): ")

if penghapusan == "ya":
    hapus = str(input("Masukkan nama buku yang ingin dihapus: "))

    if hapus in peminjaman:
        peminjaman.remove(hapus)
        print("Buku berhasil dihapus")

    else:
        print("Maaf buku tidak valid")

elif penghapusan == "tidak":
    print("Tidak ada buku yang dihapus")

else:
    print("Pilihan tidak valid")

print("Daftar buku yang dipinjam: ")
for buku in peminjaman: 
    print("-", buku)