#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Android manifest analysis module for intent filters and components."""

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

import logging
import time
from dataclasses import dataclass
from typing import Any

from ..core.base_classes import AnalysisContext
from ..core.base_classes import AnalysisStatus
from ..core.base_classes import BaseAnalysisModule
from ..core.base_classes import BaseResult
from ..core.base_classes import register_module


@dataclass
class ManifestAnalysisResult(BaseResult):
    """Result class for manifest analysis."""

    package_name: str = ""
    main_activity: str = ""
    permissions: list[str] = None
    activities: list[str] = None
    services: list[str] = None
    receivers: list[str] = None
    content_providers: list[str] = None
    intent_filters: list[dict[str, Any]] = None
    manifest_xml: str = ""

    def __post_init__(self):
        """Initialize default values for optional fields."""
        if self.permissions is None:
            self.permissions = []
        if self.activities is None:
            self.activities = []
        if self.services is None:
            self.services = []
        if self.receivers is None:
            self.receivers = []
        if self.content_providers is None:
            self.content_providers = []
        if self.intent_filters is None:
            self.intent_filters = []

    def to_dict(self) -> dict[str, Any]:
        """Convert result to dictionary."""
        base_dict = super().to_dict()
        base_dict.update(
            {
                "package_name": self.package_name,
                "main_activity": self.main_activity,
                "permissions": self.permissions,
                "activities": self.activities,
                "services": self.services,
                "receivers": self.receivers,
                "content_providers": self.content_providers,
                "intent_filters": self.intent_filters,
                "components_summary": {
                    "total_activities": len(self.activities),
                    "total_services": len(self.services),
                    "total_receivers": len(self.receivers),
                    "total_providers": len(self.content_providers),
                    "total_permissions": len(self.permissions),
                },
            }
        )
        return base_dict


@register_module("manifest_analysis")
class ManifestAnalysisModule(BaseAnalysisModule):
    """Manifest analysis module for extracting AndroidManifest.xml information."""

    def __init__(self, config: dict[str, Any]):
        """Initialize ManifestAnalysisModule with configuration."""
        super().__init__(config)
        self.logger = logging.getLogger(__name__)
        self.extract_intent_filters = config.get("extract_intent_filters", True)
        self.analyze_exported_components = config.get("analyze_exported_components", True)

    def get_dependencies(self) -> list[str]:
        """No dependencies for manifest analysis."""
        return []

    def analyze(self, apk_path: str, context: AnalysisContext) -> ManifestAnalysisResult:
        """
        Perform manifest analysis on the APK.

        Args:
            apk_path: Path to the APK file
            context: Analysis context

        Returns:
            ManifestAnalysisResult with analysis results
        """
        start_time = time.time()

        try:
            if not context.androguard_obj:
                raise ValueError("Androguard object not available in context")

            apk = context.androguard_obj.get_androguard_apk()

            # Extract basic information
            package_name = apk.get_package() or ""
            main_activity = apk.get_main_activity() or ""
            permissions = list(apk.get_permissions()) or []
            activities = list(apk.get_activities()) or []
            services = list(apk.get_services()) or []
            receivers = list(apk.get_receivers()) or []
            content_providers = list(apk.get_providers()) or []

            # Extract intent filters if enabled
            intent_filters = []
            if self.extract_intent_filters:
                intent_filters = self._extract_intent_filters(apk, services, receivers)

            # Get manifest XML if needed
            manifest_xml = ""
            try:
                manifest_xml = apk.get_android_manifest_xml()
            except Exception as e:
                self.logger.warning(f"Could not extract manifest XML: {str(e)}")

            execution_time = time.time() - start_time

            result = ManifestAnalysisResult(
                module_name=self.name,
                status=AnalysisStatus.SUCCESS,
                execution_time=execution_time,
                package_name=package_name,
                main_activity=main_activity,
                permissions=permissions,
                activities=activities,
                services=services,
                receivers=receivers,
                content_providers=content_providers,
                intent_filters=intent_filters,
                manifest_xml=manifest_xml,
            )

            # Check for Mono runtime (for compatibility with existing code)
            if "mono.MonoRuntimeProvider" in content_providers:
                # Add runtime information to context for other modules
                context.add_result("runtime_detected", "dotnetMono")

            return result

        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"Manifest analysis failed: {str(e)}")

            return ManifestAnalysisResult(
                module_name=self.name,
                status=AnalysisStatus.FAILURE,
                execution_time=execution_time,
                error_message=str(e),
            )

    def _extract_intent_filters(self, apk, services: list[str], receivers: list[str]) -> list[dict[str, Any]]:
        """Extract intent filters from services and receivers."""
        intent_filters = []

        try:
            # Process services
            for service in services:
                try:
                    intent_filter = apk.get_intent_filters("service", service)
                    if intent_filter:
                        intent_filters.append(
                            {"component_type": "service", "component_name": service, "filters": intent_filter}
                        )
                except Exception as e:
                    self.logger.warning(f"Failed to get intent filters for service {service}: {str(e)}")

            # Process receivers
            for receiver in receivers:
                try:
                    intent_filter = apk.get_intent_filters("receiver", receiver)
                    if intent_filter:
                        intent_filters.append(
                            {"component_type": "receiver", "component_name": receiver, "filters": intent_filter}
                        )
                except Exception as e:
                    self.logger.warning(f"Failed to get intent filters for receiver {receiver}: {str(e)}")

        except Exception as e:
            self.logger.error(f"Failed to extract intent filters: {str(e)}")

        return intent_filters

    def validate_config(self) -> bool:
        """Validate module configuration."""
        return True
