from attrs import define
import os
import time
import sys
import threading
import requests
from .models import (
    SearchResponse, SearchResult, NENTagResponse,
    SyncStartResponse, SyncStatusResponse, FailedDocumentInfo
)
from typing import Optional
from urllib.parse import quote
from uuid import UUID
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

@define
class COB:

    apikey: str | None = os.getenv("COB_APIKEY")
    apiurl: str = "https://www.api.cob.vondr.ai"

    def search(self, question: str, top_n: int = 8, sort: Optional[str] = None, show_full_summary: bool = False) -> SearchResponse:
        """
        Search for documents based on a query.

        Args:
            question: The search query.
            top_n: The number of results to return (1-100).
            sort: Sort order for results by date. Can be "newest_first" or "oldest_first".
            show_full_summary: If True, shows the full summary instead of short summary.

        Returns:
            SearchResponse object with detailed results.
        """
        if not self.apikey:
            raise ValueError("COB_APIKEY environment variable not set or provided.")

        headers = {"Authorization": f"bearer {self.apikey}"}

        params = {"top_n": top_n}
        if sort:
            if sort not in ["newest_first", "oldest_first"]:
                raise ValueError("Invalid sort option. Use 'newest_first' or 'oldest_first'.")
            params["sort"] = sort

        encoded_question = quote(question, safe='')
        url = f"{self.apiurl}/search/?question={encoded_question}"

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()

        search_results = []
        for r in data.get("results", []):
            nen_tag_data = r.get("NEN_tag")
            nen_tag = NENTagResponse(**nen_tag_data) if nen_tag_data else None

            date_str = r.get("date")
            doc_date = datetime.fromisoformat(date_str) if date_str else None

            search_results.append(
                SearchResult(
                    doc_id=UUID(r["doc_id"]),
                    filename=r["filename"],
                    sharepoint_link=r["sharepoint_link"],
                    sharepoint_folder_link=r.get("sharepoint_folder_link"),
                    short_summary=r["short_summary"],
                    summary=r["summary"],
                    doc_type=r["doc_type"],
                    tunnel=r["tunnel"],
                    tunnel_object=r.get("tunnel_object"),
                    NEN_tag=nen_tag,
                    date=doc_date,
                )
            )

        # Set the display preference for all results
        for result in search_results:
            result.show_full_summary = show_full_summary

        search_response = SearchResponse(
            id=UUID(data["id"]),
            question=data["question"],
            results=search_results,
            response_time=data["response_time"],
            sort_order=sort
        )
        print(search_response)
        return search_response

    def _show_status_animation(self, stop_event: threading.Event, message: str = "Checking"):
        """Show a rotating animation while an operation is in progress."""
        animation_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        i = 0

        while not stop_event.is_set():
            sys.stdout.write(f'\r{animation_chars[i % len(animation_chars)]} {message}...')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

        sys.stdout.write('\r' + ' ' * (len(message) + 10) + '\r')
        sys.stdout.flush()

    def start_sync(self, wait_for_completion: bool = False, check_interval: int = 5) -> SyncStartResponse:
        """
        Start a background sync operation.

        Args:
            wait_for_completion: If True, waits for sync to complete by polling status.
            check_interval: Seconds between status checks when waiting.

        Returns:
            SyncStartResponse with success status and message.
        """
        if not self.apikey:
            raise ValueError("COB_APIKEY environment variable not set or provided.")

        print("🔄 Starting sync with SharePoint...")

        try:
            headers = {"Authorization": f"bearer {self.apikey}"}
            response = requests.post(f"{self.apiurl}/sync/", headers=headers)

            if response.status_code == 409:
                print("⚠️  A sync is already running!")
                return SyncStartResponse(success=False, message="A sync operation is already in progress")

            response.raise_for_status()

            start_response = SyncStartResponse(**response.json())
            print(start_response)

            if start_response.success and wait_for_completion:
                print("\n📊 Waiting for sync to complete... (Press Ctrl+C to stop waiting)\n")

                stop_event = threading.Event()
                animation_thread = threading.Thread(target=self._show_status_animation, args=(stop_event, "Syncing"))
                animation_thread.daemon = True
                animation_thread.start()

                try:
                    while True:
                        time.sleep(check_interval)
                        status = self._get_status_quietly()

                        if not status.is_sync_running:
                            stop_event.set()
                            animation_thread.join(timeout=1)
                            print("✅ Sync completed!")
                            print(status)
                            break

                        if status.sync_runtime_seconds:
                            minutes, seconds = divmod(int(status.sync_runtime_seconds), 60)
                            time_str = f"({minutes}m {seconds}s)"
                            # This part is a bit tricky in a simple thread; we just restart it with a new message
                            stop_event.set()
                            animation_thread.join(timeout=0.5)
                            stop_event = threading.Event()
                            animation_thread = threading.Thread(target=self._show_status_animation, args=(stop_event, f"Syncing {time_str}"))
                            animation_thread.daemon = True
                            animation_thread.start()

                except KeyboardInterrupt:
                    stop_event.set()
                    animation_thread.join(timeout=1)
                    print("\n\n⏸️  Stopped waiting. Sync continues in background.")
                    print("Use .status() to check progress later.\n")

            return start_response

        except Exception as e:
            print(f"❌ Failed to start sync: {str(e)}")
            raise

    def _get_status_quietly(self) -> SyncStatusResponse:
        """Get status without printing (for internal use)."""
        headers = {"Authorization": f"bearer {self.apikey}"}
        response = requests.get(f"{self.apiurl}/sync/status", headers=headers)
        response.raise_for_status()

        data = response.json()
        failed_docs_data = data.get("failed_documents", [])
        data["failed_documents"] = [FailedDocumentInfo(**doc) for doc in failed_docs_data]

        return SyncStatusResponse(**data)

    def status(self) -> SyncStatusResponse:
        """
        Get the current sync status.
        """
        if not self.apikey:
            raise ValueError("COB_APIKEY environment variable not set or provided.")

        print("📊 Fetching sync status...")
        stop_event = threading.Event()
        animation_thread = threading.Thread(target=self._show_status_animation, args=(stop_event, "Loading status"))
        animation_thread.daemon = True
        animation_thread.start()

        try:
            status_response = self._get_status_quietly()
            stop_event.set()
            animation_thread.join(timeout=1)
            print(status_response)
            return status_response

        except Exception as e:
            stop_event.set()
            animation_thread.join(timeout=1)
            print(f"❌ Failed to get status: {str(e)}")
            raise

    def sync(self, wait: bool = True) -> SyncStartResponse:
        """
        Start a sync operation (backward compatibility wrapper).
        """
        return self.start_sync(wait_for_completion=wait)