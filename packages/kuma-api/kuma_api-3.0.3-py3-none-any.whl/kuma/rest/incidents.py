from typing import Dict, List, Tuple, Union

from kuma.rest._base import KumaRestAPIModule


class KumaRestAPIIncidents(KumaRestAPIModule):
    """Methods for Incidents."""
    def search(self, **kwargs) -> Tuple[int, Union[bytes, str]]:
        """
        Searching alerts from KUMA
        Args:
            page (int): Listing page of result (250 alerts per page)
            id (List[str]): Search for specified id
            tenantID (str): Tenant filter
            name (str): Case-insensetine name regex filter
            from (str): RFC3339 Lower limit
            to (str): RFC3339 Upper limit
            timestampField (str): lastSeen|firtsSeen for from-to order
            status (str): open|assigned|closed
            search (str): case-insensitive regex search in most used fields
        """
        params = {
            **kwargs,
        }
        return self._make_request("GET", "incidents", params=params)

    def assign(self, incidents_ids: list, user_id: str) -> Tuple[int, Union[bytes, str]]:
        """Alert assign method
        Args:
            incidents_ids (list): Incidents INC names list
            user_id (str): User UUID
        """
        json = {"incidentIDs": incidents_ids, "assignee": user_id}
        return self._make_request("POST", "incidents/assign", json=json)

    def close(self, incidents_ids: str, resolution: str) -> Tuple[int, Dict]:
        """
        Close alerts with reason.
        Args:
            incidents_ids (list): Incidents INC names list
            resolution (int): 1 Confirmed|0 Not confirmed
        """
        json = {"incidentIDs": incidents_ids, "resolution": resolution}
        return self._make_request("POST", "incidents/close", json=json)

    def comment(self, incident_id: str, comment: str) -> Tuple[int, Union[Dict, str]]:
        """
        Create a comment in alert.
        Args:
            incident_id (str): Incident INC id
            comment (str): Message for your SOC team
        """
        json = {"id": incident_id, "comment": comment}
        return self._make_request("POST", "incidents/comment", json=json)

    def create(
        self, incident: dict, calc_priority: bool = False
    ) -> Tuple[int, Union[Dict, str]]:
        """
        Creating new incident from JSON data
        Args:
            incident (dict): Incident JSON data, see examples
            calc_priority (str): Copy priority from alert
        """
        params = {"calcPriority": calc_priority}
        return self._make_request(
            "POST", f"incidents/create", json=incident, params=params
        )

    def get(self, incident_id: str) -> Tuple[int, Union[Dict, str]]:
        """Gets specified alert data
        Args:
            incident_id (str): Incident INC id
        """
        return self._make_request("GET", f"incidents/id/{incident_id}")

    def link_alert(
        self, incident_id: str, alerts_ids: List[str]
    ) -> Tuple[int, Union[Dict, str]]:
        """Linking event from storage to alert
        Args:
            incident_id (str): Incident INC id
            alerts_ids (str): List of alert UUID to link
        """
        json = {"incidentID": incident_id, "alertIDs": alerts_ids}
        return self._make_request("POST", f"incidents/link", json=json)

    def unlink_alert(
        self, incident_id: str, alerts_ids: List[str]
    ) -> Tuple[int, Union[Dict, str]]:
        """Linking event from storage to alert
        Args:
            incident_id (str): Incident INC id
            alerts_ids (str): List of alert UUID to unlink
        """
        json = {"incidentID": incident_id, "alertIDs": alerts_ids}
        return self._make_request("POST", f"incidents/unlink", json=json)
