# Privacy Analysis

## Federated Learning is not the same as guaranteed privacy

The core system keeps raw UCI HAR training partitions on their respective client VMs and exchanges model parameters instead of raw samples. This reduces the need to centralize training data, but **parameter updates can still leak information**.

Threats that matter in real FL deployments include:

- model / gradient inversion;
- membership inference;
- malicious-client poisoning;
- honest-but-curious coordinators;
- update interception if transport is not protected.

## Differential Privacy exercise

The coursework includes a Gaussian-mechanism Differential Privacy experiment.

A representative calculation in the report uses:

```text
epsilon = 1.0
delta   = 1e-5
sigma   = 4.844805
```

The experiment perturbs local model parameters before aggregation. Stronger privacy (smaller epsilon) requires more noise and therefore degrades utility more aggressively.

## Source-result distinction

The final class report records one privacy-utility sweep approximately as:

| Epsilon | Reported accuracy |
|---:|---:|
| 0.1 | 10.99% |
| 0.5 | 11.27% |
| 1.0 | 11.94% |
| 5.0 | 15.03% |
| 10.0 | 21.11% |
| No DP | 94.50% |

The original Group 1 challenge analysis contains a different run with another set of final values (for example, epsilon `10.0` is reported at `0.2823`). Both sources tell the same qualitative story, but they are **not identical experimental outputs**.

This portfolio therefore does not silently merge them. When quoting a number, use the source context.

## Interpretation

For this specific high-dimensional HAR setup, strict Gaussian perturbation is very destructive to the Logistic Regression parameters. The experiment demonstrates why production privacy engineering requires tuning and often additional mechanisms such as:

- clipping update sensitivity before adding noise;
- per-client privacy accounting;
- secure aggregation;
- better task/model calibration;
- larger datasets or stronger regularization;
- privacy accountants across repeated rounds.

These are production recommendations, not claims that they were implemented in the coursework.

## Privacy-utility evidence

![Privacy utility trade-off](./evidence/privacy-utility.png)

## What the experiment does establish

It establishes that the team:

1. understood that local data retention alone does not eliminate leakage risk;
2. implemented / evaluated Gaussian noise as a privacy mechanism;
3. measured the resulting utility loss;
4. discussed the privacy-accuracy-communication trade-off.

## What it does not establish

The project should **not** be described as:

- formally privacy-certified;
- production-ready DP-FL;
- resistant to every inference attack;
- using secure aggregation;
- providing cryptographic confidentiality of model updates.

Those would require additional design, threat modeling, and verification.
