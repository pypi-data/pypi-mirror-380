"""
Configuration loading and management for the entropy redaction tool.

This module handles loading and validating configuration from YAML files.
"""

import os
import yaml
from pathlib import Path

# Global configuration variables loaded from YAML
CONFIG = None
COMMON_WORDS = set()
COMMON_PREFIXES = set()
COMMON_SUFFIXES = set()
ENTROPY_SETTINGS = {}
REDACTION_PATTERNS = []
AWS_SELECTIVE_PATTERNS = []
EXACT_MATCH_PATTERNS = []
HUMAN_READABLE_DATETIME_PATTERNS = []


def get_default_config_dir():
    """Get the default configuration directory (same as module directory)."""
    return Path(__file__).parent


def load_config(
    words_config_path=None,
    entropy_config_path=None,
    patterns_config_path=None,
    config_dir=None,
):
    """
    Load configuration from YAML files.

    Args:
        words_config_path: Path to common_words.yaml (default: config_dir/common_words.yaml)
        entropy_config_path: Path to entropy_settings.yaml (default: config_dir/entropy_settings.yaml)
        patterns_config_path: Path to redaction_patterns.yaml (default: config_dir/redaction_patterns.yaml)
        config_dir: Directory containing config files (default: module directory)

    Raises:
        FileNotFoundError: If any required config file is not found
        yaml.YAMLError: If any config file cannot be parsed
        SystemExit: If required configuration sections are missing
    """
    global CONFIG, COMMON_WORDS, COMMON_PREFIXES, COMMON_SUFFIXES
    global ENTROPY_SETTINGS, REDACTION_PATTERNS, AWS_SELECTIVE_PATTERNS
    global EXACT_MATCH_PATTERNS, HUMAN_READABLE_DATETIME_PATTERNS

    # Determine config directory
    if config_dir is None:
        config_dir = get_default_config_dir()
    else:
        config_dir = Path(config_dir)

    # Set default paths
    if words_config_path is None:
        words_config_path = config_dir / "common_words.yaml"
    if entropy_config_path is None:
        entropy_config_path = config_dir / "entropy_settings.yaml"
    if patterns_config_path is None:
        patterns_config_path = config_dir / "redaction_patterns.yaml"

    # Load common words configuration
    try:
        with open(words_config_path, "r", encoding="utf-8") as f:
            words_config = yaml.safe_load(f)

        # Load common words into a set for fast lookup
        common_words_list = words_config.get("common_words", [])
        COMMON_WORDS = set(
            word.lower() for word in common_words_list if isinstance(word, str)
        )

        # Load pattern matching configuration
        patterns = words_config.get("word_patterns", {})
        COMMON_PREFIXES = set(patterns.get("prefixes", []))
        COMMON_SUFFIXES = set(patterns.get("suffixes", []))

    except FileNotFoundError:
        print(f"Error: Required config file '{words_config_path}' not found.")
        exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse words YAML config: {e}")
        exit(1)

    # Load entropy settings configuration
    try:
        with open(entropy_config_path, "r", encoding="utf-8") as f:
            entropy_config = yaml.safe_load(f)

        # Extract settings from the structured config - all required
        detection_settings = entropy_config.get("entropy_detection")

        if not detection_settings:
            print(
                f"Error: Missing 'entropy_detection' section in '{entropy_config_path}'"
            )
            exit(1)

        # Extract required settings with validation
        required_detection_keys = [
            "default_threshold",
            "word_pattern_bonus",
            "min_length",
            "window_size",
        ]

        for key in required_detection_keys:
            if key not in detection_settings:
                print(
                    f"Error: Missing required setting 'entropy_detection.{key}' in '{entropy_config_path}'"
                )
                exit(1)

        # Set settings directly from YAML without fallbacks
        ENTROPY_SETTINGS = {
            "default_threshold": detection_settings["default_threshold"],
            "word_pattern_bonus": detection_settings["word_pattern_bonus"],
            "min_length": detection_settings["min_length"],
            "window_size": detection_settings["window_size"],
        }

        # Store the full config for potential future use
        CONFIG = entropy_config

    except FileNotFoundError:
        print(f"Error: Required config file '{entropy_config_path}' not found.")
        exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse entropy YAML config: {e}")
        exit(1)

    # Load redaction patterns configuration
    try:
        with open(patterns_config_path, "r", encoding="utf-8") as f:
            patterns_config = yaml.safe_load(f)

        # Build redaction patterns list from enabled groups
        REDACTION_PATTERNS = []
        enabled_groups = patterns_config.get("pattern_groups", {}).get("enabled", [])

        for group_name in enabled_groups:
            if group_name == "aws_selective_patterns":
                # Handle selective patterns separately
                continue

            group_patterns = patterns_config.get(group_name, {})
            for pattern_name, pattern_value in group_patterns.items():
                if isinstance(pattern_value, str):
                    REDACTION_PATTERNS.append(pattern_value)

        # Load AWS selective patterns
        AWS_SELECTIVE_PATTERNS = []
        selective_patterns = patterns_config.get("aws_selective_patterns", {})
        for pattern_name, pattern_config in selective_patterns.items():
            if (
                isinstance(pattern_config, dict)
                and "pattern" in pattern_config
                and "replacement" in pattern_config
            ):
                AWS_SELECTIVE_PATTERNS.append(
                    (pattern_config["pattern"], pattern_config["replacement"])
                )

        # Load exact match patterns for token validation
        EXACT_MATCH_PATTERNS = []
        exact_patterns = patterns_config.get("exact_match_patterns", {})
        for pattern_name, pattern_value in exact_patterns.items():
            if isinstance(pattern_value, str):
                EXACT_MATCH_PATTERNS.append(pattern_value)

        # Load human-readable datetime patterns
        HUMAN_READABLE_DATETIME_PATTERNS = []
        human_datetime_patterns = patterns_config.get(
            "human_readable_datetime_patterns", {}
        )
        for pattern_name, pattern_value in human_datetime_patterns.items():
            if isinstance(pattern_value, str):
                HUMAN_READABLE_DATETIME_PATTERNS.append(pattern_value)

        # Add custom patterns if any
        custom_patterns = patterns_config.get("custom_patterns", {})
        if custom_patterns:
            for pattern_name, pattern_value in custom_patterns.items():
                if isinstance(pattern_value, str) and not pattern_name.startswith("#"):
                    REDACTION_PATTERNS.append(pattern_value)

    except FileNotFoundError:
        print(f"Error: Required config file '{patterns_config_path}' not found.")
        exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse patterns YAML config: {e}")
        exit(1)
