import h5py
import numpy as np
from pyproj import Transformer
from nisar_common import open_gunw, POINT

name, fobj = open_gunw()
base = "science/LSAR/GUNW/grids/frequencyA/unwrappedInterferogram/HH"
HALF = 50  # pixels on each side of the center

with h5py.File(fobj, "r") as f:
    g = f[base]

    proj = g["projection"]
    print("projection value:", proj[()])
    print("projection attributes:", dict(proj.attrs))

    x = g["xCoordinates"][:]
    y = g["yCoordinates"][:]
    dx = float(g["xCoordinateSpacing"][()])
    dy = float(g["yCoordinateSpacing"][()])
    print("x range:", x.min(), x.max(), "spacing:", dx)
    print("y range:", y.min(), y.max(), "spacing:", dy)

    epsg = int(proj[()])
    to_grid = Transformer.from_crs(4326, epsg, always_xy=True)
    px, py = to_grid.transform(POINT[0], POINT[1])
    print("Kalpetta in grid coordinates:", px, py)

    col = int(np.argmin(np.abs(x - px)))
    row = int(np.argmin(np.abs(y - py)))
    print("nearest pixel (row, col):", row, col)

    r0, r1 = max(row - HALF, 0), min(row + HALF, len(y))
    c0, c1 = max(col - HALF, 0), min(col + HALF, len(x))
    print("window rows", r0, r1, "cols", c0, c1)

    coh = g["coherenceMagnitude"][r0:r1, c0:c1]
    unw = g["unwrappedPhase"][r0:r1, c0:c1]
    cc = g["connectedComponents"][r0:r1, c0:c1]

def describe(label, a):
    a = a.astype("float64")
    print(label, "shape", a.shape,
          "| NaN:", int(np.isnan(a).sum()),
          "| zeros:", int((a == 0).sum()),
          "| min/mean/max:",
          np.nanmin(a), np.nanmean(a), np.nanmax(a))

describe("coherenceMagnitude", coh)
describe("unwrappedPhase", unw)
print("connectedComponents unique values:", np.unique(cc))

np.save("window_coh.npy", coh)
np.save("window_unw.npy", unw)
np.save("window_cc.npy", cc)