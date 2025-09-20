# Data Engineering Toolkit
The Data Engineering Toolkit provides lightweight Python scripts for common data engineering tasks:

- Cleaning raw data
- Transforming data frames
- Loading data into files

## Project Goal:
This toolkit aims to learn version control with Git as taught in the Data Engineering Community Launchpad program.
I’ll be creating scripts that clean data, load data, and transform data, as well as pushing changes to GitHub to practice collaborative workflows.


## Code examples


## Contribution guide

**Prerequisite:** [Python: 3.12.10](https://www.python.org/downloads/release/python-31210/)


1. **Clone the Repository:**

   From your terminal, clone the repository.

   ```bash
   git clone https://github.com/yusufokunlola/data-engineering-toolkit.git
   ```

    Navigate to the ` data-engineering-toolkit` folder.

    ```bash 
    cd data-engineering-toolkit
    ``` 

2. **Set Up Virtual Environment:**

   Create a virtual environment named `data-engineering-toolkit`.

   ```bash
   # Windows
   python -m venv de-toolkit

   # macOS or Linux
   python3 -m venv de-toolkit
   ```

   Activate the virtual environment:

   ```bash
   # Windows
   de-toolkit\Scripts\activate

   # macOS or Linux
   source de-toolkit/bin/activate
   ```

   Install necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```