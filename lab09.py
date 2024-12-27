import re

def validasi_nama(nama):
    if all(c.isalpha() or c.isspace() for c in nama) and nama.strip():
        return True, ""
    else:
        return False, "Nama lengkap harus hanya berisi huruf."

def validasi_nomor_telepon(nomor):
    if nomor.isdigit():
        return True, ""
    else:
        return False, "Nomor telepon harus hanya berisi angka."

def validasi_email(email):
    # Email harus mengandung karakter @ dan . serta format umum email
    if re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
        return True, ""
    else:
        return False, "Email harus mengandung karakter @ dan . serta sesuai format yang benar."

def validasi_pendaftaran(nama, nomor, email):
    valid = True
    pesan_error = []

    # Validasi nama lengkap
    valid_nama, pesan_nama = validasi_nama(nama)
    if not valid_nama:
        valid = False
        pesan_error.append(pesan_nama)

    # Validasi nomor telepon
    valid_nomor, pesan_nomor = validasi_nomor_telepon(nomor)
    if not valid_nomor:
        valid = False
        pesan_error.append(pesan_nomor)

    # Validasi email
    valid_email, pesan_email = validasi_email(email)
    if not valid_email:
        valid = False
        pesan_error.append(pesan_email)

    if valid:
        return "Data pendaftaran valid."
    else:
        return "\n".join(pesan_error)

# Contoh input dari pengguna
nama = input("Masukkan nama lengkap: ")
nomor = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

# Validasi data
hasil = validasi_pendaftaran(nama, nomor, email)
print(hasil)
