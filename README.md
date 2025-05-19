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