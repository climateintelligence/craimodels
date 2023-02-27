# CRAIMODELS

The models from CRAIMODELS are trained using CRAI (https://github.com/FREVA-CLINT/climatereconstructionAI) with different climate datasets.
Information about the training datasets and training parameters are given in `craimodels/models/info-models.yml`.

The trained models can be used for evaluation with:

- CRAI command line interface (CLI):
  ```bash
  crai-evaluate
  ```
- CRAI Python library:
  ```python
  from climatereconstructionai import evaluate
  evaluate()
  ```
For more information about the installation and usage of CRAI, see https://github.com/FREVA-CLINT/climatereconstructionAI/blob/main/README.md.

## License

`CRAIMODELS` is licensed under the terms of the BSD 3-Clause license.

## Contributions

`CRAIMODELS` is maintained by the Climate Informatics and Technology group at DKRZ (Deutsches Klimarechenzentrum).
- Current contributing authors: Étienne Plésiat.
