# test

## stream_flag_value.py

monitor the value of a flag value

`RELAY_PROXY_ADDRESS` address of your local relay proxy

`FF_SDK_KEY` feature flag sdk key

`FF_IDENTIFIER` flag to resolve

## toggle_flag_validate.py

test the flag value coming back from the proxy by toggling a flag and testing the value

`RELAY_PROXY_ADDRESS` address of your local relay proxy

`FF_SDK_KEY` feature flag sdk key

`FF_IDENTIFIER` flag to resolve

`HARNESS_ACCOUNT_ID` harness account id

`HARNESS_ORGANIZATION_ID` harness organization id

`HARNESS_PROJECT_ID` harness project id

`HARNESS_ENVIRONMENT_ID` harness environment id

`HARNESS_PLATFORM_API_KEY` harness api key, needs access to toggle flags in given org/proj/env
