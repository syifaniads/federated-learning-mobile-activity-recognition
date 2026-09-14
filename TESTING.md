# Testing and Validation

## FedAvg unit-style validation

The original Group 1 repository includes `challenges/challenge_1/test_fedavg.py` and the course report records all listed test scenarios as passing.

The validation covers the core aggregation properties:

- balanced weighting;
- unequal weighting;
- aggregation over multiple clients;
- output shape consistency;
- single-client behavior;
- invalid / edge input handling.

These tests are especially important because NumPy broadcasting can otherwise hide parameter-shape mistakes.

## Integration validation

The system was also validated as a distributed workflow:

1. server started and exposed its REST API;
2. clients connected to the coordinator;
3. clients loaded their assigned local partition;
4. clients received global parameters;
5. local training completed;
6. client updates were submitted to the server;
7. the server waited for the configured client set;
8. FedAvg generated a new global model;
9. multiple rounds completed;
10. the final global model was evaluated over the global test set.

## Evaluation validation

The project uses several complementary checks:

- Accuracy
- F1 macro
- F1 weighted
- Precision / Recall in classification output
- Log loss
- Confusion matrix
- Accuracy over communication rounds
- Loss over communication rounds
- Centralized ML baseline comparison

## Experiment-level validation

Separate challenge experiments validate different properties:

| Experiment | Validation target |
|---|---|
| IID vs Non-IID | impact of heterogeneous client data |
| Differential Privacy | privacy-utility trade-off under Gaussian noise |
| Local epochs | compute vs convergence |
| Partial participation | communication reduction vs stability |

## What was not validated

The available project evidence does not establish production-grade testing for:

- adversarial clients;
- model poisoning;
- secure aggregation;
- TLS / mutual authentication;
- large-scale client churn;
- network partitions;
- asynchronous update ordering;
- long-duration fault recovery;
- real mobile-device battery / bandwidth constraints.

Those gaps are explicitly retained in [LIMITATIONS.md](./LIMITATIONS.md).
