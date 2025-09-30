import re
import phonenumbers
from typing import List, Set, Tuple, Dict, Optional
from datetime import datetime, timedelta
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
    """Türkçe metinlerden isim, telefon, tarih/saat ve lokasyon/adres benzeri blokları ayıklayıcı."""

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
                 soyisimler_dosyasi: str = "soyisimler.txt",
                 lokasyon_dosyasi: str = "lokasyon.txt"):
        self.isimler_seti = self.dosyadan_set_olustur(isimler_dosyasi)
        self.soyisimler_seti = self.dosyadan_set_olustur(soyisimler_dosyasi)
        self.lokasyon_seti = self.dosyadan_set_olustur(lokasyon_dosyasi)
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
            "tarihler": self.extract_all_dates(text),
            "tarih_aralik": self.extract_date_ranges(text),
            "lokasyonlar": self.extract_locations(text)
        }

    # ---------------- TARIH ARALIKLARI ----------------
    RELATIVE_RANGE_PATTERNS = [
        r"önümüzdeki\s+hafta", r"önümüzdeki\s+ay", r"önümüzdeki\s+yıl", r"önümüzdeki\s+sene",
        r"geçen\s+hafta", r"geçen\s+ay", r"geçen\s+sene", r"geçen\s+yıl",
        r"bu\s+hafta", r"bu\s+ay", r"bu\s+yıl"
    ]

    GUN_ARALIK_PATTERN = re.compile(
        r"\b(\d{1,2})\s*-\s*(\d{1,2})\s+"  # 3-5  veya 5-10  + ay adı zorunlu
        r"(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)"  # ay
        r"(?:\s+(\d{4}))?\b",
        flags=re.IGNORECASE
    )

    AY_ARALIK_PATTERN = re.compile(
        r"\b(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)\s*-\s*"
        r"(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)"  # ikinci ay
        r"(?:\s+(\d{4}))?\b",
        flags=re.IGNORECASE
    )

    CAPRAZ_GUN_AY_ARALIK_PATTERN = re.compile(
        r"\b(\d{1,2})\s+"  # ilk gün
        r"(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)"  # ilk ay
        r"\s*-\s*"  # tire
        r"(\d{1,2})\s+"  # ikinci gün
        r"(ocak|şubat|mart|nisan|mayıs|haziran|temmuz|ağustos|eylül|ekim|kasım|aralık)"  # ikinci ay
        r"(?:\s+(\d{4}))?\b",
        flags=re.IGNORECASE
    )

    REL_WORD_PATTERN = re.compile("|".join(RELATIVE_RANGE_PATTERNS), flags=re.IGNORECASE)

    AY_ADLARI = {
        'ocak':1,'şubat':2,'mart':3,'nisan':4,'mayıs':5,'haziran':6,
        'temmuz':7,'ağustos':8,'eylül':9,'ekim':10,'kasım':11,'aralık':12
    }

    def extract_date_ranges(self, text: str) -> List[Dict[str, Optional[str]]]:
        """Metinden tarihsel aralık ifadelerini döndürür.

        Yeni format: Her öğe yalnızca "baslangic" ve "bitis" anahtarlarını içerir.
        Önceki sürümlerde 'tür' ve 'ifade' alanları vardı; kaldırıldı.
        """
        if not text or not text.strip():
            return []

        now = datetime.now()
        results: List[Dict[str, Optional[str]]] = []

        # 1) Relative range expressions
        for m in self.REL_WORD_PATTERN.finditer(text):
            expr_low = m.group(0).lower()
            start_date = None
            end_date = None
            try:
                if 'hafta' in expr_low:
                    if 'önümüzdeki' in expr_low:
                        delta = (7 - now.weekday()) % 7
                        next_monday = (now + timedelta(days=delta if delta else 7)).date()
                        start_date = next_monday
                        end_date = start_date + timedelta(days=6)
                    elif 'geçen' in expr_low:
                        monday = (now - timedelta(days=now.weekday()+7)).date()
                        start_date = monday
                        end_date = start_date + timedelta(days=6)
                    elif 'bu' in expr_low:
                        monday = (now - timedelta(days=now.weekday())).date()
                        start_date = monday
                        end_date = start_date + timedelta(days=6)
                elif 'ay' in expr_low:
                    if 'önümüzdeki' in expr_low:
                        year = now.year + (1 if now.month == 12 else 0)
                        month = 1 if now.month == 12 else now.month + 1
                    elif 'geçen' in expr_low:
                        year = now.year - (1 if now.month == 1 else 0)
                        month = 12 if now.month == 1 else now.month - 1
                    else:
                        year = now.year
                        month = now.month
                    start_date = datetime(year, month, 1).date()
                    if month == 12:
                        end_date = datetime(year+1, 1, 1).date() - timedelta(days=1)
                    else:
                        end_date = datetime(year, month+1, 1).date() - timedelta(days=1)
                elif 'yıl' in expr_low or 'sene' in expr_low:
                    if 'önümüzdeki' in expr_low:
                        year = now.year + 1
                    elif 'geçen' in expr_low:
                        year = now.year - 1
                    else:
                        year = now.year
                    start_date = datetime(year,1,1).date()
                    end_date = datetime(year,12,31).date()
            except Exception:
                pass
            results.append({
                'baslangic': start_date.isoformat() if start_date else None,
                'bitis': end_date.isoformat() if end_date else None
            })

        # 2) Gün aralığı (3-5 Ocak [2024])
        for m in self.GUN_ARALIK_PATTERN.finditer(text):
            g1, g2, ayad, yil = m.groups()
            try:
                d1 = int(g1); d2 = int(g2)
                if d1 > d2:
                    d1, d2 = d2, d1
                month = self.AY_ADLARI[ayad.lower()]
                year = int(yil) if yil else now.year
                start_date = datetime(year, month, d1).date()
                end_date = datetime(year, month, d2).date()
                results.append({
                    'baslangic': start_date.isoformat(),
                    'bitis': end_date.isoformat()
                })
            except Exception:
                continue

        # 3) Ay aralığı (Mart - Nisan [2024])
        for m in self.AY_ARALIK_PATTERN.finditer(text):
            a1, a2, yil = m.groups()
            try:
                m1 = self.AY_ADLARI[a1.lower()]; m2 = self.AY_ADLARI[a2.lower()]
                year = int(yil) if yil else now.year
                if m2 < m1 and not yil:  # Aralık - Ocak gibi yıl geçişi
                    start_date = datetime(now.year, m1, 1).date()
                    end_year = now.year + 1
                    end_date = datetime(end_year, m2, 1).date() - timedelta(days=1)
                else:
                    start_date = datetime(year, m1, 1).date()
                    if m2 == 12:
                        end_date = datetime(year+1,1,1).date() - timedelta(days=1)
                    else:
                        end_date = datetime(year, m2+1, 1).date() - timedelta(days=1)
                results.append({
                    'baslangic': start_date.isoformat(),
                    'bitis': end_date.isoformat()
                })
            except Exception:
                pass

        # 4) Çapraz gün-ay aralığı (25 Aralık - 3 Ocak [2025])
        for m in self.CAPRAZ_GUN_AY_ARALIK_PATTERN.finditer(text):
            g1, a1, g2, a2, yil = m.groups()
            try:
                d1 = int(g1); d2 = int(g2)
                m1 = self.AY_ADLARI[a1.lower()]; m2 = self.AY_ADLARI[a2.lower()]
                if yil:
                    year_start = int(yil)
                    year_end = year_start if m2 >= m1 else year_start + 1
                else:
                    year_start = now.year
                    year_end = year_start if m2 >= m1 else year_start + 1
                start_date = datetime(year_start, m1, d1).date()
                end_date = datetime(year_end, m2, d2).date()
                results.append({
                    'baslangic': start_date.isoformat(),
                    'bitis': end_date.isoformat()
                })
            except Exception:
                continue

        # Benzersiz (baslangic, bitis)
        unique: List[Dict[str, Optional[str]]] = []
        seen_keys = set()
        for r in results:
            key = (r.get('baslangic'), r.get('bitis'))
            if key not in seen_keys:
                seen_keys.add(key)
                unique.append(r)
        return unique

    # ---------------- LOKASYON / ADRES ----------------
    ADRES_PATTERN = re.compile(
        r"("  # temel adres tetikleyicileri
        r"(mah(\.|alle(si)?|allesi)?)|"  # mahalle
        r"(cd(\.|add(e(si)?)?)?)|"       # cadde
        r"(sk(\.|ok(ak|ağı)?)?)|"        # sokak
        r"(blv(\.|vd|vard|var(d|ı)?|ulvar)?)|"  # bulvar
        r"(no:?\s*\d{1,3}(?!\d))|"      # 'no' sadece 1-3 rakamla
        r"(num(?:ara|\.)?\s*\d{1,3}(?!\d))|"  # 'numara' varyantı 1-3 rakamla
        r"(kat\s*\d*|floor\s*\d*)|"    # kat
        r"(daire\s*\d*|apt|apartment)"  # daire / apt
        r")",
        flags=re.IGNORECASE
    )

    LOKASYON_EKLER = ("'de", "'da", "'te", "'ta")

    def extract_locations(self, text: str, max_char_gap: int = 8) -> List[str]:
        """Metinden lokasyon/adres tetikleyici segmentleri çıkarır.

        Kurallar:
        - Sadece tetikleyici kelimeler (pattern match) ve lokasyon sözlüğündeki kelimeler alınır.
        - Araya giren iki tetikleyici segment arasındaki ham metin karakter uzunluğu <= max_char_gap ise segmentler birleştirilir.
        - Hiçbir şekilde tetikleyici öncesi veya sonrası ekstra kelime alınmaz.
        - Lokasyon sözlüğü yoksa sadece pattern tetikleyicileri kullanılır.
        """
        raw = text
        if not raw.strip():
            return []

        # Ham metinde token sınırları yerine doğrudan regex ve sözlük eşleşmelerinin span'lerini toplayacağız.
        matches: List[Tuple[int, int]] = []

        # 1) Pattern tetikleyicileri
        for m in self.ADRES_PATTERN.finditer(raw):
            matches.append((m.start(), m.end()))

        # 2) Lokasyon sözlüğü (varsa) - tek birleşik regex ile (daha hızlı)
        if self.lokasyon_seti:
            # Çok kısa kelimeleri (1) atla
            lokasyonlar = [re.escape(l) for l in self.lokasyon_seti if len(l) > 1]
            if lokasyonlar:
                # Kelime sınırı + opsiyonel ek / apostrof ek
                # (?P<base>...) grubuyla baz span'i alıyoruz.
                pattern = r"\b(?P<loc>(" + "|".join(lokasyonlar) + r"))(?:'?(?:de|da|te|ta))?\b"
                for m in re.finditer(pattern, raw, flags=re.IGNORECASE):
                    base_start = m.start('loc')
                    base_end = m.end('loc')
                    matches.append((base_start, base_end))

        if not matches:
            return []

        # 3) Overlap & merge by gap <= max_char_gap
        matches.sort()
        birlesik: List[Tuple[int, int]] = []
        cur_s, cur_e = matches[0]
        for s, e in matches[1:]:
            gap = s - cur_e
            if gap <= max_char_gap and gap >= 0:
                # bitiştir
                if e > cur_e:
                    cur_e = e
            else:
                birlesik.append((cur_s, cur_e))
                cur_s, cur_e = s, e
        birlesik.append((cur_s, cur_e))

        # 4) Segmentleri ham metinden kes
        sonuc: List[str] = []
        for s, e in birlesik:
            frag = raw[s:e].strip()
            if len(frag) == 1:
                continue
            low = frag.lower()
            if low in {"d", "de", "da", "te", "ta"}:
                continue
            if re.fullmatch(r"\d{4,}", frag):
                continue
            if re.fullmatch(r"numara(sı)?", low) or re.fullmatch(r"num(ara|\.)?", low):
                continue
            if low == 'no':
                continue
            # Segment içindeki tokenları kontrol et
            tokens = re.findall(r"[\w']+", low)
            has_loc_word = False
            if self.lokasyon_seti:
                for t in tokens:
                    if t in self.lokasyon_seti:
                        has_loc_word = True
                        break
            # Kısa 'no:?\d{1,3}' segmenti ve lokasyon yoksa at
            if re.fullmatch(r"no:?\s*\d{1,3}", low) and not has_loc_word:
                continue
            if frag not in sonuc:
                sonuc.append(frag)
        return sonuc


if __name__ == "__main__":
    extractor = TextEntityExtractor()
    samples = [
        "Dr. Ahmet Yılmaz beni 0532 123 4567 numarasından yarın saat 19'da ara.",
        "Dr. Ahmet Yılmaz 532 123 4567 – 18 Ocak saat 19'da görüşelim.",
        "Sadece saat 19'da uygun olur.",
    ]
    for s in samples:
        print(s, "->", extractor.extract_all(s))
