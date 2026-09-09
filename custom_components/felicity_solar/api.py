import logging
import re
import json
import base64
import os
import asyncio
from urllib.parse import urljoin
from datetime import datetime
from enum import Enum
import jwt
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import aiohttp

_LOGGER = logging.getLogger(__name__)


def create_felicity_client_session(hass=None) -> aiohttp.ClientSession:
    """Create an aiohttp ClientSession with SSL verification disabled.

    The Felicity Solar API servers (shine.felicitysolar.com, shine-api.felicitysolar.com)
    serve their leaf certificate without the intermediate CA, which causes
    SSLCertVerificationError on most clients. We pass ssl=False to skip verification
    only for requests made by this integration's session.
    """
    _LOGGER.info("Creating HTTP session with SSL verification disabled for Felicity Solar hosts")
    connector = aiohttp.TCPConnector(ssl=False)
    return aiohttp.ClientSession(connector=connector)


class DeviceTypeEnum(str, Enum):
    LITHIUM_BATTERY_PACK = "LITHIUM_BATTERY_PACK"
    HIGH_FREQUENCY_INVERTER = "HIGH_FREQUENCY_INVERTER"
    LOW_FREQUENCY_INVERTER = "LOW_FREQUENCY_INVERTER"
    HYBRID_INVERTER = "HYBRID_INVERTER"
    ENERGY_STORAGE_INVERTER = "ENERGY_STORAGE_INVERTER"
    TREX_INVERTER = "TREX_INVERTER"
    SINGLE_PHASE_HYBRID_INVERTER = "SINGLE_PHASE_HYBRID_INVERTER"


class FelicitySolarAPI:
    JSON_FILE_PATH = "data/felicitySolarToken.json"
    LOGIN_URL = "https://shine.felicitysolar.com/login"
    API_URL_DEVICE_LIST = "https://shine-api.felicitysolar.com/device/list_device_all_type"
    API_URL_DEVICE_SNAPSHOT = "https://shine-api.felicitysolar.com/device/get_device_snapshot"
    API_URL_USER_LOGIN = "https://shine-api.felicitysolar.com/userlogin"
    API_URL_REFRESH_TOKEN = "https://shine-api.felicitysolar.com/openApi/sec/refreshToken"
    API_URL_DEVICE_BASIC = "https://shine-api.felicitysolar.com/openApi/data/deviceDataBasic/"
    API_URL_DEVICE_WARN = "https://shine-api.felicitysolar.com/openApi/data/deviceDataWarn/"
    API_URL_DEVICE_SETTING = "https://shine-api.felicitysolar.com/openApi/cmd/deviceSetting"
    API_URL_DEVICE_SETTING_QUERY = "https://shine-api.felicitysolar.com/openApi/cmd/deviceSetting/"
    API_URL_DEVICE_ENERGY = "https://shine-api.felicitysolar.com/openApi/data/deviceDataEnergy"
    API_URL_DEVICE_HISTORY = "https://shine-api.felicitysolar.com/openApi/data/deviceDataHistory/"

    def __init__(self, email: str, password: str, session: aiohttp.ClientSession):
        self.email = email
        self.password = password
        self.session = session

        self.bearer_token: str | None = None
        self.token_expiration: datetime | None = None
        self.refresh_token: str | None = None
        self.devices_serial_numbers: list[str] = []
        self.has_openapi_permissions: bool | None = None

    async def initialize(self) -> None:
        _LOGGER.info("Initializing Felicity Solar API for %s", self.email)
        await self._load_from_file()

        if not self._is_logged_in():
            refreshed = await self._refresh_token()
            if not refreshed:
                _LOGGER.info("Authenticating with Felicity Solar")
                await self._login()
        else:
            _LOGGER.info(
                "Token is valid, expires at %s",
                self.token_expiration.strftime("%Y-%m-%d %H:%M:%S")
            )

        await self._load_devices_serial_numbers()
        _LOGGER.info(
            "Initialization complete, found %d device(s): %s",
            len(self.devices_serial_numbers),
            self.devices_serial_numbers
        )

    async def refresh_devices(self) -> None:
        _LOGGER.info("Refreshing device list for %s", self.email)
        if not self._is_logged_in():
            refreshed = await self._refresh_token()
            if not refreshed:
                await self._login()
        await self._load_devices_serial_numbers()
        _LOGGER.info("Device refresh complete, %d device(s) found", len(self.devices_serial_numbers))

    def get_devices_serial_numbers(self) -> list[str]:
        return self.devices_serial_numbers

    async def _ensure_authenticated(self) -> None:
        if not self._is_logged_in():
            refreshed = await self._refresh_token()
            if not refreshed:
                await self._login()

    def _handle_permission_denied(self, device_sn: str, endpoint_name: str) -> None:
        """Handle 2001528 permission denied response and silence future OpenAPI calls."""
        if self.has_openapi_permissions is not False:
            self.has_openapi_permissions = False
            _LOGGER.warning(
                "Felicity Cloud account %s does not have OpenAPI privileges (code 2001528). "
                "Standard telemetry is 100%% functional, but remote controls and OpenAPI endpoints are disabled.",
                self.email,
            )

    async def get_device_basic_info(self, device_sn: str) -> dict:
        """Fetch basic device info (firmware version, collector SN, status) from OpenAPI."""
        if self.has_openapi_permissions is False:
            return {}
        await self._ensure_authenticated()

        _LOGGER.debug("Fetching basic device info for %s", device_sn)
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": self.bearer_token,
            "Lang": "en_US",
        }
        url = f"{self.API_URL_DEVICE_BASIC}{device_sn}"

        try:
            async with self.session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    code = data.get("code")
                    if code in (200, 0) and "data" in data and isinstance(data["data"], dict):
                        _LOGGER.debug("Basic info retrieved for %s: %s", device_sn, data["data"])
                        return data["data"]
                    elif code in (999, 998):
                        _LOGGER.warning("Token expired during basic info fetch for %s, re-authenticating", device_sn)
                        await self._login()
                        return await self.get_device_basic_info(device_sn)
                    elif code == 2001528:
                        self._handle_permission_denied(device_sn, "basic info")
                        return {}
                    else:
                        _LOGGER.warning("Basic info query returned code %s for %s: %s", code, device_sn, data.get("message"))
                else:
                    body = await response.text()
                    _LOGGER.warning("Basic info query for %s returned HTTP %s: %s", device_sn, response.status, body)
        except Exception as err:
            _LOGGER.warning("Failed to fetch basic info for device %s: %s", device_sn, err)
        return {}

    async def get_device_warnings(self, device_sn: str) -> list[dict]:
        """Fetch active alarms and warnings for a device from OpenAPI."""
        if self.has_openapi_permissions is False:
            return []
        await self._ensure_authenticated()

        _LOGGER.debug("Fetching warnings for device %s", device_sn)
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": self.bearer_token,
            "Lang": "en_US",
        }
        url = f"{self.API_URL_DEVICE_WARN}{device_sn}"

        try:
            async with self.session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    code = data.get("code")
                    if code in (200, 0) and "data" in data:
                        raw_warns = data["data"]
                        if isinstance(raw_warns, list):
                            return raw_warns
                        elif isinstance(raw_warns, dict):
                            return [raw_warns]
                    elif code in (999, 998):
                        _LOGGER.warning("Token expired during warning fetch for %s, re-authenticating", device_sn)
                        await self._login()
                        return await self.get_device_warnings(device_sn)
                    elif code == 2001528:
                        self._handle_permission_denied(device_sn, "warnings")
                        return []
                    else:
                        _LOGGER.warning("Warning query returned code %s for %s: %s", code, device_sn, data.get("message"))
                else:
                    body = await response.text()
                    _LOGGER.warning("Warning query for %s returned HTTP %s: %s", device_sn, response.status, body)
        except Exception as err:
            _LOGGER.warning("Failed to fetch warnings for device %s: %s", device_sn, err)
        return []

    async def get_device_settings(self, device_sn: str) -> dict:
        """Fetch remote control settings for an inverter device from OpenAPI."""
        if self.has_openapi_permissions is False:
            return {}
        await self._ensure_authenticated()

        _LOGGER.info("Fetching remote settings for inverter %s", device_sn)
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": self.bearer_token,
            "Lang": "en_US",
        }
        url = f"{self.API_URL_DEVICE_SETTING_QUERY}{device_sn}"
        params = {"deviceSn": device_sn}

        try:
            async with self.session.get(url, headers=headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    code = data.get("code")
                    if code in (200, 0) and "data" in data and isinstance(data["data"], dict) and data["data"]:
                        _LOGGER.info("Settings successfully retrieved for %s (%d parameter(s))", device_sn, len(data["data"]))
                        self.has_openapi_permissions = True
                        return data["data"]
                    elif code in (999, 998):
                        _LOGGER.warning("Token expired during settings fetch for %s, re-authenticating", device_sn)
                        await self._login()
                        return await self.get_device_settings(device_sn)
                    elif code == 2001528:
                        self._handle_permission_denied(device_sn, "settings")
                        return {}
                    elif code == 1006051:
                        _LOGGER.warning(
                            "Settings query for %s failed with code 1006051 (Failed to send command): "
                            "Inverter or datalogger is unreachable or did not respond in time.",
                            device_sn
                        )
                    else:
                        _LOGGER.warning(
                            "Settings query returned code %s for %s: %s (data: %s)",
                            code, device_sn, data.get("message"), data.get("data")
                        )
                elif response.status == 404:
                    # Fallback attempt without path variable, using query parameter only
                    alt_url = self.API_URL_DEVICE_SETTING
                    _LOGGER.info("Path endpoint returned 404, attempting fallback to %s for %s", alt_url, device_sn)
                    async with self.session.get(alt_url, headers=headers, params=params) as alt_resp:
                        if alt_resp.status == 200:
                            alt_data = await alt_resp.json()
                            alt_code = alt_data.get("code")
                            if alt_code in (200, 0) and "data" in alt_data and isinstance(alt_data["data"], dict) and alt_data["data"]:
                                _LOGGER.info("Settings retrieved via fallback query for %s (%d parameter(s))", device_sn, len(alt_data["data"]))
                                self.has_openapi_permissions = True
                                return alt_data["data"]
                            elif alt_code == 2001528:
                                self._handle_permission_denied(device_sn, "fallback settings")
                                return {}
                            else:
                                _LOGGER.warning("Fallback settings query returned code %s for %s: %s", alt_code, device_sn, alt_data.get("message"))
                        else:
                            alt_body = await alt_resp.text()
                            _LOGGER.warning("Fallback settings query returned HTTP %s for %s: %s", alt_resp.status, device_sn, alt_body)
                else:
                    body = await response.text()
                    _LOGGER.warning("Settings query for %s returned HTTP %s: %s", device_sn, response.status, body)
        except Exception as err:
            _LOGGER.warning("Failed to fetch settings for device %s: %s", device_sn, err)
        return {}

    async def set_device_setting(self, device_sn: str, content: dict) -> bool:
        """Send remote control settings for an inverter device to OpenAPI."""
        if self.has_openapi_permissions is False:
            _LOGGER.error("Cannot set parameter on device %s: account %s lacks OpenAPI permissions (code 2001528)", device_sn, self.email)
            return False
        await self._ensure_authenticated()

        _LOGGER.info("Sending setting command for device %s: %s", device_sn, content)
        headers = {
            "accept": "application/json, text/plain, */*",
            "authorization": self.bearer_token,
            "content-type": "application/json",
            "lang": "en_US",
        }
        payload = {
            "deviceSn": device_sn,
            "content": content,
        }

        try:
            async with self.session.post(self.API_URL_DEVICE_SETTING, headers=headers, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    code = data.get("code")
                    if code in (200, 0):
                        _LOGGER.info("Setting command succeeded for %s: %s", device_sn, data.get("data"))
                        return True
                    elif code in (999, 998):
                        _LOGGER.warning("Token expired during setting command for %s, re-authenticating", device_sn)
                        await self._login()
                        return await self.set_device_setting(device_sn, content)
                    elif code == 1006051:
                        _LOGGER.error("Failed to send command to device %s (code 1006051) — device may be offline or unreachable", device_sn)
                    elif code == 2001528:
                        _LOGGER.error("Insufficient permissions to set parameters on device %s (code 2001528)", device_sn)
                    else:
                        _LOGGER.error("Setting command failed for %s (code %s): %s", device_sn, code, data.get("message"))
                else:
                    _LOGGER.error("HTTP error %s when setting parameters on %s", response.status, device_sn)
        except Exception as err:
            _LOGGER.error("Exception when sending setting command to device %s: %s", device_sn, err)
        return False

    async def get_device_energy_data(
        self,
        device_sn: str,
        time_dimension: str = "day",
        date_str: str | None = None,
        page_num: int = 1,
        page_size: int = 10,
    ) -> dict:
        """Fetch historical aggregated energy data (day/month/year/total) from OpenAPI."""
        if self.has_openapi_permissions is False:
            return {}
        await self._ensure_authenticated()

        _LOGGER.debug("Fetching energy data for device %s (dim=%s)", device_sn, time_dimension)
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": self.bearer_token,
            "Lang": "en_US",
        }
        params = {
            "deviceSn": device_sn,
            "timeDimension": time_dimension,
            "pageNum": str(page_num),
            "pageSize": str(page_size),
        }
        if date_str:
            params["dateStr"] = date_str

        try:
            async with self.session.get(self.API_URL_DEVICE_ENERGY, headers=headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    code = data.get("code")
                    if code in (200, 0) and "data" in data and isinstance(data["data"], dict):
                        return data["data"]
                    elif code in (999, 998):
                        _LOGGER.warning("Token expired during energy data fetch for %s, re-authenticating", device_sn)
                        await self._login()
                        return await self.get_device_energy_data(
                            device_sn, time_dimension, date_str, page_num, page_size
                        )
                    elif code == 2001528:
                        self._handle_permission_denied(device_sn, "energy data")
                        return {}
                    else:
                        _LOGGER.debug("Energy data query returned code %s for %s: %s", code, device_sn, data.get("message"))
        except Exception as err:
            _LOGGER.warning("Failed to fetch energy data for device %s: %s", device_sn, err)
        return {}

    async def get_device_history_data(
        self,
        device_sn: str,
        date_str: str | None = None,
        page_num: int = 1,
        page_size: int = 10,
    ) -> dict:
        """Fetch historical real-time snapshot records for a device from OpenAPI."""
        if self.has_openapi_permissions is False:
            return {}
        await self._ensure_authenticated()

        _LOGGER.debug("Fetching history data for device %s", device_sn)
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": self.bearer_token,
            "Lang": "en_US",
        }
        url = f"{self.API_URL_DEVICE_HISTORY}{device_sn}"
        params = {
            "pageNum": str(page_num),
            "pageSize": str(page_size),
        }
        if date_str:
            params["dateStr"] = date_str

        try:
            async with self.session.get(url, headers=headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    code = data.get("code")
                    if code in (200, 0) and "data" in data and isinstance(data["data"], dict):
                        return data["data"]
                    elif code in (999, 998):
                        _LOGGER.warning("Token expired during history data fetch for %s, re-authenticating", device_sn)
                        await self._login()
                        return await self.get_device_history_data(device_sn, date_str, page_num, page_size)
                    elif code == 2001528:
                        self._handle_permission_denied(device_sn, "history data")
                        return {}
                    else:
                        _LOGGER.debug("History data query returned code %s for %s: %s", code, device_sn, data.get("message"))
        except Exception as err:
            _LOGGER.warning("Failed to fetch history data for device %s: %s", device_sn, err)
        return {}

    async def get_device_snapshot(self, device_sn: str) -> dict:
        await self._ensure_authenticated()

        _LOGGER.debug("Fetching snapshot for device %s", device_sn)
        today_date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        headers = {
            "accept": "application/json, text/plain, */*",
            "authorization": self.bearer_token,
            "content-type": "application/json",
        }
        payload = {
            "deviceSn": device_sn,
            "deviceType": "BP",
            "dateStr": today_date_str
        }

        async with self.session.post(self.API_URL_DEVICE_SNAPSHOT, headers=headers, json=payload) as response:
            response.raise_for_status()
            data = await response.json()

            code = data.get("code")
            if code in (999, 998):
                _LOGGER.warning("Token expired during snapshot fetch for %s, re-authenticating", device_sn)
                await self._login()
                return await self.get_device_snapshot(device_sn)

            if "data" not in data:
                _LOGGER.error("Snapshot response missing 'data' field for %s: %s", device_sn, data)
                raise ValueError(f"Failed to get device snapshot: {data}")

            device_data = data["data"]
            if "productTypeEnum" not in device_data:
                _LOGGER.error("Snapshot response missing 'productTypeEnum' for %s: %s", device_sn, device_data)
                raise ValueError(f"Invalid device data: {device_data}")

            _LOGGER.info(
                "Snapshot received for %s (type=%s)",
                device_sn, device_data.get("productTypeEnum", "unknown")
            )
            return device_data

    # --- Private Methods ---

    def _is_logged_in(self) -> bool:
        if not self.bearer_token or not self.token_expiration:
            _LOGGER.debug("Not logged in: no token or expiration stored")
            return False
        now = datetime.now()
        if self.token_expiration <= now:
            _LOGGER.debug(
                "Token expired: expiration=%s, now=%s",
                self.token_expiration.strftime("%Y-%m-%d %H:%M:%S"),
                now.strftime("%Y-%m-%d %H:%M:%S")
            )
            return False
        return True

    def _read_token_file_sync(self):
        if not os.path.exists(self.JSON_FILE_PATH):
            return None
        try:
            with open(self.JSON_FILE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None

    def _write_token_file_sync(self, data):
        os.makedirs(os.path.dirname(self.JSON_FILE_PATH) or ".", exist_ok=True)
        with open(self.JSON_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f)

    async def _load_from_file(self) -> None:
        data = await asyncio.to_thread(self._read_token_file_sync)
        if not data:
            _LOGGER.info("No token file found at %s", self.JSON_FILE_PATH)
            return

        found = next(
            (item for item in data if item["email"] == self.email), None)
        if not found:
            _LOGGER.info("No saved token found for %s in token file", self.email)
            return

        self.bearer_token = found.get("bearer")
        self.refresh_token = found.get("refreshToken")
        exp_val = found.get("exp")
        if exp_val:
            self.token_expiration = datetime.fromtimestamp(exp_val / 1000.0)
        _LOGGER.info("Loaded bearer token from file for %s", self.email)

    async def _save_to_file(self) -> None:
        if not self.bearer_token or not self.token_expiration:
            return

        data = await asyncio.to_thread(self._read_token_file_sync) or []

        found = next(
            (item for item in data if item["email"] == self.email), None)
        exp_timestamp = int(self.token_expiration.timestamp() * 1000)

        token_entry = {
            "email": self.email,
            "bearer": self.bearer_token,
            "refreshToken": self.refresh_token,
            "exp": exp_timestamp
        }

        if found:
            found.update(token_entry)
            _LOGGER.info("Updated existing token in file for %s", self.email)
        else:
            data.append(token_entry)
            _LOGGER.info("Saved new token to file for %s", self.email)

        await asyncio.to_thread(self._write_token_file_sync, data)

    async def _refresh_token(self) -> bool:
        if not self.refresh_token:
            return False
        _LOGGER.info("Attempting to refresh access token for %s", self.email)
        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
        }
        payload = {"refreshToken": self.refresh_token}
        try:
            async with self.session.post(self.API_URL_REFRESH_TOKEN, headers=headers, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    code = data.get("code")
                    if code in (200, 0) and "data" in data and isinstance(data["data"], dict):
                        token_data = data["data"]
                        new_token = token_data.get("token")
                        new_refresh = token_data.get("refreshToken")
                        if new_token:
                            clean_token = new_token.replace("Bearer_", "")
                            decrypted_token = jwt.decode(clean_token, options={"verify_signature": False})
                            self.token_expiration = datetime.fromtimestamp(decrypted_token["exp"])
                            self.bearer_token = new_token
                            if new_refresh:
                                self.refresh_token = new_refresh
                            _LOGGER.info("Access token successfully refreshed for %s", self.email)
                            await self._save_to_file()
                            return True
                    _LOGGER.warning("Token refresh returned code %s: %s", code, data.get("message"))
        except Exception as err:
            _LOGGER.warning("Token refresh request failed for %s: %s", self.email, err)
        return False

    async def _load_devices_serial_numbers(self) -> None:
        _LOGGER.debug("Fetching device list from API")
        headers = {
            "accept": "application/json, text/plain, */*",
            "authorization": self.bearer_token,
            "content-type": "application/json",
        }
        payload = {
            "pageNum": 1,
            "pageSize": 10,
            "deviceSn": "",
            "status": "",
            "sampleFlag": "",
            "oscFlag": ""
        }

        async with self.session.post(self.API_URL_DEVICE_LIST, headers=headers, json=payload) as response:
            response.raise_for_status()
            data = await response.json()
            data_list = data.get("data", {}).get("dataList", [])
            devices_sn = [device["deviceSn"] for device in data_list]
            _LOGGER.info(
                "Device list loaded: %d device(s) found — %s",
                len(devices_sn), devices_sn
            )
            self.devices_serial_numbers = devices_sn

    async def _login(self) -> None:
        _LOGGER.info("Logging in to Felicity Solar as %s", self.email)
        password_hash = await self._generate_password_hash(self.password)
        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
        }
        payload = {
            "userName": self.email,
            "password": password_hash,
            "version": "1.0"
        }

        async with self.session.post(self.API_URL_USER_LOGIN, headers=headers, json=payload) as response:
            response.raise_for_status()
            data = await response.json()

            code = data.get("code")
            if code == 1002006:
                _LOGGER.error("Login failed — Incorrect password for %s", self.email)
                raise ValueError("Wrong password (code 1002006).")
            elif code == 1002001:
                _LOGGER.error("Login failed — Account not activated for %s", self.email)
                raise ValueError("Account not activated (code 1002001).")

            res_data = data.get("data", {})
            bearer = res_data.get("token") if isinstance(res_data, dict) else None
            refresh = res_data.get("refreshToken") if isinstance(res_data, dict) else None

            if not bearer:
                _LOGGER.error("Login failed — no token in response: %s", data)
                raise ValueError("Token missing from login response.")

            clean_token = bearer.replace("Bearer_", "")
            try:
                decrypted_token = jwt.decode(
                    clean_token, options={"verify_signature": False})
            except Exception as e:
                _LOGGER.error("Failed to decode JWT token: %s", e)
                raise ValueError(f"Failed to decode token: {e}")

            self.token_expiration = datetime.fromtimestamp(
                decrypted_token["exp"])
            self.bearer_token = bearer
            if refresh:
                self.refresh_token = refresh

            _LOGGER.info(
                "Login successful for %s, token expires at %s",
                self.email,
                self.token_expiration.strftime("%Y-%m-%d %H:%M:%S")
            )
            await self._save_to_file()

    async def _generate_password_hash(self, password: str) -> str:
        public_key_str = await self._extract_public_key()
        key = RSA.import_key(public_key_str)
        cipher = PKCS1_v1_5.new(key)
        encrypted = cipher.encrypt(password.encode("utf-8"))
        return base64.b64encode(encrypted).decode("utf-8")

    async def _extract_public_key(self) -> str:
        _LOGGER.info("Extracting RSA public key from Felicity Solar login page")
        async with self.session.get(self.LOGIN_URL) as response:
            response.raise_for_status()
            combined_text = await response.text()

        _LOGGER.debug("Parsing login page HTML for JS bundle URLs")

        head_match = re.search(
            r"<head[^>]*>([\s\S]*?)<\/head>", combined_text, re.IGNORECASE)
        head_content = head_match.group(1) if head_match else ""

        script_src_regex = re.compile(
            r'(?:href|src)=["\']([^"\']*/index\.[^"\']*\.js)["\']', re.IGNORECASE)
        match = script_src_regex.search(head_content)
        script_urls = []

        if match:
            index_url = match.group(1)
            _LOGGER.info("Found main JS bundle: %s", index_url)
            try:
                absolute_index_url = urljoin(self.LOGIN_URL, index_url)
                async with self.session.get(absolute_index_url) as index_res:
                    if index_res.status == 200:
                        index_text = await index_res.text()
                        combined_text += "\n\n" + index_text
                        _LOGGER.debug("Main JS bundle fetched (%d bytes), searching for login route", len(index_text))

                        login_route_regex = re.compile(
                            r'path:\s*["\']/login["\'][\s\S]*?component:\s*\(\)\s*=>[\s\S]*?\[(.*?)\]')
                        login_match = login_route_regex.search(index_text)

                        if login_match:
                            asset_regex = re.compile(
                                r'["\']([^"\']*/index\.[^"\']*\.js)["\']')
                            script_urls.extend(
                                asset_regex.findall(login_match.group(1)))
                            _LOGGER.info("Found %d login-related JS bundle(s): %s", len(script_urls), script_urls)
                        else:
                            _LOGGER.warning("Login route pattern not found in main JS bundle")
            except Exception as err:
                _LOGGER.error(f"Failed to fetch main index script: {err}")

        _LOGGER.info("Fetching %d login JS bundle(s) to find public key", len(script_urls))
        for src in script_urls:
            absolute_url = urljoin(self.LOGIN_URL, src)
            try:
                async with self.session.get(absolute_url) as script_res:
                    if script_res.status == 200:
                        script_text = await script_res.text()
                        combined_text += "\n\n" + script_text
                        _LOGGER.debug("Fetched %s (%d bytes)", src, len(script_text))
            except Exception as err:
                _LOGGER.error("Failed to fetch script %s: %s", absolute_url, err)

        _LOGGER.debug("Searching for setPublicKey() in combined JS text")
        set_public_key_regex = re.compile(
            r"setPublicKey\s*\(\s*([a-zA-Z0-9_$]+)\s*\)")
        pk_match = set_public_key_regex.search(combined_text)

        if not pk_match:
            _LOGGER.error("Could not find setPublicKey() call in any JS bundle — the Felicity Solar website may have changed")
            raise ValueError("Could not find setPublicKey() call")

        var_name = pk_match.group(1)
        _LOGGER.debug("Found setPublicKey(%s), searching for its value assignment", var_name)
        escaped_var_name = re.escape(var_name)

        assignment_regex = re.compile(
            escaped_var_name + r"\s*=\s*(['\"`])(.*?)\1")
        matches = assignment_regex.findall(combined_text)

        if not matches:
            _LOGGER.error(
                "Could not find string assignment for variable '%s' — the Felicity Solar website may have changed", var_name
            )
            raise ValueError(
                f"Could not find the string assignment for the variable '{var_name}'.")

        # Find the longest matched string
        extracted_value = max([m[1] for m in matches], key=len)
        _LOGGER.info("RSA public key successfully extracted (%d chars)", len(extracted_value))

        return f"-----BEGIN PUBLIC KEY-----\n{extracted_value}\n-----END PUBLIC KEY-----"
