import asyncio
from typing import Any, Dict, Optional, Callable, List, cast
from .transport_http import SyncHTTP
from .transport_ws import SyncWS
from .validators import (
    require_nonempty_str, validate_volume, validate_rating,
    validate_queue_index, validate_item_type, validate_am_url
)
from .types import RepeatMode, ItemType, QueueIndex, NowPlayingInfo
from .exceptions import NotSupportedError, AuthenticationError, ConnectionError, APIServerError, ValidationError

class CiderClient:
    """Synchronous client for the Cider v2 local API (HTTP + Socket.IO).

    Args:
        host: Cider RPC host (default: "localhost").
        port: Cider RPC port (default: 10767).
        api_token: Optional API token if Cider requires authentication.
        auto_reconnect: Auto-reconnect WebSocket on disconnect.
        timeout: HTTP timeout in seconds.
        use_ws: Create a WebSocket client for real-time events.
    """

    def __init__(
        self,
        host: str = "localhost",
        port: int = 10767,
        api_token: Optional[str] = None,
        auto_reconnect: bool = True,
        timeout: float = 10.0,
        use_ws: bool = True
    ):
        base = f"http://{host}:{port}/api"
        self.http = SyncHTTP(base_url=base, api_token=api_token, timeout=timeout)
        self.ws = SyncWS(url=f"http://{host}:{port}", api_token=api_token, auto_reconnect=auto_reconnect) if use_ws else None
        self.auto_reconnect = auto_reconnect

    # Connection helpers
    def connect_ws(self):
        """Establish the WebSocket (Socket.IO) connection.

        Raises:
            AuthenticationError: Invalid/missing token when required.
            ConnectionError: Network/socket connection issue.
        """
        if self.ws:
            self.ws.connect()

    def disconnect_ws(self):
        """Close the WebSocket connection (no-op if not created)."""
        if self.ws:
            self.ws.disconnect()

    # Playback status
    def ping(self) -> bool:
        """Check if the RPC service is active.

        Returns:
            True if Cider responded (204/ok), else False.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        try:
            r = self.http.get("/v1/playback/active")
            return True if r.get("status") == "ok" else False
        except:
            return False
            
    def is_playing(self) -> bool:
        """Return current playback state.

        Returns:
            True if playing, False otherwise.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        r = self.http.get("/v1/playback/is-playing")
        return bool(r.get("is_playing"))

    def now_playing(self) -> NowPlayingInfo:
        """Fetch the now-playing metadata blob.

        Returns:
            Dict with Apple Music track info and playback fields.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        r = self.http.get("/v1/playback/now-playing")
        return cast(NowPlayingInfo, r)

    # Playback control
    def play_url(self, url: str):
        """Play an Apple Music item by share URL.

        Args:
            url: Apple Music URL (https://music.apple.com/...).

        Raises:
            ValidationError: Invalid/empty URL.
            AuthenticationError, ConnectionError, APIServerError
        """
        require_nonempty_str("url", url)
        validate_am_url(url)
        self.http.post("/v1/playback/play-url", {"href": url})

    def play_item_href(self, href: str):
        """Play an item by Apple Music href (as returned by AMAPI).

        Args:
            href: e.g. '/v1/catalog/us/songs/<id>'.

        Raises:
            ValidationError, AuthenticationError, ConnectionError, APIServerError
        """
        require_nonempty_str("href", href)
        self.http.post("/v1/playback/play-item-href", {"href": href})

    def play_item(self, item_type: ItemType, item_id: str):
        """Play an item by type and Apple Music ID.

        Args:
            item_type: 'songs' | 'albums' | 'playlists' | 'stations' | ...
            item_id: Apple Music catalog ID.

        Raises:
            ValidationError, AuthenticationError, ConnectionError, APIServerError
        """
        validate_item_type(item_type)
        require_nonempty_str("item_id", item_id)
        self.http.post("/v1/playback/play-item", {"type": item_type, "id": str(item_id)})

    def play_later(self, item_type: ItemType, item_id: str):
        """Append an item to the end of the queue (Play Later).

        Args:
            item_type: Apple Music type.
            item_id: Apple Music catalog ID.

        Raises:
            ValidationError, AuthenticationError, ConnectionError, APIServerError
        """
        validate_item_type(item_type)
        require_nonempty_str("item_id", item_id)
        self.http.post("/v1/playback/play-later", {"type": item_type, "id": str(item_id)})

    def play_next(self, item_type: ItemType, item_id: str):
        """Insert an item to play next (after current track).

        Args:
            item_type: Apple Music type.
            item_id: Apple Music catalog ID.

        Raises:
            ValidationError, AuthenticationError, ConnectionError, APIServerError
        """
        validate_item_type(item_type)
        require_nonempty_str("item_id", item_id)
        self.http.post("/v1/playback/play-next", {"type": item_type, "id": str(item_id)})

    def play(self):
        """Resume playback.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/play")

    def pause(self):
        """Pause playback.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/pause")

    def playpause(self):
        """Toggle play/pause.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/playpause")

    def stop(self):
        """Stop playback and clear the current track slot.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/stop")

    def next(self):
        """Skip to next item (or Autoplay if queue ends).

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/next")

    def previous(self):
        """Go to previous item (from history if available).

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/previous")

    # Queue
    def get_queue(self) -> list[dict]:
        """Return the current queue list.

        Notes:
            Some builds return a plain list; others wrap under 'queue'/'data'/'items'.

        Returns:
            List of track dicts.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        r = self.http.get("/v1/playback/queue")
        if isinstance(r, list):
            return r
        if isinstance(r, dict):
            for key in ("queue", "data", "items"):
                v = r.get(key)
                if isinstance(v, list):
                    return v
        return []

    def move_queue_item(self, start_index: QueueIndex, destination_index: QueueIndex, return_queue: bool = False):
        """Move a queue item to a new position (1-based indices).

        Args:
            start_index: Source index (1-based).
            destination_index: Destination index (1-based).
            return_queue: If True, server may return updated queue.

        Returns:
            Server response dict.

        Raises:
            ValidationError, AuthenticationError, ConnectionError, APIServerError
        """
        validate_queue_index(start_index)
        validate_queue_index(destination_index)
        payload = {
            "startIndex": int(start_index),
            "destinationIndex": int(destination_index),
            "returnQueue": bool(return_queue),
        }
        return self.http.post("/v1/playback/queue/move-to-position", payload)

    def remove_queue_item(self, index: QueueIndex):
        """Remove an item from the queue by index (1-based).

        Args:
            index: Queue index to remove (1-based).

        Raises:
            ValidationError, AuthenticationError, ConnectionError, APIServerError
        """
        validate_queue_index(index)
        self.http.post("/v1/playback/queue/remove-by-index", {"index": int(index)})

    def clear_queue(self):
        """Clear all upcoming items from the queue.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/queue/clear-queue")

    # Playback settings
    def seek(self, position_seconds: float):
        """Seek to a specific position in the current track.

        Args:
            position_seconds: Target position in seconds (>= 0).

        Raises:
            ValueError: Negative position.
            AuthenticationError, ConnectionError, APIServerError
        """
        if not isinstance(position_seconds, (int, float)) or position_seconds < 0:
            raise ValueError("position_seconds must be a non-negative number")
        self.http.post("/v1/playback/seek", {"position": float(position_seconds)})

    def get_volume(self) -> float:
        """Get the current volume (0.0..1.0).

        Returns:
            Float in [0.0, 1.0].

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        r = self.http.get("/v1/playback/volume")
        v = r.get("volume")
        return float(v) if v is not None else 0.0

    def set_volume(self, volume: float):
        """Set the current volume.

        Args:
            volume: Float in [0.0, 1.0].

        Raises:
            ValidationError: Out of range or wrong type.
            AuthenticationError, ConnectionError, APIServerError
        """
        validate_volume(volume)
        self.http.post("/v1/playback/volume", {"volume": float(volume)})

    def add_current_to_library(self):
        """Add the current track to the user's library (idempotent).

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/add-to-library")

    def set_rating(self, rating: int):
        """Set rating for the current track.

        Args:
            rating: -1 (dislike), 0 (clear), 1 (like).

        Raises:
            ValidationError: Invalid rating.
            AuthenticationError, ConnectionError, APIServerError
        """
        validate_rating(rating)
        self.http.post("/v1/playback/set-rating", {"rating": int(rating)})

    def get_repeat_mode(self) -> RepeatMode:
        """Get repeat mode.

        Returns:
            RepeatMode.OFF (0), RepeatMode.ONE (1), RepeatMode.ALL (2).

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        r = self.http.get("/v1/playback/repeat-mode")
        return RepeatMode(int(r.get("value", r.get("repeat", r.get("mode", 0)))))

    def toggle_repeat(self):
        """Cycle repeat mode: ONE → ALL → OFF → ONE...

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/toggle-repeat")

    def get_shuffle_mode(self) -> bool:
        """Get shuffle state.

        Returns:
            True if shuffle on, False otherwise.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        r = self.http.get("/v1/playback/shuffle-mode")
        val = r.get("value", r.get("shuffle"))
        if val is None:
            val = r.get("shuffleMode", 0)
        return bool(int(val))

    def toggle_shuffle(self):
        """Toggle shuffle on/off.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/toggle-shuffle")

    def get_autoplay(self) -> bool:
        """Get Autoplay setting.

        Returns:
            True if Autoplay is enabled.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        r = self.http.get("/v1/playback/autoplay")
        return bool(r.get("value", False))

    def toggle_autoplay(self):
        """Toggle Autoplay setting.

        Raises:
            AuthenticationError, ConnectionError, APIServerError
        """
        self.http.post("/v1/playback/toggle-autoplay")

    # Apple Music API passthrough
    def amapi_request(self, path: str) -> Dict[str, Any]:
        """Call Apple Music API through Cider.

        Args:
            path: Apple Music API path (e.g. '/v1/catalog/us/search?...').

        Returns:
            Response dict from AMAPI (wrapped by Cider).

        Raises:
            ValidationError, AuthenticationError, ConnectionError, APIServerError
        """
        require_nonempty_str("path", path)
        return self.http.post("/v1/amapi/run-v3", {"path": path})

    # Lyrics (currently non-functional)
    def get_lyrics(self, song_id: str) -> Dict[str, Any]:
        """Attempt to fetch lyrics for a song (currently not supported).

        Args:
            song_id: Apple Music song ID.

        Raises:
            NotSupportedError: Endpoint disabled in current Cider builds.
        """
        require_nonempty_str("song_id", song_id)
        raise NotSupportedError("Lyrics endpoint is currently non-functional per Cider docs")

    # Events (websocket)
    def on(self, event: str, handler: Callable[..., None]):
        """Register a WebSocket event handler.

        Args:
            event: Socket.IO event name.
            handler: Callable accepting (data) or no args.
        """
        if self.ws:
            self.ws.on(event, handler)

    def off(self, event: str):
        """Unregister a WebSocket event handler.

        Args:
            event: Socket.IO event name.
        """
        if self.ws:
            self.ws.off(event)
