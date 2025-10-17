# Curation comments for NFDI4Culture collection:

- Curated input file:
  [N4C-Educational-Resources-DALIA-Interchange-Format.csv](N4C-Educational-Resources-DALIA-Interchange-Format.csv)
- Row numbers refer to the original csv file and the curated csv file. IDs refer
  (a) to the _N4C_ID_ column and (b) to the _DALIA_ID_ column.

- Missing DIF columns have been added with empty entries (_FileFormat_,
  _LearningResourceType_, _MediaType_, _TargetGroup_, _RelatedWork_, _Size_,
  _Version_).
- For several entries the authors could be the person authors instead of an
  organization.
- Minor corrections in _Authors_ field:
  - separator `" : "` for organizations
  - row 7 (https://nfdi4culture.de/id/E4571,
    913b7adf-48de-45da-9f77-ef347b8f3e55): first/last name reorder
  - row 9 (https://nfdi4culture.de/id/E4473,
    8477f8de-a6c6-416c-bda7-2936dacad5ff): marked author as organization
  - row 17 (https://nfdi4culture.de/id/E5456,
    284d20b2-9247-47fa-8231-7f71c0bd9927): missing `"n/a"` to indicate an empty
    authors list
- Licenses:
  - All license identifiers have been corrected to be consistent with SPDX.
  - row 12 (https://nfdi4culture.de/id/E5359,
    320f52eb-e122-4487-bfeb-05bb41a941cb) has wrong license - should be
    "proprietary"
  - row 17 (https://nfdi4culture.de/id/E5456,
    284d20b2-9247-47fa-8231-7f71c0bd9927) has wrong license - should be
    "proprietary"
  - row 19 (https://nfdi4culture.de/id/E4929,
    84e64329-43d9-4e0b-a1c5-0bd0c92d1133) has wrong license - should be
    "CC-BY-3.0"
  - row 20 (https://nfdi4culture.de/id/E4683,
    7542aa37-c5cd-4ae1-bdfb-a8c750d906ac) has wrong license - should be
    "CC-BY-3.0"

Notes for the DIF group:

- The URIs in the _N4C_ID_ column could be used for linking to the NFDI4Culture
  knowledge graph via the _RelatedWork_ column. It should be discussed which
  relation type is appropriate.

Duplicates:

- (resolved) row 5 (https://nfdi4culture.de/id/E4584,
  f67d0988-eca7-4607-acd8-48e8414e5018): duplicate in MVP1 collection (_Link_ ==
  https://www.youtube.com/playlist?list=PL0eaiqVqG1ovx-A_rGpz76nylfLjd9auR)
- (resolved) row 8 (https://nfdi4culture.de/id/E4572,
  84f0a93b-b978-4ca5-b823-28fd618f3f17): duplicate in MVP1 collection (_Link_ ==
  https://doi.org/10.5281/zenodo.6674301)
- (resolved) row 16 (https://nfdi4culture.de/id/E4329,
  eb455368-b141-4a00-86fe-b6e910acdcfe): duplicate in MVP1 collection (_Link_ ==
  https://digital-history-berlin.github.io/Python-fuer-Historiker-innen/home.html)

Missing communities: None
