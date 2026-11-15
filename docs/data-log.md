| GUNW | 2025-11-18 to 2025-11-30 | 12 d | 113 | 7 | Ascending | PR | X05010 | Experimental (pre-calibration), not for mixing with P05023 |
| GUNW | 2025-11-18 to 2025-12-24 | 36 d | 113 | 7 | Ascending | PR | X05010 | Experimental (pre-calibration), not for mixing with P05023 |
| GUNW | 2025-12-24 to 2026-01-05 | 12 d | 113 | 7 | Ascending | PR | X05010 | Experimental (pre-calibration), not for mixing with P05023 |
| GUNW | 2025-11-18 to 2025-12-24 | 36 d | 113 | 7 | Ascending | PR | not read | not checked |
| GUNW | 2025-12-24 to 2026-01-05 | 12 d | 113 | 7 | Ascending | PR | not read | not checked |
| GUNW | 2026-06-22 to 2026-07-04 | 12 d | 113 | 7 | Ascending | PR | P05023 | Provisional (Oct pair verified) |
| GUNW | 2026-07-04 to 2026-08-21 | 48 d | 113 | 7 | Ascending | PR | P05023 | not checked |
| GUNW | 2026-08-21 to 2026-09-02 | 12 d | 113 | 7 | Ascending | PR | P05023 | not checked |
| GUNW | 2026-09-02 to 2026-09-14 | 12 d | 113 | 7 | Ascending | PR | P05023 | not checked |
| GUNW | 2026-09-14 to 2026-09-26 | 12 d | 113 | 7 | Ascending | PR | P05023 | not checked |
| GUNW | 2026-09-26 to 2026-10-08 | 12 d | 113 | 7 | Ascending | PR | P05023 | not checked |
| GUNW | 2026-10-08 to 2026-10-20 | 12 d | 113 | 7 | Ascending | PR | P05023 | Provisional |

Coverage: all ten footprints share one outline. Reaches about 76.4 E; the area east of that is not covered. Whole-district coverage still to be checked against the real district boundary.
## Known limitations that apply to this project

Source: NISAR Data User Guide, "Provisional Product Known Issues" (updated 30 July 2026).

- PROVISIONAL (CRID P05023) products are validated only at a limited set of sites; Wayanad's status as a validation site is not confirmed.
- BETA products (CRID X05010, Oct 2025 to Jan 2026) are pre-calibration and are kept separate from PROVISIONAL products.
- About 1 to 2% of products come from incomplete raw data, which can cause decorrelation or misplaced products in InSAR. Check quality flags before interpreting any feature.
- Ionospheric residuals are documented mainly for high latitudes; their effect at Wayanad's latitude is not established here. The GUNW ionospheric phase screen is included but not applied by default.
## Verified product: GUNW Track 113 Frame 7, 2026-10-08 to 2026-10-20

Read directly from the file's own metadata (not the filename):
- Track 113, frame 7, ascending, left-looking, L-band, polarization HH
- Reference 2026-10-08 00:32:32 UTC, secondary 2026-10-20 00:32:32 UTC, temporal baseline 12 days
- Composite release ID P05023, product version 1.0.11, specification 1.5.0
- DOI 10.5067/NIL2GUNW-P1, processed 2026-10-22
- Input data exception flags: reference 0, secondary 0 (meaning to be confirmed in the product specification)
- Unwrapped grid 4149 x 4230; wrapped grid 16596 x 16920
## Observation: zero-valued unwrapped phase near Kalpetta (explained)

In a 100 x 100 pixel window near Kalpetta (2026-10-08 to 2026-10-20 GUNW), 3,374 of 10,000 pixels have
unwrapped phase of exactly 0. The file's own `mask` description marks these as invalid samples in the
reference and/or secondary image. connectedComponents does not flag them, so it is not used as a validity test.
About 70% of the window carries the mask bit for ionosphere-interpolated pixels; the effect on
unwrapped phase is not established.