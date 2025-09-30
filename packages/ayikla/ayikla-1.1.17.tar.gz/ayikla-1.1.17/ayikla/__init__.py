from .extractor import TextEntityExtractor

__version__ = "1.1.17"

def bul(text: str):
        """Metin içinden isimler, telefon numaraları, tarih/saat, tarih aralıkları ve lokasyon/adres bloklarını çıkarır.

        Dönen sözlük anahtarları:
            - isimler -> List[str]
            - telefonlar -> List[str] (E.164 format)
            - tarihler -> List[{'tarih': YYYY-MM-DD | None, 'saat': HH:MM | None}]
            - tarih_aralik -> List[{'baslangic': YYYY-MM-DD | None, 'bitis': YYYY-MM-DD | None}]  (1.1.17+ biçimi)
            - lokasyonlar -> List[str]

        Not: 1.1.17 sürümüyle 'tarih_aralik' öğelerindeki eski 'tür' ve 'ifade' alanları kaldırılmıştır.
        """
        return TextEntityExtractor().extract_all(text)
