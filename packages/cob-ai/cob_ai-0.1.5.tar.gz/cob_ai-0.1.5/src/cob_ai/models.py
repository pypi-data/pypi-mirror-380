from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional
import textwrap
from uuid import UUID
from datetime import datetime


@dataclass
class SyncStartResponse:
    """Response when starting a sync operation."""
    success: bool
    message: str

    def __str__(self) -> str:
        icon = "✅" if self.success else "❌"
        return f"{icon} {self.message}"


@dataclass
class FailedDocumentInfo:
    filename: str
    folder: str
    error_message: str


@dataclass
class SyncStatusResponse:
    """General sync status information."""
    is_sync_running: bool
    sync_runtime_seconds: Optional[float]
    synced_folders: list[str]
    successfully_synced_count: int
    failed_documents_count: int
    failed_documents: list[FailedDocumentInfo]

    def __str__(self) -> str:
        header = "📈 Sync Status Overview"
        header_separator = "═" * len(header)

        if self.is_sync_running:
            runtime_display = f"⚡ Sync is currently running"
            if self.sync_runtime_seconds:
                minutes, seconds = divmod(int(self.sync_runtime_seconds), 60)
                runtime_display += f" ({minutes}m {seconds}s)"
        else:
            runtime_display = "💤 No sync currently running"

        summary = (
            f"✅ Successfully synced: {self.successfully_synced_count}\n"
            f"❌ Failed documents: {self.failed_documents_count}\n"
            f"📁 Synced folders: {', '.join(self.synced_folders) if self.synced_folders else 'None'}"
        )

        failed_details = ""
        if self.failed_documents:
            failed_details = "\n\n📋 Failed Documents:\n" + "─" * 20
            for i, doc in enumerate(self.failed_documents, 1):
                error_msg = textwrap.fill(doc.error_message, width=60, initial_indent="     ", subsequent_indent="     ").strip()
                failed_details += f"\n  {i}. {doc.filename}\n     📁 {doc.folder}\n     ❌ {error_msg}"

        return (
            f"\n{header}\n{header_separator}\n{runtime_display}\n\n{summary}{failed_details}\n"
        )


@dataclass
class NENTagResponse:
    main_category: str
    subcategory: Optional[str] = None

    def __str__(self) -> str:
        if self.subcategory:
            return f"{self.main_category} / {self.subcategory}"
        return self.main_category


@dataclass
class SearchResult:
    doc_id: UUID
    filename: str
    sharepoint_link: str
    sharepoint_folder_link: Optional[str]
    short_summary: str
    summary: str
    doc_type: str
    tunnel: str
    tunnel_object: Optional[str]
    NEN_tag: Optional[NENTagResponse]
    date: Optional[datetime]
    show_full_summary: bool = False

    def __str__(self) -> str:
        filename_display = f"📄 {self.filename}\n"

        details = f"   Tunnel: {self.tunnel or 'N/A'} | Type: {self.doc_type or 'N/A'}"
        if self.date:
            details += f" | Datum: {self.date.strftime('%Y-%m-%d')}\n"

        if self.show_full_summary:
            # Show both short and full summary
            wrapped_short = textwrap.fill(
                f"📝 Korte samenvatting: {self.short_summary}", width=80, initial_indent="   ", subsequent_indent="   "
            )
            wrapped_full = textwrap.fill(
                f"📋 Volledige samenvatting: {self.summary}", width=80, initial_indent="   ", subsequent_indent="   "
            )
            wrapped_summary = f"{wrapped_short}\n\n{wrapped_full}"
        else:
            # Show only short summary
            wrapped_summary = textwrap.fill(
                self.short_summary, width=80, initial_indent="   ", subsequent_indent="   "
            )

        nen_tag_display = f"\n   NEN2767: {str(self.NEN_tag)}\n" if self.NEN_tag else "\n"

        # Create clickable links using ANSI escape codes, side by side
        links = f"   Links: 📄 \033]8;;{self.sharepoint_link}\033\\Document bekijken\033]8;;\033\\"
        if self.sharepoint_folder_link:
            links += f" | 📁 \033]8;;{self.sharepoint_folder_link}\033\\Map openen\033]8;;\033\\ \n"

        output = [
            filename_display,
            details,
            wrapped_summary,
            nen_tag_display,
            links,
        ]
        return "\n".join(filter(None, output))


@dataclass
class SearchResponse:
    id: UUID
    question: str
    results: List[SearchResult]
    response_time: float
    sort_order: Optional[str] = None

    def __str__(self) -> str:
        header = f"🔍 Search Results for: \"{self.question}\""
        header_separator = "═" * len(header)

        count_info = f"Found {len(self.results)} result{'s' if len(self.results) != 1 else ''} in {self.response_time:.2f}s"

        if self.sort_order:
            sort_text = "nieuwste eerst" if self.sort_order == "newest_first" else "oudste eerst"
            count_info += f" (gesorteerd op {sort_text})"

        results_text = []
        for i, result in enumerate(self.results, 1):
            results_text.append(f"\n--- Resultaat {i} ---\n{result}")

        return (
            f"\n{header}\n{header_separator}\n{count_info}\n"
            f"{''.join(results_text)}\n"
        )