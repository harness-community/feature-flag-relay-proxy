# kubernetes deployment example

![image](https://github.com/harness-community/feature-flag-relay-proxy/assets/7338312/0030e8b6-6c6a-4974-8b8e-5ab75c2d6775)

## feature-flag-relay-proxy.yaml

deploy the relay proxy to kubernetes using this manifest

there is an example `values.yaml` included

## redis

in production deployments, redis should be used as a shared cache

deploy redis based on your internal standards

## service.yaml

an example harness service yaml for deploying the relay proxy
