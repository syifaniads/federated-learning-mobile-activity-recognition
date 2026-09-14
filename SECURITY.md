# Security and Privacy Policy

This is a public portfolio repository for an academic Federated Learning experiment.

## Do not commit

- course-lab IP addresses unless already intentionally public and still necessary;
- SSH keys or private keys;
- passwords / tokens / API keys;
- private VM configuration;
- real user sensor datasets;
- student identity records that are not necessary for portfolio evidence;
- raw logs containing credentials or internal infrastructure identifiers.

## Dataset scope

The project uses the public UCI HAR research dataset. The privacy discussion in this repository should not be interpreted as permission to use real personal sensor data without consent and an appropriate governance model.

## Federated Learning security note

Federated Learning keeps raw samples local but does not automatically protect model updates. Production systems should consider authenticated encrypted transport, secure aggregation, update validation, privacy accounting, model-poisoning defenses, and strict access control.

## Differential Privacy note

The Differential Privacy work documented here is an academic experiment. It is not a claim of formal production privacy certification.
