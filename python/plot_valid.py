import numpy as np
import matplotlib.pyplot as plt
from maskdecode import decode_mask

coh = np.load("window_coh.npy")
unw = np.load("window_unw.npy")
d = decode_mask(np.load("window_mask.npy"))
valid = d["valid"]
iono = d["iono_interp"].astype(bool)

print("valid pixels:", int(valid.sum()), "of", valid.size)
print("zero phase inside valid:", int(((unw == 0) & valid).sum()))
print("zero phase outside valid:", int(((unw == 0) & ~valid).sum()))
print("nonzero phase outside valid:", int(((unw != 0) & ~valid).sum()))
print("water pixels:", int((d["water"] > 0).sum()))
print("anomaly bits set:", int(((d["ref_anom"] > 0) | (d["sec_anom"] > 0)).sum()))
print("ionosphere-interpolated, all:", int(iono.sum()),
      "| inside valid:", int((iono & valid).sum()))
print("coherence mean, valid:", float(coh[valid].mean()))
print("phase std, valid (rad):", float(unw[valid].std()))

phase = np.ma.masked_where(~valid, unw)
phase = phase - np.ma.median(phase)

fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))
a = ax[0].imshow(np.ma.masked_where(~valid, coh), vmin=0, vmax=1, cmap="gray")
ax[0].set_title("Coherence, valid pixels only")
b = ax[1].imshow(iono & valid, cmap="Oranges", interpolation="nearest")
ax[1].set_title("Ionosphere-interpolated flag (valid pixels)")
c = ax[2].imshow(phase, cmap="RdBu_r")
ax[2].set_title("Unwrapped phase minus median (rad), valid only")
for axis, im in zip(ax, (a, b, c)):
    fig.colorbar(im, ax=axis, shrink=0.8)
fig.suptitle("NISAR GUNW T113 F7, 2026-10-08 to 2026-10-20, PROVISIONAL")
fig.tight_layout()
fig.savefig("window_valid.png", dpi=150)
print("saved window_valid.png")