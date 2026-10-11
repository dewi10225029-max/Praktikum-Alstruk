nama = input("Masukkan nama mahasiswa: ")

tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))


nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

if nilai_akhir >= 60:
    status = "Lulus"
else:
    status = "Belum Lulus"


print("\n===== HASIL PERHITUNGAN NILAI =====")
print("Nama Mahasiswa :", nama)
print("Nilai Tugas    :", tugas)
print("Nilai UTS      :", uts)
print("Nilai UAS      :", uas)
print("Nilai Akhir    :", round(nilai_akhir, 2))
print("Status         :", status)