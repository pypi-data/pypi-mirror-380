import polars as pl
import polars.selectors as cs


def default_empty_cells(df: pl.DataFrame) -> pl.DataFrame:
    """
    Fill missing values in a Polars DataFrame using column-specific logic.

    - Numeric columns: Fill missing cells with the column mean.
    - Boolean and string columns: Fill missing cells with the column's most common value (mode).
    - Date columns: Fill missing cells with the column's maximum date.
    - Other column types are left unchanged.

    Parameters
    ----------
    df : pl.DataFrame
        The input Polars DataFrame with possible missing values.

    Returns
    -------
    pl.DataFrame
        A new DataFrame with missing values filled according to the rules above.
    """

    return df.with_columns(
        cs.numeric().fill_null(cs.numeric().mean()),
        cs.boolean().fill_null(cs.boolean().mode().first()),
        cs.string().fill_null(cs.string().mode().first()),
        cs.date().fill_null(cs.date().max()),
    )
