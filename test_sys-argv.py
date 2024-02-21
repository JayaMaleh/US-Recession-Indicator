import sys

# Memeriksa jumlah argumen yang diberikan
if len(sys.argv) != 2:
    print("Usage: python script.py [string]")
    sys.exit(1)

# Mengakses argumen pertama
input_string = sys.argv[1]

# Memeriksa apakah input_string adalah string
if not isinstance(input_string, str):
    print("Input harus berupa string.")
    sys.exit(1)

# Menampilkan input_string
print("Input yang diterima:", input_string)
