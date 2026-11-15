import csv
import json
import os

rows = list(csv.DictReader(open("pair_quality.csv")))

pairs = []
for r in rows:
    pairs.append({
        "start": r["start"],
        "end": r["end"],
        "gap_days": int(r["gap_days"]),
        "valid_pixels": int(r["valid_pixels"]),
        "coherence_mean": float(r["coh_mean_valid"]),
        "phase_std_rad": float(r["phase_std_valid_rad"]),
        "iono_flag_pct": float(r["iono_flag_pct_of_valid"]),
        "anomaly_pixels": int(r["anomaly_pixels"]),
        "product": r["product"],
    })

out = {
    "dataset": "NISAR L2 GUNW, Track 113, Frame 7, ascending, HH",
    "maturity": "Provisional (CRID P05023)",
    "window": "100 x 100 pixels (about 8 km at 80 m spacing) centered near Kalpetta",
    "caution": "Statistics describe one small window. They are not district-wide and are not displacement measurements.",
    "pairs": pairs,
}

os.makedirs("../public/data", exist_ok=True)
with open("../public/data/pairs.json", "w") as fh:
    json.dump(out, fh, indent=2)
print("wrote ../public/data/pairs.json with", len(pairs), "pairs")