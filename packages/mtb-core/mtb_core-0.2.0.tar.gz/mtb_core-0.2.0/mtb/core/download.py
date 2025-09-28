import hashlib
import sys
from pathlib import Path

import requests

from .log import mklog

log = mklog("mtb.core.download")


def resume_download(url: str, filepath: str | Path, *, retries: int = 3, timeout: int = 10) -> bool:
    """
     Resumes a partially downloaded file.  Mimics wget -c behavior.

     Args:
         url: The URL to download from.
         filepath: The path to save the file to.
         retries: The number of times to retry the download if it fails.
         timeout: The timeout for the requests.get call in seconds.

    Returns
    -------
         True if the download was successful (or already complete).
         False if there was an error after all retries.
    """
    filepath = Path(filepath)
    file_size = 0
    if filepath.exists():
        file_size = filepath.stat().st_size
        headers = {"Range": f"bytes={file_size}-"}
    else:
        headers = {}

    for attempt in range(retries):
        try:
            response = requests.get(url, stream=True, headers=headers, timeout=timeout)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            total_size_in_bytes = int(response.headers.get("content-length", 0))

            if total_size_in_bytes == 0:
                log.warning("Could not determine file size from server. Starting fresh download.")
                file_size = 0
                headers = {}  # Start from the beginning

            elif file_size == total_size_in_bytes:
                log.info(f"File already fully downloaded: {filepath}")
                return True  # Already complete

            mode = "ab" if file_size > 0 else "wb"  # Append if resuming, write if new

            with open(filepath, mode) as f:
                downloaded = 0
                for chunk in response.iter_content(chunk_size=8192):  # 8KB chunks
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        file_size += len(chunk)  # Keep track of the file size as we add to it
                        sys.stdout.write(f"\rDownloaded {downloaded} / {total_size_in_bytes} bytes")
                        sys.stdout.flush()  # Ensure output is displayed immediately
                        # log.info(
                        #     f"Downloaded {downloaded} / {total_size_in_bytes} bytes", end="\r"
                        # )  # Progress

            log.info(f"\nDownload complete: {filepath}")
            return True

        except requests.exceptions.RequestException as e:
            log.warning(f"Download attempt {attempt + 1} failed: {e}")
            if attempt == retries - 1:
                log.error(f"Download failed after {retries} attempts.")
                return False  # Failed after all retries
    return False


def compute_hash(filepath: str, algorithm: str = "sha256") -> str | None:
    """
    Compute the hash of a file.

    Args:
        filepath: The path to the file.
        algorithm: The hash algorithm to use (e.g., "sha256", "md5").

    Returns
    -------
        The hex digest of the hash.  Returns None if the file doesn't exist.
    """
    file_path = Path(filepath)
    if not file_path.exists():
        log.warning(f"File {filepath} does not exist, cannot compute hash.")
        return None

    hash_obj = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hash_obj.update(chunk)

    return hash_obj.hexdigest()
