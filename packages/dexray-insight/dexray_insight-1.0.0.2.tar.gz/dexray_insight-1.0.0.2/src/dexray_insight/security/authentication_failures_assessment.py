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

"""Authentication Failures Assessment.

This module implements OWASP A07:2021 - Identification and Authentication Failures assessment.
It identifies weak authentication mechanisms and insecure session management in Android applications.
"""

import logging
from typing import Any

from ..core.base_classes import AnalysisContext
from ..core.base_classes import AnalysisSeverity
from ..core.base_classes import BaseSecurityAssessment
from ..core.base_classes import SecurityFinding
from ..core.base_classes import register_assessment


@register_assessment("authentication_failures")
class AuthenticationFailuresAssessment(BaseSecurityAssessment):
    """OWASP A07:2021 - Identification and Authentication Failures assessment."""

    def __init__(self, config: dict[str, Any]):
        """Initialize authentication failures assessment."""
        super().__init__(config)
        self.logger = logging.getLogger(__name__)
        self.owasp_category = "A07:2021-Identification and Authentication Failures"

        self.authentication_patterns = {
            "weak_credentials": [
                r'password.*=.*["\'](?:password|123456|admin|test)["\']',
                r"SharedPreferences.*putString.*(?:password|token|auth)",
                r'String.*(?:password|pwd).*=.*["\'][^"\']{1,8}["\']',  # Short passwords
            ],
            "session_management": [r"HttpURLConnection.*(?:session|cookie|auth)", r"CookieManager", r"SessionManager"],
        }

        self.session_management_checks = [
            "session timeout implementation",
            "secure session storage",
            "session invalidation",
        ]

    def assess(self, analysis_results: dict[str, Any], context: AnalysisContext | None = None) -> list[SecurityFinding]:
        """Perform authentication failures assessment."""
        findings = []

        try:
            # Check for weak authentication mechanisms
            auth_findings = self._assess_weak_authentication(analysis_results)
            findings.extend(auth_findings)

            # Check session management
            session_findings = self._assess_session_management(analysis_results)
            findings.extend(session_findings)

        except Exception as e:
            self.logger.error(f"Authentication failures assessment failed: {str(e)}")

        return findings

    def _assess_weak_authentication(self, analysis_results: dict[str, Any]) -> list[SecurityFinding]:
        findings = []

        string_results = analysis_results.get("string_analysis", {})
        string_data = string_results.to_dict() if hasattr(string_results, "to_dict") else string_results
        all_strings = string_data.get("all_strings", [])

        auth_issues = []
        weak_patterns = self.authentication_patterns["weak_credentials"]

        for string in all_strings:
            if isinstance(string, str):
                for pattern in weak_patterns:
                    import re

                    try:
                        if re.search(pattern, string, re.IGNORECASE):
                            auth_issues.append(f"Weak credential pattern: {string[:80]}...")
                            break
                    except Exception as e:
                        self.logger.debug(f"Regex pattern error for pattern '{pattern}': {e}")
                        continue

        # Check manifest for missing biometric permissions
        manifest_results = analysis_results.get("manifest_analysis", {})
        manifest_data = manifest_results.to_dict() if hasattr(manifest_results, "to_dict") else manifest_results
        permissions = manifest_data.get("permissions", [])

        has_biometric = any("FINGERPRINT" in p or "BIOMETRIC" in p for p in permissions)
        if not has_biometric:
            auth_issues.append("No biometric authentication permissions detected")

        if auth_issues:
            findings.append(
                SecurityFinding(
                    category=self.owasp_category,
                    severity=AnalysisSeverity.HIGH,
                    title="Weak Authentication Mechanisms",
                    description="Application uses weak authentication mechanisms or stores credentials insecurely.",
                    evidence=auth_issues[:8],
                    recommendations=[
                        "Implement strong authentication mechanisms",
                        "Use biometric authentication for sensitive operations",
                        "Store credentials securely using Android Keystore",
                        "Implement proper password policies",
                        "Use multi-factor authentication where appropriate",
                    ],
                )
            )

        return findings

    def _assess_session_management(self, analysis_results: dict[str, Any]) -> list[SecurityFinding]:
        findings = []

        string_results = analysis_results.get("string_analysis", {})
        string_data = string_results.to_dict() if hasattr(string_results, "to_dict") else string_results
        all_strings = string_data.get("all_strings", [])

        session_issues = []
        session_patterns = self.authentication_patterns["session_management"]

        has_session_management = False
        for string in all_strings:
            if isinstance(string, str):
                for pattern in session_patterns:
                    import re

                    if re.search(pattern, string, re.IGNORECASE):
                        has_session_management = True
                        # Check for insecure session handling
                        if "timeout" not in string.lower() and "expire" not in string.lower():
                            session_issues.append(f"Session management without timeout: {string[:80]}...")

        if has_session_management and not session_issues:
            # Session management detected but no obvious issues
            pass
        elif session_issues:
            findings.append(
                SecurityFinding(
                    category=self.owasp_category,
                    severity=AnalysisSeverity.MEDIUM,
                    title="Insecure Session Management",
                    description="Application implements session management but lacks proper security controls.",
                    evidence=session_issues,
                    recommendations=[
                        "Implement proper session timeout mechanisms",
                        "Use secure session storage practices",
                        "Implement session invalidation on logout",
                        "Use secure cookie attributes for web sessions",
                        "Monitor and log authentication events",
                    ],
                )
            )

        return findings
