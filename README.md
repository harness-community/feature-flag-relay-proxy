# feature-flag-relay-proxy

resources for deploying the relay proxy for harness feature flags

# what is included

`docker` resources for deploying the proxy with docker

`kubernetes` resources for deploying the proxy with kubernetes

`test` helpful scripts for testing the proxy

# general guidance

the three things you will need to deploy the relay proxy:
- a harness api key with project viewer for the projects in which the proxy will cover
  - a single relay proxy instance can cover any combination of projects under a single organization
- server sdk keys for each environment you want the proxy to allow connections for

# further documentation

[Read more docs from the relay proxy source repository](https://github.com/harness/ff-proxy/blob/main/docs/configuration.md)
