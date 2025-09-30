"""
JSONBin API Connector
A reusable connector for interacting with JSONBin.io API
"""

import time
import httpx
from typing import Dict, List, Optional, Any


class JSONBinConnector:
    """A connector for JSONBin.io API with httpx"""

    def __init__(self, api_token: str, base_url: str = "https://api.jsonbin.io/v3"):
        """
        Initialize the JSONBin connector

        Args:
            api_token: JSONBin API token
            base_url: JSONBin API base URL
        """
        self.api_token = api_token
        self.base_url = base_url
        self.client = httpx.Client(
            base_url=base_url,
            headers={"X-Master-Key": api_token, "Content-Type": "application/json"},
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def create_bin(
        self, data: Dict[str, Any], collection_id: Optional[str] = None
    ) -> str:
        """
        Create a new bin

        Args:
            data: The data to store in the bin
            collection_id: Optional collection ID to add the bin to

        Returns:
            The created bin ID
        """
        headers = {}
        if collection_id:
            headers["X-Collection-Id"] = collection_id

        response = self.client.post("/b", json=data, headers=headers)
        response.raise_for_status()
        return response.json()["metadata"]["id"]

    def get_bin(self, bin_id: str) -> Dict[str, Any]:
        """
        Get bin data by ID

        Args:
            bin_id: The bin ID to retrieve

        Returns:
            The bin data
        """
        response = self.client.get(f"/b/{bin_id}", headers={"X-Bin-Name": bin_id})
        response.raise_for_status()
        return response.json()["record"]

    def update_bin(self, bin_id: str, **data: Any) -> None:
        """
        Update bin data

        Args:
            bin_id: The bin ID to update
            **data: Key-value pairs to update in the bin
        """
        # Get existing data first
        existing_data = self.get_bin(bin_id)

        # Merge with new data
        updated_data = {**existing_data, **data}

        # Update the bin
        response = self.client.put(
            f"/b/{bin_id}", json=updated_data, headers={"X-Bin-Name": bin_id}
        )
        response.raise_for_status()

    def delete_bin(self, bin_id: str) -> None:
        """
        Delete a bin

        Args:
            bin_id: The bin ID to delete
        """
        response = self.client.delete(f"/b/{bin_id}", headers={"X-Bin-Name": bin_id})
        response.raise_for_status()

    def get_collections(self) -> List[Dict[str, Any]]:
        """
        Get all collections

        Returns:
            List of collections
        """
        response = self.client.get("/c")
        response.raise_for_status()
        return response.json()

    def create_collection(self, name: str) -> str:
        """
        Create a new collection

        Args:
            name: The collection name

        Returns:
            The created collection ID
        """
        response = self.client.post("/c", json={"name": name})
        response.raise_for_status()
        return response.json()["metadata"]["id"]

    def get_collection_bins(
        self, collection_id: str, after_bin_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get bins from a collection

        Args:
            collection_id: The collection ID
            after_bin_id: Optional bin ID to get bins after (for pagination)

        Returns:
            List of bins in the collection
        """
        endpoint = f"/c/{collection_id}/bins"
        if after_bin_id:
            endpoint += f"/{after_bin_id}"

        response = self.client.get(
            endpoint,
            headers={"X-Collection-Id": collection_id, "X-Sort-Order": "ascending"},
        )
        response.raise_for_status()
        return response.json()

    def close(self):
        """Close the HTTP client"""
        self.client.close()


class SideloadBinManager:
    """High-level manager for Sideload-specific JSONBin operations"""

    def __init__(self, connector: JSONBinConnector):
        """
        Initialize the sideload bin manager

        Args:
            connector: JSONBin connector instance
        """
        self.connector = connector

    def create_sideload_request(
        self, url: str, collection_id: Optional[str] = None
    ) -> str:
        """
        Create a new sideload request

        Args:
            url: The URL to sideload
            collection_id: Optional collection ID

        Returns:
            The created bin ID
        """
        data = {"url": url, "status": "CREATED", "created_at": time.time()}
        return self.connector.create_bin(data, collection_id)

    def update_sideload_status(
        self, bin_id: str, status: str, **additional_data: Any
    ) -> None:
        """
        Update sideload request status

        Args:
            bin_id: The bin ID to update
            status: The new status
            **additional_data: Additional data to update
        """
        self.connector.update_bin(bin_id, status=status, **additional_data)

    def update_progress(self, bin_id: str, progress: int) -> None:
        """
        Update download progress

        Args:
            bin_id: The bin ID to update
            progress: Progress percentage (0-100)
        """
        self.connector.update_bin(bin_id, progress=progress)

    def mark_completed(
        self,
        bin_id: str,
        package_names: List[str],
        original_filename: str,
        file_size: int,
    ) -> None:
        """
        Mark sideload request as completed

        Args:
            bin_id: The bin ID to update
            package_names: List of created package names
            original_filename: Original filename
            file_size: Original file size
        """
        self.connector.update_bin(
            bin_id,
            status="UPLOADED",
            package_names=package_names,
            total_packages=len(package_names),
            original_filename=original_filename,
            file_size=file_size,
        )

    def mark_failed(self, bin_id: str, reason: str) -> None:
        """
        Mark sideload request as failed

        Args:
            bin_id: The bin ID to update
            reason: Failure reason
        """
        self.connector.update_bin(bin_id, status="FAILED", reason=reason)

    def mark_rejected(self, bin_id: str, reason: str) -> None:
        """
        Mark sideload request as rejected

        Args:
            bin_id: The bin ID to update
            reason: Rejection reason
        """
        self.connector.update_bin(bin_id, status="REJECTED", reason=reason)

    def get_sideload_data(self, bin_id: str) -> Dict[str, Any]:
        """
        Get sideload request data

        Args:
            bin_id: The bin ID to retrieve

        Returns:
            The sideload data
        """
        return self.connector.get_bin(bin_id)

    def find_sideload_collections(self) -> List[Dict[str, Any]]:
        """
        Find collections that start with 'sideload_'

        Returns:
            List of sideload collections
        """
        collections = self.connector.get_collections()
        return [
            collection
            for collection in collections
            if collection["collectionMeta"]["name"].startswith("sideload_")
        ]

    def get_pending_requests(
        self, collection_id: str, after_bin_id: Optional[str] = None
    ) -> List[str]:
        """
        Get pending sideload requests from a collection

        Args:
            collection_id: The collection ID to check
            after_bin_id: Optional bin ID for pagination

        Returns:
            List of bin IDs that need processing
        """
        bins = self.connector.get_collection_bins(collection_id, after_bin_id)
        pending_bins = []

        for bin_data in bins:
            bin_id = bin_data["record"]
            try:
                data = self.get_sideload_data(bin_id)
                if data.get("status") == "CREATED":
                    pending_bins.append(bin_id)
            except Exception:
                # Skip bins that can't be read
                continue

        return pending_bins
