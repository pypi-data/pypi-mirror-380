from .extractor import TextEntityExtractor

def bul(text: str):
    """Metin içinden isim, telefon, tarih bilgilerini çıkarır."""
    return TextEntityExtractor().extract_all(text)
