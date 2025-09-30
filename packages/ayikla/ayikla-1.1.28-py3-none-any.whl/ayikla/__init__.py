from .extractor import TextEntityExtractor

__version__ = "1.1.28"

def bul(
    text: str,
    *,
    sadece: list | None = None,
    aktif: list | None = None,
    pasif: list | None = None,
    include_meta: bool = False,
):
    """Metinden desteklenen varlıkları (isimler, telefonlar, tarihler vb.) çıkarır.

    Seçmeli Çalıştırma:
        Öncelik sırası: sadece > aktif/pasif > (hepsi aktif varsayılan)
        - sadece=["iban","tckn"]        -> Yalnızca bu anahtarlar çalıştırılır.
        - aktif=["isimler","telefonlar"] -> Sadece bu listede olanlar çalışır.
        - pasif=["iban","uuid4"]       -> Belirtilenler hariç (diğer hepsi) çalışır.
        - include_meta=True                -> Sonuca '_pasif' anahtarı eklenir (devreye alınmayanlar listesi).

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
        - (ops.) _pasif -> List[str] (include_meta=True ise)

    Notlar (sürüm kilometre taşları):
        * 1.1.17: 'tarih_aralik' alanı sadeleşti.
        * 1.1.18: 'firmalar' eklendi.
        * 1.1.19: 'tckn' eklendi.
        * 1.1.20: 'iban' eklendi.
        * 1.1.21: 'emailler' ve 'websiteler' eklendi.
        * 1.1.22: 'ip_adresleri' ve 'uuid4' eklendi.
        * 1.1.23: 'olculer' (miktar + ölçü birimleri) eklendi.
        * 1.1.24: 'kurlar' (para birimi miktarları) eklendi.
        * 1.1.26: ölçü (olculer) çıkarımı regexleri önceden derlenerek performans iyileştirildi.
    * 1.1.27: seçmeli çalıştırma wrapper parametreleri (sadece/aktif/pasif/include_meta) eklendi.
    * 1.1.28: firma çıkarımı performansı (sözlük pattern chunk + bisect) iyileştirildi.
    """
    return TextEntityExtractor().extract_all(
        text,
        sadece=sadece,
        aktif=aktif,
        pasif=pasif,
        include_meta=include_meta,
    )
