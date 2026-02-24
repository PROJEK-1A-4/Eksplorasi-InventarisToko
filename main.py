from tambah_barang import tambah_barang
from update_barang import update_barang
from hapus_barang import hapus_barang
from lihat_barang import lihat_barang

def main():
    while True:
        print("="*5 + " " + "Sistem Inventaris Toko" + " " + "="*5)
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_barang()    
        elif pilihan == '2':
            lihat_barang()
        elif pilihan == '3':
            update_barang()
        elif pilihan == '4':
            hapus_barang()
        elif pilihan == '5':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

        print("\n")

if __name__ == "__main__":
    main()