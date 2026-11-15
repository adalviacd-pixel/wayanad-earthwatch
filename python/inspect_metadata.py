import h5py
from nisar_common import open_gunw

name, fobj = open_gunw()
print("Product name:", name)


def show(value):
    if isinstance(value, bytes):
        return value.decode()
    return value


def walk(group, depth=0):
    for key in group:
        item = group[key]
        pad = "  " * depth
        if isinstance(item, h5py.Group):
            print(pad + key + "/")
            walk(item, depth + 1)
        elif isinstance(item, h5py.Dataset):
            print(pad + key, item.shape, item.dtype)


with h5py.File(fobj, "r") as f:
    print("\n--- identification (single values) ---")
    ident = f["science/LSAR/identification"]
    for key in ident:
        ds = ident[key]
        if ds.shape == ():
            value = show(ds[()])
            if key == "boundingPolygon":
                value = str(value)[:120] + "..."
            print(key, "=", value)

    print("\n--- temporalBaseline ---")
    print(f["science/LSAR/GUNW/metadata/orbit/temporalBaseline"][()])

    print("\n--- frequencyA contents ---")
    walk(f["science/LSAR/GUNW/grids/frequencyA"])