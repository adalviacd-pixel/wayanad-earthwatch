import csv
from datetime import datetime
import h5py
import numpy as np
from pyproj import Transformer
from nisar_common import open_pair, POINT
from maskdecode import decode_mask

PAIRS = [
    ("2026-06-22", "2026-07-04"),
    ("2026-07-04", "2026-08-21"),
    ("2026-08-21", "2026-09-02"),
    ("2026-09-02", "2026-09-14"),
    ("2026-09-14", "2026-09-26"),
    ("2026-09-26", "2026-10-08"),
    ("2026-10-08", "2026-10-20"),
]
HALF = 50
BASE = "science/LSAR/GUNW/grids/frequencyA/unwrappedInterferogram"

rows = []
for start, end in PAIRS:
    gap = (datetime.strptime(end, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")).days
    row = {"start": start, "end": end, "gap_days": gap}
    try:
        name, fobj = open_pair(start, end)
        with h5py.File(fobj, "r") as f:
            g = f[BASE]
            hh = g["HH"]
            epsg = int(hh["projection"][()])
            x = hh["xCoordinates"][:]
            y = hh["yCoordinates"][:]
            px, py = Transformer.from_crs(4326, epsg, always_xy=True).transform(*POINT)
            col = int(np.argmin(np.abs(x - px)))
            r_ = int(np.argmin(np.abs(y - py)))
            r0, r1 = max(r_ - HALF, 0), min(r_ + HALF, len(y))
            c0, c1 = max(col - HALF, 0), min(col + HALF, len(x))
            coh = hh["coherenceMagnitude"][r0:r1, c0:c1]
            unw = hh["unwrappedPhase"][r0:r1, c0:c1]
            mask = g["mask"][r0:r1, c0:c1]

        d = decode_mask(mask)
        valid = d["valid"]
        n = int(valid.sum())
        iono = d["iono_interp"].astype(bool)
        row.update({
            "window_rows_cols": f"{r1 - r0}x{c1 - c0}",
            "valid_pixels": n,
            "coh_mean_valid": round(float(np.nanmean(coh[valid])), 3) if n else "",
            "phase_std_valid_rad": round(float(np.nanstd(unw[valid])), 3) if n else "",
            "iono_flag_pct_of_valid": round(100 * float((iono & valid).sum()) / n, 1) if n else "",
            "anomaly_pixels": int(((d["ref_anom"] > 0) | (d["sec_anom"] > 0)).sum()),
            "zero_phase_in_valid": int(((unw == 0) & valid).sum()),
            "product": name,
        })
    except Exception as err:
        row["error"] = str(err)[:200]
    print(row)
    rows.append(row)

fields = []
for r in rows:
    for k in r:
        if k not in fields:
            fields.append(k)
with open("pair_quality.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)
print("saved pair_quality.csv")