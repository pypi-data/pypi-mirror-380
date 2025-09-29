# Ayikla

**Ayikla**, Türkçe metinlerden **isim**, **telefon numarası** ve **tarih/saat bilgisi** ayıklayan bir Python kütüphanesidir.  
Metin içerisindeki karmaşık ifadeleri normalize ederek yapılandırılmış bir çıktı döndürür.

##  Kurulum

```bash
pip install ayikla
```

##  Kullanım

```python
from ayikla import bul

# Örnek 1: İsim + Telefon + Tarih
metin = "Dr. Ahmet Yılmaz beni 0532 123 456x numarasından yarın saat 19'da ara."
print(bul(metin))
```

Çıktı:
```python
{
    "isimler": ["Dr Ahmet Yılmaz"],
    "telefonlar": ["+90532123456x"],
    "tarihler": [{"tarih": None, "saat": "19:00"}]
}
```

---

```python
from ayikla import bul

# Örnek 2: Belirli bir tarih
metin = "Çağrı Güngör 532 123 456x – 18 Ocak saat 19 'da görüşelim."
print(bul(metin))
```

Çıktı:
```python
{
    "isimler": ["Çağrı Güngör"],
    "telefonlar": ["+905321234567"],
    "tarihler": [{"tarih": "2025-01-18", "saat": "19:00"}]
}
```

---

```python
from ayikla import bul

# Örnek 3: Sadece saat
metin = "Sadece saat 19'da uygun olur."
print(bul(metin))
```

Çıktı:
```python
{
    "isimler": [],
    "telefonlar": [],
    "tarihler": [{"tarih": None, "saat": "19:00"}]
}
```

---

##  Proje Yapısı

```
ayikla/
 ├── __init__.py
 ├── extractor.py
 ├── isimler.txt
 ├── soyisimler.txt
pyproject.toml
MANIFEST.in
README.md
```

---

##  Özellikler
- Türkçe özel isim ve soyisim sözlükleri ile daha doğru isim yakalama
- Farklı yazılmış telefon numaralarını normalize etme (`+905xx...`)
- "yarın", "bugün", "dün", "akşam 8'de" gibi doğal dil ifadelerinden tarih/saat ayıklama

---

## Yazar

**Hasan Çağrı Güngör**

İletişim: [iletisim@cagrigungor.com](mailto:iletisim@cagrigungor.com)

---

##  Lisans

MIT License. Özgürce kullanabilir ve geliştirebilirsiniz.
