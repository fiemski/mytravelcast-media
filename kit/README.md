# NAJPIERW PRZECZYTAJ – wiadomości od Grześka dla redakcji IG (rano)

## 19.11.2026 – zrzut profilu IG
Grzesiek przesłał zrzut ekranu profilu @mytravelcast z telefonu (dla redakcji IG – rano):
https://raw.githubusercontent.com/fiemski/mytravelcast-media/main/szkice/notatki/2026-11-19-profil-ig.jpg
Pobierz go i obejrzyj (Read) przed planowaniem okładek. Stan z 19.11: 29 postów, 25 obserwujących, 6,6 tys. wyświetleń w 30 dni.
Okładka karuzeli to kafelek w siatce profilu – oceniaj ją także w tej skali (kadr przycięty do ok. 3:4, mały ekran).

## 18.11.2026 – zasada nadrzędna: ZDJĘCIE PRZED TŁEM (nadrzędna wobec stylów A–D poniżej)
- Zdjęcie zajmuje cały slajd (najlepiej) albo zdecydowaną większość. Napisy leżą NA zdjęciu (gradient / mała płytka).
- NIE robimy małych zdjęć w ramkach, kółkach, kartach na dużym kolorowym tle (odrzucone: IG-052-v1/v2).
- Zdjęcia ostre, w wysokiej rozdzielczości (Unsplash min. ok. 2000–3000 px po dłuższym boku), pasujące do tekstu.
- Brak dobrych zdjęć = brak slajdu albo temat czeka.
- Wzór zaakceptowany przez Grześka: IG-052-v3 (szkice/IG-052-v3-1..4.jpg) oraz IG-056..059-v1.
- Style A–D zmieniają tylko sposób podania tekstu na zdjęciu, nie zamieniają zdjęcia w małą ramkę.

---

# Zestaw szablonów IG mytravelcast (stan 23.10.2026)

Przenośny zestaw do robienia grafik Instagrama mytravelcast w świeżym kontenerze.
Zasady publikacji Grześka: `kit/ZASADY.md` (kopia; wersja nadrzędna w Projekcie: `claude/instagram/zasady-publikacji.md`).
Rejestr i plan: Projekt, `claude/instagram/rejestr-publikacji.md` i `claude/instagram/plan-pracy.md`.

## Start
```
curl -sSL -o kit.tar.gz https://raw.githubusercontent.com/fiemski/mytravelcast-media/main/szablony/kit.tar.gz
tar -xzf kit.tar.gz && bash kit/setup.sh
```

## Karuzela (1080x1350, 4 slajdy) – wzór IG-006 Japonia
- `karuzela/s1..s4.html` + `common.css`: skopiuj katalog, podmień teksty i zdjęcia.
- Pasek trasy (nasze przejście zamiast „czytaj dalej”):
  `python3 -c "from route import route_html; print(route_html(2,4,'NASTĘPNY PRZYSTANEK','Tekst'))"`, wklej do slajdu.
- Render: `python3 kit/render_carousel.py KATALOG IG-007-v1 4`, a potem obejrzyj `contact.jpg` i każdy slajd.

## Story (1080x1920) – wzór IG-005 Machu Picchu
- `story/story.html`: żółta góra z falą, zdjęcie od 380 px, nagłówek 110 px nowrap, 4 kolorowe chipy, granatowa pigułka z adresem.
- Render: `python3 kit/render_story.py story/story.html IG-008-v1.jpg`.

## Styl (decyzje Grześka)
- Jasno, słonecznie, kolorowo i kontrastowo, mocno rzucające się w oczy. Nigdy ponuro.
- Prawdziwe, efektowne zdjęcia miejsc, a nie rysunki ani zwykłe zatłoczone ulice.
- Bez „CZYTAJ DALEJ” i bez kopiowania fly4free. Bez „link w bio”.
- Treść na kilku slajdach, źródła i linki oficjalne w pierwszym komentarzu.

## Zdjęcia (tylko Unsplash, darmowa licencja; autor w komentarzu i na ostatnim slajdzie)
Kontener nie pobiera z CDN zdjęć, więc zdjęcie zgrywa się przez Chrome:
1. Otwórz `images.unsplash.com/photo-ID?w=1080&h=H&fit=crop&crop=entropy&q=90&fm=jpg`.
2. JS: img width = 1322.45px, height = naturalHeight*1.22449 (skala zrzutu 0.8167).
3. Najedź myszą na (1450,400), żeby kursor nie wszedł w kadr.
4. Zrzuty `save_to_disk` ze **scale: 1** przy przewinięciu 0 / 919 / reszta.
5. Sklej kafle w PIL, podbij: Color 1.2–1.25, Contrast 1.05–1.08. Obejrzyj wynik.

## Zrzut mapy mytravelcast
`STYLE='NATURA I TREKKING' SHIFT=20 python3 kit/mtc_shot.py AZJA LIS out.png 1600 1000`
(SHIFT = dni strzałką na suwaku, np. LIS+20 daje 20.11–3.12). Ocenę stylu odczytaj ze zrzutu i nie zgaduj.

## Hosting i publikacja
- Pliki: repo `fiemski/mytravelcast-media` (publiczne), URL `https://raw.githubusercontent.com/fiemski/mytravelcast-media/main/<plik>`.
  Po wgraniu sprawdź sha256 przez curl.
- Metricool (blogId 7603257, Europe/Warsaw): najpierw szkic (`draft:true`). Po „ZATWIERDZAM IG-xxx-vN”
  ustaw media na URL-e raw, alt-teksty, `draft:false`, `autoPublish:true` (automat, bez muzyki i bez
  potwierdzeń w aplikacji, decyzja 23.10.2026) i termin: Story 9:00, karuzela 20:00. Story bez tekstu.
- Bez wyraźnej zgody na konkretną wersję nic nie publikujesz i nic nie planujesz do autopublikacji.

## Rotacja stylów (decyzja Grześka 26.10.2026)
Grzesiek: posty nie mogą wyglądać zawsze tak samo (widać automat). STAŁE elementy: górny wiersz (logo mytravelcast.com + pigułka) i dolny pasek trasy z samolotem. ZMIENNE: tło i sposób podania tekstu. Wzory 4 stylów: `kit/style/STYL-1..4.jpg`, kod: `kit/style/style_demo.py` (render: skopiuj common.css i zdjęcia praga.jpg/praga_tall.jpg/wieden.jpg do katalogu, `python3 style_demo.py`).
- A „Karty” – nasycone tło + białe karty z datami (dotychczasowy).
- B „Pasy” – zdjęcie w górnej części, ukośne cięcie, pod spodem nasycony kolor; tekst wprost na kolorze, linie zamiast białych podkładów.
- C „Naklejki” – zdjęcie na cały slajd, informacje na kolorowych, lekko obróconych naklejkach.
- D „Plakat” – gradient (np. pomarańcz→róż), wielkie konturowe daty/liczby, zdjęcie w kole z żółtą obwódką.
Zasada: kolejny post tego samego formatu ma INNY styl niż poprzedni (sprawdź w Historii poprzedniej karty, wpisz „styl X” do Historii). W karuzeli można mieszać 2 style między slajdami. Białe podkłady tylko w stylu A. Grzesiek prześle przykłady – wtedy zestaw się zmieni. Zawsze jasno i kolorowo, nigdy kremowo ani ponuro.
