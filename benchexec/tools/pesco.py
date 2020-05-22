# This file is part of BenchExec, a framework for reliable benchmarking:
# https://github.com/sosy-lab/benchexec
#
# SPDX-FileCopyrightText: 2007-2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import benchexec.tools.cpachecker as cpachecker


class Tool(cpachecker.Tool):
    """Tool info for PeSCo."""

    REQUIRED_PATHS = [
        "lib/java/runtime",
        "lib/*.jar",
        "lib/native/x86_64-linux",
        "scripts",
        "cpachecker.jar",
        "config",
        "resources",
    ]

    def name(self):
        return "PeSCo"
