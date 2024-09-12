INPUT_FILE="SignBloom3D Pre&Post Fact For Fun - EP1.csv"
OUTPUT_FILE="word_counts.csv"

VENV_DIR=venv

venv:
	python3 -m venv $(VENV_DIR)

install: venv
	$(VENV_DIR)/bin/pip install -r requirements.txt

run: install
	$(VENV_DIR)/bin/python main.py

clean:
	rm -rf $(VENV_DIR)
	rm -f $(OUTPUT_FILE)

requirements: venv
	$(VENV_DIR)/bin/pip freeze > requirements.txt

.PHONY: venv install run clean requirements
