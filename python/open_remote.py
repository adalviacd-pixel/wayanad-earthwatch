import earthaccess
import h5py

earthaccess.login()

results = earthaccess.search_data(
    short_name="NISAR_L2_GUNW_PROVISIONAL_V1",
    point=(76.2571, 11.6629),
    temporal=("2026-10-08", "2026-10-21"),
)
print("Granules found:", len(results))

names = [r["umm"]["GranuleUR"] for r in results]
for n in names:
    print(" ", n)

# Pick the Track 113, Frame 7 pair that ends on 20 Oct 2026
wanted = [i for i, n in enumerate(names)
          if "_113_A_007_" in n and "20261020T003232" in n]
if not wanted:
    print("That pair was not among the results. Stopping.")
    raise SystemExit

i = wanted[0]
print("Opening:", names[i])
files = earthaccess.open([results[i]])
print("Opened file object:", files[0])


def walk(group, depth=0, max_depth=5):
    for key in group:
        item = group[key]
        pad = "  " * depth
        if isinstance(item, h5py.Group):
            print(pad + key + "/")
            if depth < max_depth:
                walk(item, depth + 1, max_depth)
        elif isinstance(item, h5py.Dataset):
            print(pad + key, item.shape, item.dtype)
        else:
            print(pad + key, "(other HDF5 object:", type(item).__name__ + ")")


with h5py.File(files[0], "r") as f:
    print("Top-level keys:", list(f.keys()))
    walk(f)
    print("Finished walking the file.")