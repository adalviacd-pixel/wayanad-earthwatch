import re
from datetime import datetime, timedelta
import earthaccess

POINT = (76.2571, 11.6629)  # Kalpetta (lon, lat)
SHORT_NAME = "NISAR_L2_GUNW_PROVISIONAL_V1"


def open_gunw(end_stamp="20261020T003232", window=("2026-10-08", "2026-10-21")):
    earthaccess.login()
    results = earthaccess.search_data(
        short_name=SHORT_NAME, point=POINT, temporal=window
    )
    for r in results:
        name = r["umm"]["GranuleUR"]
        if "_113_A_007_" in name and end_stamp in name:
            return name, earthaccess.open([r])[0]
    raise RuntimeError("Requested GUNW pair not found in search results")


def open_pair(start, end):
    """start and end are dates like '2026-10-08'. Returns (name, remote file)."""
    earthaccess.login()
    stop = (datetime.strptime(end, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
    results = earthaccess.search_data(
        short_name=SHORT_NAME, point=POINT, temporal=(start, stop), count=200
    )
    s, e = start.replace("-", ""), end.replace("-", "")
    for r in results:
        name = r["umm"]["GranuleUR"]
        stamps = re.findall(r"\d{8}T\d{6}", name)
        if ("_113_A_007_" in name and len(stamps) >= 3
                and stamps[0][:8] == s and stamps[2][:8] == e):
            return name, earthaccess.open([r])[0]
    raise RuntimeError("Pair " + start + " to " + end + " not found")