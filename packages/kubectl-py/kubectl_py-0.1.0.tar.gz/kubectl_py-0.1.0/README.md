# kubectl-py

A python wrapper to provide a pip-installable [kubectl] binary.

Internally this package provides a convenient way to download the pre-built
kubectl binary for your particular platform.

### installation

```bash
pip install kubectl-py
```

### usage

After installation, the `kubectl` binary should be available in your
environment.

### As a pre-commit hook

See [pre-commit] for instructions

Sample `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/harryvince/kubectl-py
  rev: v0.1.0
  hooks:
    - id: kustomize
      args: [overlays/env]
```

[kubectl]: https://kubernetes.io/docs/reference/kubectl/
[pre-commit]: https://pre-commit.com

[inspired by](https://github.com/shellcheck-py/shellcheck-py)
