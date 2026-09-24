"""Contoh kode yang sudah diperbaiki untuk melewati Pylint."""


def hitung_nilai(a, b, c, d, e, f):
    """Menghitung hasil dari beberapa nilai."""
    hasil = a + b + c + d + e + f
    return hasil


def main():
    """Fungsi utama program."""
    hasil = hitung_nilai(1, 2, 3, 4, 5, 6)
    print(f"Hasil: {hasil}")


if __name__ == "__main__":
    main()
