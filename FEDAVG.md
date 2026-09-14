# Federated Averaging (FedAvg)

## Goal

Federated Averaging combines model parameters trained independently by multiple clients into one global model.

For client `k` with `n_k` local samples:

```text
weight_k = n_k / sum(n_i)
```

The global parameter tensor is then:

```text
parameter_global = sum(weight_k * parameter_k)
```

The same weighting rule is applied separately to the Logistic Regression coefficient matrix and intercept vector.

## Why weighted averaging matters

A simple arithmetic mean treats every client as equally informative even when their local dataset sizes differ. FedAvg instead gives more influence to clients that trained on more samples.

A project validation scenario used the following client contribution weights:

| Client | Relative FedAvg weight |
|---|---:|
| Client 1 | 0.2264 |
| Client 2 | 0.3396 |
| Client 3 | 0.1698 |
| Client 4 | 0.2641 |

Client 2 therefore contributes the largest fraction in that test because it has the largest local sample count, while Client 3 contributes the smallest.

## Balanced-data sanity check

When every client contains the same number of samples:

```text
n_1 = n_2 = ... = n_K
```

each FedAvg weight becomes:

```text
1 / K
```

and weighted FedAvg becomes equivalent to a simple average. This is a useful correctness test for the implementation.

## Shape correctness

For the HAR classifier, aggregation must preserve model parameter shapes:

```text
coef      -> 2-D matrix: classes x features
intercept -> 1-D vector: classes
```

A valid aggregator should reject malformed input rather than silently broadcasting incompatible arrays.

## Validation performed in the original project

The source repository includes a dedicated `test_fedavg.py`. The course report records PASS results for scenarios including:

- balanced client weighting;
- unequal client weighting;
- multiple clients;
- shape consistency;
- single-client behavior;
- invalid / edge input handling.

## Portfolio reference implementation

A minimal, clean reference implementation is available at [`examples/fedavg_reference.py`](./examples/fedavg_reference.py). It is included to communicate the algorithm clearly; the original collaborative implementation remains linked in [SOURCE_EVIDENCE.md](./SOURCE_EVIDENCE.md).

## Important limitation

FedAvg is a coordination algorithm, not a security boundary. A server that receives raw model updates may still learn information about client data, and malicious clients can attempt model poisoning. Differential Privacy, secure aggregation, update clipping, robust aggregation, and authenticated transport are separate concerns.
