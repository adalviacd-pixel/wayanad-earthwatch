import asf_search as asf
from shapely.geometry import shape, Point, box

TEST_POINT = Point(76.2571, 11.6629)      # Kalpetta
ROUGH_BOX = box(75.8, 11.5, 76.5, 11.95)  # ROUGH box, not the real boundary

results = asf.geo_search(
    intersectsWith="POINT(76.2571 11.6629)",
    dataset=asf.DATASET.NISAR,
    processingLevel="GUNW",
    maxResults=20,
)

print("Results found:", len(results))
print("Field names:", list(results[0].properties.keys()))
print()

for r in results:
    p = r.properties
    poly = shape(r.geometry)
    covered = poly.intersection(ROUGH_BOX).area / ROUGH_BOX.area * 100
    print(p.get("sceneName") or p.get("fileID"))
    print("  start:", p.get("startTime"),
          "| direction:", p.get("flightDirection"),
          "| path:", p.get("pathNumber"),
          "| frame:", p.get("frameNumber"))
    print("  contains test point:", poly.contains(TEST_POINT),
          "| rough box covered: %.0f%%" % covered)