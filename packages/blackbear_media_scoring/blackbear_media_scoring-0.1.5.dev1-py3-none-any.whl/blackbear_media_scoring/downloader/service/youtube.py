"""Utilities for downloading segments of YouTube videos using yt-dlp."""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any, Dict, Optional, Tuple
from urllib.parse import urlparse

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError, ExtractorError, download_range_func


class Youtube:
    """Download specific segments of YouTube videos.

    The downloader uses yt-dlp to retrieve metadata and download a trimmed clip for the
    requested time range. When no time range is provided the entire video is downloaded.
    """

    def __init__(self, output_dir: Optional[str] = None, debug: bool = False) -> None:
        """Initialize the Youtube downloader service.

        Args:
            output_dir: Directory where downloaded files will be stored. If not provided,
                the system temporary directory is used.
            debug: When ``True``, enables verbose logging from yt-dlp to stdout.
        """
        base_dir = (
            Path(output_dir).expanduser()
            if output_dir and output_dir.strip()
            else Path(tempfile.gettempdir())
        )
        self._output_dir: Path = base_dir.resolve()
        self._output_dir.mkdir(parents=True, exist_ok=True)
        self._debug = debug

    def download(
        self, url: str, start_time: Optional[int] = None, end_time: Optional[int] = None
    ) -> str:
        """Download a segment from the specified YouTube video.

        Args:
            url: Fully qualified URL of the YouTube video to download.
            start_time: Start of the desired clip in seconds. Defaults to ``0``.
            end_time: End of the desired clip in seconds. Defaults to the video's full
                duration.

        Returns:
            The absolute file path of the downloaded segment.

        Raises:
            ValueError: If the URL is invalid, the time range is invalid, or the download
                fails.
        """
        self._validate_url(url)

        start_seconds = self._coerce_time(start_time, default=0)
        if start_seconds < 0:
            raise ValueError("start_time must be non-negative")

        metadata = self._extract_metadata(url)
        video_id = metadata.get("id")
        if not video_id:
            raise ValueError("Unable to determine video ID from the provided URL")

        duration = metadata.get("duration")
        end_seconds = self._resolve_end_time(end_time, duration)

        if end_seconds is not None and end_seconds <= start_seconds:
            raise ValueError("end_time must be greater than start_time")

        download_path, info = self._download_segment(url, start_seconds, end_seconds)
        effective_end = self._determine_effective_end(end_seconds, metadata, info)
        target_path = self._rename_to_spec(
            download_path, video_id, start_seconds, effective_end
        )
        return str(target_path)

    def _validate_url(self, url: str) -> None:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Invalid URL: expected an absolute YouTube URL")
        hostname = parsed.netloc.lower()
        if not any(domain in hostname for domain in ("youtube.com", "youtu.be")):
            raise ValueError("Invalid URL: only YouTube URLs are supported")

    def _coerce_time(self, value: Optional[int], default: int) -> int:
        return int(value) if value is not None else default

    def _extract_metadata(self, url: str) -> Dict[str, Any]:
        options = {
            "quiet": not self._debug,
            "no_warnings": not self._debug,
            "skip_download": True,
            "noplaylist": True,
        }
        try:
            with YoutubeDL(options) as ydl:
                return ydl.extract_info(url, download=False)
        except (DownloadError, ExtractorError) as exc:
            raise ValueError(f"Failed to retrieve video metadata: {exc}") from exc

    def _resolve_end_time(
        self, end_time: Optional[int], duration: Optional[int]
    ) -> Optional[int]:
        if end_time is not None:
            coerced_end = int(end_time)
            if coerced_end < 0:
                raise ValueError("end_time must be non-negative")
            return coerced_end
        if duration is None:
            return None
        return int(duration)

    def _download_segment(
        self, url: str, start_seconds: int, end_seconds: Optional[int]
    ) -> Tuple[Path, Dict[str, Any]]:
        options: Dict[str, Any] = {
            "quiet": not self._debug,
            "no_warnings": not self._debug,
            "outtmpl": str(self._output_dir / "%(id)s.%(ext)s"),
            "restrictfilenames": True,
            "noplaylist": True,
            "paths": {"home": str(self._output_dir)},
            "force_keyframes_at_cuts": True,
            "format": "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<=720]/best",
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": "mp4",
                }
            ],
        }

        if start_seconds > 0 or end_seconds is not None:
            ranges: Tuple[Tuple[float, Optional[float]], ...] = (
                (
                    float(start_seconds),
                    float(end_seconds) if end_seconds is not None else None,
                ),
            )
            options["download_ranges"] = download_range_func(None, ranges)

        try:
            with YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=True)
        except (DownloadError, ExtractorError) as exc:
            raise ValueError(f"Failed to download video segment: {exc}") from exc

        return self._extract_filepath(info), info

    def _extract_filepath(self, info: Dict[str, Any]) -> Path:
        requested = info.get("requested_downloads") or []
        for item in requested:
            filepath = item.get("filepath") or item.get("_filename")
            if filepath:
                return Path(filepath).resolve()

        for key in ("filepath", "_filename"):
            if key in info and info[key]:
                return Path(info[key]).resolve()

        raise ValueError("yt-dlp did not return a filepath for the downloaded video")

    def _determine_effective_end(
        self,
        requested_end: Optional[int],
        metadata: Dict[str, Any],
        info: Dict[str, Any],
    ) -> int:
        if requested_end is not None:
            return requested_end

        duration = metadata.get("duration")
        if isinstance(duration, (int, float)):
            return int(duration)

        requested_downloads = info.get("requested_downloads") or []
        for item in requested_downloads:
            end_time: Optional[float] = item.get("end_time")
            if end_time is not None:
                return int(end_time)

        raise ValueError("Unable to determine end time for the downloaded segment")

    def _rename_to_spec(
        self,
        downloaded_path: Path,
        video_id: str,
        start_seconds: int,
        end_seconds: int,
    ) -> Path:
        target_name = f"{video_id}_s{start_seconds}_e{end_seconds}.mp4"
        target_path = self._output_dir / target_name

        if downloaded_path.resolve() == target_path.resolve():
            return target_path

        target_path.parent.mkdir(parents=True, exist_ok=True)
        return downloaded_path.replace(target_path)

