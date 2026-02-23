from database import data_inventaris as data

def tambah_barang(id, nama, jumlah, harga):
    barang_baru = {
        "id": id,
        "nama": nama,
        "jumlah": jumlah,
        "harga": harga
    }
    data.append(barang_baru)
    print(f"Barang '{nama}' berhasil ditambahkan.")

def lihat_barang():
    if not data:
        print("Inventaris kosong.")
        return

    print("\n--- Daftar Barang ---")
    for barang in data:
        print(f"ID: {barang['id']} | Nama: {barang['nama']} | Jumlah: {barang['jumlah']} | Harga: {barang['harga']}")
    print("---------------------\n")