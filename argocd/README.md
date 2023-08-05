# how-to

1. Access kubernetes,

```bash
aws eks update-kubeconfig --region ap-southeast-1 --name test
```

2. Deploy ArgoCD,

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

3. Proxy UI to localhost,

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443 --address "0.0.0.0"
```

4. Get login credential,

```bash
kubectl get secret/argocd-initial-admin-secret -n argocd -o yaml
```