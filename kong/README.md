# how-to

1. Generate Helm template,

```bash
helm repo add kong https://charts.konghq.com
helm template kong kong/kong \
--values values.yaml \
--include-crds > kong.yaml
```