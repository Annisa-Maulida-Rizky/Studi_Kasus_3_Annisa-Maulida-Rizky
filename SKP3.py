#Tuple Daftar Buku
Daftar_buku = ("Pendosa yang Merindukan Tuhan", 
               "Psikologi Digital", "Digital Marketing Trend",
                 "Pengantar Ilmu Komputer", "Menyelami Dunia Telnologi", 
                 "Digital ParenThink" )

#List pinjaman kosong
List_Pinjaman =[]

#Daftar buku
print("Daftar buku yang tersedia:")

for buku in Daftar_buku:
    print("-", buku)

#Peminjaman berulang
while True:
    print("Menu peminjaman: ")
    print("1. pinjam buku")
    print("2. hapus buku dari daftar pinjam")
    print("3. selesai")

    pilihan = input ("pilih menu(1/2/3): ")

    if pilihan == "1" :
        judul = input ("Masukkan judul buku: ")

    #Validasi buku
        if judul in Daftar_buku:
            List_Pinjaman.append(judul)
            print ("Buku berhasil dipinjam!")
        else:
            print("Buku tidak tersedia")

    elif pilihan == "2" :
        if not List_Pinjaman:
            print("Belum ada buku yang dipinjam")
        else:
            print("Daftar buku yang dipinjam: ")
            for buku in List_Pinjaman:
                print("-", buku)

    #Penghapusan buku dari list
            judul_hapus = input ("Masukkan judul buku yang ingin dihapus: ")

            if judul_hapus in List_Pinjaman:
                List_Pinjaman.remove(judul_hapus)
                print("Buku berhasil dihapus dari daftar pinjam")
            else:
                print("Buku tidak ada dalam daftar pinjam")

#Seluruh daftar buku yang dipinjam
    elif pilihan == "3":
        print("Daftar buku yang dipinjam: ")

        if not List_Pinjaman:
            print("Anda belum meminjam buku")
        else:
            for buku in List_Pinjaman:
                print("-", buku)

        break

    else:
        print("Pilihan anda tidak valid, harap memilih ulang.")


