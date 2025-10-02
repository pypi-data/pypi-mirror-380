#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

"""
Behavior Evidence Data Structure.

Represents evidence found during behavior analysis,
including the type, content, location, and context.
"""

from dataclasses import dataclass
from typing import Any
from typing import Optional


@dataclass
class BehaviorEvidence:
    """Data structure representing evidence of a behavior."""

    # Evidence content and type
    type: str  # 'string', 'code', 'permission', 'activity', 'service', 'receiver', 'metadata'
    content: str
    location: str = ""

    # Pattern matching information
    pattern_matched: Optional[str] = None

    # Code location information
    class_name: Optional[str] = None
    line_number: Optional[int] = None
    dex_index: Optional[int] = None

    # Additional context
    confidence: float = 1.0  # Confidence level 0.0-1.0
    additional_data: Optional[dict[str, Any]] = None

    def to_dict(self) -> dict[str, Any]:
        """Convert evidence to dictionary format for JSON serialization."""
        result = {"type": self.type, "content": self.content, "location": self.location, "confidence": self.confidence}

        # Add optional fields if they have values
        if self.pattern_matched:
            result["pattern_matched"] = self.pattern_matched
        if self.class_name:
            result["class_name"] = self.class_name
        if self.line_number is not None:
            result["line_number"] = self.line_number
        if self.dex_index is not None:
            result["dex_index"] = self.dex_index
        if self.additional_data:
            result["additional_data"] = self.additional_data

        return result

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "BehaviorEvidence":
        """Create BehaviorEvidence from dictionary."""
        return cls(
            type=data.get("type", ""),
            content=data.get("content", ""),
            location=data.get("location", ""),
            pattern_matched=data.get("pattern_matched"),
            class_name=data.get("class_name"),
            line_number=data.get("line_number"),
            dex_index=data.get("dex_index"),
            confidence=data.get("confidence", 1.0),
            additional_data=data.get("additional_data"),
        )

    def is_high_confidence(self) -> bool:
        """Check if this evidence has high confidence."""
        return self.confidence >= 0.8

    def is_code_evidence(self) -> bool:
        """Check if this evidence comes from code analysis."""
        return self.type == "code"

    def is_permission_evidence(self) -> bool:
        """Check if this evidence comes from permission analysis."""
        return self.type == "permission"

    def is_string_evidence(self) -> bool:
        """Check if this evidence comes from string analysis."""
        return self.type == "string"

    def get_summary(self) -> str:
        """Get a human-readable summary of the evidence."""
        if self.pattern_matched:
            return f"{self.type}: {self.content} (matched: {self.pattern_matched})"
        else:
            return f"{self.type}: {self.content}"
