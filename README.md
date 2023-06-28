# DAIS2023: [Automating Sensitive Data (PII/PHI) Detection](https://www.databricks.com/dataaisummit/session/automating-sensitive-data-piiphi-detection/)
This repo is related to a talk given by [Pouya](https://www.linkedin.com/in/pouya-data/) from [Prophecy](https://www.prophecy.io/) at the 2023 Data and AI Summit in San Franscisco. 

## Introduction
This Project Repository Houses 2 Prophecy Projects:
- pii_template : The base template where we do all the heavy lifting:
  - Decryption of Encrypted Data
  - Checking K Anonymity
  - Masking PII data
  - Copying tables to another location
- pii_demo : The (non technical) customer facing Project which inherits code from the template and allows a user to create an end to end pipeline.

## Configuration Setup
As prerequisite, for above code to run correctly, the user needs to set up Databricks Secrets. More on Databricks Secrets [here](https://docs.databricks.com/security/secrets/index.html)
The following configuration variables are required to set up for the demo project to run correctly:
- Pipeline Level Configurations:
  - `encryptionKey` (databricks-secret) : The encryptionKey used by the vendor to encrypt their data. (We are using the Cryptography Fernet module. in `python` for the same)
  - `databricks_token` (databricks-secret) : The databricks token of the user (needed to access the Model hosted on Databricks MLFlow. More details on hosting the model given [here](https://github.com/SimpleDataLabsInc/dais2023_automating_sensitive_data_detection/tree/main/pii_template)
  - `mask_character` (string) : Character with which PII data would be replaced
- Subgraph Level Configurations to overwrite:
  - `mask_pii` Subgraph:
    - `input_column` (string) : Name of the Column whose PII needs to be masked
    - `id_field` (string) : Name of the Primary Key Field for given dataset (for joining internally)
    - `filter_entity` (spark-expression) : To define a manual filter for entities received from standford-deid model. (unused as of now)
  - `copy_tables` Subgraph:
    - `source_catalog` (string) : Source Catalog (here, `clean_room`)
    - `source_schema` (string) : Source Database (here, `demo_data`)
    - `target_catalog` (string) : Target Catalog (here, `clean_room`)
    - `target_schema` (string) : Target Database (here, `hv`)
    - `tables` (array<string>) : List of table names to copy (choose the target tables from here)
  - `check_k_anonmity` Subgraph:
    - `min_num_patients` (int) : We quarantine records that may be reidentifiable, given a State and Diagnosis Code; For this we check if number of distinct users in the state, having this diagnosis code are less than `min_num_patients` 
    - `limit_records_for_model_inference` (int) : Used to limit records to mask, for demo purposes. This can be set to a higher number if this pipeline needs to be run on a complete dataset.
  - `decompress_decrypt` Subgraph : Uses the `encryptionKey` and `databricks_token` variables defined at the top (Pipeline Level)

## Setting up Databricks Secrets Configurations
To install databricks-cli and register secrets on MacOS:
```bash
brew install conda
conda create -n test_env
pip install databricks-cli
databricks configure

databricks configure --token --profile healthverity #User will be asked to provide workspace URL and Databricks token

databricks secrets create-scope --scope vendor_1 --profile healthverity
databricks secrets put --scope vendor_1 --profile healthverity --key encryption_key # Will open a file to paste the encryption key. Note that there should be no newline 
databricks secrets put --scope vendor_1 --profile healthverity --key databricks_token # Will open a file to paste the databricks token. Note that there should be no newline 
```

## Notes:
- The datasets in the `pii_template` project are READ-ONLY for the `pii_demo` project. Hence, even though these datasets can be used as Sources, they cannot be used as Targets, as writing to Target is a Write Operation.
