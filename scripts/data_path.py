from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]

raw_data = base_dir / "dataio" / "raw" / "CASATIA_Report_25122025.csv"

processed_folder = base_dir / "dataio" / "processed"

processed_data = base_dir / "dataio" / "processed" / "processed.csv"

chart_folder = base_dir / "dataio" / "chart"