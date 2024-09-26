# Define variables for file names
INPUT_FILE="SignBloom3D Pre&Post Fact For Fun - EP1.csv"
OUTPUT_FILE="word_counts.csv"
DIRECTORY_PATH="csv_directory"
ALL_OUTPUT_FILE="duplicates_report.csv"

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

# Step 3: Run the individual_ep.py script
# Run this step by typing `make run_individual`
run_individual: install
	$(VENV_DIR)/bin/python individual_ep.py $(INPUT_FILE) $(OUTPUT_FILE)

# Step 4: Run the all_ep.py script
# Run this step by typing `make run_all`
run_all: install
	$(VENV_DIR)/bin/python all_ep.py $(DIRECTORY_PATH) $(ALL_OUTPUT_FILE)

# Step 5: Run both scripts
# Run this step by typing `make run_both`
run_both: run_individual run_all

# Step 6: Clean up generated files
# Run this step by typing `make clean`
clean:
	@echo "Enter the path for the output CSV file to delete (e.g., word_counts.csv):"
	@read OUTPUT_FILE; \
	rm -rf $(VENV_DIR); \
	rm -f $$OUTPUT_FILE; \
	rm -f $(ALL_OUTPUT_FILE)

# Step 7: Generate the requirements.txt file (if you add new dependencies)
# Run this step by typing `make requirements`
requirements: venv
	$(VENV_DIR)/bin/pip freeze > requirements.txt

.PHONY: venv install run_individual run_all run_both clean requirements
