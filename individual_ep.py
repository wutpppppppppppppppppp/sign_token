import os
import pandas as pd

def split_and_count(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Ensure the column exists and handle NaN values
    if 'บท (ย่อ)' not in df.columns:
        raise ValueError("Column 'บท (ย่อ)' not found in the input file.")
    
    # Define a function to split based on '+' or spaces
    def custom_split(text):
        if '+' in text:
            return [item.strip() for item in text.split('+') if item.strip() != '']
        else:
            return [item.strip() for item in text.split() if item.strip() != '']

    # Split the 'บท (ย่อ)' column by '+' or spaces and handle NaN values
    df['split_words'] = df['บท (ย่อ)'].astype(str).fillna('').apply(custom_split)
    
    # Explode the lists into separate rows
    df_exploded = df.explode('split_words', ignore_index=True)
    
    # Drop any NaN or empty values in the exploded DataFrame
    df_exploded = df_exploded[df_exploded['split_words'].notna() & (df_exploded['split_words'] != '')]
    
    # Count occurrences of each split word
    word_counts = df_exploded['split_words'].value_counts().to_dict()
    
    # Convert the dictionary to a DataFrame for easier saving
    result_df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])
    
    # Calculate the total number of unique words
    total_count = len(result_df)
    
    # Add a row for the total count
    total_row = pd.DataFrame([['Total', total_count]], columns=['Word', 'Count'])
    result_df = pd.concat([result_df, total_row], ignore_index=True)
    
    # Save the result to a CSV file
    result_df.to_csv(output_file, index=False)
    
    print(f"Word counts have been saved to '{output_file}'.")

def main():
    # Define input and output folders
    input_folder = 'data'
    output_folder = 'words'
    
    # Process all files in the 'data' folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, f"word_counts_{file_name}")
            split_and_count(input_file, output_file)

if __name__ == '__main__':
    main()
