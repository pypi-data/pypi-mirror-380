"""
Configuration for Table Categorization Agent

Centralized configuration management using sfn_blueprint.
"""

from sfn_blueprint.config import SFNConfigManager

# Initialize configuration manager
config_manager = SFNConfigManager()

# Default configuration values
DEFAULT_CONFIG = {
    "ai": {
        "default_model": "gpt-4o-mini",
        "max_tokens": 1000,
        "temperature": 0.1,
        "timeout": 30,
    },
    "categorization": {
        "min_confidence_threshold": 0.7,
        "min_quality_threshold": 0.7,
        "max_sample_values": 5,
        "export_format": "json",
    },
    "logging": {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    },
}


# Get configuration with defaults
def get_config():
    """Get configuration with defaults"""
    config = config_manager.get_config()

    # Merge with defaults
    for section, values in DEFAULT_CONFIG.items():
        if section not in config:
            config[section] = {}
        for key, value in values.items():
            if key not in config[section]:
                config[section][key] = value

    return config


# Configuration getters
def get_ai_config():
    """Get AI configuration"""
    config = get_config()
    return config.get("ai", DEFAULT_CONFIG["ai"])


def get_categorization_config():
    """Get categorization configuration"""
    config = get_config()
    return config.get("categorization", DEFAULT_CONFIG["categorization"])


def get_logging_config():
    """Get logging configuration"""
    config = get_config()
    return config.get("logging", DEFAULT_CONFIG["logging"])
