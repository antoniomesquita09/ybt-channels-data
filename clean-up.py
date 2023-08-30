import pandas as pd

def replace_nan_with_zero(input_file, output_file):
    # Load the CSV file into a DataFrame
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Input file not found.")
        return
    
    # Replace "nan" with 0
    df.replace("nan", 0, inplace=True)
    
    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    
    print("Replacement completed. Modified data saved to", output_file)

if __name__ == "__main__":
    input_filename = "raw.csv"  # Replace with your input CSV filename
    output_filename = "cleaned-1.csv"  # Replace with the desired output CSV filename
    
    replace_nan_with_zero(input_filename, output_filename)
