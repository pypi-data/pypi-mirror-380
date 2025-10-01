from nexus.websockets import RTS, ConnectionClosed
from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from nexus.api_types.v1 import v1_NewSessionResponse
    from nexus import Nexus


class Session:
    """Represents a Nexus verification session."""

    def __init__(
        self, client: "Nexus", data: "v1_NewSessionResponse", status_code: int, id: int
    ):
        self._client = client
        self._status_code = status_code

        self.id = id
        self.code = data.get("code")
        self.url = data.get("url")
        self.renewed = data.get("renewed")
        self.expires_at = datetime.fromisoformat(
            data.get("expires_at").replace("Z", "+00:00")
        )

    @property
    def reused(self):
        """Whether this session URL has been reused (multiple requests with the same user)."""
        return self._status_code == 200

    async def wait(self):
        """Wait until the verification session is over. Returns whether the session was successful or not (account created/updated)."""
        rts = RTS(self._client._rts_base_url, self._client._nexus_key)
        await rts.connect(f"/sessions/{self.code}")

        try:
            await rts.listen()

            _cached = self._client._cache.discord_accounts.get(self.id)
            if _cached:
                self._client._cache.discord_accounts.delete(_cached.discord.id)
                self._client._cache.roblox_accounts.delete(_cached.roblox.id)

            return True
        except ConnectionClosed:
            return False

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} code={self.code}, reused={self.reused}, renewed={self.renewed}, expires_at={self.expires_at}>"
