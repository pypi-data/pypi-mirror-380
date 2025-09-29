import re
import phonenumbers
from typing import List, Set, Tuple, Dict, Optional
from datetime import datetime
from dateutil.parser import parse, parserinfo
from dateparser.search import search_dates
import os
import pkg_resources


class TurkishParserInfo(parserinfo):
    """Türkçe ay adlarını dateutil parse için tanımlar."""
    MONTHS = [
        ("Ocak", "Oca"), ("Şubat", "Şub"), ("Mart", "Mar"),
        ("Nisan", "Nis"), ("Mayıs", "May"), ("Haziran", "Haz"),
        ("Temmuz", "Tem"), ("Ağustos", "Ağu"), ("Eylül", "Eyl"),
        ("Ekim", "Eki"), ("Kasım", "Kas"), ("Aralık", "Ara"),
    ]


class TextEntityExtractor:
    """Türkçe metinlerden isim, telefon ve tarih/saat ayıklayıcı."""

    SOYISIM_EKLERI = [
        'Ak-', 'Ay-', 'Kara-', 'Öz-', 'Özt-', 'Ulu-', 'Büyük-',
        '-alp', '-ar', '-baş', '-can', '-cı', '-ci', '-cu', '-cü',
        '-çı', '-çi', '-çu', '-çü', '-demir', '-er', '-gül', '-han',
        '-kan', '-kaya', '-lı', '-li', '-lu', '-lü', '-man', '-men',
        '-oğlu', '-oğulları', '-pınar', '-soy', '-su', '-taş', '-tekin', '-türk', '-zade'
    ]

    UNVANLAR = {'dr', 'dr.', 'doktor', 'av', 'av.', 'avukat',
                'prof', 'prof.', 'profesör', 'öğretmen', 'öğr'}

    def __init__(self, isimler_dosyasi: str = "isimler.txt",
                 soyisimler_dosyasi: str = "soyisimler.txt"):
        self.isimler_seti = self.dosyadan_set_olustur(isimler_dosyasi)
        self.soyisimler_seti = self.dosyadan_set_olustur(soyisimler_dosyasi)
        self.onekler, self.sonekler = self.soyadi_eklerini_hazirla(self.SOYISIM_EKLERI)
        self.TURKISH_PARSER = TurkishParserInfo()

    # ---------------- ISIM ----------------
    def kelimeyi_temizle(self, kelime: str) -> str:
        kelime = re.split(r"[’']", kelime, maxsplit=1)[0]
        return kelime.strip(".,;:!?()[]{}\"“”„’`…—-")

    def soyadi_eklerini_hazirla(self, ekler_listesi: List[str]) -> Tuple[Set[str], Set[str]]:
        onekler = {ek.lower().replace('-', '') for ek in ekler_listesi if ek.endswith('-')}
        sonekler = {ek.lower().replace('-', '') for ek in ekler_listesi if ek.startswith('-')}
        return onekler, sonekler

    def dosyadan_set_olustur(self, dosya_yolu: str) -> Set[str]:
        try:
            # Önce paket içi kaynak olarak dene
            try:
                dosya_icerigi = pkg_resources.resource_string('ayikla', dosya_yolu).decode('utf-8')
                return {satir.strip().lower() for satir in dosya_icerigi.splitlines() if satir.strip()}
            except:
                # Eğer paket kaynak olarak bulunamazsa, yerel dosya olarak dene
                # Mevcut dosyanın dizinindeki dosyayı ara
                script_dir = os.path.dirname(os.path.abspath(__file__))
                tam_yol = os.path.join(script_dir, dosya_yolu)
                with open(tam_yol, 'r', encoding='utf-8') as f:
                    return {satir.strip().lower() for satir in f if satir.strip()}
        except FileNotFoundError:
            return set()

    def isimbul(self, metin: str) -> List[str]:
        """Metinden kişi isimlerini ve unvanlarını ayıkla."""
        if not metin:
            return []

        tokens = [t for t in re.split(r'\s+', metin) if t]

        def soyadi_mi(orijinal: str, temiz: str) -> bool:
            base = temiz.replace('-', '')
            if temiz in self.soyisimler_seti:
                return True
            if any(base.startswith(p) for p in self.onekler):
                return True
            if any(base.endswith(s) for s in self.sonekler):
                return True
            if orijinal and orijinal[0].isupper() and (temiz not in self.isimler_seti):
                return True
            return False

        bulunan_isimler = []
        i = 0
        while i < len(tokens):
            tok = self.kelimeyi_temizle(tokens[i])
            low = tok.lower()

            # Ünvan kontrolü
            tespit_edilen_unvan = ""
            if low in self.UNVANLAR:
                tespit_edilen_unvan = tok
                i += 1
                if i >= len(tokens):
                    break
                tok = self.kelimeyi_temizle(tokens[i])
                low = tok.lower()

            if low in self.isimler_seti:
                parcalar = [tok]
                j = i + 1
                # ikinci isimler
                while j < len(tokens):
                    nxt = self.kelimeyi_temizle(tokens[j])
                    if nxt.lower() in self.isimler_seti:
                        parcalar.append(nxt)
                        j += 1
                    else:
                        break
                # soyisimler
                soyadlar = []
                while j < len(tokens):
                    cand = self.kelimeyi_temizle(tokens[j])
                    if soyadi_mi(cand, cand.lower()):
                        soyadlar.append(cand)
                        j += 1
                    else:
                        break
                tam_isim = " ".join(([tespit_edilen_unvan] if tespit_edilen_unvan else [])
                                     + parcalar + soyadlar).strip().title()
                bulunan_isimler.append(tam_isim)
                i = j
            else:
                i += 1

        return bulunan_isimler

    # ---------------- TELEFON ----------------
    def extract_all_phones(self, text: str, default_region: str = "TR") -> List[str]:
        """Metinden telefon numaralarını çıkarır (E.164 formatında)."""
        if not text.strip():
            return []
        return [phonenumbers.format_number(m.number, phonenumbers.PhoneNumberFormat.E164)
                for m in phonenumbers.PhoneNumberMatcher(text, default_region)]

    def temizle_telefonlari(self, text: str) -> str:
        """Telefon numaralarını metinden çıkarır (yerine __TEL__ koyar)."""
        for m in phonenumbers.PhoneNumberMatcher(text, "TR"):
            if m.raw_string:
                text = text.replace(m.raw_string, "__TEL__")
        return re.sub(r"\b(?:\+?90)?\s*0?\s*\d{3}[\s-]?\d{3}[\s-]?\d{4}\b", "__TEL__", text)

    # ---------------- TARIH ----------------
    def normalize_turkish_time_phrases(self, text: str) -> str:
        """Türkçe doğal saat ifadelerini HH:MM'e normalize eder."""
        replacements = []
        # sabah X -> 0X:00
        for m in re.findall(r"sabah\s+(\d{1,2})", text, re.IGNORECASE):
            h = int(m)
            if 1 <= h <= 11:
                replacements.append((f"sabah {m}", f"{h:02d}:00"))
        # öğlen 12
        text = re.sub(r"öğlen\s+12", "12:00", text, flags=re.IGNORECASE)
        # öğleden sonra X -> 12+X
        for m in re.findall(r"öğleden\s+sonra\s+(\d{1,2})", text, re.IGNORECASE):
            h = int(m)
            if 1 <= h <= 11:
                replacements.append((f"öğleden sonra {m}", f"{h+12:02d}:00"))
        # akşam X -> 12+X
        for m in re.findall(r"akşam\s+(\d{1,2})", text, re.IGNORECASE):
            h = int(m)
            if 1 <= h <= 11:
                replacements.append((f"akşam {m}", f"{h+12:02d}:00"))
        # gece X
        for m in re.findall(r"gece\s+(\d{1,2})", text, re.IGNORECASE):
            h = int(m)
            if 1 <= h <= 5:
                replacements.append((f"gece {m}", f"{h:02d}:00"))
            elif 9 <= h <= 11:
                replacements.append((f"gece {m}", f"{h+12:02d}:00"))
        # saat 19'da
        for m in re.findall(r"saat\s+(\d{1,2})\s*[’']?(?:d[ae]|t[ae])?", text, re.IGNORECASE):
            h = int(m)
            replacements.append((f"saat {m}", f"{h:02d}:00"))
        # 19'da
        text = re.sub(r"\b(\d{1,2})\s*[’']?(?:d[ae]|t[ae])\b",
                      lambda m: f"{int(m.group(1)):02d}:00", text, flags=re.IGNORECASE)
        # uygula replacements
        for old, new in replacements:
            text = re.sub(re.escape(old), new, text, flags=re.IGNORECASE)
        return text

    def normalize_relative_tr_phrases(self, text: str) -> str:
        t = re.sub(r"(\d+)\s*(dk|dka|dak)\b", r"\1 dakika", text, flags=re.IGNORECASE)
        t = re.sub(r"(\d+)\s*(sn|san|saniye)\b", r"\1 saniye", t, flags=re.IGNORECASE)
        t = re.sub(r"(\d+)\s*(sa)\b", r"\1 saat", t, flags=re.IGNORECASE)
        t = re.sub(r"\bha(ftaya)?\s+(pazartesi|salı|çarşamba|perşembe|cuma|cumartesi|pazar)\b",
                   r"gelecek \2", t, flags=re.IGNORECASE)
        return t

    def _has_explicit_date_terms(self, s: str) -> bool:
        return bool(re.search(
            r"(bugün|yarın|dün|sonra|önce|gelecek|önümüzdeki|haftaya|"
            r"ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık|"
            r"pazartesi|salı|çarşamba|perşembe|cuma|cumartesi|pazar|"
            r"\d{1,2}[-/.\s]\d{1,2}([-/.\s]\d{2,4})?|\d{4}[-/.\s]\d{1,2}[-/.\s]\d{1,2}|"
            r"\d+\s+(gün|hafta|ay|yıl)\s+(sonra|önce))",
            s, re.IGNORECASE))

    def extract_all_dates(self, text: str) -> List[Dict[str, Optional[str]]]:
        """Metinden tarih ve saatleri ayıklar."""
        if not text.strip():
            return []
        text_no_tel = self.temizle_telefonlari(text)
        norm_text = self.normalize_turkish_time_phrases(text_no_tel)
        norm_text = self.normalize_relative_tr_phrases(norm_text)

        now = datetime.now()
        raw_matches = search_dates(norm_text, languages=["tr"], settings={"RELATIVE_BASE": now}) or []

        date_items: Dict[str, Dict[str, Optional[str]]] = {}
        time_only_set: Set[str] = set()

        for matched_text, dt in raw_matches:
            mt = matched_text.strip()
            if re.fullmatch(r"\d{1,2}", mt):
                continue
            if not (1000 <= dt.year <= 2100):
                continue
            explicit_time = None
            if re.search(r"\b([01]?\d|2[0-3]):[0-5]\d\b", mt) or "saat" in mt.lower():
                explicit_time = dt.strftime("%H:%M")
            if self._has_explicit_date_terms(mt):
                tarih = dt.strftime("%Y-%m-%d")
                if tarih not in date_items:
                    date_items[tarih] = {"tarih": tarih, "saat": explicit_time}
                elif explicit_time:
                    date_items[tarih]["saat"] = explicit_time
            elif explicit_time:
                time_only_set.add(explicit_time)

        for hhmm in re.findall(r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b", norm_text):
            time_only_set.add(hhmm)

        if len(date_items) == 1 and len(time_only_set) == 1:
            only_tarih = next(iter(date_items))
            if not date_items[only_tarih]["saat"]:
                date_items[only_tarih]["saat"] = next(iter(time_only_set))
                time_only_set.clear()

        results = list(date_items.values())
        if not results and time_only_set:
            results = [{"tarih": None, "saat": t} for t in sorted(time_only_set)]

        unique, seen = [], set()
        for item in results:
            key = (item.get("tarih"), item.get("saat"))
            if key not in seen:
                seen.add(key)
                unique.append(item)
        return unique

    # ---------------- HEPSINI BIRDEN ----------------
    def extract_all(self, text: str) -> Dict[str, list]:
        return {
            "isimler": self.isimbul(text),
            "telefonlar": self.extract_all_phones(text),
            "tarihler": self.extract_all_dates(text)
        }


if __name__ == "__main__":
    extractor = TextEntityExtractor()
    samples = [
        "Dr. Ahmet Yılmaz beni 0532 123 4567 numarasından yarın saat 19'da ara.",
        "Dr. Ahmet Yılmaz 532 123 4567 – 18 Ocak saat 19'da görüşelim.",
        "Sadece saat 19'da uygun olur.",
    ]
    for s in samples:
        print(s, "->", extractor.extract_all(s))
