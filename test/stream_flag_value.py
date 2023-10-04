from logging import DEBUG
from time import sleep
from os import getenv

from featureflags.evaluations.auth_target import Target
from featureflags.config import with_events_url
from featureflags.config import with_base_url
from featureflags.client import CfClient
from featureflags.util import log


log.setLevel(DEBUG)


def main():
    relay_proxy_address = getenv("RELAY_PROXY_ADDRESS", "http://localhost:7000")
    log.info(f"connecting to proxy at {relay_proxy_address}")

    client = CfClient(
        getenv("FF_SDK_KEY"),
        with_base_url(relay_proxy_address),
        with_events_url(relay_proxy_address),
    )

    target = Target(
        identifier="HT_1",
        name="Harness_Target_1",
        attributes={"location": "harness hosted ci vm"},
    )

    while True:
        log.info(client.bool_variation(getenv("FF_IDENTIFIER", "test"), target, False))
        sleep(10)


if __name__ == "__main__":
    main()
