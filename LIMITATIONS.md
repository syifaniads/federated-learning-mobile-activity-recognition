# Limitations and Non-Claims

This repository is intentionally conservative about what the coursework proves.

## 1. Coursework-scale topology

The implemented topology is small: one coordinator and four client VMs. It demonstrates FL mechanics and distributed coordination, but it does not establish behavior at hundreds or millions of clients.

## 2. VM clients are not real mobile devices

The project models mobile activity data, but training runs on VMs rather than resource-constrained smartphones. Therefore it does not measure:

- battery drain;
- cellular bandwidth;
- thermal constraints;
- intermittent connectivity;
- OS background-execution limits.

## 3. Privacy is not guaranteed by FL alone

Raw data remains local, but model updates can still leak information. The Differential Privacy challenge is an experiment, not a certified privacy implementation.

The project does not establish:

- secure aggregation;
- cryptographic confidentiality of updates;
- formal end-to-end privacy accounting across all rounds;
- resistance to every model inversion / membership inference technique.

## 4. Central coordinator remains a trust / availability point

The server coordinates rounds and aggregation. The coursework does not implement distributed coordinator failover.

## 5. Synchronous coordination

The implementation waits for a configured set of client updates. This makes the system easy to reason about but vulnerable to slow / unavailable clients.

Production alternatives could include timeouts, partial quorum, asynchronous FL, or adaptive client selection.

## 6. Security controls are not production-grade

The public evidence does not establish TLS, mutual authentication, signed updates, anti-replay protection, update attestation, or Byzantine-robust aggregation.

## 7. Multiple experimental runs

The final report and individual challenge analyses contain values from several runs/configurations. Some accuracy values therefore differ across artifacts.

This portfolio preserves run context rather than creating a fake single canonical experiment.

## 8. Dataset scope

UCI HAR is a controlled public research dataset. Real-world activity recognition can differ because of device diversity, sensor calibration, user demographics, missing data, and distribution shift.

## 9. Differential Privacy utility

The Gaussian-noise settings used in the challenge produce severe accuracy loss under strict epsilon values. This demonstrates the privacy-utility tension; it should not be read as evidence that those exact parameters are optimal for deployment.

## 10. Attribution

The class report covers multiple groups and the original implementation is collaborative. This personal repository is a portfolio presentation, not a claim of sole authorship.
