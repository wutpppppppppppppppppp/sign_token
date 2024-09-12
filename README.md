Here’s the updated `README.md` to reflect the changes in your `Makefile` and script. This version explains that the script now uses interactive input and updates the relevant sections accordingly.

---

# Project: Split and Count Words

## Description

This project processes a CSV file to split words from a specific column by a delimiter (`+`), counts the occurrences of each word, and saves the results to a new CSV file. It includes automation for setting up the environment, installing dependencies, and running the script using `Makefile`.

## Features

- **Splits** text in a column by `+` sign.
- **Counts** occurrences of each word.
- **Saves** results to a CSV file.
- **Automates** setup and execution using `Makefile`.

## Prerequisites

- Python 3.6 or higher
- `make` (optional, but recommended for automation)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/wutpppppppppppppppppp/sign_token.git
cd https://github.com/wutpppppppppppppppppp/sign_token.git
```

### 2. Create and Activate a Virtual Environment

```bash
make venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
make install
```

### 4. Create `requirements.txt`

If you need to update or generate the `requirements.txt` file:

```bash
make requirements
```

## Usage

### Running the Script

You can use the `Makefile` to automate the process:

- **Run the Full Process:**

  ```bash
  make run
  ```

  This will:

  - Create the virtual environment (if not already created).
  - Install dependencies.
  - Run the script, which will prompt you to enter the path to the input and output files.

### Manual Commands

If you prefer to run commands manually:

- **Create Virtual Environment:**

  ```bash
  make venv
  ```

- **Install Dependencies:**

  ```bash
  make install
  ```

- **Run the Script:**

  ```bash
  python split_and_count.py
  ```

  - The script will prompt you for the input CSV file and output CSV file.

- **Clean Up:**

  ```bash
  make clean
  ```

## `Makefile` Targets

- `venv`: Creates a virtual environment.
- `install`: Installs dependencies.
- `run`: Runs the script with interactive input for file names.
- `clean`: Removes the virtual environment and output files.
- `requirements`: Generates or updates the `requirements.txt` file.
