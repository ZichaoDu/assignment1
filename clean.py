import pandas as pd

def clean(input_file1, input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df_merged = df1.merge(df2, left_on="respondent_id", right_on="id")
    df_merged.drop(columns="id", inplace=True)
    df_cleaned = df_merged.dropna()
    df_cleaned = df_cleaned[~df_cleaned["job"].str.contains('insurance', case=False)]

    return df_cleaned

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file1')
    parser.add_argument('input_file2')
    parser.add_argument('output_file')
    args = parser.parse_args()
    cleaned = clean(args.input_file1,args.input_file2)
    cleaned.to_csv(args.output_file, index=False)
