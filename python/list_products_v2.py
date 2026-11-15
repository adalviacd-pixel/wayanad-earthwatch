import csv
import asf_search as asf
from shapely.geometry import shape, Point, box

TEST_POINT = Point(76.2571, 11.6629)      # Kalpetta
ROUGH_BOX = box(75.8, 11.5, 76.5, 11.95)  # ROUGH box, not the real boundary

results = asf.geo_search(
    intersectsWith="POINT(76.2571 11.6629)",
    dataset=asf.DATASET.NISAR,
    processingLevel="GUNW",
    maxResults=60,
)

rows = []
for r in results:
    p = r.properties
    poly = shape(r.geometry)
    covered = poly.intersection(ROUGH_BOX).area / ROUGH_BOX.area * 100
    name = p.get("sceneName") or p.get("fileID") or ""
    rows.append({
        "config": "UR" if "_UR_" in name else "PR" if "_PR_" in name else "?",
        "direction": p.get("flightDirection"),
        "track": p.get("pathNumber"),
        "frame": p.get("frameNumber"),
        "start": str(p.get("startTime"))[:10],
        "covered_pct": round(covered),
        "contains_point": poly.contains(TEST_POINT),
        "name": name,
    })

rows.sort(key=lambda row: row["covered_pct"], reverse=True)

with open("products.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Saved", len(rows), "rows to products.csv")
for row in rows[:10]:
    print(row["covered_pct"], row["config"], row["direction"],
          "track", row["track"], "frame", row["frame"], row["start"])