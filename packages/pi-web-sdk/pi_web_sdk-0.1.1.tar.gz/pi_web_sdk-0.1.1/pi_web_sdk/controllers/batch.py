"""Controllers for batch and related operations."""

from __future__ import annotations

from typing import Dict, List

from .base import BaseController

__all__ = [
    'BatchController',
    'CalculationController',
    'ChannelController',
]

class BatchController(BaseController):
    """Controller for Batch operations."""

    def execute(self, requests: List[Dict]) -> Dict:
        """Execute multiple API requests in a single batch call.

        Args:
            requests: List of request dictionaries with keys:
                - Method: HTTP method (GET, POST, PUT, etc.)
                - Resource: API endpoint path
                - Parameters: Optional query parameters
                - Content: Optional request body
                - Headers: Optional additional headers
        """
        return self.client.post("batch", data=requests)

    def replace_time_range_values(
        self, point_webid: str, start_time: str, end_time: str, new_values: List[Dict]
    ) -> Dict:
        """Delete all values in a time range and write new ones.

        Args:
            point_webid: WebID of the point
            start_time: Start of time range (e.g., "2024-01-01T00:00:00Z")
            end_time: End of time range (e.g., "2024-01-01T23:59:59Z")
            new_values: List of value dicts with Timestamp, Value, etc.
        """
        # First, get existing values in the time range
        existing_data = self.client.stream.get_recorded(
            web_id=point_webid,
            start_time=start_time,
            end_time=end_time,
            max_count=10_000,  # Adjust as needed
        )

        requests = []

        # Add delete requests for each existing timestamp
        for item in existing_data.get("Items", []):
            timestamp = item.get("Timestamp")
            if timestamp:
                requests.append(
                    {
                        "Method": "PUT",
                        "Resource": f"streams/{point_webid}/value",
                        "Content": {"Timestamp": timestamp, "Value": None},
                        "Parameters": {"updateOption": "Remove"},
                    }
                )

        # Add write requests for new values
        for value in new_values:
            requests.append(
                {
                    "Method": "PUT",
                    "Resource": f"streams/{point_webid}/value",
                    "Content": value,
                    "Parameters": {"updateOption": "Replace"},
                }
            )

        return self.execute(requests)


class CalculationController(BaseController):
    """Controller for Calculation operations."""

    pass


class ChannelController(BaseController):
    """Controller for Channel operations."""

    pass
