from typing import TypedDict


class SubAccount(TypedDict):
    """
    Representation of a SubAccount.
    """

    id: str
    business_name: str
    settlement_code: str  # "wave" or "afrimoney"
    account_number: int
    percentage: float
    business_id: str
    account_id: str
    test_mode: bool
    active: bool
    balance: float


class SubAccountParams(TypedDict):
    """
    Parameters required to create a SubAccount.
    Only includes business_name, percentage, settlement_code, and account_number.
    """

    business_name: str
    percentage: float
    settlement_code: str  # "wave" or "afrimoney"
    account_number: int


class SubAccountUpdateParams(TypedDict, total=False):
    """
    Parameters required to update a SubAccount.
    All fields are optional: active, settlement_code, account_number, and percentage.
    """

    active: bool
    settlement_code: str  # "wave" or "afrimoney"
    account_number: int
    percentage: float
