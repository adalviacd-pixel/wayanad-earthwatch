import re
from datetime import datetime
import asf_search as asf
from shapely.geometry import shape, box

ROUGH_BOX = box(75.8, 11.5, 76.5, 11.95)  # ROUGH box, not the real boundary

results = asf.geo_search(
    intersectsWith="POINT(76.2571 11.6629)",
    dataset=asf.DATASET.NISAR,
    processingLevel="GUNW",
    maxResults=100,
)
print("Total GUNW results at this point:", len(results))

rows = []
shown_gap = False
for r in results:
    p = r.properties
    if str(p.get("pathNumber")) != "113" or str(p.get("frameNumber")) != "7":
        continue

    name = p.get("sceneName") or p.get("fileID") or ""
    stamps = re.findall(r"\d{8}T\d{6}", name)
    if len(stamps) < 4:
        print("Could not read dates from:", name)
        continue

    first = datetime.strptime(stamps[0][:8], "%Y%m%d")
    second = datetime.strptime(stamps[2][:8], "%Y%m%d")
    crid = re.search(r"_([PX]\d{5})_", name)
    config = "UR" if "_UR_" in name else "PR" if "_PR_" in name else "?"
    rows.append((first, second, (second - first).days,
                 crid.group(1) if crid else "?", config))

    if not shown_gap:
        part = shape(r.geometry).intersection(ROUGH_BOX)
        print("Rough box (W, S, E, N):", ROUGH_BOX.bounds)
        print("Covered part   (W, S, E, N):", tuple(round(v, 3) for v in part.bounds))
        shown_gap = True

rows.sort()
print("Track 113, Frame 7 pairs:", len(rows))
for first, second, gap, crid, config in rows:
    print(first.date(), "->", second.date(), "| gap", gap, "days |", crid, config)