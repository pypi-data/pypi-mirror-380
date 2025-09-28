import pandas as pd
import numpy as np
from collections import Counter


def initial_data_overview(df: pd.DataFrame, target: str = None, is_classification: bool = True, verbose: bool = True):
    """
    Perform an initial structured overview of a dataset (simplified version).
    
    This function checks for missing values, duplicates, outliers, validity issues, 
    and low variance features. Results are summarized and optionally printed.
    
    Parameters
    ----------
    df : pd.DataFrame
        The input dataset.
    target : str, optional
        Target column name (for supervised tasks). Default is None.
    is_classification : bool, default=True
        Whether the task is classification (True) or regression (False).
    verbose : bool, default=True
        If True, prints results to console. If False, only returns summary dictionary.
    
    Returns
    -------
    dict
        Dictionary with the following possible keys:
        
        - "missing_values": list of dicts, each with
            {"feature": str, "count": int, "percentage": float}
            Example access:
                summary["missing_values"][0]["feature"]  # first column name with missing
                summary["missing_values"][0]["percentage"]  # percentage missing
        
        - "duplicates": dict with {"count": int}
            Example access:
                summary["duplicates"]["count"]
        
        - "outliers": list of dicts, each with
            {"feature": str, "count": int, "percentage": float}
            Example access:
                summary["outliers"][0]["feature"]  # feature with most outliers
        
        - "validity": list of str with issues
            Example access:
                summary["validity"]
        
        - "low_variance": list of str (columns with constant values)
            Example access:
                summary["low_variance"]
    """

    summary = {}

    # ==============================
    # 1. Missing Values
    # ==============================
    missing = df.isna().sum()
    missing_pct = df.isna().mean() * 100
    missing_results = [
        {"feature": col, "count": int(missing[col]), "percentage": round(missing_pct[col], 2)}
        for col in df.columns if missing[col] > 0
    ]
    missing_results = sorted(missing_results, key=lambda x: x["percentage"], reverse=True)
    if missing_results:
        summary["missing_values"] = missing_results

    # ==============================
    # 2. Duplicates
    # ==============================
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        summary["duplicates"] = {"count": int(dup_count)}

    # ==============================
    # 3. Outliers (IQR Method)
    # ==============================
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    outlier_results = []
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        pct = len(outliers) / len(df) * 100
        if len(outliers) > 0:
            outlier_results.append({"feature": col, "count": int(len(outliers)), "percentage": round(pct, 2)})
    outlier_results = sorted(outlier_results, key=lambda x: x["percentage"], reverse=True)
    if outlier_results:
        summary["outliers"] = outlier_results

    # ==============================
    # 4. Validity Checks
    # ==============================
    validity_issues = []
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            if (df[col] < 0).any():
                validity_issues.append(f"Column '{col}' contains negative values")
        elif df[col].dtype == 'object':
            if df[col].str.strip().eq('').any():
                validity_issues.append(f"Column '{col}' contains empty strings")
    if validity_issues:
        summary["validity"] = validity_issues

    # ==============================
    # 5. Low Variance Features
    # ==============================
    low_var = [col for col in df.columns if df[col].nunique() <= 1]
    if low_var:
        summary["low_variance"] = low_var

    # ==============================
    # Verbose Print
    # ==============================
    if verbose:
        print("=" * 50)
        print("📊 INITIAL DATA OVERVIEW")
        print("=" * 50)

        if missing_results:
            print("\nMISSING VALUES")
            for r in missing_results:
                print(f" - {r['feature']}: {r['count']} missing ({r['percentage']}%)")

        if dup_count > 0:
            print("\nDUPLICATES")
            print(f" - {dup_count} duplicate rows detected")

        if outlier_results:
            print("\nOUTLIERS (IQR METHOD)")
            for r in outlier_results:
                print(f" - {r['feature']}: {r['count']} rows ({r['percentage']}%)")

        if validity_issues:
            print("\nVALIDITY CHECK")
            for issue in validity_issues:
                print(f" - {issue}")

        if low_var:
            print("\nLOW VARIANCE FEATURES")
            for col in low_var:
                print(f" - {col}")

        print("\n" + "=" * 50)
        print("✅ INITIAL DATA CHECK COMPLETE")
        print("=" * 50)

    return summary
