from packaging import version
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.core.logger import log


class NPMChromeDriver(ChromeDriver):
    def _get_version_form_net(self, os_version, net_versions):
        for v in net_versions:
            if os_version in v["name"]:
                return v["name"]
        raise Exception(f"No such driver version {os_version} for {self._browser_type}")

    def get_latest_release_version(self):
        determined_browser_version = self.get_browser_version_from_os()
        log(f"Get LATEST {self._name} version for {self._browser_type}")
        if determined_browser_version is not None and version.parse(determined_browser_version) >= version.parse("115"):
            url = "https://registry.npmmirror.com/-/binary/chrome-for-testing"
            response = self._http_client.get(url)
            response_list = response.json()
            determined_browser_version = self._get_version_form_net(determined_browser_version, response_list)
            if determined_browser_version.endswith("/"):
                determined_browser_version = determined_browser_version[:-1]
            return determined_browser_version
        # Remove the build version (the last segment) from determined_browser_version for version < 113
        determined_browser_version = ".".join(determined_browser_version.split(".")[:3])
        latest_release_url = (
            self._latest_release_url
            if (determined_browser_version is None)
            else f"{self._latest_release_url}_{determined_browser_version}"
        )
        resp = self._http_client.get(url=latest_release_url)
        return resp.text.rstrip()

    def get_url_for_version_and_platform(self, browser_version, platform):
        base_url = f"https://registry.npmmirror.com/-/binary/chrome-for-testing/{browser_version}/"

        platform_path_map = {
            'linux64': 'linux64/chromedriver-linux64.zip',
            'mac-x64': 'mac-x64/chromedriver-mac-x64.zip',
            'mac-arm64': 'mac-arm64/chromedriver-mac-arm64.zip',
            'win32': 'win32/chromedriver-win32.zip',
            'win64': 'win64/chromedriver-win64.zip',
        }

        download_url = base_url + platform_path_map[platform]
        return download_url
