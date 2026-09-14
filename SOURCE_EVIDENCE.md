# Source Evidence

This portfolio remains traceable to the original collaborative coursework instead of replacing its source history.

## Final course report

The primary report used to reconstruct the portfolio is:

**Federated Learning pada Mobile Activity Recognition - Sistem Komputasi Terdistribusi B - 2026**

The report documents:

- server/client setup;
- UCI HAR dataset preparation;
- local model training;
- REST communication;
- weighted FedAvg;
- global evaluation;
- centralized comparison;
- IID vs Non-IID experiments;
- Differential Privacy;
- convergence and communication experiments.

The raw report is not mirrored into this public repository because some pages contain course-lab infrastructure addresses.

## Original Group 1 implementation

https://github.com/AmosJuang/FL-Mobile-Kelompok-1-

Important paths:

- `server/app.py` - FL coordinator / REST API
- `client/client.py` - local training client
- `data/download_data.py` - UCI HAR acquisition
- `data/partition_data.py` - client data partitioning
- `evaluation/evaluate_global.py` - global evaluation / centralized comparison
- `challenges/challenge_1/` - FedAvg
- `challenges/challenge_2/` - IID vs Non-IID
- `challenges/challenge_3/` - Differential Privacy
- `challenges/challenge_4/` - convergence / communication

The original Group 1 README describes a 1-server + 4-client VM architecture, 561-feature UCI HAR input, and the HTTP model-update lifecycle.

## Group 1 analysis evidence

### IID vs Non-IID

https://github.com/AmosJuang/FL-Mobile-Kelompok-1-/blob/main/challenges/challenge_2/analisis.md

This source reports the `alpha=0.5` Non-IID experiment, EMD values, client drift analysis, and the final IID/Non-IID accuracy comparison used in this portfolio.

### Differential Privacy

https://github.com/AmosJuang/FL-Mobile-Kelompok-1-/blob/main/challenges/challenge_3/analisis.md

This source records a separate DP run. Its exact accuracy values differ from the consolidated class report, so the portfolio keeps the two contexts separate.

### Convergence and communication

https://github.com/AmosJuang/FL-Mobile-Kelompok-1-/blob/main/challenges/challenge_4/analisis.md

This source records local-epoch timing, partial client participation, variance, and communication estimates.

## Other class implementation repositories

The appendix of the final report links:

- Group 2: https://github.com/Kyouun7/SKT_Challenge
- Group 3: https://github.com/sandhika-rizq/FL-Mobile-Kelompok-3/tree/main/challenges
- Group 4: https://github.com/SakaGintoki/FL-Mobile-Kelompok-4/tree/main/challenges

## Sanitized evidence in this repository

Instead of copying raw report screenshots, the public portfolio reconstructs selected figures from the **reported values**:

- [`evidence/global-evaluation.svg`](./evidence/global-evaluation.svg)
- [`evidence/iid-vs-noniid.svg`](./evidence/iid-vs-noniid.svg)
- [`evidence/privacy-utility.svg`](./evidence/privacy-utility.svg)
- [`evidence/convergence-participation.svg`](./evidence/convergence-participation.svg)

These SVGs are explanatory visualizations of existing coursework results. They are **not newly generated benchmark results** and intentionally omit lab IPs / infrastructure identifiers.

## Evidence integrity rule

This portfolio follows a simple rule:

> If an exact metric differs between report sections or experiment runs, keep the run context instead of silently reconciling the numbers.

This is why the main global evaluation, IID/Non-IID challenge, and Differential Privacy challenge can contain different final accuracy values.
