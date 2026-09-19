# ExcelForge — Animation Lab A/B/C

DEV-only / prototype-only. Nie jest propozycją automatycznej zmiany animacji homepage ani publikacją. Public distribution: **NOT AUTHORIZED**.

Uruchom z katalogu repozytorium:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
```

Podgląd: `http://127.0.0.1:8765/dev/logo-motion-lab.html`.
Lab nie jest podłączony do homepage, jej nawigacji ani skryptów.

## Wspólne parametry

| Parametr | Wartość |
|---|---|
| Duration | 1300 ms na blok |
| Stagger | 70 ms; opóźnienia 0 / 70 / 140 / 210 ms |
| Całość | 1510 ms |
| Easing | `cubic-bezier(0.25, 0.1, 0.25, 1)` = dotychczasowe `ease` |
| Perspective | 900 px, środek znaku |
| Obrót | 1: Y −85° → 0°; 2: X +85° → 0°; 3: X −85° → 0°; 4: Y +85° → 0° |
| Powtórzenia | Jeden przebieg; kolejne tylko przyciskiem |
| Rozmiar znaku | 256 × 256 CSS px; 208 × 208 przy węższym układzie |
| Głębokość C | 18% szerokości malowanego bloku: 20,16 px przy 112 px; 16,38 px przy 91 px |

## Różnice

- **A — edge / hinge:** oryginalne kwadranty PNG, krawędziowe osie i opacity 0 → 1, jak w homepage. Zmieniono wyłącznie czas i stagger dla porównania.
- **B — central flat:** te same płaskie kwadranty, to samo opacity i kierunki, ale `transform-origin: center center`.
- **C — central cube:** płytki prostopadłościan zgodny z żądaną głębokością 18%, obracany wokół własnego środka w trzech wymiarach. Front i jedna sąsiednia ściana; bez fade, aby litera na widocznym boku nie znikała. Nie ma pozostałych czterech ścian ani dodatkowych liter.

Ściany widoczne w C: blok 1 — front/prawa; blok 2 — front/dolna; blok 3 — front/górna; blok 4 — front/lewa. Obrót ściany bocznej i jej rodzica daje frontową, nielustrzaną literę na początku ruchu.

Źródło wszystkich liter: niezmieniony `../assets/EF_Block_Guardian_v0.png`, SHA-256 `b9bf927d140acc58e5f58c702065ba91808b652e9d451efb879cdb02db133ddd`. Fronty i boczne litery to wycinki rastera w CSS, bez nowych plików graficznych. Kolory ścian odczytane z oryginalnego PNG: `#7dcb65`, `#4cbe5b`, `#26913f`, `#0e6b3a`.

Na wąskiej ścianie C litera jest proporcjonalnie mniejsza: zachowanie jej wielkości z frontu wymagałoby rozciągnięcia, przycięcia albo znacznie większej głębokości. Wybrano zachowanie proporcji. To ograniczenie wizualnej ciągłości do oceny właściciela, nie nowy projekt liternictwa.

W stanie końcowym, bez JS i przy reduced-motion każdy panel wyświetla ten sam oryginalny obraz. Animowane warstwy zachowują zarezerwowane wymiary. Końcowy stan jest więc identyczny także dla C.

## Visual QA — 2026-09-19

- Desktop 1440 px: trzy warianty obok siebie; identyczne 256 × 256 px, tło i odstępy. Obejrzano stan końcowy i klatkę obrotu.
- Mobile 390 i 320 px: pionowy układ, jednakowe wymiary A/B/C, brak poziomego overflow; sprawdzono także niższe panele B/C. Wysokość komunikatu na mobile zarezerwowana, aby start/koniec nie przesuwały logo (62,398 px przed, w trakcie i po przebiegu przy 320 px).
- Chrome/Chromium: klatka 350 ms, przycisk Enter, odtwarzanie i powrót do końcowego logo — PASS.
- Safari/WebKit: wizualna kontrola klatki 350 ms i powrót po odtworzeniu do statycznego znaku — PASS. Nie wykonywano emulacji telefonu w Safari ani testu na fizycznym iPhonie.
- Oś B: przeglądarka potwierdza `64px 64px` dla powierzchni 128 × 128 px.
- Oś C: `56px 56px` przy bloku 112 × 112 px; bryła ma front na +depth/2 i ścianę dochodzącą do −depth/2. Zewnętrzne cofnięcie o depth/2 ustawia końcowy front na płaszczyźnie znaku.
- Dokładnie dwie ściany na bryłę, każda z poprawnym wycinkiem E/F; `backface-visibility: hidden`. W sprawdzonej klatce brak lustrzanych liter.
- Ruch 1,3 s jest dłuższy i bardziej czytelny od punktu odniesienia 0,9 s; mały stagger daje nakładanie ruchów. Ocena, który charakter ruchu najlepiej pasuje do marki, pozostaje otwarta.
- C ma zauważalną, niewielką grubość; bez cieni, gradientów i dodatkowych kolorów. Boczne litery są małe, co osłabia efekt ciągłości względem pełnego sześcianu.
- Brak błędów/ostrzeżeń w odczytanej konsoli podglądu.

## Reduced-motion i testy logiki

JS sprawdza `matchMedia` przed każdym przebiegiem. Włączenie reduce podczas animacji ją anuluje. Przycisk jest disabled, a CSS dodatkowo ukrywa całą warstwę 3D i pokazuje oryginalny obraz. Parametr klatki QA także respektuje reduce.

Test `node tools/check-motion-lab.mjs`: PASS — start z reduce, próba replay przy reduce, zmiana preferencji w trakcie ruchu, wspólne timing/startTime, szybkie ponawianie i spóźnione zakończenie starszej animacji. Test wykonuje właściwy skrypt labu w kontrolowanym środowisku z atrapami DOM/WAAPI/matchMedia. Nie zastępuje natywnego testu ustawienia OS. Próba użycia emulacji DevTools przez narzędzie UI nie została ukończona; natywne przełączenie preferencji pozostaje niesprawdzone.

Pozostałe kontrole: poprawna składnia JS, `python3 tools/check_prototype.py`, `git diff --check`.

Opcjonalna klatka QA: `logo-motion-lab.html?frame=350` (czas w ms, 0–1510). Korzysta z tych samych animacji, zatrzymanych dla oględzin. Przycisk wraca do pełnego przebiegu. Nie ma takiego mechanizmu na homepage.

## Granica zmian

Baza: `4ab90e417c425a7b4d1f00d7bc808330d7ed02a6` na `draft/guardian-g1-1-pilot-site-pl`.
Nie zmieniono `docs/index.html`, plików `docs/assets/`, brandingu, pakietów ani konfiguracji publikacji. Nie aktywowano pobierania. Wyłącznie lokalny commit; bez push, merge i publikacji.
