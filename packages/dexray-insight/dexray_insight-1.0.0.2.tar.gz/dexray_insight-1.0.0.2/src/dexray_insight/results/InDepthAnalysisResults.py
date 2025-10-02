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

"""In-depth analysis results module for comprehensive APK analysis data aggregation."""

import json
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Optional

from ..Utils.file_utils import CustomJSONEncoder


@dataclass
class Results:
    """
    Represents the in-depth analysis results of an APK file.

    Attributes:
        intents (str): List of intent filters in the APK.
        filtered_permissions (str): Filtered critical permissions.
        signatures (str): Signature analysis results.
        strings_ip (list): List of IP addresses found in the APK.
        strings_domain (list): List of domains found in the APK.
        strings_urls (list): List of URLs found in the APK.
        strings_emails (list): List of email addresses found in the APK.
        dotnetMono_assemblies (list): List of .NET assemblies used in the APK
        strings_props (list): List of a dict of properties and its description in the APK
        signature_koodous (str): Koodous signature check result.
        signatures_vt (str): VirusTotal signature check result.
        apk_name (str): Name of the APK file.
        additional_data (dict): Additional analysis results.
    """

    intents: list[str] = field(default_factory=list)
    filtered_permissions: list[str] = field(default_factory=list)
    signatures: dict[str, Optional[Any]] = field(default_factory=lambda: {"koodous": None, "vt": None, "triage": None})
    strings_ip: list[str] = field(default_factory=list)
    strings_domain: list[str] = field(default_factory=list)
    strings_props: list[str] = field(default_factory=list)
    strings_urls: list[str] = field(default_factory=list)
    strings_emails: list[str] = field(default_factory=list)
    dotnetMono_assemblies: list[str] = field(default_factory=list)
    apk_name: str = ""
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Combined results
    additional_data: dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> str:
        """Serialize the object into a JSON string."""
        return json.dumps(asdict(self), cls=CustomJSONEncoder, indent=4)

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary (JSON-compatible)."""
        return asdict(self)

    def print_results(self):
        """Print the results in a formatted JSON style."""
        print(self.to_json())

    def update_additional_data(self, key: str, value: Any):
        """Add or update additional data not directly tied to class attributes."""
        self.additional_data[key] = value

    def extend_from_dict(self, updates: dict[str, Any]):
        """Update attributes or additional_data dynamically from a dictionary."""
        for key, value in updates.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                self.additional_data[key] = value

    def pretty_print(self):
        """Pretty print the in-depth analysis results, showing only non-empty fields."""
        print(f"\nResults for: {self.apk_name}\n")
        for field_name, field_value in self.to_dict().items():
            if field_value:  # Only print non-empty fields
                field_title = field_name.replace("_", " ").title()
                print(f"=== {field_title} ===")
                if isinstance(field_value, list):
                    for item in field_value:
                        print(f"- {item}")
                elif isinstance(field_value, dict):
                    for sub_key, sub_value in field_value.items():
                        print(f"{sub_key.replace('_', ' ').title()}: {sub_value}")
                else:
                    print(field_value)
                print()  # Add space between sections

    def pretty_print2(self):
        """Pretty print the in-depth analysis results, showing only non-empty fields."""
        print(f"\nResults for: {self.apk_name}\n")

        # Iterate through all fields and print non-empty ones
        for field_name, field_value in self.to_dict().items():
            if field_value:  # Print only if the field has a value
                # Format the field name for display
                field_title = field_name.replace("_", " ").title()
                print(f"=== {field_title} ===")

                # Print the value based on its type
                if isinstance(field_value, list):
                    for item in field_value:
                        print(f"- {item}")
                elif isinstance(field_value, dict):
                    for sub_key, sub_value in field_value.items():
                        print(f"{sub_key.replace('_', ' ').title()}: {sub_value}")
                else:
                    print(field_value)
                print()  # Blank line for better readability
