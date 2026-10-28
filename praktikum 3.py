nilai = 82
kehadiran = 90

print("Nilai memenuhi syarat:", nilai >= 75)
print("Kehadiran memenuhi syarat:", kehadiran >= 80)
print("Lulus dengan AND:", nilai >= 75 and kehadiran >= 80)

#Nilai di ubah jdi 70
nilai = 70

print("\nSetelah nilai diubah menjadi 70:")
print("Lulus dengan AND:", nilai >= 75 and kehadiran >= 80)
print("Lulus dengan OR:", nilai >= 75 or kehadiran >= 80)
