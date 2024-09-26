import os
import pandas as pd

def check_duplicates_in_csv(file_path):
    """Check for duplicate words in the 'Word' column of a CSV file."""
    df = pd.read_csv(file_path)
    
    if 'Word' not in df.columns:
        print(f"Warning: 'Word' column not found in {file_path}. Skipping this file.")
        return None

    # Check for duplicates in the 'Word' column
    duplicated_words = df[df.duplicated('Word', keep=False)]
    
    if not duplicated_words.empty:
        # Create a list of duplicated words along with the file they came from
        duplicated_words['Source_File'] = os.path.basename(file_path)
        return duplicated_words[['Word', 'Source_File']].drop_duplicates()
    return None

def check_all_csv_files_in_directory(directory_path, output_file):
    """Check for duplicates in all CSV files in the given directory and save results."""
    csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the directory.")
        return
    
    all_duplicated_entries = []
    
    for file in csv_files:
        file_path = os.path.join(directory_path, file)
        duplicates = check_duplicates_in_csv(file_path)
        
        if duplicates is not None:
            all_duplicated_entries.append(duplicates)
    
    # Concatenate all the duplicated entries into one DataFrame
    if all_duplicated_entries:
        duplicated_df = pd.concat(all_duplicated_entries, ignore_index=True)
        duplicated_df = duplicated_df.groupby('Word')['Source_File'].apply(lambda x: ', '.join(x.unique())).reset_index()
        duplicated_df.columns = ['Word', 'Source_Files']

        # Save the result to a CSV file
        duplicated_df.to_csv(output_file, index=False)
        print(f"Duplicate words and their source files have been saved to '{output_file}'.")
    else:
        print("No duplicates found in any of the CSV files.")

def main():
    # Define input and output folders
    directory_path = 'words'  # Folder where word count CSVs are stored
    output_file = os.path.join('words', 'duplicate_words_report.csv')
    
    if os.path.isdir(directory_path):
        check_all_csv_files_in_directory(directory_path, output_file)
    else:
        print(f"Invalid directory: {directory_path}")

if __name__ == '__main__':
    main()
