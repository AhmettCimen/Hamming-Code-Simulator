# 🧠 Hamming SEC-DED Kodlayıcı ve Hata Simülatörü (Tkinter Arayüzü)

Bu proje, **tek-bit hataları düzeltebilen** ve **çift-bit hataları tespit edebilen** Hamming SEC-DED (Single-Error-Correcting Double-Error-Detecting) kodunu görselleştiren ve simüle eden bir Tkinter GUI uygulamasıdır.

## ✨ Özellikler

- Kullanıcıdan 8, 16 veya 32 bitlik ikili veri girişi alma
- Hamming kodu üretme (otomatik olarak parite bitleri yerleştirilir)
- Hamming kodunu ekranda gösterme
- Rastgele:
  - **Tek bit hatası** ekleme
  - **Çift bit hatası** ekleme
- Manuel olarak bir indekste bit hatası oluşturma
- Hamming kodundaki hataları:
  - 🔍 Tespit etme
  - 🛠️ Tek bit hatasını düzeltme (kullanıcı onayıyla)

## 🖼️ Arayüz Ekranı

Uygulama kullanıcı dostu bir arayüz sunar:

- **Veri uzunluğu seçici**: 8 / 16 / 32 bit
- **Veri girişi**: Yalnızca 0 ve 1 kabul edilir
- **Encode butonu**: Verilen veriye Hamming kodu üretir
- **Hamming kodu kutusu**: Üretilen veya hatalı hale getirilmiş kodu gösterir
- **Hata ekleme butonları**:
  - Tek bitlik hata
  - Çift bitlik hata
  - Belirli indekste manuel hata
- **Kontrol butonu**: Kodda hata olup olmadığını kontrol eder
- **Düzelt butonu**: Hata tespit edilirse aktif hale gelir

## 🧪 Kullanım

1. Uygulama açıldığında veri uzunluğunu seçin.
2. Veri kısmına 0 ve 1 içeren ikili veriyi girin (uzunluk sınırı seçilen bit kadar).
3. Encode butonuna basarak Hamming kodunu oluşturun.
4. Hata ekleyerek simülasyonu test edin:
   - 🎯 Rastgele tek/çift hata
   - ✏️ Manuel hata
5. Kontrol butonuyla hatayı test edin.
6. Tek hata varsa **Düzelt** butonuyla otomatik düzeltin.

## 🧬 Teknik Bilgi

### 🧾 Hamming Kodlama

- Kod uzunluğu: `m` veri biti + `p` parite biti + 1 global parity biti
- Parite bitleri pozisyonları: `2^i` (örn. 1, 2, 4, 8, ...)
- Global parity: mod 2 toplam kontrolü ile çift sayıda hata algılanmasını sağlar ✅

### 🛠️ Hata Tespiti ve Düzeltme

- Syndrome hesaplama ile hata pozisyonu tespiti
- Tek hata bulunursa **Düzelt** butonu aktif hale gelir
- Çift hata varsa tespit edilir ama düzeltilemez 🚫

# 🚀 Kullanım

Projeyi bilgisayarınıza klonlamak için:

```bash
git clone https://github.com/kullaniciadi/hamming-sec-ded-simulator.git
cd hamming-sec-ded-simulator


```
Uygulamayı çalıştırmak için:
```bash
python gui.py
```







