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
Please note that the format of the output of Secure Code Scan is actually SARIF.

For further information on SARIF have a look at: https://sarifweb.azurewebsites.net/
"""

import json
import logging
import os
import subprocess

from apkstaticanalysismonitor.Utils.file_utils import backup_and_replace_with_template


def execute_dotnet_mono_security_analysis(app_name, dll_target_dir):
    """Execute security analysis for .NET/Mono runtime assemblies.

    Args:
        app_name: Name of the application being analyzed
        dll_target_dir: Directory containing extracted DLL files

    Returns:
        list: Security analysis results for .NET assemblies
    """
    _results = []
    template = "template.csproj"
    try:
        print("===== Performing .NET security analysis =====")
        _dec_dlls = os.listdir(dll_target_dir)
        for _dll in _dec_dlls:
            _cs_file = ".".join(_dll.split(".")[:-1]) + ".csproj"
            _output_files = []
            target_cs_file = f"{dll_target_dir}/{_dll}/{_cs_file}"
            if os.path.isfile(target_cs_file):
                debug_output = False
                result = subprocess.run(
                    ["security-scan", target_cs_file, f"--export={_cs_file}.sarif.json"],
                    stdout=None if debug_output else subprocess.DEVNULL,
                    stderr=None if debug_output else subprocess.STDOUT,
                )
                if result.returncode != 0:
                    backup_and_replace_with_template(target_cs_file, template)
                    subprocess.run(
                        ["security-scan", target_cs_file, "--ignore-msbuild-errors", f"--export={_cs_file}.sarif.json"],
                        stdout=None if debug_output else subprocess.DEVNULL,
                        stderr=None if debug_output else subprocess.STDOUT,
                    )

                _output_files.append(f"{_cs_file}.sarif.json")
            elif os.path.isfile(f"{dll_target_dir}/Project.sln"):
                subprocess.run(
                    ["security-scan", f"{dll_target_dir}/Project.sln", f"--export={app_name}.sarif.json"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT,
                )
                _output_files.append(f"{app_name}.sarif.json")

        bug_cnt = 0  # counts the number of "bugs" has been identified

        # This for-loop extracts the results from the scan
        for _file_path in _output_files:
            with open(_file_path) as _f:
                _out = json.load(_f)
                bug_cnt = bug_cnt + len(_out["runs"][0]["results"])
                _results.append(_out["runs"][0]["results"])

        return _results, bug_cnt

    except Exception as e:
        logging.error(f"Exception while .NET Security Analysis: {e}")
        return []
