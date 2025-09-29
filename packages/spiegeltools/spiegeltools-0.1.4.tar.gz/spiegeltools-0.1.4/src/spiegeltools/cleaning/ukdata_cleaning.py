import polars as pl
import os, glob
from typing import TextIO, Tuple
import geopandas as gpd

def merge_csv_files(input_folder: str, output_file: str) -> Tuple[pl.DataFrame, TextIO]:
    """Merge all CSV files in the input folder into a single DataFrame and save it to the output file.
    Args:
        input_folder (str): Path to the folder containing CSV files.
        output_file (str): Path to the output CSV file.
    Returns:
        Tuple[pl.DataFrame, TextIO]: Merged DataFrame and a file object for the output file.
    """
    csv_files = glob.glob(os.path.join(input_folder, "*.csv"))
    df_list = [pl.read_csv(file) for file in csv_files]
    df = pl.concat(df_list)
    df.write_parquet(output_file)
def set_location(df: pl.DataFrame, country: str, city: str, capital: bool, year: int) -> pl.DataFrame:
    """Set date and location information in the DataFrame.
    Args:
        df (pl.DataFrame): DataFrame to modify.
        country (str): Country name.
        city (str): City name.
        capital (bool): Whether the city is a capital.
        year (int): Year of the data.
    Returns:
        pl.DataFrame: Modified DataFrame with location and date information.
    """
    df = df.with_columns([
        pl.lit(country).alias("Country"),
        pl.lit(city).alias("City"),
        pl.lit(capital).alias("Capital"),
        pl.lit(year).alias("Year")
    ])
    return df
def split_month_year(df: pl.DataFrame) -> pl.DataFrame:
    """Split the 'Month' column into separate month and year columns.
    Args:
        df (pl.DataFrame): DataFrame with a 'Month' column in 'YYYY-MM'
    Returns:
        pl.DataFrame: DataFrame with 'Month' as an integer column.
    """
    try:
        df = df.with_columns(
        pl.col("Month")
        .str.split("-")
        .list.get(1)
        .cast(pl.Int8)
        .alias("Month")
        )
    except Exception as e:
        print("This function only supports UK Crime Datasets.")
    return df
def compare_dataframes(df: pl.DataFrame) -> str:
    """Compare the columns of the DataFrame with a standard DataFrame.
    Args:
        df (pl.DataFrame): DataFrame to compare.
    Returns:
        str: Message indicating if the DataFrame matches the standard structure.
    """
    standard_df = pl.DataFrame({
        "Year": ["Hey, You"],
        "Month": ["Out there on your own"],
        "Country": ["Sitting naked by the phone"],
        "City": ["Would you touch me?"],
        "Capital": ["Hey, you"],
        "Crime Type": ["Don't tell me there's no hope at all"],
        "Outcome": ["Together we stand, divided we fall"],
    })
    # Yeah this is a Pink Floyd song, but it fits the context of checking DataFrame columns.
    print("Missing: \n")
    for col in [c.lower() for c in standard_df.columns]:
        if col not in [c.lower() for c in df.columns]:
            print(col)
    print("\nNot Important: \n")
    for col in [c.lower() for c in df.columns]:
        if col not in [c.lower() for c in standard_df.columns]:
            print(col)
def compute_crime_stats(df: pl.DataFrame) -> pl.DataFrame:
    """
    Compute crime statistics by LSOA code.
    Args:
        df (pl.DataFrame): DataFrame containing crime data with 'LSOA21NM' and 'Crime type' columns.
    Returns:
        pl.DataFrame: DataFrame with LSOA code, number of crimes, number of solved crimes, crime rate, and solved rate. 
    """
    
    # List of outcomes that indicate a solved crime
    solved_outcomes = [
        "Investigation complete; no suspect identified",
        "Offender given a caution",
        "Offender given a penalty notice",
        "Offender given a drug possession warning",
        "Local resolution",
    ]

    # Calculate crime counts and rates by LSOA code
    crime_data = df.with_columns(pl.col("Last outcome category").is_in(solved_outcomes).alias("is_solved"))
    crime_data = crime_data.group_by("LSOA21NM").agg(
        pl.count("Crime type").alias("ncrimes"),
        pl.sum("is_solved").alias("nsolved")
    )
    total_crimes = crime_data["ncrimes"].sum()
    crime_data = crime_data.with_columns(
        (pl.col("ncrimes") / total_crimes * 100).round(2).alias("crime_rate")
    )

    # Calculate the solved rate
    crime_data = crime_data.with_columns(((crime_data["nsolved"] / crime_data["ncrimes"]) * 100).round(2).alias("solved_rate"))
    total_solved = crime_data["nsolved"].sum()

    return crime_data, total_crimes, total_solved
def prepare_lsoa_crime_data(df: pl.DataFrame) ->  tuple[pl.DataFrame, int, int]:
    """
    Prepare LSOA crime data by cleaning and computing statistics.
    Args:
        df (pl.DataFrame): DataFrame containing raw crime data.
    Returns:
        tuple: A tuple containing:
            - pl.DataFrame: DataFrame with LSOA code, number of crimes, number of solved crimes, crime rate, and solved rate.
            - int: Total number of crimes.
            - int: Total number of solved crimes.
    """
    
    # Clean and prepare the data
    df = df.drop_nulls()
    df = df.drop(["Crime ID", "Reported by", "LSOA code", "Falls within", "Location"])
    df = df.rename({"LSOA name": "LSOA21NM"})

    # Compute crime statistics
    crime_data, total_crimes, total_solved = compute_crime_stats(df)
    
    return crime_data, total_crimes, total_solved
def get_lsoa_boundaries(df: pl.DataFrame) -> gpd.GeoDataFrame:
    """Get LSOA boundaries compatible with the crime data.
    Args:
        df (pl.DataFrame): DataFrame containing crime data and LSOA Codes.
    Returns:
        gpd.GeoDataFrame: GeoDataFrame containing LSOA boundaries.
    """
    # Load LSOA boundaries
    lsoa_boundaries_file = gpd.read_file("../data/lsoa_boundaries.geojson")
    lsoa_boundaries_file["LSOA21NM"] = lsoa_boundaries_file["LSOA21NM"].astype(str)

    # Get list of LSOA codes from the crime data so we can filter the boundaries
    lsoa_list = df["LSOA21NM"].to_list()

    # Check which LSOA codes are not in the boundaries file
    lsoa_boundaries_nan = lsoa_boundaries_file[~lsoa_boundaries_file["LSOA21NM"].isin(lsoa_list)]
    lsoa_boundaries = lsoa_boundaries_file[lsoa_boundaries_file["LSOA21NM"].isin(lsoa_list)]

    # Merge crime data with LSOA boundaries 
    merged = lsoa_boundaries.merge(df.to_pandas(), on="LSOA21NM", how="left")
    
    # Keep only relevant columns
    cols_to_keep = ["LSOA21NM", "crime_rate", "ncrimes", "nsolved", "geometry", "solved_rate"]
    merged = merged[cols_to_keep]
    cols_to_keep_nan = ["LSOA21NM", "geometry"]
    lsoa_boundaries_nan = lsoa_boundaries_nan[cols_to_keep_nan]
    
    return merged, lsoa_boundaries_nan