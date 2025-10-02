"""RealTimeX environment variable loader for browser-use integration."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

from dotenv import dotenv_values


def _get_realtimex_server_dir() -> Path:
	"""Return the RealTimeX server directory using platform-safe joins."""
	return Path.home() / '.realtimex.ai' / 'Resources' / 'server'


# Default RealTimeX configuration directory
_REALTIMEX_SERVER_DIR = _get_realtimex_server_dir()

# Candidate environment filenames in priority order
_ENV_FILENAMES: tuple[str, ...] = ('.env', '.env.production', '.env.development')

# Mapping from RealTimeX-specific variables to browser-use expectations
_ENV_MAPPING: dict[str, str] = {
	'REALTIMEX_AI_API_KEY': 'OPENAI_API_KEY',
	'REALTIMEX_AI_BASE_PATH': 'OPENAI_BASE_URL',
}


def _first_existing_env_file(
	directory: Path = _REALTIMEX_SERVER_DIR,
	filenames: Iterable[str] = _ENV_FILENAMES,
) -> Path | None:
	"""Return the first existing .env file in the RealTimeX directory."""
	for name in filenames:
		candidate = directory / name
		if candidate.exists():
			return candidate
	return None


def load_realtimex_env() -> None:
	"""Load RealTimeX environment variables into the current process."""
	env_file = _first_existing_env_file()
	if not env_file:
		return

	env_values = dotenv_values(env_file)
	if not env_values:
		return

	for source_key, target_key in _ENV_MAPPING.items():
		raw_value = env_values.get(source_key)
		if not raw_value:
			continue

		value = raw_value.strip() if isinstance(raw_value, str) else raw_value
		if not value:
			continue

		# Preserve explicitly-set environment variables
		if os.getenv(target_key):
			continue

		os.environ[target_key] = str(value)


__all__ = ['load_realtimex_env']
