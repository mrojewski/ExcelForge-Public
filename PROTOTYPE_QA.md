# Guardian G1.1 Pilot — prototyp strony PL

Data: 2026-09-18. Status: RC do oceny wizualnej, **PUBLIC DISTRIBUTION NOT AUTHORIZED**.
Branch: `draft/guardian-g1-1-pilot-site-pl`. Brak merge, push i publikacji.

## Źródła sprawdzone przed zmianami

- ExcelForge-Public: `35e3c6fe65f661c73ee22fae23f642049a796e4b` (stan main i brancha roboczego).
- ExcelForge-Evidence/main: `12385069cf497511086559ab1a4dcc6a31170652`.
  Kanoniczny dokument: `Evidence/Session Summaries/EF-SS-2026-09-18_Guardian-G1.1-PL-Release-Docs-Support-and-Public-Website-Concept.md`.
- ExcelForge/release/guardian-g1-1-pilot-packaging: `b16aea44b02b048dd4bd44e94c8551938faf28f5`.
  Zakres ograniczeń: `RELEASE_NOTES_KNOWN_LIMITATIONS_2026-09-18_PL_DRAFT.md` (v0.5).
- Repozytoria źródłowe odczytane z tymczasowych kopii. Istniejące lokalne repozytoria prywatne i ich zmiany robocze pozostawione bez modyfikacji.

## Branding i rozstrzygnięcia

PNG skopiowany bajt w bajt z `_working/local/Guardian_G1_1_Windows/EF_Block_Guardian_v0.png` kanonicznego brancha produktu. SHA-256: `b9bf927d140acc58e5f58c702065ba91808b652e9d451efb879cdb02db133ddd`.
Hero wykorzystuje cztery kwadranty tego samego obrazu, bez przerysowywania znaku. Pozostałe wystąpienia używają całego obrazu.

Session Summary pozostawia wybór animacji otwarty. Bieżące zlecenie wybiera flat tile flip dla tego prototypu: 900 ms + stagger 50 ms, cztery zadane kierunki, jeden przebieg na załadowanie. To nie oznacza zatwierdzenia finalnego motion designu. Nie dodano wariantu cube-like.

Release Notes nadal mają status DO NOT PUBLISH. Ich CTA jest disabled / Wkrótce; nie skopiowano dokumentu ani pakietów do repozytorium publicznego. Nie podpięto Installation Guides. Historyczne sformułowanie Release Notes o oczekującym kanale kontaktu jest zastąpione późniejszym potwierdzeniem support@excelforge.eu w kanonicznym Session Summary. Nie modyfikowano źródeł.

## Challenge Pass

| # | Kontrola | Wynik |
|---|---|---|
| 1 | Brak sugestii gotowego publicznego pobierania | PASS — informacja o prototypie i statusie dystrybucji, disabled CTA |
| 2 | Zakres zgodny z evidence | PASS — podział kolumnowy, zachowane cztery granice z Release Notes |
| 3 | Kolory nie dominują | PASS — neutralne tło, logo i małe akcenty |
| 4 | Brak wymuszonej struktury czterech elementów | PASS — trzy korzyści, cztery kroki, dwie platformy |
| 5 | Nieprzeciążony hero | PASS — znak, produkt/Pilot, headline i jeden opis |
| 6 | Czytelny mobile | PASS w sprawdzonych viewportach — pionowy układ i brak poziomego overflow |
| 7 | Menu klawiaturą | PASS — Enter/Tab/Escape, zamknięcie po wyborze, fokus w sekcji, aria-expanded |
| 8 | prefers-reduced-motion | PASS przeglądu CSS — animacje tylko w no-preference; reduce wymusza none. Natywne przełączenie preferencji OS nie było testowane |
| 9 | Brak martwych aktywnych linków dystrybucji | PASS — wszystkie aktywne linki to istniejące kotwice lub mailto |
| 10 | Brak starego Guardian G1 | PASS — kontrola treści i metadanych |
| 11 | Spójne terminy PL | PASS — polskie nagłówki i komunikaty, Pilot/macOS/FAQ jako nazwy |
| 12 | Adres wsparcia | PASS — wszystkie mailto prowadzą do support@excelforge.eu; bez wysyłania wiadomości |
| 13 | Istniejący branding | PASS — identyczny hash zatwierdzonego assetu, bez nowego logo |

## QA techniczne i wizualne

- Lokalny podgląd HTTP, bez publikacji; brak frameworka i zależności.
- Desktop: hero i karty pobierania sprawdzone wizualnie; układ poziomy i sticky navigation.
- Mobile: hero, menu, karty pobierania i Pilot sprawdzone wizualnie; menu nie przesuwa treści.
- Tablet: sprawdzony układ pośredni. Rzeczywiste szerokości CSS odczytane z DOM obejmowały 1440, 640, 390 i 266 px (narzędzie viewport uwzględniało skalowanie przeglądarki). Brak poziomego overflow w odczytach.
- Nawigacja do Pobierz: aktualny wskaźnik, sekcja poniżej sticky header, fokus w sekcji, menu zamknięte. Escape przywraca fokus do przycisku.
- Logo ma jawny aspect-ratio, obrazy width/height, systemowy font bez pobierania; animowane są transform/opacity. Brak mechanizmu powodującego layout shift; nie wykonywano pomiaru laboratoryjnego CLS.
- Pełnostronicowy screenshot narzędzia zawierał powielone fragmenty; nie traktowano go jako wiarygodnego artefaktu. QA oparto na widokach sekcji i odczytach DOM.
- Przeglądarka poprawnie parsuje 121 reguł CSS, w tym oba warianty prefers-reduced-motion; brak błędów i ostrzeżeń konsoli.
- Sprawdzone kontrasty tekst/tło: podstawowy 14,14:1; drugorzędny 6,16:1; disabled CTA 5,52:1; biały tekst CTA 6,60:1.
- Offline guardrails: `python3 tools/check_prototype.py`. Dodatkowo `git diff --check`.
- Brak testu na fizycznych urządzeniach, pełnego audytu screen readerem i natywnego testu preferencji OS. Przegląd reduced-motion nie jest deklaracją takiego testu.

## Otwarte kwestie wizualne

- Ocena właściciela: skala znaku w hero, rytm odstępów i intensywność jednorazowego flipu.
- Istniejący raster 256 × 256 jest wyświetlany do 300 CSS px. Zachowano oryginał; ewentualny większy zatwierdzony asset poprawi ostrość na ekranach HiDPI.
- FAQ, wideo i wsparcie rozwoju pozostają wyraźnie przyszłymi miejscami. Dokumentacja i pobieranie wymagają osobnej autoryzacji przed aktywacją.

## Lokalny podgląd

Z katalogu repozytorium:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
```

Otwórz `http://127.0.0.1:8765`. Nie używać tego prototypu jako decyzji o publikacji. `noindex` jest dodatkową metadaną prototypu, nie kontrolą dostępu.
