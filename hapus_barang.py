from database import data_inventaris

def hapus_barang():
    print("=== Hapus Barang ===")
    id_barang = input("Masukan ID barang yang ingin dihapus: ")
    for barang in data_inventaris:
        if barang['id'] == id_barang:
            data_inventaris.remove(barang)
            print("Barang Berhasil dihapus!")
            return 
    print("Barang dengan ID tersebut tidak ditemukan!") 