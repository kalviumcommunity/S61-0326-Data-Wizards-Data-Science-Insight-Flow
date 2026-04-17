from __future__ import annotations

from pathlib import Path

import pandas as pd
import numpy as np


CSV_FILE = Path("data/raw/sample_people.csv")


def explain_milestone() -> None:
    """Explain the milestone objectives and why this matters."""
    print("=" * 80)
    print("MILESTONE: COMPARING DISTRIBUTIONS ACROSS MULTIPLE COLUMNS")
    print("=" * 80)
    print("\n[OBJECTIVE]")
    print("- Understand what a data distribution represents")
    print("- Compare central tendency across columns (mean, median)")
    print("- Compare spread and variability across columns (std, range)")
    print("- Identify differences and similarities between variables")
    print("- Build intuition for multi-column analysis")

    print("\n[WHY THIS MATTERS]")
    print("- Most real insights come from comparison, not isolation")
    print("- Analyzing columns in isolation misses relationships")
    print("- Distribution comparison reveals hidden patterns")
    print("- Informs decisions for deeper analysis")
    print("- Prevents misleading conclusions from single-column analysis")
    print("\n[KEY TAKEAWAY]")
    print("Think of distribution comparison as putting columns side by side")
    print("and asking: 'How are these different?'")


def load_dataframe(csv_path: Path) -> pd.DataFrame:
    """Load the sample data."""
    print("\n[STEP 1] LOAD THE DATAFRAME")
    print("-" * 80)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    df = pd.read_csv(csv_path)
    print(f"✓ Loaded from: {csv_path}")
    print(f"✓ Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print("\nDataFrame:")
    print(df)
    print("\nColumn data types:")
    print(df.dtypes)
    return df


def understand_distributions(df: pd.DataFrame) -> None:
    """Explain what distributions mean for this dataset."""
    print("\n[STEP 2] UNDERSTANDING DISTRIBUTIONS IN OUR DATA")
    print("-" * 80)
    
    print("\nWhat is a distribution?")
    print("- A distribution describes how data values are spread across a range")
    print("- It shows patterns: where values cluster, how they vary")
    print("- Each column in our data has its own distribution")
    
    print("\nNumeric columns in our dataset:")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    print(f"✓ {numeric_cols}")
    
    print("\nWhy compare distributions?")
    print("- Age and Salary are in different units and scales")
    print("- Direct comparison (Salary > Age) is meaningless")
    print("- We need to compare patterns, not raw values")
    print("- This shows us which variable is more consistent, which has more variation")


def compare_central_tendency(df: pd.DataFrame) -> pd.DataFrame:
    """Compare means and medians across numeric columns."""
    print("\n[STEP 3] COMPARING CENTRAL TENDENCY")
    print("-" * 80)
    
    print("\nCentral tendency measures where the 'center' of data is")
    print("- MEAN: The average (sum ÷ count)")
    print("- MEDIAN: The middle value when sorted")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Create comparison table
    central_stats = pd.DataFrame({
        'Column': numeric_cols,
        'Mean': [df[col].mean() for col in numeric_cols],
        'Median': [df[col].median() for col in numeric_cols],
    })
    
    print("\nCentral Tendency Comparison:")
    print(central_stats.to_string(index=False))
    
    print("\n[INTERPRETATION]")
    for col in numeric_cols:
        mean_val = df[col].mean()
        median_val = df[col].median()
        diff = mean_val - median_val
        
        print(f"\n'{col}' Column:")
        print(f"  Mean: {mean_val:.2f}")
        print(f"  Median: {median_val:.2f}")
        
        if abs(diff) < 1:
            print(f"  → Mean ≈ Median: Distribution is fairly symmetric")
        elif diff > 0:
            print(f"  → Mean > Median: Distribution is right-skewed (some high values)")
        else:
            print(f"  → Mean < Median: Distribution is left-skewed (some low values)")
    
    return central_stats


def compare_spread_variability(df: pd.DataFrame) -> pd.DataFrame:
    """Compare ranges and standard deviations across numeric columns."""
    print("\n[STEP 4] COMPARING SPREAD AND VARIABILITY")
    print("-" * 80)
    
    print("\nVariability measures how scattered or concentrated data is")
    print("- RANGE: Max - Min (how wide the data spans)")
    print("- STD (Standard Deviation): Measures average distance from mean")
    print("- VARIANCE: Squared standard deviation")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Create variability table
    variability_stats = pd.DataFrame({
        'Column': numeric_cols,
        'Min': [df[col].min() for col in numeric_cols],
        'Max': [df[col].max() for col in numeric_cols],
        'Range': [df[col].max() - df[col].min() for col in numeric_cols],
        'Std Dev': [df[col].std() for col in numeric_cols],
        'Variance': [df[col].var() for col in numeric_cols],
    })
    
    print("\nVariability Comparison:")
    print(variability_stats.to_string(index=False))
    
    print("\n[INTERPRETATION]")
    std_values = {col: df[col].std() for col in numeric_cols}
    max_std_col = max(std_values, key=std_values.get)
    min_std_col = min(std_values, key=std_values.get)
    
    print(f"\nHighest variability: '{max_std_col}' (Std Dev: {std_values[max_std_col]:.2f})")
    print(f"  → Data is more scattered, less consistent")
    
    print(f"\nLowest variability: '{min_std_col}' (Std Dev: {std_values[min_std_col]:.2f})")
    print(f"  → Data is more concentrated, more stable")
    
    return variability_stats


def identify_patterns_and_anomalies(df: pd.DataFrame) -> None:
    """Detect interesting behavior and patterns."""
    print("\n[STEP 5] IDENTIFYING PATTERNS AND ANOMALIES")
    print("-" * 80)
    
    print("\nLet's use statistics to raise questions about our data:")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    for col in numeric_cols:
        print(f"\n'{col}' Column Analysis:")
        
        # Quartile analysis
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1  # Interquartile range
        
        print(f"  Q1 (25th percentile): {q1:.2f}")
        print(f"  Q3 (75th percentile): {q3:.2f}")
        print(f"  IQR (middle 50% range): {iqr:.2f}")
        
        # Check for outliers
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        
        if len(outliers) > 0:
            print(f"  ⚠ Potential outliers detected: {len(outliers)} values")
            print(f"    (Values outside {lower_bound:.2f} to {upper_bound:.2f})")
            print(f"    Outlier values: {outliers[col].tolist()}")
        else:
            print(f"  ✓ No outliers detected (within bounds {lower_bound:.2f} to {upper_bound:.2f})")
        
        # Coefficient of variation (relative variability)
        cv = (df[col].std() / df[col].mean()) * 100
        print(f"  Coefficient of Variation: {cv:.1f}%")
        if cv < 15:
            print(f"    → Low relative variation (stable variable)")
        elif cv < 30:
            print(f"    → Moderate relative variation")
        else:
            print(f"    → High relative variation (volatile variable)")


def comprehensive_summary(df: pd.DataFrame) -> None:
    """Create a comprehensive summary of all statistics."""
    print("\n[STEP 6] COMPREHENSIVE SUMMARY ALL STATISTICS")
    print("-" * 80)
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    print("\nUsing describe() - comprehensive statistics:")
    print(df[numeric_cols].describe())
    
    print("\n[WHAT THIS TELLS US]")
    print("- count: Number of non-null values")
    print("- mean: Average value")
    print("- std: Standard deviation (spread)")
    print("- min: Smallest value")
    print("- 25%: First quartile (Q1)")
    print("- 50%: Median (middle value)")
    print("- 75%: Third quartile (Q3)")
    print("- max: Largest value")


def compare_relative_distributions(df: pd.DataFrame) -> None:
    """Compare distributions in relative terms (normalized)."""
    print("\n[STEP 7] COMPARING RELATIVE DISTRIBUTIONS (NORMALIZED)")
    print("-" * 80)
    
    print("\nSince Age and Salary are in different scales, let's normalize them")
    print("to compare distributions fairly using Z-scores:")
    print("  Z-score = (value - mean) / std_dev")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Create normalized version
    df_normalized = df[numeric_cols].copy()
    for col in numeric_cols:
        df_normalized[col] = (df[col] - df[col].mean()) / df[col].std()
    
    print("\nOriginal data vs Normalized (Z-scores):")
    comparison = pd.DataFrame({
        'Age (original)': df['Age'],
        'Age (normalized)': df_normalized['Age'].round(3),
        'Salary (original)': df['Salary'],
        'Salary (normalized)': df_normalized['Salary'].round(3),
    })
    print(comparison)
    
    print("\n[INTERPRETATION]")
    print("- Normalized values show relative spread independent of scale")
    print("- Values near 0 are close to the mean")
    print("- Positive values are above mean, negative values are below")
    print("- Both columns now on the same scale for fair comparison")


def guide_deeper_analysis(df: pd.DataFrame) -> None:
    """Provide insights for next steps."""
    print("\n[STEP 8] GUIDING DEEPER ANALYSIS - QUESTIONS TO ASK")
    print("-" * 80)
    
    print("\nBased on distribution comparison, here are questions to explore:")
    
    print("\n1. CORRELATION ANALYSIS:")
    print("   Q: Do Age and Salary move together?")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(numeric_cols) > 1:
        corr = df[numeric_cols].corr()
        print(f"   Correlation matrix:\n{corr.to_string()}")
        age_salary_corr = df['Age'].corr(df['Salary'])
        print(f"   Age-Salary correlation: {age_salary_corr:.3f}")
        if age_salary_corr > 0.5:
            print("   → Strong positive relationship (higher age, higher salary)")
        elif age_salary_corr > 0.2:
            print("   → Weak to moderate positive relationship")
        else:
            print("   → Weak or no linear relationship")
    
    print("\n2. OUTLIER INVESTIGATION:")
    print("   Q: Which individuals have unusual Age or Salary values?")
    age_mean = df['Age'].mean()
    age_std = df['Age'].std()
    salary_mean = df['Salary'].mean()
    salary_std = df['Salary'].std()
    
    df['Age_Zscore'] = (df['Age'] - age_mean) / age_std
    df['Salary_Zscore'] = (df['Salary'] - salary_mean) / salary_std
    
    unusual = df[(abs(df['Age_Zscore']) > 1.5) | (abs(df['Salary_Zscore']) > 1.5)]
    if len(unusual) > 0:
        print(f"   Found {len(unusual)} individuals with unusual values:")
        print(unusual[['Name', 'Age', 'Salary', 'Age_Zscore', 'Salary_Zscore']])
    else:
        print("   No obvious outliers detected")
    
    print("\n3. CONSISTENCY ANALYSIS:")
    age_cv = (df['Age'].std() / df['Age'].mean()) * 100
    salary_cv = (df['Salary'].std() / df['Salary'].mean()) * 100
    print(f"   Q: Which variable is more consistent?")
    print(f"   Age variability: {age_cv:.1f}%")
    print(f"   Salary variability: {salary_cv:.1f}%")
    if age_cv < salary_cv:
        print(f"   → Age is more consistent (lower variation)")
    else:
        print(f"   → Salary is more consistent (lower variation)")
    
    print("\n4. DISTRIBUTION SHAPE:")
    print("   Q: Are distributions symmetric or skewed?")
    for col in numeric_cols:
        skewness = df[col].skew()
        print(f"   {col} skewness: {skewness:.3f}", end="")
        if abs(skewness) < 0.5:
            print(" → Fairly symmetric")
        elif skewness > 0:
            print(" → Right-skewed (tail on right)")
        else:
            print(" → Left-skewed (tail on left)")


def main() -> None:
    """Main execution function."""
    explain_milestone()
    
    # Load data
    df = load_dataframe(CSV_FILE)
    
    # Step 2-5: Distribution analysis
    understand_distributions(df)
    central_stats = compare_central_tendency(df)
    variability_stats = compare_spread_variability(df)
    identify_patterns_and_anomalies(df)
    comprehensive_summary(df)
    compare_relative_distributions(df)
    guide_deeper_analysis(df)
    
    # Final summary
    print("\n" + "=" * 80)
    print("MILESTONE COMPLETE: DISTRIBUTION COMPARISON ANALYSIS")
    print("=" * 80)
    print("\n[KEY LEARNINGS]")
    print("✓ Computed summary statistics for multiple columns")
    print("✓ Compared means, medians, and ranges across columns")
    print("✓ Identified columns with higher/lower variability")
    print("✓ Detected patterns and potential anomalies")
    print("✓ Used comparisons to guide deeper analysis")
    print("\n[NEXT STEPS]")
    print("- Visualize these distributions (histograms, box plots)")
    print("- Perform correlation analysis")
    print("- Investigate outliers")
    print("- Build intuition for pattern recognition")
    print("=" * 80)


if __name__ == "__main__":
    main()
