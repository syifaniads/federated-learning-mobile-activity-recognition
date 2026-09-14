# Results

## Main global evaluation

The final course report records a global evaluation against the complete UCI HAR test split (`n=2,947`):

| Metric | Value |
|---|---:|
| Accuracy | **0.942314** |
| F1 macro | **0.942374** |
| F1 weighted | **0.942420** |
| Log loss | **0.152159** |
| Test samples | **2,947** |

![Global evaluation](./evidence/global-evaluation.png)

The confusion matrix shows strong performance across all six activity classes. The most visible confusion occurs between the closely related static classes **SITTING** and **STANDING**, which is a plausible difficulty for sensor-based activity recognition.

## Centralized baseline

The report compares the FL global model with a centralized model trained over centrally available training data.

One documented comparison reports approximately:

```text
Federated Learning : 94.23%
Centralized ML      : 95.52%
Difference          : -1.29 percentage points
```

This result should be interpreted as an experiment-specific comparison, not as a universal guarantee that FL always matches centralized training.

## Training behavior

A 10-round discussion table records accuracy improving rapidly in the early rounds:

```text
Round 1  : 90.06%
Round 2  : 92.47%
Round 3  : 93.71%
Round 4  : 93.82%
Round 7  : 94.01%  <- highest value in this table
Round 10 : 93.90%
```

Loss falls sharply from `0.3442` at Round 1 to the `~0.15-0.16` range later in training.

The report therefore characterizes the later behavior as small oscillation around a converged region rather than continuing large gains every round.

## IID / Non-IID experimental result

The original Group 1 challenge analysis reports the following separate experiment:

| Metric | IID | Non-IID (`alpha=0.5`) |
|---|---:|---:|
| Round 1 | 94.10% | 88.77% |
| Round 5 | 94.60% | 92.60% |
| Round 10 | 94.71% | 93.21% |
| Round 15 | **94.71%** | **93.45%** |
| Mean EMD | 0.0094 | 0.3116 |

![IID vs Non-IID](./evidence/iid-vs-noniid.png)

The lower and slower Non-IID trajectory is consistent with local client distributions pulling the optimization in different directions.

## Communication / convergence result

The original Group 1 Challenge 4 analysis reports:

### Local epochs

| Local epochs (`E`) | Final accuracy | Total time |
|---:|---:|---:|
| 1 | **0.9433** | **0.40 s** |
| 5 | 0.9406 | 1.98 s |
| 10 | 0.9389 | 3.38 s |
| 20 | 0.9376 | 6.30 s |
| 50 | 0.9342 | 15.68 s |

For that run, increasing local work did not improve final accuracy and increased compute time substantially.

### Partial participation

| Fraction | Active clients | Final accuracy | Last-5-round variance |
|---:|---:|---:|---:|
| 0.25 | 1 | 0.9189 | 0.00005446 |
| 0.50 | 2 | 0.9403 | 0.00000952 |
| 0.75 | 3 | **0.9406** | **0.00000026** |
| 1.00 | 4 | 0.9389 | 0.00000085 |

The source analysis selects `fraction=0.75` as the minimum stable fraction in that experiment.

![Convergence and partial participation](./evidence/convergence-participation.png)

## Reproducibility note

The class report, challenge scripts, and challenge analyses contain results from several separate runs. That is why some reported accuracy values differ slightly across sections. This portfolio preserves the run context instead of pretending every number came from one execution.
