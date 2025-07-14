import numpy as np

np.random.seed(42)  # untuk hasil acak yang bisa direproduksi

print(np.random.rand(3))       # 3 angka float acak (0 - 1)
print(np.random.randint(1, 10, 5))  # 5 angka int acak antara 1 dan 9
print(np.random.randn(4))      # 4 angka dari distribusi normal
print(np.random.choice([10, 20, 30, 40, 50], 2))  # Pilih 2 angka dari list
