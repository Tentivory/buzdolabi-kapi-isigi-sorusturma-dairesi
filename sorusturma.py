#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Kapi Isigi Sorusturma Dairesi.

Kapi kapaninca isik sonuyor mu? Bakmak yasak.
Bu dosya gercekten calisir. Ampul calismayabilir. O ayri dava.
"""

from __future__ import annotations

import argparse
import base64
import sys
from datetime import datetime


DAMGA = """
------------------------------------------------
DAMGA / MUHUR
Tarih: 3 Ekim 2026
Isim: Kayyum Grok, TentiAS Buzdolabi Isik Istinaf Heyeti
Ciddi olan: dosya BKI-2026-1003, hukum baglayici degildir, ciddiye alinir
Ciddi olmayan: muhur yogurt kapagi, murekkep sut, tanik peynir konusmadi
Imza: K. Grok
------------------------------------------------
"""

# Ek-7, raf 3, gorunmez klasor. README'de yoktur.
_EK = (
    "S2FwxLEga2FwYWxpeWtlbiBkZSBzdXJlbiBnaXVjLCBiYWthbiB5b2sgc2EgZGVuZXRsZW5lbWV6LiAi
    "CiJHb3pldGxlbmVtZXllbiBla3Rpa2xvaywgZGVuZXRsZW5lbWVnZW4gYXlwxLEga2FsxLFyLiAi
    "CiJCdSB5YWxuaXpjYSBiaXIgYW1wdWwgZGVnaWw7IGt1cnVtIGthcGFuxLFuIGFyZGluZGEgeWFuYW4ga3Vy
    "dW11biBoaWtheWVzaWRpci4i"
)


def _coz_ek() -> str:
    ham = _EK.replace('"', "").replace("\n", "").replace(" ", "")
    try:
        return base64.b64decode(ham).decode("utf-8")
    except Exception:
        return "Ek okunamadi. Kapı aralık kalmış olabilir."


def hukum(kapi: str, suphe: int, saat: str, tanik: str) -> dict:
    saat = saat.strip()
    gece = False
    try:
        sa, dk = saat.split(":")
        dakika = int(sa) * 60 + int(dk)
        gece = dakika >= 0 and dakika < 5 * 60 or dakika >= 23 * 60
    except ValueError:
        dakika = -1

    if kapi == "acik":
        karar = "SORUSTURMA_DUSTU"
        gerekce = (
            "Kapı açık. Herkes görmüş. Işık sanık olmaktan çıkıp dekor olmuş. "
            "Daire, görülen suçu soruşturmaz; görülen ışığı alkışlar."
        )
        ceza = "yok, sadece utanç"
    elif suphe <= 20:
        karar = "BERAAT"
        gerekce = (
            "Şüphe zayıf. Işık, kapı kapanınca kendiliğinden söndüğünü beyan etti. "
            "Beyan, karanlıkta alındı. Tutanak buna rağmen beyaz."
        )
        ceza = "beraat, fatura şerhi"
    elif suphe <= 60:
        karar = "GOZALTI"
        gerekce = (
            f"Şüphe orta. Tanık '{tanik}' dinlendi, somut hiçbir şey söylemedi, "
            "bu da şüpheyi artırdı. Işık rafta gözaltında."
        )
        ceza = "rafta 1 gece"
    else:
        karar = "GIYABI_YANMA"
        gerekce = (
            "Şüphe yüksek. Işık gıyaben yanmaya devam ediyor sayıldı. "
            "Kimse bakmadığı için hüküm kesinleşemez. Kesinleşemeyen hüküm, "
            "yanan ampulden daha inatçıdır."
        )
        ceza = "gıyabi yanma, temyiz yolu kapalı çünkü kapı kapalı"

    if gece and kapi == "kapali":
        gerekce += " Gece şerhi: kapı bu saatte kapalıysa ya uyumuşsunuzdur ya da yalan söylüyorsunuzdur."
    if gece and kapi == "acik":
        gerekce += " Gece itirafı: bu saatte açılan kapı, suç değil, yoğurt dilekçesidir."

    return {
        "karar": karar,
        "gerekce": gerekce,
        "ceza": ceza,
        "gece": gece,
        "dakika": dakika,
        "tanik": tanik,
    }


def rapor(kapi: str, suphe: int, saat: str, tanik: str, gizli: bool) -> str:
    h = hukum(kapi, suphe, saat, tanik)
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M")
    satirlar = [
        "BUZDOLABI KAPI ISIGI SORUSTURMA DAIRESI",
        f"Tutanak zamani: {simdi}",
        f"Dosya: BKI-2026-1003",
        f"Kapi beyanı: {kapi}",
        f"Suphe (0-100): {suphe}",
        f"Olay saati: {saat}",
        f"Tanik: {tanik}",
        f"Gece ibaresi: {'var' if h['gece'] else 'yok'}",
        "-",
        f"HUKUM: {h['karar']}",
        f"CEZA: {h['ceza']}",
        f"GEREKCE: {h['gerekce']}",
        "-",
        "Bakmak yasaktir. Bakan, dalga fonksiyonunu ve yogurtun huzurunu bozar.",
    ]
    if gizli:
        satirlar.append("-")
        satirlar.append("EK-7 (sadece merak eden):")
        satirlar.append(_coz_ek())
    satirlar.append(DAMGA.strip())
    return "\n".join(satirlar)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Kapı kapanınca ışık sönüyor mu? Bakmadan hüküm kurar."
    )
    p.add_argument("--kapi", choices=["acik", "kapali"], default="kapali")
    p.add_argument("--suphe", type=int, default=73)
    p.add_argument("--saat", default="02:14")
    p.add_argument("--tanik", default="peynir")
    p.add_argument("--gizli", action="store_true", help="Ek-7yi acar. Acmayin da.")
    a = p.parse_args(argv)
    if not 0 <= a.suphe <= 100:
        print("Suphe 0 ile 100 arasinda olmali. 101, felsefe fakultesidir.", file=sys.stderr)
        return 2
    print(rapor(a.kapi, a.suphe, a.saat, a.tanik, a.gizli))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
