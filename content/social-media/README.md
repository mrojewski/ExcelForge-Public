# Social media publications

This directory is the working archive for public social-media copy. It is not
part of the GitHub Pages site and does not publish anything by itself.

## Channel structure

- `facebook/` — posts intended for the ExcelForge Facebook channel;
- `instagram/` — posts intended for the ExcelForge Instagram channel;
- `linkedin-personal/` — posts published from Marcin's personal LinkedIn
  profile, rather than an official ExcelForge account.

Each channel contains one Markdown file for each channel-specific publication.
The same topic may be adapted for more than one channel; in that case, create
one file in each relevant channel directory and keep the same `topic_id` in
their front matter.

Posts are written in a declared language. A language-derived or adapted
variant remains a separate file and records its origin with
`source_publication`; this keeps the relationship explicit without changing
the one-file lifecycle of either post.

For example:

```text
content/social-media/
├── facebook/PUB-001.md
├── instagram/PUB-001.md
└── linkedin-personal/PUB-001.md
```

`PUB-001` is an example only. It is the **ID tematu** from the `Publikacje`
sheet, not a separate GitHub identifier. Despite the retained field name,
`topic_id` identifies the concrete publication record being reconciled with
that sheet, rather than a broad editorial theme.

## Publication-file standard

Start every new file by copying [`_template.md`](_template.md). The front
matter is the structured record used to reconcile the file with `Publikacje`:

| Field | Rule |
|---|---|
| `topic_id` | Required. Exact ID tematu for the concrete publication record in `Publikacje`. Channel adaptations of that record keep the same value. |
| `channel` | Required. Must match the directory: `facebook`, `instagram`, or `linkedin-personal`. |
| `language` | Required. Lowercase language code for the post, for example `pl` or `en`. Use `pl` for an original Polish post. |
| `source_publication` | Optional. Leave blank for an original Polish post. For a language-derived or adapted variant, record the source publication ID, for example `PUB-001`. |
| `status` | Required. One of: `draft`, `review`, `scheduled`, `published`, `cancelled`. |
| `planned_publication_date` | Optional. Use `YYYY-MM-DD` when a date is planned. |
| `published_at` | Leave blank until publication; then record the actual date and time in ISO 8601 form, including timezone when known. |
| `publication_url` | Leave blank until publication; then link to the public post when a stable URL is available. |

The body holds the publication copy, graphic/format notes, linked assets, and
the short publication record. Keep private drafting comments out of copy that
could be published by mistake.

## Kierunek wizualny FB/IG

Zatwierdzonym wzorcem dla grafik FB/IG jest post nr 1 i jego wspólny asset
[`PUB-001_PUB-002_pl_czym-jest-excelforge.svg`](assets/PUB-001_PUB-002_pl_czym-jest-excelforge.svg).
Kolejne grafiki należą do tej samej rodziny wizualnej, lecz nie kopiują
kompozycji posta nr 1 w skali 1:1.

- Przygotowuj format 1:1, mobile-first, na jasnym tle `#FFFFFF → #F4F8F4`.
- Projektuj najpierw pod typowy ekran telefonu, nie pod desktop. Nagłówek,
  główna oś przekazu, ikony i etapy procesu muszą być czytelne bez zoomu.
- Ograniczaj liczbę elementów na planszy. Preferuj jeden główny komunikat i
  najwyżej kilka dużych, prostych elementów wspierających. Drobne opisy i
  rozwinięcia zostają w caption.
- Nie używaj małych ikon, miniaturek, cienkich etykiet ani drobnego tekstu,
  który jest czytelny dopiero po powiększeniu. Obowiązkowy jest sanity check
  po zmniejszeniu grafiki do rozmiaru typowego feedu mobilnego.
- Stosuj płaski, techniczno-edytorialny charakter: duży, prosty nagłówek,
  cienkie linie, subtelną siatkę / guide lines oraz geometryczne markery.
- Kanonicznym źródłem logo jest `mrojewski/ExcelForge`, branch `main`.
  Do finalnych grafik używaj gotowych assetów:
  `brand/logo/ef-block-primary.svg` albo
  `brand/logo/ef-lockup-horizontal.svg`.
- Generator grafiki nie może tworzyć, przerysowywać ani interpretować logo
  lub wordmarku. Nie wolno zmieniać układu 2×2, kolejności `E F / E F`,
  kolorów, proporcji, liter ani dodawać ramek, cieni, gradientów czy własnych
  wariantów znaku. Generator może tworzyć kompozycję i motywy, a canonical
  logo jest dokładane jako gotowy asset na etapie składu.
- Outline EF Block może być używany jako wtórny motyw dekoracyjny lub
  procesowy, ale nie zastępuje kanonicznego logo.
- Grafika jest branded openerem, a główna treść merytoryczna pozostaje w
  caption.
- Nie używaj stockowego ani lifestyle’owego looku: bez laptopów, biurek,
  kubków, roślin, notebooków, zdjęć i fotorealistycznych scen.
- Tam, gdzie pasuje do układu i przekazu, stosuj stopkę / ton:
  `Praktycznie. Świadomie. Bez skrótów.`


### Workflow projektowania i akceptacji grafik FB/IG

Dla kolejnych postów stosuj stały, czteroetapowy workflow, aby ograniczyć poprawki i utrzymać spójność serii:

1. **Kompozycja bez brandingu** — generator przygotowuje wyłącznie układ 1:1, hierarchię, ikony, tło i motywy. Nie generuje logo, wordmarku ani napisu `ExcelForge`. W projekcie należy zostawić czystą, przewidzianą strefę na kanoniczny znak.
2. **Podgląd mobilny jako obowiązkowy etap oceny** — każdą wersję oceniaj w mockupie telefonu / typowego feedu FB/IG. Sprawdź czy nagłówek, etapy procesu i ikony są czytelne bez zoomu oraz czy całość zachowuje właściwą hierarchię na małym ekranie.
3. **Branding dopiero po akceptacji układu** — po zatwierdzeniu kompozycji i mobile sanity check wstaw gotowy asset z `mrojewski/ExcelForge` / `main`: `brand/logo/ef-block-primary.svg` albo `brand/logo/ef-lockup-horizontal.svg`.
4. **Finalny mobile sanity check** — po dodaniu kanonicznego logo wykonaj ponowną ocenę w feedzie mobilnym. Jeśli tekst lub ikony wymagają powiększania, grafika nie jest gotowa.


- **Mockup mobilny jest wyłącznie warstwą prezentacyjną** — nie wolno mu modyfikować, przerysowywać ani reinterpretować gotowego assetu 1:1 ani zatwierdzonego copy. Mockup ma jedynie osadzić dokładnie ten sam asset i dokładnie ten sam tekst w symulowanym feedzie/telefonie. Nie dodawać własnych hashtagów, skrótów, zmienionych proporcji ani alternatywnych wersji treści.

Ten workflow rozdziela kompozycję, czytelność mobilną i branding. Nie należy wracać do pełnej generacji całej planszy tylko dlatego, że korekty wymaga jeden z tych trzech obszarów.

## Lifecycle and history

One channel-specific post has **one Markdown file**. Edit that file through
`draft` → `review` → `scheduled` → `published`; do not make `v2`, `final`, or
date-suffixed copies. Git history records the evolution of the draft.

Set `language` when the file is created and keep it accurate through the
lifecycle. Do not overwrite an original-language file to turn it into a
translation: create the adapted post as its own file, set its `language`, and
link it to the original with `source_publication`.

Once published, update the same file with the actual publication date, URL,
and final publication record. The copy in the file should then represent the
version that was published. Later factual corrections are allowed, but should
be made transparently in the same file and its Git history.

Before changing a post to `published`, confirm that it follows the public
communication rule in the repository root `README.md`: validated, current
capabilities must be distinguished from limitations, investigation, and future
intent.
