print('----------------------------------------')
print('Nama     :Zahra Aulia Rahmah            ')
print('Program  :DDP MINPRO 2                  ')
print('----------------------------------------')


from prettytable import PrettyTable


# konsultasi
packages = {
    'konsultasi': {'konsultasi': 'facial', 'status': 'waiting list, jadwal, selesai'},
    'konsultasi': {'konsultasi': 'botox', 'status': 'waiting list, jadwal, selesai'},
    'konsultasi': {'konsultasi': 'angkat komedo', 'status': 'waiting list, jadwal, selesai'},
}


# data
pengguna = {
    'admin': {'password': 'mimin24', 'role': 'admin'},
    'zahra aulia rahmah': {'password': 'zahra24', 'role': 'pengguna'}
}

consultations = []


# login
def login():
    username = input("Username: ")
    password = input("Password: ")
    

    if username in pengguna and pengguna[username]['password'] == password:
        print(f"Login berhasil sebagai {pengguna[username]['role']}")
        return pengguna[username]['role'], username
    else:
        print("username atau password salah")
        return None, None


# admin
def admin_menu():
    while True:
        print("\nmenu Admin:")
        print("1. tambah Konsultasi")
        print("2. lihat Konsultasi")
        print("3. update Konsultasi")
        print("4. hapus Konsultasi")
        print("5. logout")
        choice = input("pilih menu: ")

        if choice == '1':
            add_consultation()
        elif choice == '2':
            read_consultation()
        elif choice == '3':
            update_consultation()
        elif choice == '4':
            delete_consultation()
        elif choice == '5':
            break
        else:
            print("pilihan tidak valid.")


# crate konsultasi
def add_consultation():
    nama = input("nama pengguna: ")
    perawatan = input("jenis perawatan: ")
    tanggal = input("tanggal konsultasi (DD/MM/YYYY): ")
    jam = input("jam konsultasi (HH:MM): ")
    consultation = {
        'id': len(consultations) + 1,
        'nama': nama,
        'perawatan': perawatan,
        'tanggal': tanggal,
        'jam': jam, 
        'status': 'waiting list'
    }
    consultations.append(consultation)
    print("konsultasi berhasil ditambahkan.")


# read konsultasi
def read_consultation():
    if consultations:
        table = PrettyTable()
        table.field_names = ["ID", "nama", "perawatan", "tanggal", "jam", "status"]
        for c in consultations:
            table.add_row([c['id'], c['nama'], c['perawatan'], c['tanggal'], c['jam'], c['status']])
        print(table)

    else:
        print("tidak ada konsultasi.")


# update konsultasi
def update_consultation():
    id_consultation = int(input("masukkan ID konsultasi yang ingin diperbarui: "))
    for c in consultations:
        if c['id'] == id_consultation:
            c['status'] = input("masukkan status baru (waiting list/jadwal/selesai): ")
            print("konsultasi berhasil diperbarui.")
            return
    print("konsultasi tidak ditemukan.")


# delete konsultasi
def delete_consultation():
    id_consultation = int(input("masukkan ID konsultasi yang ingin dihapus: "))
    for c in consultations:
        if c['id'] == id_consultation:
            consultations.remove(c)
            print("konsultasi berhasil dihapus.")
            return
    print("konsultasi tidak ditemukan.")


# pengguna
def pengguna_menu(username):
    while True:
        print("\nmenu pengguna:")
        print("1. buat konsultasi")
        print("2. lihat status konsultasi")
        print("3. logout")
        choice = input("pilih menu: ")

        if choice == '1':
            create_consultation(username)
        elif choice == '2':
            view_consultation(username)
        elif choice == '3':
            break
        else:
            print("pilihan tidak valid.")

# create konsultasi
def create_consultation(username):
    perawatan = input("jenis perawatan yang diminta: ")
    tanggal = input("tanggal konsultasi (DD/MM/YYYY): ")
    jam = input("jam konsultasi (HH:MM): ")
    consultation = {
        'id': len(consultations) + 1,
        'nama': username,
        'perawatan': perawatan,
        'tanggal': tanggal,
        'jam': jam, 
        'status': 'waiting list'
    }
    consultations.append(consultation)
    print("konsultasi berhasil diajukan.")


# lihat konsultasi
def view_consultation(username):
    user_consultations = [c for c in consultations if c['nama'] == username]
    if user_consultations:
        table = PrettyTable()
        table.field_names = ["ID", "perawatan", "tanggal", "jam", "status"]
        for c in user_consultations:
            table.add_row([c['id'], c['perawatan'], c['tanggal'], c['jam'], c['status']])
        print(table)
            
    else:
        print("tidak ada konsultasi yang diajukan.")


# main program
def main():
    role, username = login()
    
    if role == 'admin':
        while True:
            admin_menu()
            lanjut = input("apakah ingin melanjutkan? (ya/tidak): ")
            if lanjut.lower() != 'ya':
                print("terima kasih sudah berkunjung di tempat kami. be happy :)")
                break

    elif role == 'pengguna':
        while True:
            pengguna_menu(username)
            lanjut = input("apakah ingin melanjutkan? (ya/tidak): ")
            if lanjut.lower() != 'ya':
                print("terima kasih sudah berkunjung di tempat kami. be happy :)")
                break

if __name__ == "__main__":
    main()