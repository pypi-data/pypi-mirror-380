# SPDX-License-Identifier: CC-BY-SA-3.0-DE
# SPDX-FileCopyrightText: 2025 PyGremlinBox Maintainer <simon@sigre.xyz>

"""
PyGremlinBox CC-BY-SA-3.0-DE - Supply chain security testing module.

This package is licenced under the Creative Commons Attribution-ShareAlike 3.0 Germany (CC-BY-SA-3.0-DE).
It is designed for testing supply chain security tools and their ability to detect
licences in Python packages.

The package provides basic functionality for licence detection testing whilst
maintaining compliance with CC-BY-SA-3.0-DE requirements.
"""

__version__ = "1.3.0"
__licence__ = "CC-BY-SA-3.0-DE"

import os
from pathlib import Path


def get_licence_identifier():
    """
    Return the licence identifier for this package.
    
    Returns:
        str: The SPDX licence identifier
    """
    return "CC-BY-SA-3.0-DE"


def retrieve_licence_content():
    """
    Retrieve the full licence text content.
    
    Returns:
        str: The complete licence text, or error message if not found
    """
    try:
        # Look for licence file in package root
        package_dir = Path(__file__).parent.parent.parent
        licence_file = package_dir / "LICENCE"
        
        if licence_file.exists():
            return licence_file.read_text(encoding='utf-8')
        else:
            return f"Licence file not found at expected location: {licence_file}"
    except Exception as e:
        return f"Error reading licence file: {str(e)}"


def get_package_metadata():
    """
    Return basic metadata about this package.
    
    Returns:
        dict: Package metadata including name, version, and licence
    """
    return {
        "name": "pygremlinbox-cc-by-sa-3-0-de",
        "version": __version__,
        "licence": __licence__,
        "description": "Supply chain security testing module with Creative Commons Attribution-ShareAlike 3.0 Germany",
        "spdx_licence_id": "CC-BY-SA-3.0-DE"
    }


# Export main functions
__all__ = [
    "get_licence_identifier", 
    "retrieve_licence_content", 
    "get_package_metadata"
]