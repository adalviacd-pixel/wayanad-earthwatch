import numpy as np
import matplotlib.pyplot as plt

coh = np.load("window_coh.npy")
unw = np.load("window_unw.npy")
cc = np.load("window_cc.npy")

valid = cc > 0
print("pixels with connected component > 0:", int(valid.sum()), "of", cc.size)
print("zero phase AND cc == 0:", int(((unw == 0) & ~valid).sum()))
print("zero phase BUT cc > 0:", int(((unw == 0) & valid).sum()))
print("coherence, valid pixels: mean", float(coh[valid].mean()))
print("coherence, cc == 0 pixels: mean", float(coh[~valid].mean()))

unw_m = np.ma.masked_where(~valid, unw)
rel = unw_m - np.ma.median(unw_m)

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
im0 = axes[0].imshow(coh, vmin=0, vmax=1, cmap="gray")
axes[0].set_title("Coherence magnitude (0 to 1)")
im1 = axes[1].imshow(cc, cmap="viridis", interpolation="nearest")
axes[1].set_title("Connected components")
im2 = axes[2].imshow(rel, cmap="RdBu_r")
axes[2].set_title("Unwrapped phase minus median (radians)\nvalid pixels only")
for ax, im in zip(axes, (im0, im1, im2)):
    ax.set_xlabel("column (80 m pixels)")
    ax.set_ylabel("row (80 m pixels)")
    fig.colorbar(im, ax=ax, shrink=0.8)
fig.suptitle("NISAR GUNW T113 F7, 2026-10-08 to 2026-10-20, PROVISIONAL, window near Kalpetta")
fig.tight_layout()
fig.savefig("window_preview.png", dpi=150)
print("saved window_preview.png")