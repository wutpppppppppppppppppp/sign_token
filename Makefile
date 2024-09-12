# Define variables for file names
INPUT_FILE="SignBloom3D Pre&Post Fact For Fun - EP1.csv"
OUTPUT_FILE="word_counts.csv"

# Virtual environment directory
VENV_DIR=venv

# Step 1: Create a virtual environment
# Run this step by typing `make venv`
venv:
	python3 -m venv $(VENV_DIR)

# Step 2: Activate the virtual environment and install dependencies
# Run this step by typing `make install`
install: venv
	$(VENV_DIR)/bin/pip install -r requirements.txt

# Step 3: Run the Python script
# Run this step by typing `make run`
run: install
	$(VENV_DIR)/bin/python main.py

# Step 4: Clean up generated files
# Run this step by typing `make clean`
clean:
	@echo "Enter the path for the output CSV file to delete (e.g., word_counts.csv):"
	@read OUTPUT_FILE; \
	rm -rf $(VENV_DIR); \
	rm -f $$OUTPUT_FILE

# Step 5: Generate the requirements.txt file (if you add new dependencies)
# Run this step by typing `make requirements`
requirements: venv
	$(VENV_DIR)/bin/pip freeze > requirements.txt

.PHONY: venv install run clean requirements
