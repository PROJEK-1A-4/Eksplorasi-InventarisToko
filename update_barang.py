from database import data_inventaris def update_barang(id, nama_baru=None, jumlah_baru=None, harga_baru=None): 
    # Mulai proses update barang 
    print("=== Update Barang ===") 
    # Looping untuk mencari barang berdasarkan ID for barang in data_inventaris: 
    if barang['id'] == id: 
    # Jika nama_baru diberikan, update field 'nama' 
    if nama_baru is not None: barang['nama'] = nama_baru