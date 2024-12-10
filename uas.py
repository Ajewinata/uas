while True:
    print("Hai selamat datang di uji coba UAS semester 1, mau uji yang mana😎???")
    print("1. Luas Persegi Panjang")
    print("2. Luas Lingkaran")
    print("3. Fungsi fx")
    pilihanku = int(input("Masukkan pilihan Anda (1/2/3): "))
    if pilihanku == 1:
        def luaspersegipanjang(panjang, lebar):
            return panjang * lebar
        panjang = int(input("Masukan panjang: "))
        lebar = int(input("Masukan lebar: "))
        print(f"Luas persegi panjang adalah: ", luaspersegipanjang(panjang, lebar))
    elif pilihanku == 2:
        import math
        def hitung_lingkaran(jari_jari):
            luas = math.pi * (jari_jari ** 2)
            return luas
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = hitung_lingkaran(jari_jari)
        print(f"Luas lingkaran: {luas:.2f}")
    elif pilihanku == 3:
        def f(x):
            return 2 * x**2 + 3 * x - 10
        x = int(input("Nilai x: "))
        print(f(x))
    else:
        print("maaf belum bisa sampai sana ya😘 ")
    print("\n")
    jawabanku = input("Apakah ingin melanjutkan? (ya/tidak): ")
    if jawabanku!= "ya":
        if jawabanku == "tidak":
            print ("ya udah👌 jangan lupa kasih rating bintang * lima")
            break
