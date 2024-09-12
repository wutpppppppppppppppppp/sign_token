import pandas as pd
import argparse

def split_and_count(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Ensure the column exists and handle NaN values
    if 'บท (ย่อ)' not in df.columns:
        raise ValueError("Column 'บท (ย่อ)' not found in the input file.")
    
    # Split the 'บท (ย่อ)' column by '+' sign and handle NaN values
    df['split_words'] = df['บท (ย่อ)'].astype(str).fillna('').str.split('+').apply(
        lambda x: [item.strip() for item in x if item.strip() != '']
    )
    
    # Explode the lists into separate rows
    df_exploded = df.explode('split_words', ignore_index=True)
    
    # Drop any NaN or empty values in the exploded DataFrame
    df_exploded = df_exploded[df_exploded['split_words'].notna() & (df_exploded['split_words'] != '')]
    
    # Count occurrences of each split word
    word_counts = df_exploded['split_words'].value_counts().to_dict()
    
    # Convert the dictionary to a DataFrame for easier saving
    result_df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])
    
    # Save the result to a CSV file
    result_df.to_csv(output_file, index=False)
    
    print(f"Word counts have been saved to '{output_file}'.")

def main():
    # Ask for user input
    input_file = input("Enter the path to the input CSV file: ")
    output_file = input("Enter the path for the output CSV file: ")
    
    # Call the function with the user-provided file names
    split_and_count(input_file, output_file)

if __name__ == '__main__':
    main()
