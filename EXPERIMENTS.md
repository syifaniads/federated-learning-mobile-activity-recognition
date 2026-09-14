# Experiments

This project evaluates more than a single FL training run. The coursework includes several experiments intended to expose practical trade-offs in federated optimization.

## Experiment matrix

| Experiment | Variable | Question |
|---|---|---|
| Main FL training | communication rounds | Can distributed clients converge to a competitive global model? |
| Centralized baseline | training architecture | How much utility is lost relative to centralized ML? |
| IID vs Non-IID | client label distribution | How does heterogeneous data affect convergence? |
| Differential Privacy | epsilon / Gaussian noise | How much accuracy is lost for stronger formal privacy? |
| Local epoch analysis | `E` | Is additional client-side computation worth the cost? |
| Partial participation | active-client fraction | Can communication be reduced while keeping training stable? |

## 1. Main FL run

The report documents a 10-round distributed run using 4 clients and local Logistic Regression training.

The per-round accuracy/loss table in the course discussion is:

| Round | Accuracy | Loss |
|---:|---:|---:|
| 1 | 90.06% | 0.3442 |
| 2 | 92.47% | 0.2051 |
| 3 | 93.71% | 0.1763 |
| 4 | 93.82% | 0.1642 |
| 5 | 93.85% | 0.1642 |
| 6 | 93.64% | 0.1638 |
| 7 | **94.01%** | 0.1593 |
| 8 | 93.76% | 0.1614 |
| 9 | 93.94% | **0.1518** |
| 10 | 93.90% | 0.1629 |

The report interprets the post-round-4 behavior as near-convergence with small oscillations rather than divergence.

## 2. Centralized comparison

A separate global evaluation records:

- federated accuracy: about **94.23%**;
- centralized baseline: about **95.52%**;
- accuracy gap: about **1.29 percentage points**.

The important engineering conclusion is not that FL is "better" than centralized ML, but that this experiment retained most of the baseline utility while avoiding central collection of the clients' raw training partitions.

## 3. IID vs Non-IID

Group 1's dedicated analysis uses `alpha=0.5` to create heterogeneous label distributions.

Results from that source analysis:

| Metric | IID | Non-IID |
|---|---:|---:|
| Round 1 | 94.10% | 88.77% |
| Round 5 | 94.60% | 92.60% |
| Round 10 | 94.71% | 93.21% |
| Round 15 | **94.71%** | **93.45%** |
| Mean EMD | 0.0094 | 0.3116 |

This exposes client drift: local objectives become less aligned when clients observe different class distributions.

## 4. Differential Privacy

The report and original challenge artifacts contain multiple DP experiment runs with different reported utility values. They consistently show the same qualitative behavior:

- smaller epsilon -> larger Gaussian noise;
- larger noise -> lower classification utility;
- no-DP baseline -> highest utility.

Because the raw course artifacts contain results from multiple runs, this portfolio avoids collapsing them into a single fabricated canonical number. See [PRIVACY.md](./PRIVACY.md) for the exact source distinction.

## 5. Local epochs

The Group 1 convergence analysis varies:

```text
E = {1, 5, 10, 20, 50}
```

It reports `E=1` as the most efficient configuration in that run because larger local-epoch counts increase compute time without improving final accuracy.

## 6. Partial participation

The same analysis varies:

```text
fraction = {0.25, 0.50, 0.75, 1.00}
```

The source analysis selects `fraction=0.75` (3 of 4 clients) as the smallest stable participation level in that experiment, balancing model stability and communication.

## 7. Communication observation

The course discussion reports roughly **34 seconds** total for 10 rounds in one 4-client local-network run and notes that stopping earlier around the near-converged region could reduce repeated parameter exchange.

This is an experiment-specific result, not a general FL performance claim.

## Reproducibility caveat

Different report sections and challenge outputs correspond to different experimental runs/configurations. Small metric differences should therefore be expected. This repository preserves those distinctions rather than presenting every value as if it came from one identical execution.
