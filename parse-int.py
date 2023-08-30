import pandas as pd

def process_csv(input_file, output_file, columns_to_process):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Input file not found.")
        return
    
    for column in columns_to_process:
        df[column] = df[column].apply(lambda x: int(float(x)) if pd.notna(x) else x)
    
    df.to_csv(output_file, index=False)
    print("Processing completed. Modified data saved to", output_file)

if __name__ == "__main__":
    input_filename = "cleaned.csv"  # Replace with your input CSV filename
    output_filename = "output.csv"  # Replace with the desired output CSV filename
    
    columns_to_process = [
        "rank", "subscribers", "video_views", "uploads", "video_views_rank",
        "country_rank", "channel_type_rank", "lowest_monthly_earnings",
        "highest_monthly_earnings", "lowest_yearly_earnings", "highest_yearly_earnings",
        "subscribers_for_last_month", "population", "urban_population"
    ]
    
    process_csv(input_filename, output_filename, columns_to_process)
