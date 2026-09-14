# Visual Evidence

The public portfolio uses **sanitized SVG reconstructions from reported metrics** instead of raw lab screenshots. This keeps the evidence readable while avoiding course-lab infrastructure identifiers.

## Included

- `global-evaluation.svg` - global FL metrics, confusion matrix, and round-level accuracy trend reconstructed from the final report.
- `iid-vs-noniid.svg` - IID vs Non-IID accuracy and EMD summary reconstructed from the Group 1 analysis.
- `privacy-utility.svg` - privacy-budget vs utility values from the final report's Differential Privacy discussion.
- `convergence-participation.svg` - local-epoch and partial-client-participation values from the Group 1 Challenge 4 analysis.

## Evidence rule

These visualizations are **not newly generated benchmark results**. They summarize values already recorded in the original report / challenge analyses.

When separate source artifacts report different experimental runs, the portfolio keeps those contexts separate rather than silently reconciling them.

## Why the full report is not mirrored

Some raw report pages contain course-lab IP addresses and infrastructure identifiers. The portfolio therefore preserves only the non-sensitive information needed to substantiate engineering claims.

See [`../SOURCE_EVIDENCE.md`](../SOURCE_EVIDENCE.md) for original repositories and provenance.
