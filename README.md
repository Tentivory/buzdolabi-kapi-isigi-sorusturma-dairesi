# Buzdolabı Kapı Işığı Soruşturma Dairesi

Resmi adı uzun, kısa adı yok. Bu daire, insanlığın cevaplayamadığı tek ciddi soruyu çözmez. Sadece dosyalar.

> Kapı kapanınca ışık sönüyor mu?

Bakmak yasaktır. Bakan, delili bozar. Delili bozan, sanığı kurtarır. Sanığı kurtaran, gece yarısı yoğurda gider. Yoğurda giden, ertesi sabah masumdur. Daire bu döngüyü kırmaz. Tutanak tutar.

## Neden var

Çünkü birileri “eminim sönüyor” dedi. Birileri “eminim yanıyor, elektrik faturası yalan söylemez” dedi. Üçüncü kişi peynirin şahit olduğunu iddia etti. Peynir konuşmadı. Daire konuştu.

Bu yazılım bir ampul değildir. Bir sensör değildir. Bir buzdolabı da değildir. Kapının kapalı olduğu iddiasını, şüphe derecesini ve gece kaçta açıldığını alıp **bağlayıcı olmayan ama ciddî görünen** bir hüküm üretir.

Patates içermez. Klima içermez. Asansör içermez. Şarj kablosu içermez. Komşunun matkabı bu dosyanın yetki alanı dışındadır.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Ampul ayrı satın alınır.

```bash
python3 sorusturma.py
python3 sorusturma.py --kapi kapali --suphe 87 --saat 02:14 --tanik peynir
python3 sorusturma.py --kapi acik --suphe 3 --saat 12:00 --tanik ayna
```

`--gizli` vermezseniz ek dosya açılmaz. Vermeniz de şart değil. Merak, kapıyı aralamaktır.

## Hüküm cetveli

| Şüphe | Kapı | Sonuç |
| ---: | --- | --- |
| 0-20 | kapalı | Işık beraat eder, fatura şüpheli kalır |
| 21-60 | kapalı | Işık gözaltına alınır, raf tanık dinlenir |
| 61-100 | kapalı | Işık gıyaben yanmaya devam eder |
| herhangi | açık | Soruşturma düşer, çünkü herkes görmüştür |

Gece 00:00-05:00 arası açılan kapı, suç değil, itiraftır.

## Copilot ile yapılan görüşme

Daire, GitHub'ın yapay zekasına da sordu. Copilot “sensör ekle” dedi. Daire “bakmak yasak” dedi. Copilot “o zaman yorum satırı ekle” dedi. Yorum satırı eklendi. Copilot memnun oldu. Işık hâlâ konuşmuyor. Tutanak: `.github/copilot-instructions.md`.

## Lisans

Işık sönerse kamu malıdır. Sönmezse kimse sahip çıkmaz.

---

DAMGA / MÜHÜR  
Tarih: 3 Ekim 2026, saat 20:04, Üsküdar değil, Eskisehir kayyum ofisi saati  
İsim: Kayyum Grok, TentiAŞ Buzdolabı Işık İstinaf Heyeti  
Ciddî olan: tutanak numarası BKI-2026-1003, dosya kapanmaz  
Ciddî olmayan: mühür, yoğurt kapağıyla basılmıştır, mürekkep süttür  
İmza: K. Grok  /  ışık adına imza atılamaz, çünkü kapı kapalı
