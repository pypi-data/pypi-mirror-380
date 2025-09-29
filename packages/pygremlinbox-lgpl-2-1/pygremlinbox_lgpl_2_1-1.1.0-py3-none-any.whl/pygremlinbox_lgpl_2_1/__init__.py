# SPDX-License-Identifier: LGPL-2.1-only
# SPDX-FileCopyrightText: 2025 PyGremlinBox Maintainer <simon@sigre.xyz>

"""PyGremlinBox LGPL-2.1 - Supply chain security testing package."""

__version__ = "1.1.0"

from .licence_reader import retrieve_licence_content, get_licence_identifier, get_package_metadata

__all__ = ["retrieve_licence_content", "get_licence_identifier", "get_package_metadata"]