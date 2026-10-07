import csv
import pandas as pd

data = []
with open("nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(f"Total data: {len(data)} baris")
print("Data pertama:", data[0])
print("-" * 30)

nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])
print("-" * 30)

rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata_kelas = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata_kelas:>8.1f}")
print("-" * 30)


print("--- Hasil Analisis Pandas ---")
df = pd.read_csv("nilai.csv")


print("\nRata-rata per kelas:")
print(df.groupby("kelas")["nilai"].mean())


print("\nDaftar Lulus:")
print(df[df["nilai"] >= 75]["nama"].tolist())


print("\nSiswa Nilai Tertinggi:")
print(df.sort_values("nilai").tail(1))