import os
import pandas as pd

def check_duplicates_in_csv(file_path, all_duplicates):
    """Check for duplicate words in the 'Word' column of a CSV file and mark duplicates."""
    df = pd.read_csv(file_path)
    
    if 'Word' not in df.columns:
        print(f"Warning: 'Word' column not found in {file_path}. Skipping this file.")
        return None

    # Normalize words to lowercase for case-insensitive comparison
    df['Normalized_Word'] = df['Word'].str.lower()

    # Check if normalized words in the current file exist in the overall duplicates dictionary
    df['Duplicated'] = df['Normalized_Word'].apply(lambda word: all_duplicates.get(word, ''))

    # Drop the normalized column before saving
    df.drop(columns=['Normalized_Word'], inplace=True)

    # Save the updated CSV file with the 'Duplicated' column
    df.to_csv(file_path, index=False)
    return df

def check_all_csv_files_in_directory(directory_path):
    """Check for duplicates in all CSV files in the given directory and return all duplicates."""
    csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the directory.")
        return {}
    
    all_words = {}
    
    # First, collect all words from all files
    for file in csv_files:
        file_path = os.path.join(directory_path, file)
        df = pd.read_csv(file_path)
        
        if 'Word' not in df.columns:
            print(f"Warning: 'Word' column not found in {file_path}. Skipping this file.")
            continue
        
        # Normalize words to lowercase and associate them with their files
        for word in df['Word']:
            if pd.notna(word):  # Exclude NaN
                word = word.strip().lower()  # Convert to lowercase for case-insensitivity
                if word in all_words:
                    # Ensure each file is listed only once for each word
                    if file not in all_words[word]:
                        all_words[word].append(file)
                else:
                    all_words[word] = [file]
    
    # Create a dictionary of duplicates where a word appears in more than one file
    all_duplicates = {word: ', '.join(files) for word, files in all_words.items() if len(files) > 1}
    
    return all_duplicates

def process_csv_files(directory_path):
    """Check all CSV files for duplicates and update them with a 'Duplicated' column."""
    # Check all CSV files in the directory for duplicates
    all_duplicates = check_all_csv_files_in_directory(directory_path)
    
    if not all_duplicates:
        print("No duplicates found in any of the CSV files.")
        return
    
    # Process each file again to add the 'Duplicated' column
    for file in os.listdir(directory_path):
        if file.endswith('.csv'):
            file_path = os.path.join(directory_path, file)
            check_duplicates_in_csv(file_path, all_duplicates)

def main():
    # Define input folder
    directory_path = 'words'  # Folder where word count CSVs are stored
    
    if os.path.isdir(directory_path):
        process_csv_files(directory_path)
    else:
        print(f"Invalid directory: {directory_path}")

if __name__ == '__main__':
    main()
