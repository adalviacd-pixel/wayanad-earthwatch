import asf_search as asf

results = asf.geo_search(
    intersectsWith="POINT(76.2571 11.6629)",
    dataset=asf.DATASET.NISAR,
    processingLevel="GUNW",
    maxResults=5,
)

print("Results found:", len(results))

first = results[0]
for key, value in first.properties.items():
    print(key, ":", value)

print("Footprint:", first.geometry)