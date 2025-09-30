from .extractor import TextEntityExtractor

__version__ = "1.1.24"

def bul(text: str):
        """Metin içinden isimler, telefon numaraları, tarih/saat, tarih aralıkları, lokasyon/adres,
        firma adları, T.C. Kimlik numaraları, IBAN, e‑posta adresleri, web siteleri, IP adresleri (IPv4/IPv6),
        UUID4 değerleri, miktar + ölçü birimleri (olculer) ve para birimi miktarlarını (kurlar) çıkarır.

        Dönen sözlük anahtarları:
            - isimler -> List[str]
            - telefonlar -> List[str] (E.164 format)
            - tarihler -> List[{ 'tarih': YYYY-MM-DD | None, 'saat': HH:MM | None }]
            - tarih_aralik -> List[{ 'baslangic': YYYY-MM-DD | None, 'bitis': YYYY-MM-DD | None }]
            - lokasyonlar -> List[str]
            - firmalar -> List[str]
            - tckn -> List[str]
            - iban -> List[str]
            - emailler -> List[str]
            - websiteler -> List[str]
            - ip_adresleri -> List[str]
            - uuid4 -> List[str]
            - olculer -> List[{ 'miktar': int|float, 'birim': str, 'ham': str }]
            - kurlar -> List[{ 'miktar': int|float, 'kur': str, 'ham': str }]

        Notlar:
            * 1.1.17: 'tarih_aralik' alanı sadeleşti.
            * 1.1.18: 'firmalar' eklendi.
            * 1.1.19: 'tckn' eklendi.
            * 1.1.20: 'iban' eklendi.
            * 1.1.21: 'emailler' ve 'websiteler' eklendi.
            * 1.1.22: 'ip_adresleri' ve 'uuid4' eklendi.
            * 1.1.23: 'olculer' (miktar + ölçü birimleri) eklendi.
            * 1.1.24: 'kurlar' (para birimi miktarları) eklendi.
        """
        return TextEntityExtractor().extract_all(text)
