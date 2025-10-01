from typing import Dict, TypedDict, Union


class v1_NewSessionResponse(TypedDict):
    code: str
    url: str
    renewed: bool
    expires_at: str


class v1_PlatformAccount(TypedDict):
    id: str


class v1_AccountResponse(TypedDict):
    roblox: v1_PlatformAccount
    discord: v1_PlatformAccount


v1_AccountsResponse = Dict[str, Union[v1_AccountResponse, None]]
