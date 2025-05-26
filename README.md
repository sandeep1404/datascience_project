# datascience_project
## Project Workflow

1. **Create Conda Environment**

    ```bash
    conda create -p venv python==3.10 -y
    ```

    This command creates a new conda environment with Python 3.10 in the `venv` directory.

2. **Add `venv` to `.gitignore`**

    To prevent the `venv` folder from being tracked by git, add the following line to your `.gitignore` file:

    ```
    venv/
    ```

    This ensures the environment files are not included in version control.

    3. **Install Requirements**

        To install the required Python packages, use the `requirements.txt` file with the following command:

        ```bash
        pip install -r requirements.txt
        ```

        This will install all dependencies listed in `requirements.txt` into your conda environment.

### Workflow--ML pipeline

1. Data Ingestion: Collect and preprocess data for analysis.
2. Data Transformation and validation: Cleanse and transform raw data into a usable format.
3. Model Training: Train machine learning models on transformed data.
4. Model Evaluation: Assess model performance using appropriate metrics. -- ML Flow and dagshub
5. Deployment: Deploy trained models for real-world applications or predictions.


## Workflows

1.update config.yaml
2.Update schema.yaml
3.Update params.yaml
4.Update entity
5.Update configuration manager
6.Update components
7.Update pipeline.py
8.update main.py