from typing import Optional

from modempay.resources.base import BaseResource
from modempay.types.customer import (
    Customer,
    CustomerParams,
    CustomerCreateOption,
    CustomerListOption,
)
from modempay.types.sub_account import (
    SubAccount,
    SubAccountParams,
    SubAccountUpdateParams,
)
from modempay.types.type import List, ListOption


class SubAccountResources(BaseResource):
    """
    Resource class for managing sub-accounts.
    """

    def __init__(self, api_key: str, max_retries: int, timeout: int):
        super().__init__(api_key, max_retries, timeout)

    def create(self, params: SubAccountParams) -> SubAccount:
        """
        Creates a new sub-account.

        Args:
            params (SubAccountParams): Parameters for creating the sub-account.

        Returns:
            SubAccount: The created sub-account object.
        """
        return self.request(
            "post",
            "/v1/sub-accounts",
            headers=self.get_headers(),
            json={**params},
        )

    def retrieve(self, id: str) -> SubAccount:
        """
        Retrieves a sub-account by ID.

        Args:
            id (str): The sub-account ID.

        Returns:
            SubAccount: The retrieved sub-account object.
        """
        return self.request(
            "get",
            f"/v1/sub-accounts/{id}",
            headers=self.get_headers(),
        )

    def list(
        self,
        options: Optional[ListOption] = None,
    ) -> List[SubAccount]:
        """
        Returns a list of sub-accounts.

        Args:
            options (ListOption, optional): Options for listing sub-accounts.

        Returns:
            List[SubAccount]: A list of sub-accounts and metadata.
        """
        if options is None:
            options = {"limit": 10, "offset": 0, "search": ""}
        search_term = options.get("search", "")
        params = {"offset": options.get("offset", 0), **options}
        return self.request(
            "get",
            f"/v1/sub-accounts?term={search_term}",
            headers=self.get_headers(),
            params=params,
        )

    def update(self, id: str, params: SubAccountUpdateParams):
        """
        Updates the specified sub-account.

        Args:
            id (str): The sub-account ID.
            params (SubAccountUpdateParams): Parameters to update.

        Returns:
            SubAccount: The updated sub-account object.
        """
        return self.request(
            "put",
            f"/v1/sub-accounts/{id}",
            headers=self.get_headers(),
            json={"data": {**params}},
        )
