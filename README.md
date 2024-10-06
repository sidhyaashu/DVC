# DVC (Data Version Control) for MLOps

[DVC](https://dvc.org/) is an open-source tool designed to manage machine learning projects similarly to how Git manages code. DVC helps in versioning large datasets, model files, and other data dependencies, enabling efficient collaboration, reproducibility, and CI/CD in ML workflows.

It integrates well with Git, making it a popular choice for MLOps (Machine Learning Operations), enhancing the lifecycle management of ML projects. Here's an overview of how DVC fits into MLOps:

## Key Features of DVC for MLOps

- **Versioning Data and Models**: Like Git, DVC version controls not only code but also large datasets and models, allowing you to track changes in your ML pipelines.
  
- **Pipeline Management**: DVC enables the definition and management of complex ML pipelines with dependencies, ensuring that data, code, and experiments are properly tracked.
  
- **Storage Agnostic**: DVC works with different storage backends (e.g., cloud storage like S3, Google Cloud, Azure, or even remote SSH and shared file systems) to handle large datasets efficiently.
  
- **Reproducibility**: By keeping track of datasets and models along with the code, DVC ensures that every experiment is reproducible by anyone on the team.
  
- **Collaboration**: Team members can share models, datasets, and experiments easily through Git-like workflows, making collaboration seamless in an ML project.
  
- **Data Pipelines**: DVC allows you to define stages in your ML pipeline and track their output, making it easier to rerun only the required stages when input changes.
  
- **CI/CD for ML**: DVC integrates well with CI/CD tools, enabling the automation of model training, validation, and deployment pipelines.

## DVC Workflow in MLOps

### 1. Setup Git and DVC

1. Initialize your Git repository:

   ```bash
   git init
   ```
2. Track your data and model files with DVC::

   ```bash
   dvc add data/dataset.csv
   dvc add models/model.pkl
   ```
3. Define ML Pipeline
 - Use DVC to define and structure your ML pipeline (from data preprocessing to model training). You can create a dvc.yaml file to define the pipeline:

 **yaml**

 ```bash
 stages:
  preprocess:
    cmd: python src/preprocess.py
    deps:
      - src/preprocess.py
      - data/dataset.csv
    outs:
      - data/processed/

  train:
    cmd: python src/train.py
    deps:
      - src/train.py
      - data/processed/
    outs:
      - models/model.pkl
```

4. Run the pipeline:

```bash
dvc repro
```

10. Check Dag:
```bash
dvc dag
```
5. Version Control Data and Models:
 - Add large datasets or models to DVC and push them to remote storage. DVC will generate small "tracking files" in the Git repository, while the actual data remains in the remote storage:

 ```bash
 git add data/dataset.csv.dvc models/model.pkl.dvc .gitignore
 git commit -m "Add dataset and model tracking with DVC"
 ```

6. Run and Track Experiments
   Use DVC to run experiments and keep track of the results, models, and corresponding data used:

```bash
    dvc exp run

    dvc exp show
   ```
7. Deploy Models:
   Once models are finalized, you can deploy them by integrating DVC pipelines into CI/CD systems. DVC works well with CI/CD tools, such as GitHub Actions, Jenkins, and GitLab CI, for automating model training, validation, and deployment.

```bash
    dvc push

    dvc pull
   ```
8. Setting Up Remote Storage
   Configure remote storage (e.g., S3, Google Cloud, Azure, etc.) to store large data files and models:

```bash
    dvc remote add -d myremote s3://mybucket/path
    dvc push
   ```
9. CI/CD Integration Example (GitHub Actions):

```bash
name: CI
on: [push]
jobs:
  dvc_pipeline:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Pull DVC data
        run: dvc pull
      - name: Run DVC pipeline
        run: dvc repro
```

