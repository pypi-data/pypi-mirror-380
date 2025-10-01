"""
AI LLS Library - Core business logic for Landline Scrubber.

This library provides phone verification and DNC checking capabilities.
"""
from ai_lls_lib.core.models import (
    PhoneVerification,
    BulkJob,
    BulkJobStatus,
    LineType,
    VerificationSource,
    JobStatus
)
from ai_lls_lib.core.verifier import PhoneVerifier
from ai_lls_lib.core.processor import BulkProcessor
from ai_lls_lib.core.cache import DynamoDBCache

__version__ = "1.4.0-rc.6"
__all__ = [
    "PhoneVerification",
    "BulkJob",
    "BulkJobStatus",
    "LineType",
    "VerificationSource",
    "JobStatus",
    "PhoneVerifier",
    "BulkProcessor",
    "DynamoDBCache",
]
