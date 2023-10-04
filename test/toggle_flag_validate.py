from logging import DEBUG
from time import sleep
from os import getenv
from sys import exit

from requests import patch

from featureflags.evaluations.auth_target import Target
from featureflags.config import with_events_url
from featureflags.config import with_base_url
from featureflags.client import CfClient
from featureflags.util import log


log.setLevel(DEBUG)


def toggle_flag(flag: str, state: bool = False):
    ff_state = "off"
    if state:
        ff_state = "on"

    resp = patch(
        f"https://app.harness.io/cf/admin/features/{flag}",
        params={
            "accountIdentifier": getenv("HARNESS_ACCOUNT_ID"),
            "orgIdentifier": getenv("HARNESS_ORGANIZATION_ID"),
            "projectIdentifier": getenv("HARNESS_PROJECT_ID"),
            "environmentIdentifier": getenv("HARNESS_ENVIRONMENT_ID"),
        },
        headers={"x-api-key": getenv("HARNESS_PLATFORM_API_KEY")},
        json={
            "instructions": [
                {"kind": "setFeatureFlagState", "parameters": {"state": ff_state}},
            ],
        },
    )

    if resp.status_code == 200:
        log.info(f"flag toggled to {ff_state}")
    else:
        log.error(f"failed to toggle flag: {resp.text}")
        exit(1)


def get_falg_value(client: CfClient, flag: str, target: Target):
    flag_value = client.bool_variation(flag, target, None)
    if flag_value == None:
        log.error("flag failed to resolve")
        exit(1)

    return flag_value


def main():
    relay_proxy_address = getenv("RELAY_PROXY_ADDRESS", "http://localhost:7000")
    log.info(f"connecting to proxy at {relay_proxy_address}")

    flag = getenv("FF_IDENTIFIER", "test")
    log.info(f"resolving flag {flag}")

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

    sleep(5)
    print("\n\n\n")

    flag_value = get_falg_value(client, flag, target)
    log.info(f"inital state of flag: {str(flag_value)}")
    print("\n\n\n")

    log.info("toggling flag to false")
    toggle_flag(flag, False)
    sleep(5)
    print("\n\n\n")

    flag_value = get_falg_value(client, flag, target)
    log.info(f"state of flag: {str(flag_value)}")
    if flag_value:
        log.error("flag is true when it should be false")
        exit(1)
    print("\n\n\n")

    log.info("toggling flag to true")
    toggle_flag(flag, True)
    sleep(5)
    print("\n\n\n")

    flag_value = get_falg_value(client, flag, target)
    log.info(f"state of flag: {str(flag_value)}")
    if not flag_value:
        log.error("flag is false when it should be true")
        exit(1)
    print("\n\n\n")

    log.info("flag pass toggling tests")


if __name__ == "__main__":
    main()
