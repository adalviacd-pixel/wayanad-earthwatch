import earthaccess

POINT = (76.2571, 11.6629)  # Kalpetta (lon, lat)


def open_gunw(end_stamp="20261020T003232", window=("2026-10-08", "2026-10-21")):
    earthaccess.login()
    results = earthaccess.search_data(
        short_name="NISAR_L2_GUNW_PROVISIONAL_V1",
        point=POINT,
        temporal=window,
    )
    for r in results:
        name = r["umm"]["GranuleUR"]
        if "_113_A_007_" in name and end_stamp in name:
            return name, earthaccess.open([r])[0]
    raise RuntimeError("Requested GUNW pair not found in search results")