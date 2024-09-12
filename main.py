import pandas as pd
import argparse

def split_and_count(input_file, output_file):
    df = pd.read_csv(input_file)
    df['split_words'] = df['บท (ย่อ)'].astype(str).fillna('').str.split('+').apply(
        lambda x: [item.strip() for item in x]
    )
    df_exploded = df.explode('split_words', ignore_index=True)
    word_counts = df_exploded['split_words'].value_counts().to_dict()
    result_df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])
    result_df.to_csv(output_file, index=False)
    print(f"Word counts have been saved to '{output_file}'.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Split words by + sign and count occurrences.')
    parser.add_argument('-i', '--input', required=True, help='Input CSV file name')
    parser.add_argument('-o', '--output', required=True, help='Output CSV file name')
    args = parser.parse_args()
    split_and_count(args.input, args.output)

if __name__ == '__main__':
    main()
