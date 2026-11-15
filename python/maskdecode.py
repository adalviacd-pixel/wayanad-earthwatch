import numpy as np


def decode_mask(mask):
    m = mask.astype("uint32")
    low = m & 0xFF
    return {
        "water": low // 100,
        "ref_sub": (low // 10) % 10,
        "sec_sub": low % 10,
        "iono_interp": (m >> 24) & 1,
        "sec_anom": (m >> 8) & 0xFF,
        "ref_anom": (m >> 16) & 0xFF,
        "valid": ((low // 10) % 10 > 0) & (low % 10 > 0),
    }