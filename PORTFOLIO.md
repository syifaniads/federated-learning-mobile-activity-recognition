# Portfolio Summary

## 30-second recruiter summary

**Federated Learning for Mobile Activity Recognition** is a collaborative distributed-systems project that trains a Human Activity Recognition classifier across multiple client VMs without centralizing their raw training partitions.

The system uses a Flask REST coordinator, local scikit-learn Logistic Regression training, weighted Federated Averaging, and the UCI HAR dataset. The project also evaluates Non-IID client data, Differential Privacy, convergence, communication cost, and partial client participation.

## Technical highlights

- 1 FL coordinator + 4 distributed client VMs
- Flask REST API for global-model and client-update exchange
- UCI HAR: 7,352 train / 2,947 test samples, 561 features, 6 activities
- Weighted FedAvg aggregation
- Global FL accuracy around 94.23% in the main report evaluation
- Centralized baseline around 95.52% in that comparison
- IID vs Non-IID analysis
- Gaussian Differential Privacy experiment
- Local-epoch and partial-participation analysis
- Confusion-matrix and convergence evaluation

## CV-ready version

> **Federated Learning for Mobile Activity Recognition** - Built and evaluated a multi-client federated-learning workflow for UCI HAR using Flask, scikit-learn, NumPy and FedAvg across distributed VMs. Analyzed IID vs Non-IID data, Differential Privacy, convergence and client-participation trade-offs; the reported global model reached ~94.2% accuracy while keeping raw client training partitions local.

## Short portfolio-card version

> Distributed Federated Learning system for smartphone activity recognition. Coordinated four client VMs through a Flask server, aggregated local Logistic Regression models with FedAvg, and evaluated Non-IID data, Differential Privacy and communication/convergence trade-offs.

## Interview talking points

A useful interview walkthrough is:

1. **Why FL?** - avoid collecting every client's raw training data centrally.
2. **What actually travels?** - model coefficients/intercepts and metadata, not the raw UCI HAR partition.
3. **Why FedAvg weighting?** - clients with more training samples should have proportionally more influence.
4. **What broke under Non-IID?** - client drift because different clients optimize against different local class distributions.
5. **What did DP teach?** - stronger noise can destroy utility if sensitivity/noise is not tuned carefully.
6. **What is the distributed-systems issue?** - synchronous rounds introduce quorum, straggler and stale-round problems.
7. **What would you change for production?** - authenticated TLS, secure aggregation, robust update validation, better client sampling, retries/idempotency, privacy accounting and real mobile-device benchmarking.

## Suggested portfolio tags

`Federated Learning` · `Distributed Systems` · `Python` · `Flask` · `scikit-learn` · `NumPy` · `Machine Learning` · `Differential Privacy` · `FedAvg` · `UCI HAR` · `Privacy Engineering`
