# Curation comments for NFDI Sektion Metadaten AG Cookbooks collection

- Curated input file:
  [Resources (DIF) - section-metadata-wg-cookbooks resources.csv](<Resources%20(DIF)%20-%20section-metadata-wg-cookbooks%20resources.csv>)
- Row numbers refer to the curated csv file and not the original Google
  Spreadsheet. IDs refer (a) to the _Resource Local ID_ column (if an ID exists
  there) and (b) to the _DALIA_ID_ column.

- In the _Authors_ field URLs to Wikidata pages were used. These are not the
  correct URIs to Wikidata entities (aka _Concept URIs_). Corrected.
- In the _Keywords_ field URLs to Wikidata pages were used. (a) These are not
  the correct URIs to Wikidata entities (aka _Concept URIs_). (b) Our
  application cannot handle these URIs at the moment, and to be honest we do not
  have any concept for handling them yet. Thus, those URLs were substituted with
  their label from the Wikidata page in the language of the respective learning
  resource.
- In the _LearningResourceType_ field:
  - Compact URIs (CURIEs) were used (e.g. "mo:Cookbook" instead of "Cookbook").
    This might be due to ambiguity in the DIF document. Corrected.
  - Corrected several entries, so they work in the mapping. (Spelling of the
    labels or substituting labels with URIs from HCRT)
- other corrections/notes:
  - row 3 (cb3, 69aebdfe-73f6-4bac-85d7-047dd8cec076): license looks correct;
    this is the license of the
    [Git repository](https://github.com/rdawg-pidinst/white-paper-pdf), which
    also points to this ressource
  - row 5 (cb14, d3201f8f-ddff-481f-a4c6-7f8c311bec53): added license
    "proprietary"
  - row 9 (1fa5e48b-464c-4a33-995d-993ee7c54139): added license "proprietary"
  - row 10 (cb26, 34375e88-6a6b-4cb8-9929-5c867459dd7d): added license
    "proprietary"
  - row 11 (5508bdc3-90a5-4ab6-9c0b-c2528317264e): added license "proprietary"
  - row 12 (928c6d5f-043a-4cc0-8a08-ca98bf2f8c08): added license "proprietary"
  - row 16 (cb18, c9e1f1e4-ec3f-4b6d-8b48-d3aecb946c5a): added license
    "proprietary"
  - row 17 (cb19, 93febfcd-33bf-4e38-b769-02874e3f7558): corrected link
  - row 20 (cb22, 4c75adad-4e33-4388-9dba-3fe1e3a97659): added license
    "proprietary"
  - row 26 (cb29, e6947cc5-dd70-4467-9577-e70a246c00f8): added license
    "proprietary"
  - row 28 (cb7, 4374117c-1a89-424b-ae77-c15076d399f3): changed license to
    "proprietary"
  - row 29 (cb7-2, ff90860a-a6a0-4f1c-91d7-ef9277df03fd): changed license to
    "proprietary"
  - row 32 (cb12, bb221201-93a8-4e77-977b-73552fe3b781): added license
    "proprietary"
  - row 33 (cb13, 7f3ed964-824d-4895-a258-5770a9fa9460): added license
    "proprietary"

Notes for the DIF group:

- Learning resource type "Video" was used, which comes from
  [hcrt:video](https://w3id.org/kim/hcrt/video). This kind of clashes with the
  media type "Video".
- Learning resource type "Sonstiges" was used, which comes from
  [hcrt:other](https://w3id.org/kim/hcrt/other).

Duplicates:

- (resolved) row 6 (cb30, 0d9de230-7a7f-497e-ae1a-9cd8efdc2105): duplicate in
  MVP1 collection (_Link_ == https://textplus.hypotheses.org/9035)
- (resolved) row 23 (cb24, 767c763c-7cd1-4d43-84e0-9c8845a37fe8): duplicate in
  MVP1 collection (_Link_ == https://rdmkit.elixir-europe.org/index.html)
- row 24 (cb24.1, 4ad26087-389d-42d2-8bb5-4c8d9fb24783): duplicate in FAIRagro
  collection, row 15 (_Link_ == https://rdmkit.elixir-europe.org/plant_sciences)
- row 25 (cb2.1, 921276e4-b5be-4524-9e2a-5b26691c7786): duplicate in FAIRagro
  collection, row 14 (_Link_ ==
  https://faircookbook.elixir-europe.org/content/recipes/reusability/miappe.html)

Missing communities:

- Section Metadata WG Cookbooks
- DINI-AG KIM
- FAIRsharing
- DCMI Application Profiles Working Group
- Verbundzentrale des GBV
- DataCite
- Helmholtz Metadata Collaboration (HMC)
- FAIRplus
- Earth Science Information Partners (ESIP)
- Forschungsdatenmanagement Bayern
- DCC Digital Curation Centre
- Kompetenzzentrum Interoperable Metadaten (KIM)
- Deutsche Initiative für Netzwerkinformation
