import h5py
import numpy as np
from nisar_common import open_gunw

R0, R1, C0, C1 = 903, 1003, 3349, 3449   # same window as before

name, fobj = open_gunw()
base = "science/LSAR/GUNW/grids/frequencyA/unwrappedInterferogram"


def text(v):
    return v.decode() if isinstance(v, bytes) else str(v)


with h5py.File(fobj, "r") as f:
    g = f[base]
    print("--- layer descriptions stored in the file ---")
    for path in ["HH/unwrappedPhase", "HH/coherenceMagnitude",
                 "HH/connectedComponents", "mask"]:
        print(path)
        for k, v in g[path].attrs.items():
            print("   ", k, ":", text(v))

    mask = g["mask"][R0:R1, C0:C1]
    unw = g["HH/unwrappedPhase"][R0:R1, C0:C1]

print("\n--- mask values in this window ---")
vals, counts = np.unique(mask, return_counts=True)
for v, c in zip(vals, counts):
    print("mask =", v, ":", c, "pixels")

zero = unw == 0
print("\n--- zero phase versus mask ---")
for v in vals:
    sel = mask == v
    print("mask =", v, "| pixels:", int(sel.sum()),
          "| of which zero phase:", int((zero & sel).sum()))

np.save("window_mask.npy", mask)