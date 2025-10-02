#!/usr/bin/env python3
"""Results container for tracker analysis findings and statistics."""

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# # Copyright (C) {{ year }} Dexray Insight Contributors
# #
# # This file is part of Dexray Insight - Android APK Security Analysis Tool
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

from dataclasses import dataclass
from typing import Any


@dataclass
class TrackerAnalysisResults:
    """Results container for tracker analysis with formatting methods."""

    detected_trackers: list[dict[str, Any]]
    total_trackers: int
    exodus_trackers: list[dict[str, Any]]
    custom_detections: list[dict[str, Any]]
    analysis_errors: list[str]
    execution_time: float

    def __init__(self, tracker_result):
        """Initialize from TrackerAnalysisResult object."""
        self.detected_trackers = [tracker.to_dict() for tracker in tracker_result.detected_trackers]
        self.total_trackers = tracker_result.total_trackers
        self.exodus_trackers = tracker_result.exodus_trackers
        self.custom_detections = [tracker.to_dict() for tracker in tracker_result.custom_detections]
        self.analysis_errors = tracker_result.analysis_errors
        self.execution_time = tracker_result.execution_time

    def get_summary(self) -> str:
        """Get a human-readable summary of tracker analysis results."""
        if self.total_trackers == 0:
            return "🟢 No trackers detected in this APK"

        summary_lines = [f"📍 **{self.total_trackers} tracker{'s' if self.total_trackers != 1 else ''} detected**\n"]

        # Group trackers by category
        by_category: dict[str, list[dict[str, Any]]] = {}
        for tracker in self.detected_trackers:
            category = tracker.get("category", "Unknown")
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(tracker)

        # Display by category
        for category, trackers in by_category.items():
            summary_lines.append(f"**{category}:**")
            for tracker in trackers:
                name = tracker["name"]
                version = f" (v{tracker['version']})" if tracker.get("version") else ""
                confidence = tracker.get("confidence", 1.0)
                confidence_icon = "🔴" if confidence >= 0.9 else "🟡" if confidence >= 0.7 else "🟠"
                summary_lines.append(f"  {confidence_icon} {name}{version}")
            summary_lines.append("")

        if self.analysis_errors:
            summary_lines.append("⚠️  **Analysis Warnings:**")
            for error in self.analysis_errors:
                summary_lines.append(f"  • {error}")

        return "\n".join(summary_lines)

    def get_console_summary(self) -> str:
        """Get a console-friendly summary without markdown."""
        if self.total_trackers == 0:
            return "✓ No trackers detected in this APK"

        summary_lines = [f"📍 {self.total_trackers} tracker{'s' if self.total_trackers != 1 else ''} detected:", ""]

        # Group trackers by category for better organization
        by_category: dict[str, list[dict[str, Any]]] = {}
        for tracker in self.detected_trackers:
            category = tracker.get("category", "Unknown")
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(tracker)

        # Display by category
        for category, trackers in by_category.items():
            summary_lines.append(f"{category}:")
            for tracker in trackers:
                name = tracker["name"]
                version = f" (v{tracker['version']})" if tracker.get("version") else ""
                confidence = tracker.get("confidence", 1.0)
                confidence_icon = "●" if confidence >= 0.9 else "◐" if confidence >= 0.7 else "○"
                summary_lines.append(f"  {confidence_icon} {name}{version}")
            summary_lines.append("")

        return "\n".join(summary_lines)

    def get_detailed_results(self) -> dict[str, Any]:
        """Get detailed results for JSON export."""
        return {
            "tracker_analysis": {
                "total_trackers_detected": self.total_trackers,
                "detected_trackers": self.detected_trackers,
                "analysis_errors": self.analysis_errors,
                "execution_time_seconds": round(self.execution_time, 2),
                "detection_sources": {
                    "built_in_database": len(self.custom_detections),
                    "exodus_privacy_api": len(self.exodus_trackers),
                },
            }
        }

    def get_tracker_by_name(self, name: str) -> dict[str, Any] | None:
        """Get specific tracker details by name."""
        for tracker in self.detected_trackers:
            if tracker["name"].lower() == name.lower():
                return tracker
        return None

    def get_trackers_by_category(self, category: str) -> list[dict[str, Any]]:
        """Get all trackers in a specific category."""
        return [
            tracker for tracker in self.detected_trackers if tracker.get("category", "").lower() == category.lower()
        ]

    def get_high_confidence_trackers(self, threshold: float = 0.9) -> list[dict[str, Any]]:
        """Get trackers with confidence above threshold."""
        return [tracker for tracker in self.detected_trackers if tracker.get("confidence", 0) >= threshold]

    def export_to_dict(self) -> dict[str, Any]:
        """Export all results to dictionary format."""
        return {
            "detected_trackers": self.detected_trackers,
            "total_trackers": self.total_trackers,
            "exodus_trackers": self.exodus_trackers,
            "custom_detections": self.custom_detections,
            "analysis_errors": self.analysis_errors,
            "execution_time": self.execution_time,
        }
