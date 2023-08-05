# how-to

1. Push to Dockerhub,

```bash
docker build -t mesoliticadev/translation-api:main .
docker run -p 8080:8080 mesoliticadev/translation-api:main
docker push mesoliticadev/translation-api:main
```