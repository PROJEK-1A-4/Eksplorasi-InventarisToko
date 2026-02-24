from database import data_inventaris

def update_barang(): 
    print("=== Update Barang ===")
    id = input("Masukkan ID barang yang ingin diupdate: ")  

    for barang in data_inventaris:
        if barang['id'] == id:
            nama_baru = input(f"Nama baru (enter untuk skip, saat ini: {barang['nama']}): ")
            jumlah_baru = input(f"Jumlah baru (enter untuk skip, saat ini: {barang['jumlah']}): ")
            harga_baru = input(f"Harga baru (enter untuk skip, saat ini: {barang['harga']}): ")

            if nama_baru != "":
                barang['nama'] = nama_baru
            if jumlah_baru != "":
                barang['jumlah'] = int(jumlah_baru)  
            if harga_baru != "":
                barang['harga'] = int(harga_baru)    

            print("Barang berhasil diupdate!")
            print(f"Id: {barang['id']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
            return

    print("Barang dengan ID tersebut tidak ditemukan!")