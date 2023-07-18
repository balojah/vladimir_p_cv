[![Coverage Status](https://coveralls.io/repos/github/balojah/vladimir_p_cv/badge.svg?branch=main&kill_cache=1)](https://coveralls.io/github/balojah/vladimir_p_cv?branch=main)
![example workflow](https://github.com/balojah/vladimir_p_cv/actions/workflows/ci-example.yml/badge.svg)
# balojah.pp.ua

My personal website and online CV: [balojah.pp.ua](https://balojah.pp.ua)

## Description

The simplest django application. Uses [jwilder/docker-letsencrypt-nginx-proxy-companion
](https://github.com/jwilder/docker-letsencrypt-nginx-proxy-companion) for creation/renewal of Let's Encrypt 
certificates automatically.

## Build Setup

``` bash
# run localy for develop 
# fill in .env.file with your credentials 
$ docker compose up -d --build

# run in production with letsencrypt
# rename .env.prod.sample .env.letsencrypt.sample .env.proxy.samle
# fill in env.prod .env.letsencrypt .env.proxy with your credentials
$ mv .env.prod.sample .env.prod && mv .env.letsencrypt.sample .env.letsencrypt && mv .env.proxy.samle .env.proxy
$ docker compose -f docker-compose.prod.yml up -d --build
```

## Disclaimer

All my repositories remain private due to non-disclosure agreement with my clients.
