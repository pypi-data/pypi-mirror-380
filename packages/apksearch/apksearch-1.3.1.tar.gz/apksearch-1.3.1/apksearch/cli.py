import argparse

from collections.abc import Callable
from apksearch import (
    APKPure,
    APKMirror,
    AppTeka,
    APKCombo,
    APKFab,
    APKad,
    Aptoide,
)
from requests.exceptions import ConnectionError, ConnectTimeout

# Color codes
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
NC = "\033[0m"


def search(
    func: Callable[[str, str], object],
    pkg_name: str,
    version: str | None,
    log_err: bool = False,
) -> None:
    try:
        func(pkg_name, version)
    except Exception as exc:
        if log_err:
            print(f"Error in {func.__name__}: {exc}")
        else:
            pass


def search_apkpure(pkg_name: str, version: str | None) -> None:
    apkpure = APKPure(pkg_name)
    try:
        result_apkpure: tuple[str, str] | None = apkpure.search_apk()
    except (ConnectionError, ConnectTimeout):
        result_apkpure = None
        print(f"{RED}Failed to resolve 'apkpure.net'!{NC}")
    if result_apkpure:
        title, apk_link = result_apkpure
        print(f"{BOLD}APKPure:{NC} Found {GREEN}{title}{NC}") if title else None
        print(f"      ╰─> {BOLD}Link: {YELLOW}{apk_link}{NC}") if not version else None
        if version:
            versions: list[tuple[str, str]] = apkpure.find_versions(apk_link)
            if versions:
                for version_tuple in versions:
                    if version_tuple[0] == version:
                        print(
                            f"      ╰─> {BOLD}Version: {GREEN}{version}{NC} - {YELLOW}{version_tuple[1]}{NC}"
                        )
                        break
                else:
                    print(f"{BOLD}APKPure:{NC} Version {RED}{version}{NC} not found!")
    else:
        print(f"{BOLD}APKPure:{NC} No Results!")


def search_apkfab(pkg_name: str, version: str | None) -> None:
    apkfab = APKFab(pkg_name)
    try:
        result_apkfab: tuple[str, str] | None = apkfab.search_apk()
    except (ConnectionError, ConnectTimeout):
        result_apkfab = None
        print(f"{RED}Failed to resolve 'apkfab.com'!{NC}")
    if result_apkfab:
        title, apk_link = result_apkfab
        print(f"{BOLD}APKFab:{NC} Found {GREEN}{title}{NC}") if title else None
        print(f"      ╰─> {BOLD}Link: {YELLOW}{apk_link}{NC}") if not version else None
        if version:
            versions: list[tuple[str, str]] = apkfab.find_versions(apk_link)
            if versions:
                for version_tuple in versions:
                    if version_tuple[0] == version:
                        print(
                            f"      ╰─> {BOLD}Version: {GREEN}{version}{NC} - {YELLOW}{version_tuple[1]}{NC}"
                        )
                        break
                else:
                    print(f"{BOLD}APKFab:{NC} Version {RED}{version}{NC} not found!")
    else:
        print(f"{BOLD}APKFab:{NC} No Results!")


def search_apkad(pkg_name: str, version: str | None) -> None:
    apkad = APKad(pkg_name)
    try:
        result_apkad: tuple[str, str] | None = apkad.search_apk()
    except (ConnectionError, ConnectTimeout):
        result_apkad = None
        print(f"{RED}Failed to resolve 'api.apk.ad'!{NC}")
    if result_apkad:
        title, apk_link = result_apkad
        print(f"{BOLD}APKAD:{NC} Found {GREEN}{title}{NC}") if title else None
        print(
            f"      ╰─> {BOLD}Link: {YELLOW}{apk_link}{NC}"
        ) if not version else print("      ╰─> Doesn't support version search!")
    else:
        print(f"{BOLD}APKAD:{NC} No Results!")


def search_apkcombo(pkg_name: str, version: str | None) -> None:
    apkcombo = APKCombo(pkg_name)
    try:
        result_apkcombo: tuple[str, str] | None = apkcombo.search_apk()
    except (ConnectionError, ConnectTimeout):
        result_apkcombo = None
        print(f"{RED}Failed to resolve 'apkcombo.app'!{NC}")
    if result_apkcombo:
        title, apk_link = result_apkcombo
        print(f"{BOLD}APKCombo:{NC} Found {GREEN}{title}{NC}") if title else None
        print(f"      ╰─> {BOLD}Link: {YELLOW}{apk_link}{NC}") if not version else None
        versions: list[tuple[str, str]] = apkcombo.find_versions(apk_link)
        if version:
            for version_tuple in versions:
                if version_tuple[0] == version:
                    print(
                        f"      ╰─> {BOLD}Version: {GREEN}{version}{NC} - {YELLOW}{version_tuple[1]}{NC}"
                    )
                    break
            else:
                print(f"{BOLD}APKCombo:{NC} Version {RED}{version}{NC} not found!")
    else:
        print(f"{BOLD}APKCombo:{NC} No Results!")


def search_apkmirror(pkg_name: str, version: str | None) -> None:
    apkmirror = APKMirror(pkg_name)
    try:
        result_apkmirror: tuple[str, str] | None = apkmirror.search_apk()
    except (ConnectionError, ConnectTimeout):
        result_apkmirror = None
        print(f"{RED}Failed to resolve 'apkmirror.com'!{NC}")
    if result_apkmirror:
        title, apk_link = result_apkmirror
        print(f"{BOLD}APKMirror:{NC} Found {GREEN}{title}{NC}") if title else None
        print(f"      ╰─> {BOLD}Link: {YELLOW}{apk_link}{NC}") if not version else None
        if version:
            download_link = apkmirror.find_version(apk_link, version)
            if download_link:
                print(
                    f"      ╰─> {BOLD}Version: {GREEN}{version}{NC} - {YELLOW}{download_link}{NC}"
                )
            else:
                print(f"{BOLD}APKMirror:{NC} Version {RED}{version}{NC} not found!")
    else:
        print(f"{BOLD}APKMirror:{NC} No Results!")


def search_appteka(pkg_name: str, version: str | None) -> None:
    appteka = AppTeka(pkg_name)
    try:
        result_appteka: tuple[str, str] | None = appteka.search_apk(version)
    except (ConnectionError, ConnectTimeout):
        result_appteka = None
        print(f"{RED}Failed to resolve 'appteka.store'!{NC}")
    if result_appteka:
        title, apk_link = result_appteka
        print(f"{BOLD}AppTeka:{NC} Found {GREEN}{title}{NC}") if title else None
        if version:
            if apk_link:
                print(
                    f"      ╰─> {BOLD}Version: {GREEN}{version}{NC} - {YELLOW}{apk_link}{NC}"
                )
            else:
                print(f"{BOLD}AppTeka:{NC} Version {RED}{version}{NC} not found!")
        else:
            print(f"      ╰─> {BOLD}Link: {YELLOW}{apk_link}{NC}")
    else:
        print(f"{BOLD}AppTeka:{NC} No Results!")


def search_aptoide(pkg_name: str, version: str | None) -> None:
    aptoide = Aptoide(pkg_name)
    try:
        result_aptoide: tuple[str, str] | None = aptoide.search_apk()
    except (ConnectionError, ConnectTimeout):
        result_aptoide = None
        print(f"{RED}Failed to resolve 'aptoide.com'!{NC}")
    if result_aptoide:
        title, apk_link = result_aptoide
        print(f"{BOLD}Aptoide:{NC} Found {GREEN}{title}{NC}") if title else None
        print(f"      ╰─> {BOLD}Link: {YELLOW}{apk_link}{NC}") if not version else None
        if version:
            versions: list[str | None] = aptoide.find_versions(apk_link)
            if versions:
                if version in versions:
                    print(
                        f"      ╰─> {BOLD}Version: {GREEN}{version}{NC} - {YELLOW}{apk_link}versions{NC}"
                    )
                else:
                    print(f"{BOLD}Aptoide:{NC} Version {RED}{version}{NC} not found!")
    else:
        print(f"{BOLD}Aptoide:{NC} No Results!")


def main():
    parser = argparse.ArgumentParser(
        prog="APKSearch", description="Search for APKs on various websites"
    )
    parser.add_argument("pkg_name", help="The package name of the APK")
    parser.add_argument("--version", help="The version of the APK", required=False)
    parser.add_argument(
        "--log_err", help="Enable error logs", action="store_true", required=False
    )
    args = parser.parse_args()

    pkg_name = args.pkg_name
    version = args.version
    log_err = args.log_err
    print(f"{BOLD}Searching for {YELLOW}{pkg_name}{NC}...")
    # Initiate search on apkpure
    search(search_apkpure, pkg_name, version, log_err)
    # Initiate search on apkmirror
    search(search_apkmirror, pkg_name, version, log_err)
    # Initiate search on aptoide
    search(search_aptoide, pkg_name, version, log_err)
    # Initiate search on appteka
    search(search_appteka, pkg_name, version, log_err)
    # Initiate search on apkcombo
    search(search_apkcombo, pkg_name, version, log_err)
    # Initiate search on apkfab
    search(search_apkfab, pkg_name, version, log_err)
    # Initiate search on apkad
    search(search_apkad, pkg_name, version, log_err)


if __name__ == "__main__":
    main()
