# ExcelForge — DEV backlog

## Token procesu w sekcji „Jak to działa?”

**Status:** odłożony eksperyment DEV-only. Nie jest zmianą homepage ani planem publikacji.

### Zamysł

- Ruch uruchamia się tylko raz po wejściu sekcji w widok; nie ma pętli ani automatycznego powtarzania.
- Punkt 01 otrzymuje krótki impuls na starcie.
- Małe, wyraźne kółko rusza od 01 do 02 w kolorze punktu 01.
- Po dotarciu do kolejnego punktu ten punkt dostaje krótki impuls, a kółko przejmuje jego kolor.
- Sekwencja powtarza się dla 02 → 03 i 03 → 04; po dojściu do 04 strona wraca do statycznego stanu.
- Na mobile ten sam proces porusza się pionowo między istniejącymi punktami.
- `prefers-reduced-motion` zachowuje wyłącznie obecny, statyczny układ.

### Granice

- Nie chodzi o samą animowaną linię kropek. Kropkowana linia jest jedynie trasą dla pojedynczego tokenu procesu.
- Nie zmienia geometrii kart kroków, treści, kolorów ani animacji logo EF/EF.
- Nie wymaga nowych assetów, fontów, trackerów ani publicznych pobrań.

### Decyzja na teraz

Pomysł jest zachowany na później. Obecna strona komunikuje cztery kroki wystarczająco dobrze bez dodatkowego ruchu, a wdrożenie teraz nie wnosi proporcjonalnej wartości. Jeśli wróci jako eksperyment, najpierw powstaje osobny DEV-only podgląd i ocena desktopu, mobile oraz reduced motion.
