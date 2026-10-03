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

# Ek-7. README'de yok. Acmak icin --gizli. Merak kapidir.
_EK = (
    "S2FwxLEga2FwYWzEsXlrZW4gZGUgc8O8cmVuIGfDvMOnLCBiYWthbiB5b2tzYSBkZW5ldGxlbmVtZXou"
    "IEfDtnpldGxlbmVtZXllbiBpa3RpZGFyLCBkZW5ldGxlbmVtZXllbiBiaXIgYXnEsXAgb2xhcmFrIHJh"
    "ZnRhIGthbMSxci4gQnUgeWFsbsSxemNhIGJpciBhbXB1bCBkZcSfaWw7IGthcMSxc8SxIGthcGFuYW4g"
    "a3VydW11biBoaWvDonllc2lkaXIu"
)


def _coz_ek() -> str:
    try:
        return base64.b64decode(_EK).decode("utf-8")
    except Exception:
        return "Ek okunamadi. Kapi aralik kalmis olabilir."


def hukum(kapi: str, suphe: int, saat: str, tanik: str) -> dict:
    gece = False
    try:
        sa, dk = saat.strip().split(":")
        dakika = int(sa) * 60 + int(dk)
        gece = (0 <= dakika < 5 * 60) or (dakika >= 23 * 60)
    except ValueError:
        dakika = -1

    if kapi == "acik":
        karar = "SORUSTURMA_DUSTU"
        gerekce = (
            "Kapi acik. Herkes gormus. Isik sanik olmaktan cikmis, dekor olmus. "
            "Daire, gorulen sucu sorusturmaz; gorulen isigi alkislar."
        )
        ceza = "yok, sadece utanc"
    elif suphe <= 20:
        karar = "BERAAT"
        gerekce = (
            "Suphe zayif. Isik, kapi kapaninca kendiliginden sondugunu beyan etti. "
            "Beyan karanlikta alindi. Tutanak buna ragmen beyaz."
        )
        ceza = "beraat, fatura serhi"
    elif suphe <= 60:
        karar = "GOZALTI"
        gerekce = (
            f"Suphe orta. Tanik '{tanik}' dinlendi, somut hicbir sey soylemedi, "
            "bu da supheyi artirdi. Isik rafta gozaltinda."
        )
        ceza = "rafta 1 gece"
    else:
        karar = "GIYABI_YANMA"
        gerekce = (
            "Suphe yuksek. Isik giyaben yanmaya devam ediyor sayildi. "
            "Kimse bakmadigi icin hukum kesinlesemez. Kesinlesemeyen hukum, "
            "yanan ampulden daha inatcidir."
        )
        ceza = "giyabi yanma, temyiz yolu kapali cunku kapi kapali"

    if gece and kapi == "kapali":
        gerekce += " Gece serhi: kapi bu saatte kapaliysa ya uyumussunuzdur ya da yalan soyluyorsunuzdur."
    if gece and kapi == "acik":
        gerekce += " Gece itirafi: bu saatte acilan kapi, suc degil, yogurt dilekcesidir."

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
        "Dosya: BKI-2026-1003",
        f"Kapi beyani: {kapi}",
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
        description="Kapi kapaninca isik sonuyor mu? Bakmadan hukum kurar."
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
