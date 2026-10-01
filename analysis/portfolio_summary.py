from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "synthetic_curriculum_portfolio.csv"
REFERENCE_DATE = pd.Timestamp("2026-10-01")
df = pd.read_csv(DATA_PATH, parse_dates=["launch_date", "last_refresh_date"])
required = {"product_id", "title", "topic", "format", "delivery_mode", "lifecycle_stage", "launch_date", "registrations", "attendees", "completion_rate", "satisfaction_score", "last_refresh_date"}
missing = required.difference(df.columns)
assert not missing, f"Missing required columns: {sorted(missing)}"
df = df.drop_duplicates().copy()
df["attendance_rate"] = df["attendees"] / df["registrations"]
max_registrations = df["registrations"].max()
df["utilization_score"] = 100 * (0.35 * (df["registrations"] / max_registrations) + 0.25 * df["attendance_rate"] + 0.20 * df["completion_rate"] + 0.20 * (df["satisfaction_score"] / 5))
df["refresh_age_months"] = ((REFERENCE_DATE - df["last_refresh_date"]).dt.days / 30.44).round(1)
df["refresh_candidate"] = df["lifecycle_stage"].eq("Refresh") | ((df["utilization_score"] &lt; 60) & (df["refresh_age_months"] &gt;= 12))

print("CURRICULUM PORTFOLIO SUMMARY")
print("=" * 28)
print(f"Products: {len(df):,}")
print(f"Topics: {df['topic'].nunique():,}")
print(f"Formats: {df['format'].nunique():,}")
print(f"Total registrations: {df['registrations'].sum():,}")
print(f"Total attendees: {df['attendees'].sum():,}")
print(f"Portfolio attendance rate: {df['attendees'].sum() / df['registrations'].sum():.1%}")
print(f"Average completion rate: {df['completion_rate'].mean():.1%}")
print(f"Average satisfaction: {df['satisfaction_score'].mean():.2f} / 5")

print("\nRegistrations by topic")
print(df.groupby("topic")["registrations"].sum().sort_values(ascending=False).to_string())

print("\nPortfolio by format")
print(df.groupby("format").agg(products=("product_id", "count"), registrations=("registrations", "sum"), attendees=("attendees", "sum")).sort_values("registrations", ascending=False).to_string())

print("\nTop products by utilization score")
print(df[["product_id", "title", "utilization_score"]].sort_values("utilization_score", ascending=False).head(5).to_string(index=False, formatters={"utilization_score": "{:.1f}".format}))

print("\nRefresh candidates")
print(df.loc[df["refresh_candidate"], ["product_id", "title", "lifecycle_stage", "utilization_score", "refresh_age_months"]].sort_values("utilization_score").to_string(index=False, formatters={"utilization_score": "{:.1f}".format}))
