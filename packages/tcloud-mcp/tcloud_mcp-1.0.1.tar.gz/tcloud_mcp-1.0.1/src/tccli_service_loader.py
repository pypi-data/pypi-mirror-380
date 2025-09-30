"""
TCCLI Service Definition Loader

Loads service definitions from tccli/services directory to provide
rich API descriptions and examples.
"""

import json
import os
import glob
from typing import Dict, Any, List, Optional
from pathlib import Path


class TCCLIServiceLoader:
    """Loads TCCLI service definitions from JSON files."""

    def __init__(self, tccli_root: str = None):
        """Initialize with TCCLI root directory."""
        if tccli_root is None:
            # Try to find tccli directory relative to current file
            current_dir = Path(__file__).parent.parent.parent
            self.tccli_root = current_dir / "tccli"
        else:
            self.tccli_root = Path(tccli_root)

        self.services_dir = self.tccli_root / "services"
        self._service_cache = {}
        self._api_cache = {}
        self._examples_cache = {}

    def get_available_services(self) -> List[str]:
        """Get list of available services from tccli/services directory."""
        if not self.services_dir.exists():
            return []

        services = []
        for service_dir in self.services_dir.iterdir():
            if service_dir.is_dir() and not service_dir.name.startswith('.'):
                services.append(service_dir.name)

        return sorted(services)

    def get_service_versions(self, service: str) -> List[str]:
        """Get available versions for a service."""
        service_path = self.services_dir / service
        if not service_path.exists():
            return []

        versions = []
        for version_dir in service_path.iterdir():
            if version_dir.is_dir() and version_dir.name.startswith('v'):
                versions.append(version_dir.name)

        return sorted(versions)

    def load_api_definitions(self, service: str, version: str = None) -> Optional[Dict[str, Any]]:
        """Load API definitions from api.json."""
        if version is None:
            # Get the latest version
            versions = self.get_service_versions(service)
            if not versions:
                return None
            version = versions[-1]  # Use latest version

        cache_key = f"{service}_{version}_api"
        if cache_key in self._api_cache:
            return self._api_cache[cache_key]

        api_file = self.services_dir / service / version / "api.json"
        if not api_file.exists():
            return None

        try:
            with open(api_file, 'r', encoding='utf-8') as f:
                api_data = json.load(f)

            self._api_cache[cache_key] = api_data
            return api_data
        except Exception as e:
            print(f"Error loading API definitions for {service} {version}: {e}")
            return None

    def load_examples(self, service: str, version: str = None) -> Optional[Dict[str, Any]]:
        """Load examples from examples.json."""
        if version is None:
            versions = self.get_service_versions(service)
            if not versions:
                return None
            version = versions[-1]

        cache_key = f"{service}_{version}_examples"
        if cache_key in self._examples_cache:
            return self._examples_cache[cache_key]

        examples_file = self.services_dir / service / version / "examples.json"
        if not examples_file.exists():
            return None

        try:
            with open(examples_file, 'r', encoding='utf-8') as f:
                examples_data = json.load(f)

            self._examples_cache[cache_key] = examples_data
            return examples_data
        except Exception as e:
            print(f"Error loading examples for {service} {version}: {e}")
            return None

    def get_service_info(self, service: str, version: str = None) -> Dict[str, Any]:
        """Get comprehensive service information."""
        api_data = self.load_api_definitions(service, version)
        examples_data = self.load_examples(service, version)

        if not api_data:
            return {"error": f"Service {service} not found or invalid"}

        if version is None:
            versions = self.get_service_versions(service)
            version = versions[-1] if versions else "unknown"

        actions = api_data.get("actions", {})

        return {
            "service": service,
            "version": version,
            "total_actions": len(actions),
            "available_actions": sorted(actions.keys()),
            "has_examples": examples_data is not None,
            "metadata": api_data.get("metadata", {})
        }

    def get_action_info(self, service: str, action: str, version: str = None) -> Dict[str, Any]:
        """Get detailed information about a specific action."""
        api_data = self.load_api_definitions(service, version)
        examples_data = self.load_examples(service, version)

        if not api_data:
            return {"error": f"Service {service} not found"}

        actions = api_data.get("actions", {})
        if action not in actions:
            return {"error": f"Action {action} not found in service {service}"}

        action_info = actions[action]
        result = {
            "service": service,
            "action": action,
            "name": action_info.get("name", action),
            "document": action_info.get("document", ""),
            "input": action_info.get("input", ""),
            "output": action_info.get("output", ""),
            "status": action_info.get("status", "unknown")
        }

        # Add examples if available
        if examples_data and "actions" in examples_data:
            action_examples = examples_data["actions"].get(action, [])
            if action_examples:
                result["examples"] = []
                for example in action_examples:
                    example_info = {
                        "title": example.get("title", ""),
                        "document": example.get("document", ""),
                        "input": example.get("input", ""),
                        "output": example.get("output", "")
                    }
                    result["examples"].append(example_info)

        return result

    def search_actions(self, query: str, service: str = None) -> List[Dict[str, Any]]:
        """Search for actions matching the query."""
        results = []

        services_to_search = [service] if service else self.get_available_services()

        for svc in services_to_search:
            api_data = self.load_api_definitions(svc)
            if not api_data:
                continue

            actions = api_data.get("actions", {})
            for action_name, action_info in actions.items():
                # Search in action name, display name, and document
                searchable_text = f"{action_name} {action_info.get('name', '')} {action_info.get('document', '')}"
                if query.lower() in searchable_text.lower():
                    results.append({
                        "service": svc,
                        "action": action_name,
                        "name": action_info.get("name", action_name),
                        "document": action_info.get("document", "")[:200] + "..." if len(action_info.get("document", "")) > 200 else action_info.get("document", "")
                    })

        return results