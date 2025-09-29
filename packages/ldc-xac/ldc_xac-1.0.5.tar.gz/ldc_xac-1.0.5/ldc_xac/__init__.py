"""
External API Caller - XAC

A utility package for making external API calls with comprehensive logging.
"""

import logging
from .api_caller import ExternalAPICaller, make_external_api_request

# # Auto-configure logging if not already configured
# if not logging.getLogger("ldc_xac").handlers:
#     logging.basicConfig(
#         level=logging.INFO,
#         format='%(message)s'
#     )

__version__ = "1.0.5"
__author__ = "Ayush Sonar"
__all__ = ["ExternalAPICaller", "make_external_api_request"]
