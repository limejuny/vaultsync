Installation

* `argocd app create vaultsync --repo https://github.com/limejuny/vaultsync.git --path helm --dest-namespace vaultwarden --dest-server https://kubernetes.default.svc --values values.yaml --values secrets+gpg-import:///helm-secrets-private-keys/key.asc?secrets.yaml`
