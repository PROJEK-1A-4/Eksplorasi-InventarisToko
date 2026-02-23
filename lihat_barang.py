from database import data_inventaris

def lihat_barang():
    print("== Daftar Barang di Inventaris ==")
    for barang in data_inventaris:
        print(f"Id: {barang['id']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")