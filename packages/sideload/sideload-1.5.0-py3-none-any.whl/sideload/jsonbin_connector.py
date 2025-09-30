import os
import httpx

JSONBIN_TOKEN = os.environ["JSONBIN_TOKEN"]
JSONBIN_VERIFY_SSL = os.environ.get("JSONBIN_VERIFY_SSL", "true").lower() in ("true", "1", "yes")
JSONBIN_KEY_TYPE = os.environ.get("JSONBIN_KEY_TYPE", "master").lower()  # "master" or "access"


class JSONBinConnector:
    def __init__(self, verify_ssl: bool = None, key_type: str = None):
        # Use provided values or fall back to environment variables
        verify = JSONBIN_VERIFY_SSL if verify_ssl is None else verify_ssl
        key_type = key_type or JSONBIN_KEY_TYPE

        # Determine the key header to use
        if key_type == "access":
            key_header = "X-Access-Key"
        else:
            key_header = "X-Master-Key"

        self.client = httpx.Client(
            base_url="https://api.jsonbin.io/v3",
            headers={key_header: JSONBIN_TOKEN, "Content-Type": "application/json"},
            verify=verify,
        )

    def get_collections(self) -> list:
        response = self.client.get("/c")
        response.raise_for_status()
        return response.json()

    def get_collection_bins(
        self, collection_id: str, last_bin_id: str | None = None
    ) -> list:
        url = f"/c/{collection_id}/bins"
        if last_bin_id:
            url = f"{url}/{last_bin_id}"
        response = self.client.get(
            url,
            headers={"X-Sort-Order": "ascending"},
        )
        response.raise_for_status()
        return response.json()

    def create_bin(self, collection_id: str, bin_name: str, data: dict) -> str:
        headers = {"X-Collection-Id": collection_id, "X-Bin-Name": bin_name}
        response = self.client.post("/b", json=data, headers=headers)
        response.raise_for_status()
        return response.json()["metadata"]["id"]

    def get_bin(self, bin_id: str) -> dict:
        response = self.client.get(f"/b/{bin_id}", headers={"X-Bin-Name": bin_id})
        response.raise_for_status()
        return response.json()["record"]

    def update_bin(self, bin_id: str, data: dict) -> None:
        existing_data = self.get_bin(bin_id)
        updated_data = {**existing_data, **data}
        response = self.client.put(
            f"/b/{bin_id}", json=updated_data, headers={"X-Bin-Name": bin_id}
        )
        response.raise_for_status()
