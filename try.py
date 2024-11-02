# Original array
original_array = [1, 1, 2, 5, 4, 6, 3, 2, 5, 1]

# Panjang array
n = len(original_array)
print(n)

# Buat set untuk melacak angka yang sudah ada
existing_numbers = set()
result_array = []

# Tambahkan angka unik ke result_array
for num in original_array:
    if num in existing_numbers:
        result_array.append(None)  # Tempat penampung untuk angka yang kembar
    else:
        result_array.append(num)
        existing_numbers.add(num)

# Temukan angka yang hilang dari 1 hingga n
missing_numbers = set(range(1, n + 1)) - existing_numbers

# Ganti None dengan angka yang hilang
missing_numbers = iter(sorted(missing_numbers))  # Urutkan angka yang hilang
for i in range(len(result_array)):
    if result_array[i] is None:
        result_array[i] = next(missing_numbers)

print(result_array)
