# proll-service

Sistema para avaliação de higienização hospitalar.

Aplicação disponível em [https://proll-service.herokuapp.com/](https://proll-service.herokuapp.com/)

[![Build Status](https://travis-ci.org/diegosorrilha/jornada-empreendedor-diagnostico.svg?branch=master)](https://travis-ci.org/diegosorrilha/jornada-empreendedor-diagnostico)
[![codecov](https://codecov.io/gh/diegosorrilha/jornada-empreendedor-diagnostico/branch/master/graph/badge.svg)](https://codecov.io/gh/diegosorrilha/jornada-empreendedor-diagnostico)




Setup
=========

### PROD

#### Setup
```bash
# Criar app com nome e remote
heroku create proll-service-app --remote prod
```

```bash
# Setar variáveis de ambiente
heroku config:set SECRET_KEY=segredo DEBUG=False ALLOWED_HOSTS='proll-service-app.herokuapp.com' DISABLE_COLLECTSTATIC=1 --remote prod
```


#### Deploy
```bash
git push prod master
```

### Disponível em 

[https://proll-service-app.herokuapp.com/](https://proll-service-app.herokuapp.com/)

-------

### HOMOLOG

#### Setup
```bash
# Criar app com nome e remote
heroku create proll-service-app-homolog --remote homolog
```

```bash
# Setar variáveis de ambiente
heroku config:set SECRET_KEY=segredo DEBUG=True ALLOWED_HOSTS='proll-service-app-homolog.herokuapp.com' DISABLE_COLLECTSTATIC=1 --remote homolog
```


#### Deploy
```bash
git push homolog master
```

#### Disponível em
[https://proll-service-app-homolog.herokuapp.com/](https://proll-service-app-homolog.herokuapp.com/)

-------

### DEV

#### Setup
```bash
# Criar app com nome e remote
heroku create proll-service-app-staging --remote staging
```

```bash
# Setar variáveis de ambiente
heroku config:set SECRET_KEY=segredo DEBUG=True ALLOWED_HOSTS='proll-service-app-staging.herokuapp.com' DISABLE_COLLECTSTATIC=1 --remote staging
```

```bash
# Criar .env basico
cp contrib/env-sample .env
```

```bash
#Rodar o projeto
make dev
```

#### Deploy
```bash
# Criar app com nome e remote
git push staging master
```

#### Disponível em
[https://proll-service-app-staging.herokuapp.com/](https://proll-service-app-staging.herokuapp.com/)
