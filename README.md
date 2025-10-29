# DALIA Curation

This repository contains open educational resources (OERs) curated by the DALIA
team in the DALIA Interchange Format (DIF).

## Contributing

1. read the
   [curation guide](https://github.com/data-literacy-alliance/dalia-dif/blob/main/docs/curation.md)
   to understand the tabular format.
2. After signing in to GitHub, do one of the following:
   1. edit a file in the repository by navigating through the
      [curation/](curation/) folder then press the pencil icon in the top-right
      corner. Click the big green button to create a commit then again the next
      big green button to create a PR.
   2. add a new file following this tutorial
      https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

This repository is set up to use continuous integration (CI) to run a validation
on all CSV files on commits and pull requests, so you will get immediate
feedback on any errors.

## Exports

The curated OERs encoded in the DIF v1.3 schema can be downloaded as
[`dalia-dif13.ttl` (RDF)](https://github.com/data-literacy-alliance/dalia-curation/raw/refs/heads/main/export/dalia-dif13.ttl)
or
[`dalia-dif13.jsonl` (JSON lines)](https://github.com/data-literacy-alliance/dalia-curation/raw/refs/heads/main/export/dalia-dif13.jsonl).

The DALIA Knowledge Graph (DALIA-KG) combines both the OERs encoded in the DIF
v1.3 schema and the ontologies underlying the fields inside the data model. It
can be downloaded from
[`dalia-dif13-full.ttl` (RDF)](https://github.com/data-literacy-alliance/dalia-curation/raw/refs/heads/main/export/dalia-dif13-full.ttl).
It incorporates both the original DALIA curations (licensed under CC0) and:

1. Learning resource types are imported from
   [Hochschulcampus Ressourcentypen](https://github.com/dini-ag-kim/hcrt) (CC0)
2. Disciplines are imported from
   [Hochschulfächersystematik](https://github.com/dini-ag-kim/hochschulfaechersystematik)
   (unlicensed,
   [see discussion](https://github.com/dini-ag-kim/hochschulfaechersystematik/issues/30))
3. Licenses - SPDX (unlicensed,
   [see discussion](https://github.com/spdx/license-list-XML/issues/2597))
4. Languages - LEXVO (CC-BY-SA-3.0)
5. MoDALIA (CC0)

## Summary

![](export/summary.svg)

## Case Study

The following SPARQL query federates the DALIA-KG and NFDI4Chem to connect
training materials in DALIA about the instruments used to produce data in
experiments in Chemotion.

```sparql
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX CHMO: <http://purl.obolibrary.org/obo/CHMO_>
PREFIX nfdi4chem.doi: <https://doi.org/10.14272/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX educor: <https://github.com/tibonto/educor#>

SELECT *
WHERE {
    ?oer a educor:EducationalResource .
    ?oer oboInOwl:hasDbXref ?measurementProcess .

    # This subquery connects datasets, experiments, and the
    # measurement processes using the NFDI4Chem knowledge graph
    SERVICE <https://search.nfdi4chem.de/sparql> {
        ?dataset prov:wasGeneratedBy/prov:used ?experiment .
        ?experiment prov:wasGeneratedBy/rdf:type ?measurementProcess .
    }
}
```

## 👋 Attribution

### ⚖️ License

The curated data in this repository is licensed under the CC0 license.

### 📖 Citation

An abstract describing the DIF has been published in the proceedings of the
2<sup>nd</sup> Conference on Research Data Infrastructure (CoRDI).

```bibtex
@misc{steiner2025,
    author = {Steiner, Petra C. and Geiger, Jonathan D. and Fuhrmans, Marc and Amer Desouki, Abdelmoneim and Hüppe, Henrika M.},
    title = {The Revised DALIA Interchange Format - New Picklists for Describing Open Educational Resources},
    month = aug,
    year = 2025,
    publisher = {Zenodo},
    doi = {10.5281/zenodo.16736170},
    url = {https://doi.org/10.5281/zenodo.16736170},
}
```

### 🎁 Support

This project has been supported by the following organizations (in alphabetical
order):

- [NFDI4Chem](https://www.nfdi4chem.de)
- [NFDI4Culture](https://nfdi4culture.de)
- [NFDI4Ing](https://nfdi4ing.de)

### 💰 Funding

This project has been supported by the following grants:

| Funding Body                                                       | Program | Grant Number |
| ------------------------------------------------------------------ | ------- | ------------ |
| German Federal Ministry of Research, Technology, and Space (BMFTR) |         | 16DWWQP07    |
| EU Capacity Building and Resilience Facility                       |         | 16DWWQP07    |
