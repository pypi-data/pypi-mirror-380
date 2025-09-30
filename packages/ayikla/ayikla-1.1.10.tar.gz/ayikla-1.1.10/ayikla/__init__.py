from .extractor import TextEntityExtractor

__version__ = "1.1.8"

def bul(text: str):
    """Metin içinden isimler, telefon numaraları, tarih/saat ve lokasyon/adres bloklarını çıkarır.

    Dönen sözlük anahtarları: "isimler", "telefonlar", "tarihler", "lokasyonlar".
    """
    return TextEntityExtractor().extract_all(text)
