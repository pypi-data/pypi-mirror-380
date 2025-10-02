#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive analysis results aggregation and formatting for Dexray Insight."""
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

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING
from typing import Any
from typing import Optional

if TYPE_CHECKING:
    from .DeepAnalysisResults import DeepAnalysisResults

from ..Utils.file_utils import CustomJSONEncoder
from .apkidResults import ApkidResults
from .apkOverviewResults import APKOverview
from .BehaviourAnalysisResults import BehaviourAnalysisResults
from .InDepthAnalysisResults import Results
from .kavanozResults import KavanozResults
from .LibraryDetectionResults import LibraryDetectionResults
from .TrackerAnalysisResults import TrackerAnalysisResults


@dataclass
class FullAnalysisResults:
    """Combines both APK overview results and in-depth analysis results.

    Fields:
        apk_overview: The APK overview results.
        in_depth_analysis: The in-depth analysis results.
        apkid_analysis: The analysis results of running apkID (identifies known compiler, packer, obfuscation and much more)
        kavanoz_analysis: Tells if the apk is packed or not. If its packed Kavanoz tries to statically unpack them
    """

    apk_overview: Optional[APKOverview] = None
    in_depth_analysis: Optional[Results] = None
    apkid_analysis: Optional[ApkidResults] = None
    kavanoz_analysis: Optional[KavanozResults] = None
    security_assessment: Optional[dict[str, Any]] = None
    tracker_analysis: Optional[TrackerAnalysisResults] = None
    behaviour_analysis: Optional[BehaviourAnalysisResults] = None
    library_detection: Optional[LibraryDetectionResults] = None
    deep_analysis: Optional["DeepAnalysisResults"] = None

    def __post_init__(self):
        """Ensure fields are initialized to empty objects if they are None."""
        if self.apk_overview is None:
            self.apk_overview = APKOverview()
        if self.in_depth_analysis is None:
            self.in_depth_analysis = Results()
        if self.apkid_analysis is None:
            self.apkid_analysis = ApkidResults(apkid_version="")
        if self.kavanoz_analysis is None:
            self.kavanoz_analysis = KavanozResults()

    def to_dict(self, include_security: bool = False) -> dict[str, Any]:
        """Return the combined object as a dictionary.

        Args:
            include_security: Whether to include security assessment results.
                            Default False to keep security separate from main results.
        """
        result = {
            "apk_overview": self.apk_overview.to_dict() if self.apk_overview else {},
            "in_depth_analysis": self.in_depth_analysis.to_dict() if self.in_depth_analysis else {},
            "apkid_analysis": self.apkid_analysis.to_dict() if self.apkid_analysis else {},
            "kavanoz_analysis": self.kavanoz_analysis.to_dict() if self.kavanoz_analysis else {},
        }

        # Include tracker analysis results if available
        if self.tracker_analysis:
            result["tracker_analysis"] = self.tracker_analysis.export_to_dict()

        # Include behaviour analysis results if available
        if self.behaviour_analysis:
            result["behaviour_analysis"] = self.behaviour_analysis.to_dict()

        # Include library detection results if available
        if self.library_detection:
            result["library_detection"] = self.library_detection.get_detailed_results()["library_detection"]

        # Include security assessment results only if explicitly requested
        if include_security and self.security_assessment:
            result["security_assessment"] = self.security_assessment

        # Include deep analysis results if available
        if self.deep_analysis:
            result["deep_analysis"] = self.deep_analysis.to_dict()

        return result

    def to_json(self) -> str:
        """Return the combined object as a JSON string."""
        return json.dumps(self.to_dict(), cls=CustomJSONEncoder, indent=4)

    def get_security_results_dict(self) -> dict[str, Any]:
        """Return only the security assessment results as a dictionary.

        Used for saving security results to a separate JSON file.
        """
        if self.security_assessment:
            return self.security_assessment
        return {}

    def security_results_to_json(self) -> str:
        """Return only the security assessment results as a JSON string."""
        return json.dumps(self.get_security_results_dict(), cls=CustomJSONEncoder, indent=4)

    def print_results(self):
        """Print the combined results as a JSON string."""
        print(self.to_json())

    def print_analyst_summary(self):
        """Print a concise, analyst-friendly summary of the analysis results.

        Shows key findings with truncated details for better readability.

        Refactored to use single-responsibility functions following SOLID principles.
        Maintains exact same behavior as original while improving maintainability.

        Each section is now handled by a dedicated function with single responsibility:
        - Header formatting
        - APK information display
        - Permissions analysis
        - String analysis summary
        - Security assessment
        - Tool analysis results
        - Component and behavior analysis
        - Footer formatting
        """
        # Use refactored single-responsibility functions for each section
        self._print_summary_header()
        self._print_apk_information()
        self._print_permissions_summary()
        self._print_string_analysis_summary()
        self._print_security_assessment_summary()
        self._print_tool_analysis_summary()
        self._print_component_behavior_summary()
        self._print_summary_footer()

    def _print_summary_header(self):
        """Print formatted header for analysis summary.

        Single Responsibility: Display the standardized header section only.
        """
        print("\n" + "=" * 80)
        print("📱 DEXRAY INSIGHT ANALYSIS SUMMARY")
        print("=" * 80)

    def _print_apk_information(self):
        """Print APK file and application information.

        Single Responsibility: Display APK metadata and application details only.
        """
        if self.apk_overview and hasattr(self.apk_overview, "general_info"):
            gen_info = self.apk_overview.general_info
            print("\n📋 APK INFORMATION")
            print("-" * 40)

            # File details
            if "file_name" in gen_info:
                print(f"File Name: {gen_info['file_name']}")
            if "file_size" in gen_info:
                print(f"File Size: {gen_info['file_size']}")
            if "md5" in gen_info:
                print(f"Md5: {gen_info['md5']}")
            if "sha1" in gen_info:
                print(f"Sha1: {gen_info['sha1']}")
            if "sha256" in gen_info:
                print(f"Sha256: {gen_info['sha256']}")

            # App details
            if "app_name" in gen_info:
                print(f"App Name: {gen_info['app_name']}")
            if "package_name" in gen_info:
                print(f"Package Name: {gen_info['package_name']}")
            if "main_activity" in gen_info and gen_info["main_activity"]:
                print(f"Main Activity: {gen_info['main_activity']}")

            # SDK and version info
            if "target_sdk" in gen_info and gen_info["target_sdk"]:
                print(f"Target Sdk: {gen_info['target_sdk']}")
            if "min_sdk" in gen_info and gen_info["min_sdk"]:
                print(f"Min Sdk: {gen_info['min_sdk']}")
            if "max_sdk" in gen_info and gen_info["max_sdk"]:
                print(f"Max Sdk: {gen_info['max_sdk']}")
            else:
                print("Max Sdk: None")
            if "android_version_name" in gen_info and gen_info["android_version_name"]:
                print(f"Android Version Name: {gen_info['android_version_name']}")
            if "android_version_code" in gen_info and gen_info["android_version_code"]:
                print(f"Android Version Code: {gen_info['android_version_code']}")

            # Cross-platform info
            if self.apk_overview.is_cross_platform:
                print(f"🔗 Cross-Platform: {self.apk_overview.cross_platform_framework}")

    def _print_permissions_summary(self):
        """Print permissions analysis with critical permission highlighting.

        Single Responsibility: Display permissions information with categorization only.
        """
        if self.apk_overview and hasattr(self.apk_overview, "permissions"):
            perms = self.apk_overview.permissions.get("permissions", [])
            if perms:
                print(f"\n🔐 PERMISSIONS ({len(perms)} total)")
                print("-" * 40)

                # Show critical permissions first
                critical_perms = [
                    p
                    for p in perms
                    if any(
                        crit in p.upper()
                        for crit in ["CAMERA", "LOCATION", "CONTACTS", "SMS", "PHONE", "STORAGE", "MICROPHONE", "ADMIN"]
                    )
                ]

                if critical_perms:
                    print("⚠️  Critical Permissions:")
                    for perm in critical_perms[:5]:  # Show max 5
                        print(f"   • {perm}")
                    if len(critical_perms) > 5:
                        print(f"   ... and {len(critical_perms) - 5} more critical permissions")

                # Show other permissions (truncated)
                other_perms = [p for p in perms if p not in critical_perms]
                if other_perms:
                    print(f"ℹ️  Other Permissions: {len(other_perms)} (see full JSON for details)")

    def _print_string_analysis_summary(self):
        """Print string analysis results with categorization and truncation.

        Single Responsibility: Display string analysis findings only.
        """
        if self.in_depth_analysis:
            # Count string analysis results for summary
            email_count = len(self.in_depth_analysis.strings_emails) if self.in_depth_analysis.strings_emails else 0
            ip_count = len(self.in_depth_analysis.strings_ip) if self.in_depth_analysis.strings_ip else 0
            url_count = len(self.in_depth_analysis.strings_urls) if self.in_depth_analysis.strings_urls else 0
            domain_count = len(self.in_depth_analysis.strings_domain) if self.in_depth_analysis.strings_domain else 0

            # Create summary string
            summary_parts = []
            if url_count > 0:
                summary_parts.append(f"URLs: {url_count}")
            if email_count > 0:
                summary_parts.append(f"E-Mails: {email_count}")
            if ip_count > 0:
                summary_parts.append(f"IPs: {ip_count}")
            if domain_count > 0:
                summary_parts.append(f"Domains: {domain_count}")

            summary = f" ({', '.join(summary_parts)})" if summary_parts else ""
            print(f"\n🔍 STRING ANALYSIS{summary}")
            print("-" * 40)

            # IPs
            if self.in_depth_analysis.strings_ip:
                print(f"🌐 IP Addresses: {len(self.in_depth_analysis.strings_ip)}")
                for ip in self.in_depth_analysis.strings_ip[:3]:  # Show max 3
                    print(f"   • {ip}")
                if len(self.in_depth_analysis.strings_ip) > 3:
                    print(f"   ... and {len(self.in_depth_analysis.strings_ip) - 3} more")

            # Domains
            if self.in_depth_analysis.strings_domain:
                print(f"🏠 Domains: {len(self.in_depth_analysis.strings_domain)}")
                for domain in self.in_depth_analysis.strings_domain[:3]:  # Show max 3
                    print(f"   • {domain}")
                if len(self.in_depth_analysis.strings_domain) > 3:
                    print(f"   ... and {len(self.in_depth_analysis.strings_domain) - 3} more")

            # URLs
            if self.in_depth_analysis.strings_urls:
                print(f"🔗 URLs: {len(self.in_depth_analysis.strings_urls)}")
                for url in self.in_depth_analysis.strings_urls[:2]:  # Show max 2
                    # Truncate long URLs
                    display_url = url if len(url) <= 60 else url[:57] + "..."
                    print(f"   • {display_url}")
                if len(self.in_depth_analysis.strings_urls) > 2:
                    print(f"   ... and {len(self.in_depth_analysis.strings_urls) - 2} more")

            # Emails
            if self.in_depth_analysis.strings_emails:
                print(f"📧 Email Addresses: {len(self.in_depth_analysis.strings_emails)}")
                for email in self.in_depth_analysis.strings_emails[:3]:  # Show max 3
                    print(f"   • {email}")
                if len(self.in_depth_analysis.strings_emails) > 3:
                    print(f"   ... and {len(self.in_depth_analysis.strings_emails) - 3} more")

            # .NET assemblies
            if self.in_depth_analysis.dotnetMono_assemblies:
                print(f"⚙️  .NET Assemblies: {len(self.in_depth_analysis.dotnetMono_assemblies)}")
                for assembly in self.in_depth_analysis.dotnetMono_assemblies[:3]:  # Show max 3
                    print(f"   • {assembly}")
                if len(self.in_depth_analysis.dotnetMono_assemblies) > 3:
                    print(f"   ... and {len(self.in_depth_analysis.dotnetMono_assemblies) - 3} more")

    def _print_security_assessment_summary(self):
        """
        Print security assessment results with findings and risk scoring.

        Single Responsibility: Display security analysis findings only.
        """
        # Tracker Analysis Summary
        if self.tracker_analysis:
            print("\n📍 TRACKER ANALYSIS")
            print("-" * 40)
            print(self.tracker_analysis.get_console_summary())

        # Library Detection Summary
        if self.library_detection:
            print("\n📚 LIBRARY DETECTION")
            print("-" * 40)
            print(self.library_detection.get_console_summary())

            # Show version analysis results if available and security analysis was enabled
            self._print_version_analysis_summary()

        # Security Assessment Summary
        if self.security_assessment:
            print("\n🛡️  SECURITY ASSESSMENT")
            print("-" * 40)

            total_findings = self.security_assessment.get("total_findings", 0)
            risk_score = self.security_assessment.get("overall_risk_score", 0)

            print(f"Security Findings: {total_findings}")
            print(f"Risk Score: {risk_score:.2f}/100")

            # Show findings by severity
            findings_by_severity = self.security_assessment.get("findings_by_severity", {})
            if findings_by_severity:
                severity_parts = []
                for severity, count in findings_by_severity.items():
                    if count > 0:
                        severity_parts.append(f"{severity.title()}: {count}")
                if severity_parts:
                    print(f"Severity Distribution: {', '.join(severity_parts)}")

            # Show OWASP categories affected
            categories = self.security_assessment.get("owasp_categories_affected", [])
            if categories:
                print(f"OWASP Categories: {', '.join(categories[:3])}")
                if len(categories) > 3:
                    print(f"   ... and {len(categories) - 3} more")

            # Show key findings
            findings = self.security_assessment.get("findings", [])
            if findings:
                print("\nKey Findings:")
                for finding in findings[:3]:  # Show max 3 findings
                    title = finding.get("title", "Security Finding")
                    category = finding.get("category", "Unknown")
                    severity = finding.get("severity", "unknown")
                    if isinstance(severity, dict) and "value" in severity:
                        severity = severity["value"]
                    severity_str = severity.value if hasattr(severity, "value") else str(severity)
                    print(f"   • [{severity_str.upper()}] {category}: {title}")
                if len(findings) > 3:
                    print(f"   ... and {len(findings) - 3} more findings (see security JSON file)")

            # Signature results
            if self.in_depth_analysis.signatures:
                print("\n🛡️  SIGNATURE ANALYSIS")
                print("-" * 40)
                sigs = self.in_depth_analysis.signatures

                if sigs.get("vt"):
                    vt_result = sigs["vt"]
                    if isinstance(vt_result, dict) and "positives" in vt_result:
                        print(f"VirusTotal: {vt_result.get('positives', 0)}/{vt_result.get('total', 0)} detections")
                    else:
                        print(f"VirusTotal: {vt_result}")

                if sigs.get("koodous"):
                    print(f"Koodous: {sigs['koodous']}")

                if sigs.get("triage"):
                    print(f"Triage: {sigs['triage']}")

    def _print_tool_analysis_summary(self):
        """
        Print results from external analysis tools (APKID, Kavanoz, Signatures).

        Single Responsibility: Display tool-specific analysis results only.
        """
        # Kavanoz results
        if self.kavanoz_analysis and hasattr(self.kavanoz_analysis, "is_packed"):
            print("\n📦 PACKING ANALYSIS")
            print("-" * 40)
            if self.kavanoz_analysis.is_packed:
                print("⚠️  APK appears to be packed")
                if hasattr(self.kavanoz_analysis, "unpacking_result"):
                    print(f"Unpacking result: {self.kavanoz_analysis.unpacking_result}")
            else:
                print("✅ APK does not appear to be packed")

        # APKID results - Show compiler information and repacking warnings
        if self.apkid_analysis:
            # Check if apkid_analysis has files attribute and non-empty files
            files = getattr(self.apkid_analysis, "files", [])

            # If no files in the object, try to parse from raw_output
            if not files and hasattr(self.apkid_analysis, "raw_output") and self.apkid_analysis.raw_output:
                try:
                    import json

                    raw_data = json.loads(self.apkid_analysis.raw_output)
                    if "files" in raw_data:
                        from .apkidResults import ApkidFileAnalysis

                        files = [
                            ApkidFileAnalysis(
                                filename=file_data.get("filename", ""), matches=file_data.get("matches", {})
                            )
                            for file_data in raw_data["files"]
                        ]
                        # Update the object with parsed files
                        self.apkid_analysis.files = files
                except Exception as e:
                    import logging

                    logging.getLogger(__name__).debug(f"Failed to parse APKID raw_output: {e}")

            if files:
                print("\n🔧 COMPILER & APKID ANALYSIS")
                print("-" * 40)

                # Collect all compiler and packer information
                compilers = []
                packers = []
                other_findings = {}
                first_dex_compiler = None

                for file_analysis in files:
                    # Skip library files to avoid noise
                    if "!lib/" in file_analysis.filename.lower():
                        continue

                    # Check if this is the first/main dex file
                    filename_lower = file_analysis.filename.lower()
                    is_main_dex = (
                        filename_lower.endswith("classes.dex")
                        or filename_lower.endswith("classes1.dex")
                        or "!classes.dex" in filename_lower
                        or "!classes1.dex" in filename_lower
                    )

                    for category, matches in file_analysis.matches.items():
                        if category.lower() == "compiler":
                            compilers.extend(matches)
                            # Capture first dex compiler for special highlighting
                            if is_main_dex and first_dex_compiler is None and matches:
                                first_dex_compiler = matches[0] if isinstance(matches, list) else matches
                        elif category.lower() == "packer":
                            packers.extend(matches)
                        else:
                            # Collect other interesting findings
                            if category.lower() in ["obfuscator", "anti_vm", "anti_debug", "anti_disassembly"]:
                                if category not in other_findings:
                                    other_findings[category] = []
                                other_findings[category].extend(matches)

                # Remove duplicates
                compilers = list(set(compilers))
                packers = list(set(packers))

                # Show first dex compiler prominently if found
                if first_dex_compiler:
                    print(f"🎯 Primary DEX Compiler: {first_dex_compiler}")

                    # Check for repacking indicators
                    compiler_lower = first_dex_compiler.lower()
                    if any(
                        repack_indicator in compiler_lower for repack_indicator in ["dexlib", "dx", "baksmali", "smali"]
                    ):
                        print(f"   ⚠️  WARNING: {first_dex_compiler} detected - APK may be repacked/modified")
                    print()

                # Show all compiler information
                if compilers:
                    print("🛠️  All Compiler(s) Detected:")
                    for compiler in compilers:
                        # Mark the first dex compiler if it's in the list
                        if compiler == first_dex_compiler:
                            print(f"   • {compiler} ⭐ (Primary DEX)")
                        else:
                            print(f"   • {compiler}")
                    print()

                # Show packer information
                if packers:
                    print("📦 Packer(s) Detected:")
                    for packer in packers:
                        print(f"   • {packer}")
                    print()

                # Show other security-relevant findings
                for category, matches in other_findings.items():
                    if matches:
                        unique_matches = list(set(matches))
                        print(f"🛡️  {category.replace('_', ' ').title()}:")
                        for match in unique_matches[:3]:  # Show max 3
                            print(f"   • {match}")
                        if len(unique_matches) > 3:
                            print(f"   ... and {len(unique_matches) - 3} more")
                        print()

                # If no specific categories found, show general findings
                if not compilers and not packers and not other_findings:
                    print("ℹ️  No specific compiler, packer, or security findings detected")
                    # Show any other findings from the first file
                    if files and files[0].matches:
                        shown = 0
                        for category, matches in files[0].matches.items():
                            if matches and shown < 3:
                                print(f"   {category.replace('_', ' ').title()}: {', '.join(matches[:2])}")
                                shown += 1

    def _print_component_behavior_summary(self):
        """
        Print component analysis and behavioral analysis results.

        Single Responsibility: Display component and behavior analysis findings only.
        """
        # Components summary
        if self.apk_overview and hasattr(self.apk_overview, "components"):
            components = self.apk_overview.components
            if components:
                print("\n🏗️  COMPONENTS")
                print("-" * 40)
                for comp_type, comp_list in components.items():
                    if comp_list and len(comp_list) > 0:
                        count = len(comp_list)
                        print(f"{comp_type.replace('_', ' ').title()}: {count}")

        # Behaviour analysis summary
        if self.behaviour_analysis:
            detected_features = self.behaviour_analysis.get_detected_features()
            if detected_features:
                print(f"\n🔍 BEHAVIOUR ANALYSIS ({len(detected_features)} behaviors detected)")
                print("-" * 40)
                for feature in detected_features:
                    # Convert snake_case to readable format
                    readable_name = feature.replace("_", " ").title()
                    print(f"✓ {readable_name}")

        # Deep analysis summary
        if self.deep_analysis and hasattr(self.deep_analysis, "findings"):
            detected_features = self.deep_analysis.get_detected_features()
            if detected_features:
                print(f"\n🔍 DEEP ANALYSIS ({len(detected_features)} behaviors detected)")
                print("-" * 40)
                for feature in detected_features:
                    # Convert snake_case to readable format
                    readable_name = feature.replace("_", " ").title()
                    print(f"✓ {readable_name}")

    def _print_summary_footer(self):
        """
        Print formatted footer with usage hints and file information.

        Single Responsibility: Display the standardized footer section only.
        """
        print(f"\n{'='*80}")
        print("📄 Complete details saved to JSON file")
        if self.security_assessment:
            print("🛡️  Security findings saved to separate security JSON file")
        print("💡 Use -v flag for verbose terminal output")
        print("=" * 80 + "\n")

    def update_from_dict(self, updates: dict[str, Any]):
        """
        Update the fields from a dictionary.

        Args:
            updates: A dictionary containing updates for fields.
        """
        if "apk_overview" in updates and self.apk_overview:
            self.apk_overview.update_from_dict(updates["apk_overview"])
        if "in_depth_analysis" in updates and self.in_depth_analysis:
            self.in_depth_analysis.update_from_dict(updates["in_depth_analysis"])
        if "apkid_analysis" in updates and self.apkid_analysis:
            self.apkid_analysis.update_from_dict(updates["apkid_analysis"])
        if "kavanoz_analysis" in updates and self.kavanoz_analysis:
            self.kavanoz_analysis.update_from_dict(updates["kavanoz_analysis"])

    def _print_version_analysis_summary(self):
        """
        Print version analysis results as part of the library detection summary.

        Only displays when security analysis is enabled and libraries have version information.
        """
        if not self.library_detection or not hasattr(self.library_detection, "detected_libraries"):
            return

        # Check if security analysis was performed (indicator that version analysis might have run)
        if not self.security_assessment:
            return

        # Get libraries with version information
        libraries = self.library_detection.detected_libraries or []
        libraries_with_versions = [lib for lib in libraries if hasattr(lib, "version") and lib.version]

        if not libraries_with_versions:
            return

        # Show all libraries with versions, not just those with years_behind analysis
        # This fixes the library count discrepancy issue
        libraries_with_analysis = libraries_with_versions

        if not libraries_with_analysis:
            return

        print("\n📚 LIBRARY VERSION ANALYSIS")
        print("=" * 80)

        # Count libraries with and without years_behind data
        with_years_analysis = [
            lib for lib in libraries_with_analysis if hasattr(lib, "years_behind") and lib.years_behind is not None
        ]

        # Libraries without years analysis but with version info
        no_analysis_libs = [
            lib
            for lib in libraries_with_analysis
            if not (hasattr(lib, "years_behind") and lib.years_behind is not None)
        ]

        print(f"Libraries with versions: {len(libraries_with_analysis)} detected")
        if len(with_years_analysis) < len(libraries_with_analysis):
            print(f"Version analysis completed: {len(with_years_analysis)} libraries")
            no_analysis = len(libraries_with_analysis) - len(with_years_analysis)
            print(f"Version analysis pending/unavailable: {no_analysis} libraries")

        # Group libraries by security risk (only for those with years_behind data)
        critical_libs = [
            lib for lib in with_years_analysis if hasattr(lib, "security_risk") and lib.security_risk == "CRITICAL"
        ]
        high_risk_libs = [
            lib for lib in with_years_analysis if hasattr(lib, "security_risk") and lib.security_risk == "HIGH"
        ]
        medium_risk_libs = [
            lib for lib in with_years_analysis if hasattr(lib, "security_risk") and lib.security_risk == "MEDIUM"
        ]
        low_risk_libs = [
            lib
            for lib in with_years_analysis
            if not hasattr(lib, "security_risk") or lib.security_risk in ["LOW", None]
        ]

        # Print critical libraries first
        if critical_libs:
            print(f"\n⚠️  CRITICAL RISK LIBRARIES ({len(critical_libs)}):")
            print("-" * 40)
            for lib in sorted(critical_libs, key=lambda x: getattr(x, "years_behind", 0), reverse=True):
                formatted = self._format_library_version_output(lib)
                print(f"   {formatted}")
                if hasattr(lib, "version_recommendation") and lib.version_recommendation:
                    print(f"   └─ {lib.version_recommendation}")

        # Print high risk libraries
        if high_risk_libs:
            print(f"\n⚠️  HIGH RISK LIBRARIES ({len(high_risk_libs)}):")
            print("-" * 40)
            for lib in sorted(high_risk_libs, key=lambda x: getattr(x, "years_behind", 0), reverse=True):
                formatted = self._format_library_version_output(lib)
                print(f"   {formatted}")
                if hasattr(lib, "version_recommendation") and lib.version_recommendation:
                    print(f"   └─ {lib.version_recommendation}")

        # Print medium risk libraries
        if medium_risk_libs:
            print(f"\n⚠️  MEDIUM RISK LIBRARIES ({len(medium_risk_libs)}):")
            print("-" * 40)
            for lib in sorted(medium_risk_libs, key=lambda x: getattr(x, "years_behind", 0), reverse=True):
                formatted = self._format_library_version_output(lib)
                print(f"   {formatted}")

        # Print low risk libraries (summary only)
        if low_risk_libs:
            current_libs = [lib for lib in low_risk_libs if getattr(lib, "years_behind", 0) < 0.5]
            outdated_libs = [lib for lib in low_risk_libs if getattr(lib, "years_behind", 0) >= 0.5]

            if outdated_libs:
                print(f"\n📋 OUTDATED LIBRARIES ({len(outdated_libs)}):")
                print("-" * 40)
                for lib in sorted(outdated_libs, key=lambda x: getattr(x, "years_behind", 0), reverse=True):
                    formatted = self._format_library_version_output(lib)
                    print(f"   {formatted}")

            if current_libs:
                print(f"\n✅ CURRENT LIBRARIES ({len(current_libs)}):")
                print("-" * 40)
                for lib in sorted(current_libs, key=lambda x: getattr(x, "name", "")):
                    formatted = self._format_library_version_output(lib)
                    print(f"   {formatted}")

        # Show libraries without version analysis
        if no_analysis_libs:
            print(f"\n📋 LIBRARIES WITH VERSIONS (no age analysis): ({len(no_analysis_libs)})")
            print("-" * 40)
            for lib in sorted(
                no_analysis_libs[:10], key=lambda x: getattr(x, "name", "").lower()
            ):  # Limit to first 10 for readability
                name = getattr(lib, "name", "Unknown")
                version = getattr(lib, "version", "Unknown")
                method = getattr(lib, "detection_method", "unknown")
                print(f"   {name} ({version}) - detected via {method}")
            if len(no_analysis_libs) > 10:
                print(f"   ... and {len(no_analysis_libs) - 10} more libraries")

        # Print summary statistics
        if libraries_with_analysis:
            print("\n📊 SUMMARY:")
            print("-" * 40)
            print(f"   Total libraries with versions: {len(libraries_with_analysis)}")

            if with_years_analysis:
                print(f"   Libraries with age analysis: {len(with_years_analysis)}")
                print(f"   Critical risk: {len(critical_libs)}")
                print(f"   High risk: {len(high_risk_libs)}")
                print(f"   Medium risk: {len(medium_risk_libs)}")
                print(f"   Low risk: {len(low_risk_libs)}")

                years_values = [
                    lib.years_behind
                    for lib in with_years_analysis
                    if hasattr(lib, "years_behind") and lib.years_behind is not None
                ]
                if years_values:
                    avg_years = sum(years_values) / len(years_values)
                    print(f"   Average years behind: {avg_years:.1f}")

            if no_analysis_libs:
                print(f"   Libraries without age analysis: {len(no_analysis_libs)}")

            # Enhanced CVE summary integration
            self._print_enhanced_cve_summary(libraries_with_versions)

            # Add CVE vulnerability summary
            self._print_cve_summary()

        print("=" * 80)

    def _safe_get_finding_attribute(self, finding, attr_name, default=""):
        """
        Safely get attribute from finding object or dictionary, handling both attributes/methods and dict keys.

        Args:
            finding: The security finding object or dictionary
            attr_name: Name of the attribute/method/key to get
            default: Default value if attribute/method/key not found or fails

        Returns:
            Value of the attribute/method/key, or default value (preserves original type for lists/objects)
        """
        try:
            # If finding is a dictionary, access by key
            if isinstance(finding, dict):
                return finding.get(attr_name, default)

            # If finding is an object, try attribute/method access
            if hasattr(finding, attr_name):
                attr_value = getattr(finding, attr_name)
                # If it's a method, call it
                if callable(attr_value):
                    result = attr_value()
                    return result if result is not None else default
                # If it's an attribute, return it (preserving original type)
                else:
                    return attr_value if attr_value is not None else default
            return default
        except Exception as e:
            import logging

            logger = logging.getLogger(__name__)
            logger.debug(f"Error accessing finding attribute '{attr_name}': {e}")
            return default

    def _extract_top_critical_cves(self, findings: list) -> list[dict[str, Any]]:
        """Extract top critical CVEs with library attribution for terminal display."""
        critical_cves = []

        for finding in findings:
            # Check if this is a critical CVE finding
            category = self._safe_get_finding_attribute(finding, "category")
            title = self._safe_get_finding_attribute(finding, "title")

            if (
                category
                and isinstance(category, str)
                and "cve" in category.lower()
                and title
                and isinstance(title, str)
                and "critical" in title.lower()
            ):
                # Extract detailed CVE information from additional_data
                additional_data = self._safe_get_finding_attribute(finding, "additional_data", {})
                if isinstance(additional_data, dict) and "detailed_cves" in additional_data:
                    for cve_data in additional_data["detailed_cves"]:
                        if isinstance(cve_data, dict) and cve_data.get("severity") == "CRITICAL":
                            # Get library information from mapping
                            cve_id = cve_data.get("cve_id", "Unknown")
                            library_mapping = additional_data.get("cve_library_mapping", {})
                            affected_library = None

                            # Find which library this CVE affects
                            for lib_name, cve_list in library_mapping.items():
                                if cve_id in cve_list:
                                    affected_library = lib_name
                                    break

                            critical_cves.append(
                                {
                                    "cve_id": cve_id,
                                    "library": affected_library or "Unknown",
                                    "version": "unknown",  # Will be populated from library data if available
                                    "cvss_score": cve_data.get("cvss_score", "N/A"),
                                    "summary": cve_data.get("summary", "No summary available"),
                                }
                            )

        # Sort by CVSS score (highest first)
        def sort_key(cve):
            score = cve["cvss_score"]
            if isinstance(score, (int, float)):
                return score
            return 0  # Unknown scores go to end

        critical_cves.sort(key=sort_key, reverse=True)
        return critical_cves

    def _print_cve_summary(self):
        """Print CVE vulnerability scanning summary."""
        try:
            # Check if we have CVE/security assessment results
            if not hasattr(self, "security_assessment") or not self.security_assessment:
                print("   CVE scanning: Not performed or no results available")
                return

            # Look for CVE-related findings with more robust detection
            cve_findings = []
            total_vulnerabilities = 0

            # Check if security_assessment has findings in the expected structure
            findings = []
            if isinstance(self.security_assessment, dict) and "findings" in self.security_assessment:
                findings = self.security_assessment["findings"]
            elif hasattr(self.security_assessment, "findings"):
                findings = self.security_assessment.findings
            elif isinstance(self.security_assessment, list):
                findings = self.security_assessment
            elif isinstance(self.security_assessment, dict):
                # Flatten dict to find findings
                for key, value in self.security_assessment.items():
                    if isinstance(value, list):
                        findings.extend(value)
                    elif hasattr(value, "__iter__") and not isinstance(value, str):
                        try:
                            findings.extend(value)
                        except Exception:
                            pass

            # Look for CVE findings with multiple criteria
            for finding in findings:
                is_cve_finding = False

                # Check category for CVE indicators
                category = self._safe_get_finding_attribute(finding, "category")
                if category and isinstance(category, str):
                    category_lower = category.lower()
                    if "cve" in category_lower or "vulnerability" in category_lower:
                        is_cve_finding = True

                # Check title for CVE indicators
                title = self._safe_get_finding_attribute(finding, "title")
                if title and isinstance(title, str):
                    title_lower = title.lower()
                    if "cve" in title_lower or "vulnerability" in title_lower:
                        is_cve_finding = True

                if is_cve_finding:
                    cve_findings.append(finding)
                    # Try to extract vulnerability count from title, description, and evidence
                    count_found = False

                    # Check title for numbers
                    finding_title = self._safe_get_finding_attribute(finding, "title")
                    if finding_title and isinstance(finding_title, str):
                        import re

                        title_numbers = re.findall(r"(\d+)\s*(?:vulnerabilities?|cves?)", finding_title.lower())
                        if title_numbers:
                            total_vulnerabilities += int(title_numbers[0])
                            count_found = True

                    # Check description for numbers
                    if not count_found:
                        finding_description = self._safe_get_finding_attribute(finding, "description")
                        if finding_description and isinstance(finding_description, str):
                            import re

                            desc_numbers = re.findall(
                                r"(\d+)\s*(?:vulnerabilities?|cves?)", finding_description.lower()
                            )
                            if desc_numbers:
                                total_vulnerabilities += int(desc_numbers[0])
                                count_found = True

                    # Check evidence for numbers
                    if not count_found:
                        finding_evidence = self._safe_get_finding_attribute(finding, "evidence", [])
                        if finding_evidence:
                            # Handle case where evidence might be returned as string instead of list
                            evidence_list = (
                                finding_evidence if isinstance(finding_evidence, list) else [finding_evidence]
                            )
                            for evidence in evidence_list:
                                if isinstance(evidence, str):
                                    import re

                                    evidence_numbers = re.findall(
                                        r"(\d+)\s*(?:vulnerabilities?|cves?)", evidence.lower()
                                    )
                                    if evidence_numbers:
                                        total_vulnerabilities += int(evidence_numbers[0])
                                        count_found = True
                                        break
                                    # Also look for specific CVE count patterns
                                    total_pattern = re.search(
                                        r"total\s+cve\s+vulnerabilities\s+found:\s*(\d+)", evidence.lower()
                                    )
                                    if total_pattern:
                                        total_vulnerabilities = int(
                                            total_pattern.group(1)
                                        )  # Use exact count, don't add
                                        count_found = True
                                        break

            # Print enhanced CVE summary with top critical findings
            if cve_findings:
                if total_vulnerabilities > 0:
                    print(f"   CVE vulnerabilities found: {total_vulnerabilities}")

                    # Extract and display top 3 critical CVEs with library attribution
                    critical_cves = self._extract_top_critical_cves(findings)
                    if critical_cves:
                        print("   🚨 Top Critical CVEs:")
                        for i, cve_info in enumerate(critical_cves[:3], 1):
                            print(f"      {i}. {cve_info['cve_id']} in {cve_info['library']} (v{cve_info['version']})")
                            print(f"         CVSS: {cve_info['cvss_score']} - {cve_info['summary'][:80]}...")

                    print("   🔍 Review security assessment for complete CVE details and remediation")
                else:
                    print(f"   CVE scanning performed: {len(cve_findings)} assessment(s) completed")
                    print("   ✅ No known CVE vulnerabilities detected")
            else:
                print("   CVE scanning: Not performed or no results available")

        except Exception as e:
            # Enhanced error handling for debugging
            import traceback

            error_details = traceback.format_exc()
            print(f"   CVE scanning: Error processing results ({str(e)})")
            # Log detailed error for debugging (but don't print to console)
            import logging

            logging.debug(f"CVE summary error: {error_details}")

    def _print_enhanced_cve_summary(self, libraries_with_versions):
        """Enhanced CVE summary that integrates with library version analysis."""
        try:
            if not hasattr(self, "security_assessment") or not self.security_assessment:
                return

            # Extract detailed CVE information for each library
            cve_by_library = self._extract_cve_by_library()

            if not cve_by_library:
                return

            print("   CVE Analysis Details:")

            # Show libraries with CVEs
            libraries_with_cves = 0
            total_cves = 0

            for lib_name, cves in cve_by_library.items():
                if cves:
                    libraries_with_cves += 1
                    total_cves += len(cves)

                    # Find matching library in version analysis
                    matching_lib = None
                    for lib in libraries_with_versions:
                        if (
                            hasattr(lib, "name")
                            and lib.name
                            and lib_name.lower() in lib.name.lower()
                            or lib.name.lower() in lib_name.lower()
                        ):
                            matching_lib = lib
                            break

                    if matching_lib:
                        version = getattr(matching_lib, "version", "Unknown")
                        years_behind = getattr(matching_lib, "years_behind", None)
                        years_text = f" ({years_behind} years behind)" if years_behind else ""

                        # Group CVEs by severity
                        critical = sum(1 for cve in cves if "critical" in cve.get("severity", "").lower())
                        high = sum(1 for cve in cves if "high" in cve.get("severity", "").lower())
                        medium = sum(1 for cve in cves if "medium" in cve.get("severity", "").lower())
                        low = sum(1 for cve in cves if "low" in cve.get("severity", "").lower())

                        severity_text = []
                        if critical:
                            severity_text.append(f"{critical} Critical")
                        if high:
                            severity_text.append(f"{high} High")
                        if medium:
                            severity_text.append(f"{medium} Medium")
                        if low:
                            severity_text.append(f"{low} Low")

                        print(
                            f"     • {lib_name} ({version}){years_text}: {len(cves)} CVEs ({', '.join(severity_text)})"
                        )

            if libraries_with_cves > 0:
                print(f"   Summary: {libraries_with_cves} libraries with {total_cves} total CVEs")

        except Exception as e:
            # Silently handle errors in enhanced CVE summary
            import logging

            logging.debug(f"Enhanced CVE summary error: {e}")

    def _extract_cve_by_library(self):
        """Extract CVE information organized by library."""
        cve_by_library = {}

        try:
            # Get findings from security assessment
            findings = []
            if hasattr(self.security_assessment, "__iter__"):
                findings = self.security_assessment
            elif hasattr(self.security_assessment, "findings"):
                findings = self.security_assessment.findings
            elif isinstance(self.security_assessment, dict) and "findings" in self.security_assessment:
                findings = self.security_assessment["findings"]

            for finding in findings:
                # Check if finding has CVE category
                category = self._safe_get_finding_attribute(finding, "category")
                if not category or not isinstance(category, str):
                    continue

                category_lower = category.lower()
                if "cve" not in category_lower and "vulnerability" not in category_lower:
                    continue

                # Extract CVE information from evidence
                finding_evidence = self._safe_get_finding_attribute(finding, "evidence", [])
                if finding_evidence:
                    # Handle case where evidence might be returned as string instead of list
                    evidence_list = finding_evidence if isinstance(finding_evidence, list) else [finding_evidence]
                    for evidence in evidence_list:
                        if isinstance(evidence, str):
                            # Parse CVE entries from evidence
                            import re

                            # Look for patterns like "CVE-XXXX-XXXX (severity: XXX): description"
                            cve_matches = re.findall(
                                r"(CVE-\d{4}-\d+)\s*(?:\((?:CVSS:\s*[\d.]+\s*,?\s*)?severity:\s*(\w+)\))?\s*:\s*([^\\n]*)",
                                evidence,
                            )

                            for cve_id, severity, description in cve_matches:
                                # Try to extract library name from context
                                # Look for patterns like "Found X CVE: " or mentions of library names
                                lib_context = re.search(r"Found\s+(\w+)\s+CVE:", evidence)
                                if lib_context:
                                    lib_name = lib_context.group(1)
                                    if lib_name not in cve_by_library:
                                        cve_by_library[lib_name] = []
                                    cve_by_library[lib_name].append(
                                        {
                                            "cve_id": cve_id,
                                            "severity": severity or "Unknown",
                                            "description": description,
                                        }
                                    )

        except Exception as e:
            import logging

            logging.debug(f"Error extracting CVE by library: {e}")

        return cve_by_library

    def _format_library_version_output(self, library):
        """
        Format version analysis output for console display.

        Format: library name (version): smali path : years behind
        Example: Gson (2.8.5): /com/google/gson/ : 2.1 years behind
        """
        name = getattr(library, "name", "Unknown")
        version = getattr(library, "version", "Unknown")
        years_behind = getattr(library, "years_behind", None)
        smali_path = getattr(library, "smali_path", "")
        security_risk = getattr(library, "security_risk", None)

        # Format smali path part
        path_part = f": {smali_path} " if smali_path else ""

        if years_behind is not None:
            years_part = f": {years_behind} years behind"

            # Add security risk indicator
            risk_indicator = ""
            if security_risk == "CRITICAL":
                risk_indicator = " ⚠️ CRITICAL"
            elif security_risk == "HIGH":
                risk_indicator = " ⚠️ HIGH RISK"
            elif security_risk == "MEDIUM":
                risk_indicator = " ⚠️ MEDIUM RISK"

            return f"{name} ({version}){path_part}{years_part}{risk_indicator}"
        else:
            return f"{name} ({version}){path_part}: version analysis unavailable"
