import re
import bisect
import phonenumbers
from typing import List, Set, Tuple, Dict, Optional
from datetime import datetime, timedelta
from dateutil.parser import parse, parserinfo
from dateparser.search import search_dates
import os
import pkg_resources
import ipaddress


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

    TURKISH_NUMBER_WORDS = {
        'sıfır': 0, 'bir': 1, 'iki': 2, 'üç': 3, 'dört': 4, 'beş': 5, 'altı': 6, 'yedi': 7, 'sekiz': 8, 'dokuz': 9,
        'on': 10, 'yirmi': 20, 'otuz': 30, 'kırk': 40, 'elli': 50, 'altmış': 60, 'yetmiş': 70, 'seksen': 80, 'doksan': 90,
        'yüz': 100, 'bin': 1000, 'milyon': 1_000_000, 'milyar': 1_000_000_000
    }

    def __init__(self, isimler_dosyasi: str = "isimler.txt",
                 soyisimler_dosyasi: str = "soyisimler.txt",
                 lokasyon_dosyasi: str = "lokasyon.txt",
                 firmalar_dosyasi: str = "firmalar.txt",
                 olculer_dosyasi: str = "olculer.txt",
                 kurlar_dosyasi: str = "kurlar.txt"):
        self.isimler_seti = self.dosyadan_set_olustur(isimler_dosyasi)
        self.soyisimler_seti = self.dosyadan_set_olustur(soyisimler_dosyasi)
        self.lokasyon_seti = self.dosyadan_set_olustur(lokasyon_dosyasi)
        self.firmalar_seti = self.dosyadan_set_olustur(firmalar_dosyasi)
        self._company_patterns = []  # precompiled regex chunks for firmalar
        # Ölçüler
        self.olcu_alias2base: Dict[str, str] = {}
        self.olcu_base_units: Set[str] = set()
        self._olculeri_yukle(olculer_dosyasi)
        # Kurlar
        self.kur_alias2code: Dict[str, str] = {}
        self.kur_codes: Set[str] = set()
        self._kurlari_yukle(kurlar_dosyasi)
        self.onekler, self.sonekler = self.soyadi_eklerini_hazirla(self.SOYISIM_EKLERI)
        self.TURKISH_PARSER = TurkishParserInfo()
        self._prepare_measurement_patterns()
        self._prepare_company_patterns()

    def _olculeri_yukle(self, dosya: str) -> None:
        try:
            try:
                content = pkg_resources.resource_string('ayikla', dosya).decode('utf-8')
            except Exception:
                script_dir = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(script_dir, dosya), 'r', encoding='utf-8') as f:
                    content = f.read()
        except FileNotFoundError:
            return
        for line in content.splitlines():
            raw = line.strip()
            if not raw or raw.startswith('#'):
                continue
            parts = [p.strip().lower() for p in raw.split(',') if p.strip()]
            if not parts:
                continue
            base = parts[0]
            self.olcu_base_units.add(base)
            for alias in parts:
                if alias not in self.olcu_alias2base:
                    self.olcu_alias2base[alias] = base

    def _kurlari_yukle(self, dosya: str) -> None:
        try:
            try:
                content = pkg_resources.resource_string('ayikla', dosya).decode('utf-8')
            except Exception:
                script_dir = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(script_dir, dosya), 'r', encoding='utf-8') as f:
                    content = f.read()
        except FileNotFoundError:
            return
        for line in content.splitlines():
            raw = line.strip().strip('\u200b')  # olası zero-width
            if not raw or raw.startswith('#'):
                continue
            # Satır sonundaki çift boşluklar kaldır
            raw = re.sub(r"\s+", " ", raw)
            parts = [p.strip().strip().lower() for p in raw.split(',') if p.strip()]
            if not parts:
                continue
            base_code = parts[0].upper()  # ISO kod
            self.kur_codes.add(base_code)
            for alias in parts:
                # Para sembolleri ve aliaslar
                if not alias:
                    continue
                self.kur_alias2code[alias.lower()] = base_code
        # Özel sembol varyasyonlarını normalize
        # Örn: TL tekrarları vs. zaten dosyada var.

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
    ALL_KEYS = [
        "isimler","telefonlar","tarihler","tarih_aralik","lokasyonlar","firmalar",
        "tckn","iban","emailler","websiteler","ip_adresleri","uuid4","olculer","kurlar"
    ]

    def extract_all(self, text: str, aktif: Optional[List[str]] = None, pasif: Optional[List[str]] = None,
                    sadece: Optional[List[str]] = None, include_meta: bool = False) -> Dict[str, list]:
        """Tüm varlıkları (veya seçilenleri) döndürür.

        Parametre öncelik sırası:
        1) sadece: Belirtilirse sadece bu anahtarlar çalıştırılır.
        2) aktif + pasif: aktif listesi verilirse o çalışır; pasif listesi belirtilirse o anahtarlar çıkarılır.
           Hiçbiri verilmezse varsayılan: tüm anahtarlar aktif.
        - Bilinmeyen anahtarlar sessizce yok sayılır.
        - Dönen sözlükte her zaman tüm anahtarlar yer alır (çalışmayanlar []). Şema stabil kalır.
        - include_meta=True ise '_pasif' eklenir.
        """
        text = text or ""
        all_keys = self.ALL_KEYS

        if sadece:
            hedef = [k for k in sadece if k in all_keys]
        else:
            if aktif:
                hedef = [k for k in aktif if k in all_keys]
            else:
                hedef = list(all_keys)
            if pasif:
                pset = set(k for k in pasif if k in all_keys)
                hedef = [k for k in hedef if k not in pset]

        hedef_set = set(hedef)
        sonuc: Dict[str, list] = {}

        # Her anahtar için koşullu çağrı; yoksa boş liste.
        sonuc["isimler"] = self.isimbul(text) if "isimler" in hedef_set else []
        sonuc["telefonlar"] = self.extract_all_phones(text) if "telefonlar" in hedef_set else []
        sonuc["tarihler"] = self.extract_all_dates(text) if "tarihler" in hedef_set else []
        sonuc["tarih_aralik"] = self.extract_date_ranges(text) if "tarih_aralik" in hedef_set else []
        sonuc["lokasyonlar"] = self.extract_locations(text) if "lokasyonlar" in hedef_set else []
        sonuc["firmalar"] = self.extract_companies(text) if "firmalar" in hedef_set else []
        sonuc["tckn"] = self.extract_tckn(text) if "tckn" in hedef_set else []
        sonuc["iban"] = self.extract_ibans(text) if "iban" in hedef_set else []
        sonuc["emailler"] = self.extract_emails(text) if "emailler" in hedef_set else []
        sonuc["websiteler"] = self.extract_urls(text) if "websiteler" in hedef_set else []
        sonuc["ip_adresleri"] = self.extract_ip_addresses(text) if "ip_adresleri" in hedef_set else []
        sonuc["uuid4"] = self.extract_uuid4(text) if "uuid4" in hedef_set else []
        sonuc["olculer"] = self.extract_measurements(text) if "olculer" in hedef_set else []
        sonuc["kurlar"] = self.extract_currencies(text) if "kurlar" in hedef_set else []

        if include_meta:
            pasif_list = [k for k in all_keys if k not in hedef_set]
            sonuc["_pasif"] = pasif_list
        return sonuc

    # ---------------- TCKN ----------------
    @staticmethod
    def tc_kimlik_dogrula(tc_no: str) -> bool:
        """Verilen T.C. Kimlik No algoritmasını doğrular."""
        if not isinstance(tc_no, str) or not tc_no.isdigit() or len(tc_no) != 11:
            return False
        if tc_no.startswith('0'):
            return False
        rakamlar = [int(d) for d in tc_no]
        tekler_top = sum(rakamlar[0:9:2])
        ciftler_top = sum(rakamlar[1:8:2])
        hesap10 = ((tekler_top * 7) - ciftler_top) % 10
        if hesap10 != rakamlar[9]:
            return False
        hesap11 = sum(rakamlar[0:10]) % 10
        if hesap11 != rakamlar[10]:
            return False
        return True

    def extract_tckn(self, text: str) -> List[str]:
        """Metindeki geçerli T.C. Kimlik numaralarını (benzersiz) döndürür.

        Kurallar:
        - 11 haneli tamamen rakam.
        - İlk hanesi 0 olamaz.
        - Algoritma kontrollerini geçmeli.
        - Telefon numaralarıyla karışmaması için öncesinde +, -, ( gibi semboller varsa atlanır.
        - Aynı numara tekrar ederse tek kez döner.
        """
        if not text or not text.strip():
            return []
        adaylar = re.finditer(r"(?<![+\d])\b\d{11}\b", text)  # önünde + veya rakam yoksa
        sonuc = []
        seen = set()
        for m in adaylar:
            num = m.group(0)
            if num in seen:
                continue
            if self.tc_kimlik_dogrula(num):
                seen.add(num)
                sonuc.append(num)
        return sonuc

    # ---------------- IBAN ----------------
    @staticmethod
    def iban_dogrula(iban: str) -> bool:
        """TR IBAN geçerlilik (MOD 97) kontrolü yapar."""
        if not iban:
            return False
        iban = iban.replace(" ", "").upper()
        if len(iban) != 26 or not iban.startswith("TR"):
            return False
        rearranged = iban[4:] + iban[:4]
        numeric = []
        for ch in rearranged:
            if ch.isdigit():
                numeric.append(ch)
            elif 'A' <= ch <= 'Z':
                numeric.append(str(ord(ch) - ord('A') + 10))
            else:
                return False
        try:
            num_str = "".join(numeric)
            # Büyük sayıyı mod 97 almak için parça parça ilerle
            remainder = 0
            for i in range(0, len(num_str), 9):
                remainder = int(str(remainder) + num_str[i:i+9]) % 97
            return remainder == 1
        except Exception:
            return False

    def extract_ibans(self, text: str) -> List[str]:
        """Metindeki TR IBAN'ları normalize (boşluksuz büyük harf) ve benzersiz döndürür.

        Kurallar:
        - TR + 24 alfanumerik karakter; aralara tek boşluk girebilir (grup bazlı).
        - Boşluklar kaldırılıp MOD97 doğrulaması yapılır.
        - Aynı IBAN tekrar etmez.
        Performans:
        - Geniş "TR[0-9A-Za-z ]{10,60}" taraması yerine sabit uzunlukta tekrarlı desen kullanılır:
          TR(?: ?[0-9A-Za-z]){24}
        """
        if not text or not text.strip():
            return []
        pattern = re.compile(r"TR(?: ?[0-9A-Za-z]){24}", flags=re.IGNORECASE)
        sonuc: List[str] = []
        seen: Set[str] = set()
        for m in pattern.finditer(text):
            raw = m.group(0)
            compact = raw.replace(" ", "").upper()
            if len(compact) != 26:
                continue
            if not re.fullmatch(r"TR[0-9A-Z]{24}", compact):
                continue
            if compact in seen:
                continue
            if self.iban_dogrula(compact):
                seen.add(compact)
                sonuc.append(compact)
        return sonuc

    # ---------------- EMAIL ----------------
    EMAIL_REGEX = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}\b")

    def extract_emails(self, text: str) -> List[str]:
        if not text:
            return []
        found = self.EMAIL_REGEX.findall(text)
        unique = []
        seen = set()
        for e in found:
            low = e.lower()
            if low not in seen:
                seen.add(low)
                unique.append(e)
        return unique

    # ---------------- URL / WEBSITE ----------------
    URL_REGEX = re.compile(
        r"\b((?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+\.(?:[a-zA-Z]{2,})(?:/[\w\-./?%&=+#]*)?)",
        flags=re.IGNORECASE
    )

    def extract_urls(self, text: str) -> List[str]:
        if not text:
            return []
        raw = self.URL_REGEX.findall(text)
        cleaned = []
        seen = set()
        for u in raw:
            # Noktalama son eki temizle
            cleaned_u = u.rstrip(').,;!?:"\'')
            # Protokol yoksa http varsayımı? Şimdilik orijinali koru.
            low = cleaned_u.lower()
            if low not in seen:
                seen.add(low)
                cleaned.append(cleaned_u)
        return cleaned

    # ---------------- IP ADDRESS (IPv4 & IPv6) ----------------
    # Basit aday regex'leri; doğrulamayı ipaddress modülüyle yapacağız.
    IPV4_CANDIDATE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    # IPv6 aday (basit): hex bloklar ve :: kısaltımı; daha sonra doğrulanacak
    IPV6_CANDIDATE = re.compile(r"\b(?:[A-Fa-f0-9]{1,4}:){1,7}[A-Fa-f0-9]{1,4}\b|\b(?:[A-Fa-f0-9]{1,4}:){1,7}:|\b::(?:[A-Fa-f0-9]{1,4}:){0,6}[A-Fa-f0-9]{1,4}\b")

    def extract_ip_addresses(self, text: str) -> List[str]:
        if not text:
            return []
        candidates = set()
        for m in self.IPV4_CANDIDATE.finditer(text):
            candidates.add(m.group(0))
        for m in self.IPV6_CANDIDATE.finditer(text):
            candidates.add(m.group(0))
        valid = []
        seen = set()
        for c in candidates:
            try:
                ipaddress.ip_address(c)
                lc = c.lower()
                if lc not in seen:
                    seen.add(lc)
                    valid.append(c)
            except ValueError:
                continue
        return sorted(valid, key=lambda x: (":" in x, x))  # IPv4'ler önce

    # ---------------- UUID4 ----------------
    UUID4_REGEX = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b")

    def extract_uuid4(self, text: str) -> List[str]:
        if not text:
            return []
        found = self.UUID4_REGEX.findall(text)
        unique = []
        seen = set()
        for u in found:
            low = u.lower()
            if low not in seen:
                seen.add(low)
                unique.append(u)
        return unique

    # ---------------- FIRMA / ŞİRKET ----------------
    FIRMA_SON_EKLER = [
        r"holding",
        r"a\.ş\.?|aş",  # a.ş., a.ş, aş
        r"anonim\s+şirketi",
        r"ltd\.\s*şti\.?",  # ltd. şti.
        r"ltd\s*şti",        # ltd şti
        r"ltd\.?",           # ltd, ltd.
        r"şti\.?,?",         # şti, şti.
        r"şirketi",
        r"firması"
    ]

    FIRMA_SON_EK_REGEX = re.compile(r"\b(" + "|".join(FIRMA_SON_EKLER) + r")\b", flags=re.IGNORECASE)

    def _prepare_company_patterns(self, chunk_size: int = 60):
        """Firma sözlüğü için uzun tek tek aramalar yerine parça parça ön-derlenmiş regex listesi oluşturur.

        Neden:
        - Önceki sürüm her firma için ayrı re.finditer çağırıyordu (O(N_firma * |metin|)).
        - Şimdi uzunluktan kısaya sıralı gruplar halinde alternation ile tarama yapıyoruz.
        - Çok büyük setlerde tek dev regex yavaş ve derlemesi maliyetli olabileceğinden chunk'lıyoruz.
        """
        if not self.firmalar_seti:
            self._company_patterns = []
            return
        entries = sorted(self.firmalar_seti, key=len, reverse=True)
        patterns = []
        for i in range(0, len(entries), chunk_size):
            chunk = entries[i:i+chunk_size]
            # re.escape ile güvenli kıl, uzun ifadeler önce (zaten sıralı)
            alt = "|".join(re.escape(e) for e in chunk if e)
            if not alt:
                continue
            # \b sınırları dış kısımda; IGNORECASE ile derlenir
            pat = re.compile(rf"\b(?:{alt})\b", flags=re.IGNORECASE)
            patterns.append(pat)
        self._company_patterns = patterns

    def extract_companies(self, text: str) -> List[str]:
        """Metinden firma adlarını döndürür.

        Kurallar:
        1) `firmalar.txt` sözlüğündeki tam girişler (çok kelimeli olabilir) eşleşirse eklenir.
        2) Sonek heuristiği: Sonunda 'holding', 'aş', 'a.ş.', 'anonim şirketi', 'ltd', 'ltd şti', 'şti', 'şirketi', 'firması'
           bulunan yapılarda önceki 1-3 ardışık kelime büyük harf ile başlıyorsa (Türkçe harf dahil) o blok + sonek firma kabul edilir.
           Tek kelimelik blok sadece o kelime bir kişi adı sözlüğünde değilse kabul edilir.
        3) "Ahmet ülker ltd" örneğinde ikinci kelime küçük harfle başladığından blok parçalanır ve tek kelime (Ahmet) kişi adı olduğu için atılır.
        """
        if not text or not text.strip():
            return []

        bulunmus: List[Tuple[int, str]] = []  # (ilk_index, firma_adı)
        lower_text = text.lower()

        # 1) Sözlük tabanlı (firmalar_seti) - precompiled chunk pattern'leri ile
        for pat in getattr(self, '_company_patterns', []) or []:
            for m in pat.finditer(text):
                bulunmus.append((m.start(), m.group(0)))

        # 2) Sonek heuristiği
        # Tokenları span ile çıkar
        token_iter = list(re.finditer(r"\b[\wÇĞİÖŞÜçğıöşü.]+\b", text))
        token_end_positions = [t.end() for t in token_iter]
        for suffix_match in self.FIRMA_SON_EK_REGEX.finditer(text):
            s_start = suffix_match.start()
            # Bisect ile O(log n) önceki token index'i
            insert_pos = bisect.bisect_right(token_end_positions, s_start) - 1
            if insert_pos < 0:
                continue
            last_idx = insert_pos
            # Geriye doğru 3'e kadar büyük harfle başlayan ardışık token al
            collected = []
            idx = last_idx
            while idx >= 0 and len(collected) < 3:
                tok = token_iter[idx].group(0)
                # Sonek zaten - bu noktada tok soneke ait olabilir; sonekle karışmasın diye kontrol
                if self.FIRMA_SON_EK_REGEX.fullmatch(tok.lower()):
                    idx -= 1
                    continue
                if re.match(r"^[A-ZÇĞİÖŞÜ]", tok):
                    collected.append(tok)
                    idx -= 1
                else:
                    break
            if not collected:
                continue
            collected.reverse()
            # Tek kelimelik ve kişi adı ise at
            if len(collected) == 1 and collected[0].lower() in self.isimler_seti:
                continue
            firma_ad = " ".join(collected + [suffix_match.group(0)]).strip()
            bulunmus.append((collected and token_iter[last_idx - (len(collected)-1)].start() or s_start, firma_ad))

        # Sıralı benzersiz
        bulunmus.sort(key=lambda x: x[0])
        seen_lower = set()
        sonuc: List[str] = []
        for _, name in bulunmus:
            low = name.lower()
            if low not in seen_lower:
                seen_lower.add(low)
                sonuc.append(name.strip())
        return sonuc

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

    # ---------------- OLCU ----------------
    class MeasurementParseException(Exception):
        pass

    def turkce_sayi_coz(self, sayi_kelime: str) -> Optional[float]:
        """Türkçe sayı kelimelerini (ör. yüz yirmi beş) sayısal değere çevirir.

        Desteklenen formatlar:
        - Basit: bir, iki, üç, dört, beş, altı, yedi, sekiz, dokuz, on, yüz, bin, milyon, milyar
        - Birleşik: onüç, yirmibeş, üçyüz, beşbin, onmilyon
        - Kesir: yarım, çeyrek, buçuk
        - Negatif: eksi beş, eksi üç buçuk
        """
        if not sayi_kelime or not isinstance(sayi_kelime, str):
            return None
        orijinal = sayi_kelime.strip().lower()

        # Negatif kontrolü
        negatif = orijinal.startswith("eksi")
        if negatif:
            orijinal = orijinal[5:].strip()

        # Kesir kontrolü
        if orijinal in {"yarım", "çeyrek", "buçuk"}:
            return (0.5 if orijinal == "yarım" else
                    0.25 if orijinal == "çeyrek" else
                    0.5)

        # Ayrık sayı kelimeleri
        sayi_parcalari = re.findall(r"\d+|[a-zA-Z]+", orijinal)
        toplam = 0
        mevcut = 0
        for parca in sayi_parcalari:
            if parca.isdigit():
                mevcut += int(parca)
            elif parca in self.TURKISH_NUMBER_WORDS:
                mevcut += self.TURKISH_NUMBER_WORDS[parca]
            else:
                raise self.MeasurementParseException(f"Geçersiz sayı kelimesi: {parca}")
            # 10, 100, 1000 gibi katları belirle
            if mevcut >= 1000:
                toplam += mevcut
                mevcut = 0
            elif mevcut >= 100:
                toplam += mevcut
                mevcut = 0
        toplam += mevcut
        return -toplam if negatif else toplam

    def _prepare_measurement_patterns(self):
        """Ölçü birimi regex kalıplarını önceden derler (performans için)."""
        if not self.olcu_alias2base:
            self._meas_patterns = None
            return
        all_aliases = sorted(self.olcu_alias2base.keys(), key=len, reverse=True)
        alias_pattern = "|".join(sorted({re.escape(a) for a in all_aliases}, key=len, reverse=True))
        NUM_PATTERN = r"(?:(?:(?:\d+[.,]?\d*)|(?:\d*[,\.]\d+)))"
        NUMBER_WORDS = r"(?:sıfır|bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on|yirmi|otuz|kırk|elli|altmış|yetmiş|seksen|doksan|yüz|bin|milyon|milyar)"
        WORD_SEQ = rf"{NUMBER_WORDS}(?:\s+{NUMBER_WORDS})*"
        self._meas_patterns = {
            'numeric': re.compile(rf"\b({NUM_PATTERN})\s*({alias_pattern})\b", re.IGNORECASE),
            'conc': re.compile(rf"\b({NUM_PATTERN})({alias_pattern})\b", re.IGNORECASE),
            'word': re.compile(rf"\b({WORD_SEQ})\s+({alias_pattern})\b", re.IGNORECASE),
            'word_conc': re.compile(rf"\b({WORD_SEQ})({alias_pattern})\b", re.IGNORECASE)
        }

    def extract_measurements(self, text: str) -> List[Dict[str, object]]:
        if not text or not text.strip() or not self.olcu_alias2base or not getattr(self, '_meas_patterns', None):
            return []
        results: List[Dict[str, object]] = []
        seen_spans: Set[Tuple[int,int]] = set()
        text_lower = text.lower()
        patterns_order = (
            self._meas_patterns['numeric'],
            self._meas_patterns['conc'],
            self._meas_patterns['word'],
            self._meas_patterns['word_conc']
        )

        def add_result(miktar_raw: str, unit_raw: str, span: Tuple[int,int], ham: str):
            base_lookup_key = unit_raw.lower()
            if base_lookup_key not in self.olcu_alias2base:
                return
            if re.search(r"\d", miktar_raw):
                miktar_norm = miktar_raw.replace(',', '.').strip('.').strip()
                try:
                    val = float(miktar_norm)
                except ValueError:
                    return
            else:
                try:
                    val_words = self.turkce_sayi_coz(miktar_raw)
                except Exception:
                    return
                if val_words is None:
                    return
                val = val_words
            if span in seen_spans:
                return
            seen_spans.add(span)
            results.append({
                'miktar': int(val) if isinstance(val, float) and val.is_integer() else val,
                'birim': self.olcu_alias2base[base_lookup_key],
                'ham': ham
            })

        for pat in patterns_order:
            for m in pat.finditer(text_lower):
                miktar_raw, unit_raw = m.group(1), m.group(2)
                span = m.span()
                ham = text[m.start():m.end()]
                add_result(miktar_raw, unit_raw, span, ham)

        results.sort(key=lambda x: x['ham'].lower())
        return results

    # ---------------- PARA BIRIMI / KUR ----------------
    def extract_currencies(self, text: str) -> List[Dict[str, object]]:
        """Metinden miktar + para birimi (kur) çiftlerini çıkarır.

        Kurallar:
        - `kurlar.txt` ilk öğe ISO kodu; satırın diğer alias/sembollerine map edilir.
        - Desteklenen biçimler:
          250 TL, 250tl, 250,5 TL, 1.250,75 usd, 99$, 45€ , 10 us dollar, 20 türk lirası
        - Sayı: 1.234,56 veya 1,234.56 gibi karışık desenlerde TR formatı (virgül ondalık) öncelik verilir.
          Basit normalize stratejisi:
            * Eğer hem nokta hem virgül varsa ve virgül sonda 2 hane -> virgül ondalık
            * Sadece virgül varsa -> virgül ondalık
            * Sadece nokta varsa -> nokta ondalık
        - Çıktı örneği: {'miktar': 250.5, 'kur': 'TRY', 'ham': '250,5 TL'}
        """
        if not text or not text.strip() or not self.kur_alias2code:
            return []
        lowered = text.lower()
        results: List[Dict[str, object]] = []
        used_spans: Set[Tuple[int,int]] = set()

        # Alias pattern (uzundan kısaya)
        aliases_sorted = sorted(self.kur_alias2code.keys(), key=len, reverse=True)
        alias_pattern = "|".join(re.escape(a) for a in aliases_sorted)

        # Sayı pattern: 1.234,56 ya da 1234,56 ya da 1,234.56 ya da 1234.56 veya 1234
        NUM = r"(?:\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?|\d+[.,]\d+|\d+)"

        # 1) Sayı + opsiyonel boşluk + alias/sembol
        pattern_num_first = re.compile(rf"\b({NUM})\s*({alias_pattern})\b", flags=re.IGNORECASE)
        # 2) Sembol/alias + sayı (daha az yaygın) (örn. TL250)
        pattern_unit_first = re.compile(rf"\b({alias_pattern})\s*({NUM})\b", flags=re.IGNORECASE)
        # 3) Bitişik sayı + sembol (99$) -> sembol tek karakter olabilir; alias_pattern bunu kapsıyor
        pattern_conc = re.compile(rf"\b({NUM})({alias_pattern})\b", flags=re.IGNORECASE)

        def parse_amount(raw: str) -> Optional[float]:
            s = raw.strip()
            if not s:
                return None
            # TR format sezgisi
            if ',' in s and '.' in s:
                # Son 3 içinde virgül ve ardından 2 hane -> virgül ondalık, noktalar binlik
                if re.search(r",\d{1,2}$", s):
                    s_clean = s.replace('.', '').replace(',', '.')
                else:
                    # Tam tersi (sonda .xx) -> nokta ondalık, virgüller binlik
                    s_clean = s.replace(',', '')
                try:
                    return float(s_clean)
                except ValueError:
                    return None
            elif ',' in s:
                # Virgül ondalık varsay
                s_clean = s.replace('.', '').replace(',', '.')
            else:
                s_clean = s
            try:
                return float(s_clean)
            except ValueError:
                return None

        def add(miktar_raw: str, alias_raw: str, span: Tuple[int,int], ham: str):
            akey = alias_raw.lower()
            if akey not in self.kur_alias2code:
                return
            amount = parse_amount(miktar_raw)
            if amount is None:
                return
            if span in used_spans:
                return
            used_spans.add(span)
            results.append({
                'miktar': int(amount) if float(amount).is_integer() else amount,
                'kur': self.kur_alias2code[akey],
                'ham': ham
            })

        for pat in (pattern_num_first, pattern_conc, pattern_unit_first):
            for m in pat.finditer(lowered):
                if pat is pattern_unit_first:
                    alias_raw, miktar_raw = m.group(1), m.group(2)
                else:
                    miktar_raw, alias_raw = m.group(1), m.group(2)
                span = m.span()
                ham = text[m.start():m.end()]
                add(miktar_raw, alias_raw, span, ham)

        # Benzersiz ham'a göre sıralama
        results.sort(key=lambda x: (x['kur'], x['miktar']))
        return results


if __name__ == "__main__":
    extractor = TextEntityExtractor()
    samples = [
        "Dr. Ahmet Yılmaz beni 0532 123 4567 numarasından yarın saat 19'da ara.",
        "Dr. Ahmet Yılmaz 532 123 4567 – 18 Ocak saat 19'da görüşelim.",
        "Sadece saat 19'da uygun olur.",
    ]
    for s in samples:
        print(s, "->", extractor.extract_all(s))
