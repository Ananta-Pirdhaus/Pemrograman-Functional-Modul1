# Inisialisasi data peserta (kosong)
peserta = []

# Fungsi untuk mengecek hasil akhir
def cek_hasil(nilai):
    return "Lolos" if nilai >= 75 else "Tidak Lolos"

# Fungsi untuk admin
def admin():
    while True:
        print("\nMenu Admin:")
        print("1. Tambah Peserta")
        print("2. Edit Nilai Peserta")
        print("3. Lihat Data Peserta")
        print("0. Kembali")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            nama = input("Masukkan nama peserta: ")
            nilai = int(input("Masukkan nilai peserta: "))
            peserta.append({"id": len(peserta), "nama": nama, "nilai": nilai})
            print("Peserta berhasil ditambahkan.")
        elif pilihan == "2":
            id_peserta = int(input("Masukkan ID peserta: "))
            if id_peserta < len(peserta):
                p = peserta[id_peserta]
                print(f"\nID: {p['id']}, Nama: {p['nama']}, Nilai: {p['nilai']}")
                print(f"Hasil Akhir: {cek_hasil(p['nilai'])}")
                new_nilai = int(input("Masukkan nilai baru: "))
                peserta[id_peserta]["nilai"] = new_nilai
                print("Nilai berhasil diubah.")
            else:
                print(f"\nID Peserta {id_peserta} tidak ditemukan.")
        elif pilihan == "3":
            lihat_data()  # Panggil fungsi lihat_data
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 0.")

# Fungsi untuk melihat data peserta
def lihat_data():
    print("\nData Peserta:")
    print(f"{'ID':<5}{'Nama':<15}{'Nilai':<15}{'Status':<15}")  # Header kolom
    for p in peserta:
        print(f"{p['id']:<5}{p['nama']:<15}{p['nilai']:<15}{cek_hasil(p['nilai'])}")

# Fungsi untuk info peserta
def info_peserta():
    id_peserta = int(input("\nMasukkan ID Anda: "))
    if id_peserta < len(peserta):
        p = peserta[id_peserta]
        print(f"\nID: {p['id']}, Nama: {p['nama']}, Nilai: {p['nilai']}")
        print(f"Hasil Akhir: {cek_hasil(p['nilai'])}")
    else:
        print(f"\nID Peserta {id_peserta} tidak ditemukan.")

# Fungsi untuk memilih peran
def choose_role():
    while True:
        print("\nPilih Peran:")
        print("1. Admin")
        print("2. Peserta")
        print("0. Keluar")
        role = input("Masukkan peran Anda: ")
        if role == "1":
            admin()
        elif role == "2":
            print("\nPilihan:")
            print("1. Lihat Data Peserta")
            print("2. Lihat Info Saya")  # Ubah nomor pilihan menjadi 2
            pilihan = input("Masukkan pilihan Anda: ")
            if pilihan == "1":
                lihat_data()
            elif pilihan == "2":
                info_peserta()
            else:
                print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")
        elif role == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 0.")

if __name__ == "__main__":
    choose_role()
