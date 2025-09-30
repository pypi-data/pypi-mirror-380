from .extractor import TextEntityExtractor

__version__ = "1.1.8"

def bul(text: str):
    """Metin içinden isimler, telefon numaraları, tarih/saat, tarih aralıkları ve lokasyon/adres bloklarını çıkarır.

    Dönen sözlük anahtarları: "isimler", "telefonlar", "tarihler", "tarih_aralik", "lokasyonlar".
    """
    return TextEntityExtractor().extract_all(text)
