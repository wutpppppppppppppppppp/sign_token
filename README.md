# Project: Simple Script for splitting sign language

## Description

This project processes a CSV file to split words from a specific column by a delimiter (`+`), counts the occurrences of each word, and saves the results to a new CSV file. It includes automation for setting up the environment, installing dependencies, and running the script.

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
git clone <repository-url>
cd <repository-directory>
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
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
  - Run the script with the default input and output file names specified in the `Makefile`.

- **Specify Custom Input and Output Files:**

  Modify the `INPUT_FILE` and `OUTPUT_FILE` variables in the `Makefile`, or pass them as arguments if you adjust the `Makefile` to support it.

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
  python split_and_count.py -i "path/to/your_input_file.csv" -o "path/to/your_output_file.csv"
  ```

- **Clean Up:**

  ```bash
  make clean
  ```

## `Makefile` Targets

- `venv`: Creates a virtual environment.
- `install`: Installs dependencies.
- `run`: Runs the script with the specified input and output files.
- `clean`: Removes the virtual environment and output files.
- `requirements`: Generates or updates the `requirements.txt` file.

## Contributing

Feel free to contribute by submitting issues, suggestions, or pull requests. Ensure your code follows the project's style and includes appropriate tests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or issues, please contact [Your Name](your-email@example.com).

---

Adjust the placeholders like `<repository-url>`, `<repository-directory>`, and `[Your Name](your-email@example.com)` as needed for your specific project details. Let me know if there are any additional details or sections you’d like to include!
