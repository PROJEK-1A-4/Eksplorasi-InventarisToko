from database import data_inventaris as data

def hapus_barang():  
    id = input("Masukkan ID barang yang ingin dihapus: ") 
    barang_ditemukan = None

    for barang in data:
        if barang["id"] == id:
            barang_ditemukan = barang
            break

    if barang_ditemukan:
        data.remove(barang_ditemukan)
        print(f"Barang dengan ID {id} berhasil dihapus.")
    else:
        print(f"Barang dengan ID {id} tidak ditemukan.")