# ExcelForge — Social Publications Working Plan

> **Status:** PUBLICATION SET A — OWNER GO / READY FOR SCHEDULING  
> **Checkpoint updated:** 2026-11-04  
> This file records current publication and visual-production decisions. It is not a product-model document and does not change Guardian/ExcelForge requirements.

## Publication set A — 06 / 10 / 13 November 2026

### 2026-11-06 — orientation: row vs column

**Final FB/IG copy — OWNER GO**

Te same dane można prezentować na różne sposoby.

Czasem najważniejsza informacja znajduje się w kolumnie, czasem w wierszu.

Dla użytkownika to zwykle nie jest problem.
Patrzy na tabelę i dość szybko rozumie, gdzie jest podział i według czego dane powinny zostać podzielone.

Dla narzędzia nie jest to już takie oczywiste.

Jeśli z góry założymy, że podział zawsze odbywa się według kolumny, rozwiązanie będzie działało dobrze tylko dla części przypadków.

A przecież użytkownik nie powinien za każdym razem przebudowywać danych tylko dlatego, że narzędzie rozumie jeden układ lepiej od drugiego.

Dlatego coraz bardziej przekonuje mnie prosta zasada:

narzędzie może podpowiadać, jak interpretuje strukturę danych, ale nie powinno wymuszać jednej orientacji jako jedynej poprawnej.

Wiersz czy kolumna?

Czasem narzędzie powinno po prostu oddać decyzję użytkownikowi.

**Graphic — OWNER GO / final publication asset approved**
- common series layout;
- headline direction: **„Wiersz czy kolumna?”**
- secondary line: **„Te same dane. Różny układ.”**
- two equal-size spreadsheet views;
- left: same information arranged/selected as a column;
- right: same information arranged/selected as a row;
- identical semantic data in both views;

---

### 2026-11-10 — data reading vs user intent

**Final FB/IG copy — OWNER GO**

Narzędzie może poprawnie odczytać dane, a intencja użytkownika może nadal pozostać nieznana.

Z tą samą tabelą można zrobić wiele:
podzielić ją,
zachować w całości,
pominąć część danych,
potraktować fragment jako podsumowanie, a nie element właściwego zakresu.

W tym miejscu samo rozpoznanie już nie wystarcza.

Narzędzie może sugerować najbardziej prawdopodobny sposób działania.
Może wskazać, jak interpretuje dane.

Użytkownik powinien określać cel.

Poprawne odczytanie danych nie oznacza poprawnego odczytania intencji.

**Graphic — OWNER GO / final publication asset approved**
- common series layout;
- headline direction: **„Jakie dane wybierasz?”**
- secondary line: **„Pojedynczą wartość, zakres czy całą tabelę?”**
- central visual: three spreadsheet sheets in a cascade;
- back: whole table;
- middle: selected data range;
- front: single selected value;
- sheets should be large enough to remain legible at social-feed size;

---

### 2026-11-13 — scope boundaries

**Final FB/IG copy — OWNER GO**

Nie zawsze potrzebujemy lepszego rozpoznawania danych przez narzędzie. Czasem ważniejsze jest precyzyjne określenie zakresu jego działania.

W jednej tabeli mogą znajdować się właściwe dane, podsumowania, sumy częściowe albo elementy pomocnicze.

Można próbować automatycznie rozpoznawać każdy z tych przypadków.

Ale można też podejść do problemu inaczej.

Zamiast zgadywać, które fragmenty powinny zostać uwzględnione, pozwolić użytkownikowi jasno wskazać zakres, na którym narzędzie ma pracować.

To zmienia perspektywę.

Nie próbujemy wtedy rozwiązać każdego możliwego przypadku interpretacją.
Ograniczamy obszar działania do tego, co zostało świadomie wskazane.

Czasem większa kontrola nie wymaga bardziej złożonej automatyzacji.

Wymaga lepiej określonych granic.

**Graphic — OWNER GO / final publication asset approved**
- common series layout;
- preferred direction: one large spreadsheet, not a complex multi-step diagram;
- one clearly highlighted working range;
- subtotal / total / auxiliary rows or cells outside the range visibly muted;
- small distinction between **„zakres działania”** and **„poza zakresem”**;
- headline direction: **„Zakres ma znaczenie.”**
- secondary direction: **„Czasem lepiej określić granice niż próbować rozpoznać wszystko.”**


## Final asset manifest — Publication set A

Owner decision on 2026-11-04: **#1 GO / #2 GO / #3 GO**.

Publication-ready source files prepared at 1080 × 1080:

| Date | Publication | Canonical filename | SHA-256 |
| --- | --- | --- | --- |
| 2026-11-06 | Wiersz czy kolumna? | `ExcelForge_2026-11-06_Wiersz-czy-kolumna_1080.png` | `ea353b4512bf476b9dbf92ca4203229edbaeaba66fe1da61f0409e5a9078b1e5` |
| 2026-11-10 | Jakie dane wybierasz? | `ExcelForge_2026-11-10_Jakie-dane-wybierasz_1080.png` | `5417c9beae13a0c18e86411ea2348af4630dc1f3fe8a25b18517dfaddfb8b00b` |
| 2026-11-13 | Zakres ma znaczenie. | `ExcelForge_2026-11-13_Zakres-ma-znaczenie_1080.png` | `7c58c471d584d8f81e03306160cff2f1f62d2a58c88495112b686eac59882b42` |

These hashes identify the exact approved PNG snapshots produced in the 2026-11-04 session and should be used to verify any repository/archive copy.

### Visual decision record

- #1 remains the cleanest reference/master for the series.
- #2 was iterated after the first series review because the cascading-sheet layout was visually less ordered than #1 and #3. Final GO uses one large sheet on the left and two sheets on the right, calmer callout backgrounds and only the three primary labels: `Zakres danych`, `Cała tabela`, `Pojedyncza wartość`.
- #3 retains the single-large-sheet concept with a clearly selected working range and muted data outside the range.
- Series typography remains deliberately lighter than generator-default heavy bold; visual priority is clarity and calmness rather than maximum headline weight.

## Channel adaptation

The three texts above are the **FB/IG working variants**.

For each topic, still prepare:
- **LinkedIn company** — closer to ExcelForge/Guardian and the concrete product/design implication;
- **LinkedIn personal** — adapted to the established “Notatnik inżyniera” voice, observation/reflection first.

Do not mechanically copy the FB/IG text across channels.

## Publication set B — working bank

Planned dates and topic order:
- **2026-11-16** — an experiment can show not only what works, but also what the solution does not solve;
- **2026-11-19** — one counterexample can change the meaning of many positive tests;
- **2026-11-23** — “test passed” does not automatically mean “we can deploy”.

Planned channels for each:
- FB/IG;
- LinkedIn company;
- LinkedIn personal.

## Visual-production rule for this set

Use the approved ExcelForge social graphic workflow:
1. copy first;
2. generator for illustration only;
3. freeze accepted illustration/layout;
4. canonical logo, exact copy, colors, icons and footer applied as controlled layers;
5. one final 1080×1080 PNG as source of truth for previews;
6. owner PASS remains separate from scheduling/publication.

Additional typography preference confirmed in this session:
- avoid heavy/bold-heavy headlines;
- prefer a lighter **semibold / medium-bold** visual weight;
- preserve readability without making typography visually dominant.

## Meta promotion experiment — first test

Selected post: **„AI jako partner, nie autopilot”**.

**Organic baseline captured before promotion**
- impressions: 14;
- viewers: 2;
- reactions: 0;
- clicks: 0;
- comments: 0;
- shares: 0;
- follows: 0;
- 92.9% of impressions reported from non-followers (do not confuse this with unique viewers).

**Promotion setup**
- platform: Meta (Facebook + Instagram);
- objective: more engagement;
- audience: Poland, all genders, 18–65+;
- interest signals: Microsoft Excel, data analysis, artificial intelligence, automation, Business intelligence tools;
- no CTA button;
- Advantage+ placements retained;
- AI-content disclosure selected for the generated/AI-edited visual;
- advertiser: ExcelForge;
- payer: Marcin Rojewski;
- start: 2026-11-04 09:00;
- duration: 5 days;
- planned end: 2026-11-09 09:00;
- budget: 8 PLN/day, approx. 40 PLN total.

**Experiment principle**
Do not change copy, visual, audience or budget during the test unless there is a genuine technical failure.

Primary question:
> Does paid exposure create meaningful behavior from new relevant audiences, or only additional impressions?

Final assessment after the full promotion period should distinguish:
- paid exposure / reach;
- engagement and clicks;
- profile/page interest;
- follows;
- qualitative behavior;
- PASS / INCONCLUSIVE / FAIL for the experiment hypothesis.

## Next checkpoint

Publication set A visual and FB/IG copy review is complete: **3× GO**.

Next work:
1. schedule/publish 06.11, 10.11 and 13.11 using the exact approved assets;
2. prepare LinkedIn company adaptations;
3. prepare LinkedIn personal adaptations;
4. continue Publication set B (16.11 / 19.11 / 23.11);
5. evaluate the Meta promotion experiment after the full test period.
