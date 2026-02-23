from database import data_inventaris as data # rename agar lebih pendek

def hapus_barang(id):
    barang_ditemukan = None # default calue

    for barang in data:
        if barang["id"] == id:
            barang_ditemukan = barang # Id barang
            break

    if barang_ditemukan: # none = false,
        data.remove(barang_ditemukan) # mengahpus barang
        print(f"Barang dengan ID {id} berhasil dihapus.") # message success
    else:
        print(f"Barang dengan ID {id} tidak ditemukan.") # message failed