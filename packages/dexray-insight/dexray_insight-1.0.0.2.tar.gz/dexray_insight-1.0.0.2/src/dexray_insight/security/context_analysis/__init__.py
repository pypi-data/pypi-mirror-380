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
Context-Aware Security Analysis Module.

This module provides context-aware security analysis capabilities that enhance
traditional pattern-based secret detection with intelligent context analysis,
false positive reduction, and risk correlation.

Key Components:
- ContextualSecretAnalyzer: Main orchestrator for context-aware analysis
- CodeContextAnalyzer: Analyzes code context around detected secrets
- FalsePositiveFilter: Enhanced filtering with context-aware rules
- RiskCorrelationEngine: Correlates findings across analysis modules
- UsagePatternAnalyzer: Determines how secrets are used in practice

Design Principles:
- Incremental enhancement of existing detection capabilities
- SOLID principles with single-responsibility components
- Strategy pattern integration with existing security framework
- Backwards compatibility with current analysis pipeline
"""

from .code_context_analyzer import CodeContextAnalyzer
from .contextual_secret_analyzer import ContextualSecretAnalyzer
from .false_positive_filter import FalsePositiveFilter
from .risk_correlation_engine import RiskCorrelationEngine
from .usage_pattern_analyzer import UsagePatternAnalyzer

__all__ = [
    "ContextualSecretAnalyzer",
    "CodeContextAnalyzer",
    "FalsePositiveFilter",
    "RiskCorrelationEngine",
    "UsagePatternAnalyzer",
]
