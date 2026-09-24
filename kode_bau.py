"""Contoh kode yang sudah diperbaiki untuk melewati Pylint."""


def hitung_nilai(a, b, c):
    """Menghitung jumlah tiga nilai."""
    return a + b + c


def main():
    """Fungsi utama program."""
    hasil = hitung_nilai(1, 2, 3)
    print(f"Hasil: {hasil}")


if __name__ == "__main__":
    main()