"""
Core entropy calculation and redaction functions.

This module contains the main logic for detecting and redacting high-entropy strings
while preserving common words and applying pattern-based detection.
"""

import math
import re
from collections import Counter

from . import config


def is_common_word(word):
    """Check if a word is a common English word or technical term."""
    return word.lower() in config.COMMON_WORDS


def is_always_redact_pattern(text):
    """
    Check if text matches patterns that should always be redacted regardless of word detection.
    This includes timestamps, UUIDs, long numeric sequences, etc.
    """
    # UUID patterns (8-4-4-4-12 hex digits)
    uuid_pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    if re.match(uuid_pattern, text):
        return True

    # Partial UUID segments (hex characters that are likely random)
    # Must be 6+ chars OR contain both letters and numbers OR not be common values
    if len(text) >= 4 and re.match(r"^[0-9a-fA-F]+$", text):
        # Exclude common words that happen to be hex
        common_hex_words = {
            "beef",
            "cafe",
            "dead",
            "face",
            "fade",
            "feed",
            "deed",
            "bead",
            "deaf",
        }

        # If it's all numeric, apply stricter rules
        if text.isdigit():
            num_val = int(text)
            # Don't redact years, small port numbers, or common small numbers
            if (
                1900 <= num_val <= 2100
                or 1 <= num_val <= 1000  # Years  # Small numbers
                or num_val
                in {8080, 8443, 3000, 5432, 3306, 5000, 9000}  # Common ports
            ):
                return False

        # If it's 6+ characters or contains both letters and digits, likely random
        if len(text) >= 6 or (
            any(c.isdigit() for c in text) and any(c.isalpha() for c in text)
        ):
            if text.lower() not in common_hex_words:
                return True

    # Long numeric sequences (8+ digits, often account IDs, timestamps)
    # But exclude reasonable years (1900-2100) and short numeric values
    if len(text) >= 8 and text.isdigit():
        return True

    # Also catch 6-7 digit sequences that are likely IDs
    if len(text) >= 6 and text.isdigit():
        # Exclude years and reasonable small numbers
        num_val = int(text)
        if not (1900 <= num_val <= 2100 or num_val <= 100):
            return True

    # Epoch timestamps (10 or 13 digits)
    if text.isdigit():
        # 10-digit epoch (seconds since 1970) - roughly 2001-2038 range
        if len(text) == 10 and 1000000000 <= int(text) <= 2147483647:
            return True
        # 13-digit epoch (milliseconds since 1970)
        if len(text) == 13 and 1000000000000 <= int(text) <= 2147483647000:
            return True

    # Date/time string patterns from YAML configuration
    for pattern in config.EXACT_MATCH_PATTERNS:
        if re.match(pattern, text):
            return True

    # Human-readable datetime strings from YAML configuration
    for pattern in config.HUMAN_READABLE_DATETIME_PATTERNS:
        if re.match(pattern, text, re.IGNORECASE):
            return True

    # Mixed alphanumeric sequences that look like tokens/hashes (6+ chars, mixed case/digits)
    if (
        len(text) >= 6
        and any(c.isdigit() for c in text)
        and any(c.isalpha() for c in text)
        and not any(c in "aeiouAEIOU" for c in text[1:-1])
    ):  # No vowels in middle (unlikely to be words)
        return True

    # Base64-like patterns (ends with = or ==, or long alphanumeric)
    if (
        len(text) >= 8
        and (text.endswith("=") or text.endswith("=="))
        and re.match(r"^[A-Za-z0-9+/]+=*$", text)
    ):
        return True

    return False


def has_word_pattern(text):
    """
    Check if text follows common word patterns that suggest it's a real word
    rather than random characters.
    """
    text_lower = text.lower()

    # Check for prefix patterns
    for prefix in config.COMMON_PREFIXES:
        if text_lower.startswith(prefix) and len(text) > len(prefix) + 2:
            return True

    # Check for suffix patterns
    for suffix in config.COMMON_SUFFIXES:
        if text_lower.endswith(suffix) and len(text) > len(suffix) + 2:
            return True

    # Check for vowel distribution (real words usually have vowels)
    vowels = set("aeiou")
    vowel_count = sum(1 for c in text_lower if c in vowels)
    vowel_ratio = vowel_count / len(text) if text else 0

    # Real words typically have 20-50% vowels
    if 0.2 <= vowel_ratio <= 0.5:
        return True

    return False


def calculate_entropy(text):
    """Calculate Shannon entropy of a string."""
    if not text:
        return 0

    # Count character frequencies
    char_counts = Counter(text.lower())
    length = len(text)

    # Calculate entropy
    entropy = 0
    for count in char_counts.values():
        probability = count / length
        if probability > 0:
            entropy -= probability * math.log2(probability)

    return entropy


def is_high_entropy_segment(segment, entropy_threshold=None, min_length=None):
    """
    Determine if a segment has high entropy and is not a common word.

    Args:
        segment: String segment to analyze
        entropy_threshold: Minimum entropy to consider "high" (uses config default if None)
        min_length: Minimum length to consider for redaction (uses config default if None)

    Returns:
        bool: True if segment should be redacted
    """
    # Use configured defaults if not specified
    if entropy_threshold is None:
        entropy_threshold = config.ENTROPY_SETTINGS.get("default_threshold", 2.5)
    if min_length is None:
        min_length = config.ENTROPY_SETTINGS.get("min_length", 4)

    if len(segment) < min_length:
        return False

    # Check for patterns that should always be redacted (timestamps, UUIDs, etc.)
    if is_always_redact_pattern(segment):
        return True

    # Check if it's a common word - if so, don't redact
    if is_common_word(segment):
        return False

    # Check if it has word-like patterns - if so, be more conservative
    if has_word_pattern(segment):
        # For word-like patterns, require higher entropy to redact
        word_pattern_bonus = config.ENTROPY_SETTINGS.get("word_pattern_bonus", 0.5)
        entropy_threshold = entropy_threshold + word_pattern_bonus

    entropy = calculate_entropy(segment)

    # Additional heuristics for common high-entropy patterns
    has_mixed_case = any(c.isupper() for c in segment) and any(
        c.islower() for c in segment
    )
    has_digits_and_letters = any(c.isdigit() for c in segment) and any(
        c.isalpha() for c in segment
    )
    digit_ratio = sum(1 for c in segment if c.isdigit()) / len(segment)

    # Boost entropy score for mixed patterns
    adjusted_entropy = entropy
    if has_mixed_case:
        adjusted_entropy += 0.3
    if has_digits_and_letters:
        adjusted_entropy += 0.4
    if digit_ratio > 0.6:  # Mostly numeric sequences
        adjusted_entropy += 0.2

    return adjusted_entropy >= entropy_threshold


def redact_high_entropy_strings(
    text,
    entropy_threshold=None,
    min_length=None,
    window_size=None,
    condense_asterisks=None,
):
    """
    Redact high-entropy substrings from text using a sliding window approach.

    Args:
        text: Input string to process
        entropy_threshold: Minimum entropy to consider "high" (uses config default if None)
        min_length: Minimum length of segments to consider (uses config default if None)
        window_size: Size of sliding window for analysis (uses config default if None)
        condense_asterisks: If True, condense consecutive asterisks to single asterisk

    Returns:
        str: Text with high-entropy segments replaced with asterisks
    """
    # Use configured defaults if not specified
    if entropy_threshold is None:
        entropy_threshold = config.ENTROPY_SETTINGS.get("default_threshold", 2.5)
    if min_length is None:
        min_length = config.ENTROPY_SETTINGS.get("min_length", 4)
    if window_size is None:
        window_size = config.ENTROPY_SETTINGS.get("window_size", 6)
    if condense_asterisks is None:
        condense_asterisks = False

    if len(text) < min_length:
        return text

    # Split text into tokens (preserve separators)
    tokens = re.findall(r"[a-zA-Z0-9]+|[^a-zA-Z0-9]", text)

    redacted_tokens = []

    for token in tokens:
        if not re.match(r"^[a-zA-Z0-9]+$", token):
            # Keep separators as-is
            redacted_tokens.append(token)
            continue

        if len(token) < min_length:
            # Keep short tokens as-is
            redacted_tokens.append(token)
            continue

        # Use sliding window to find high-entropy regions
        redacted_chars = list(token)
        i = 0

        while i <= len(token) - window_size:
            window = token[i : i + window_size]

            if is_high_entropy_segment(window, entropy_threshold, min_length):
                # Mark this region for redaction and extend it
                start = i
                end = i + window_size

                # Extend backwards if previous chars are also high entropy
                while start > 0:
                    extended_window = token[start - 1 : end]
                    if is_high_entropy_segment(
                        extended_window, entropy_threshold, min_length
                    ):
                        start -= 1
                    else:
                        break

                # Extend forwards if next chars are also high entropy
                while end < len(token):
                    extended_window = token[start : end + 1]
                    if is_high_entropy_segment(
                        extended_window, entropy_threshold, min_length
                    ):
                        end += 1
                    else:
                        break

                # Redact the identified region
                for j in range(start, end):
                    redacted_chars[j] = "*"

                # Skip ahead to avoid overlapping redactions
                i = end
            else:
                i += 1

        redacted_tokens.append("".join(redacted_chars))

    result = "".join(redacted_tokens)

    # Condense consecutive asterisks if requested
    if condense_asterisks:
        result = re.sub(r"\*+", "*", result)

    return result


def redact_high_entropy_tokens(
    text, entropy_threshold=None, min_length=None, condense_asterisks=None
):
    """
    Simpler approach that analyzes and redacts entire tokens.
    Also handles multi-token datetime patterns.

    Args:
        text: Input string to process
        entropy_threshold: Minimum entropy to consider "high" (uses config default if None)
        min_length: Minimum length of tokens to consider (uses config default if None)
        condense_asterisks: If True, condense consecutive asterisks to single asterisk

    Returns:
        str: Text with high-entropy tokens replaced with asterisks
    """
    # Use configured defaults if not specified
    if entropy_threshold is None:
        entropy_threshold = config.ENTROPY_SETTINGS.get("default_threshold", 2.5)
    if min_length is None:
        min_length = config.ENTROPY_SETTINGS.get("min_length", 4)
    if condense_asterisks is None:
        condense_asterisks = False

    # First, check for multi-token datetime patterns that should be redacted entirely
    datetime_replacements = []

    # Use patterns loaded from YAML configuration
    for pattern in config.REDACTION_PATTERNS:
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        for match in matches:
            replacement = "*" * len(match.group())
            datetime_replacements.append((match.start(), match.end(), replacement))

    # Selective redaction for AWS service hostnames (preserve service/domain parts)
    for pattern, replacement in config.AWS_SELECTIVE_PATTERNS:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Apply datetime replacements first
    if datetime_replacements:
        # Sort by start position in reverse order to avoid index shifts
        datetime_replacements.sort(key=lambda x: x[0], reverse=True)
        result_text = text
        for start, end, replacement in datetime_replacements:
            result_text = result_text[:start] + replacement + result_text[end:]
        text = result_text

    # Split on common separators while preserving them
    parts = re.split(r"([^a-zA-Z0-9]+)", text)

    redacted_parts = []
    for part in parts:
        if re.match(r"^[a-zA-Z0-9]+$", part) and is_high_entropy_segment(
            part, entropy_threshold, min_length
        ):
            # Redact high-entropy alphanumeric tokens
            redacted_parts.append("*" * len(part))
        else:
            redacted_parts.append(part)

    result = "".join(redacted_parts)

    # Condense consecutive asterisks if requested
    if condense_asterisks:
        result = re.sub(r"\*+", "*", result)

    return result


def redact_sensitive_data(
    text, entropy_threshold=None, min_length=None, condense_asterisks=None
):
    """
    Default function for redacting sensitive data using the token-based approach.

    This is the recommended function to use as it provides the most reliable results
    by analyzing complete tokens and using pattern-based detection for structured data.

    Args:
        text: Input string to process
        entropy_threshold: Minimum entropy to consider "high" (uses config default if None)
        min_length: Minimum length of tokens to consider (uses config default if None)
        condense_asterisks: If True, condense consecutive asterisks to single asterisk

    Returns:
        str: Text with high-entropy tokens and structured patterns replaced with asterisks
    """
    return redact_high_entropy_tokens(
        text, entropy_threshold, min_length, condense_asterisks
    )
