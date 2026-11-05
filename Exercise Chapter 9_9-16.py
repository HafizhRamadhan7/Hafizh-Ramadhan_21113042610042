from datetime import datetime

waktu_sekarang = datetime.now()

print("--- Eksplorasi Modul Bawaan Python: datetime ---")
print(f"Waktu mentah dari sistem : {waktu_sekarang}")
print(f"Format tanggal dan waktu : {waktu_sekarang.strftime('%d %B %Y, pukul %H:%M:%S')}")