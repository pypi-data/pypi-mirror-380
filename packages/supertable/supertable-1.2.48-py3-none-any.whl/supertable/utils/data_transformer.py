import polars as pl

def convert_spark_to_polars_via_row_iteration(records) -> pl.DataFrame:

    # Convert row by row - completely avoids PyArrow
    rows = records.collect()

    # Create a dictionary to hold column data
    data = {}
    for col_name in records.columns:
        data[col_name] = []

    # Populate the data
    for row in rows:
        for col_name in records.columns:
            data[col_name].append(row[col_name])

    # Create Polars DataFrame
    polars_df = pl.DataFrame(data)
    return polars_df
