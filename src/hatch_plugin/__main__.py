# SPDX-FileCopyrightText: 2025-present elkamelsallemi <elkamel.sallemi@gmail.com>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from hatch_plugin.cli import monorepo

    sys.exit(monorepo())
