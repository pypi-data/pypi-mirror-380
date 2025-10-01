#!/usr/bin/env python3
import urllib.request
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class TemplateInfo:
    name: str
    url: str

GITHUB_TEMPLATES: List[TemplateInfo] = [
    TemplateInfo(
        name="example",
        url="https://raw.githubusercontent.com/browserbase/stagehand-python/main/examples/example.py",
    ),
    TemplateInfo(
        name="cua-example",
        url="https://raw.githubusercontent.com/browserbase/stagehand-python/main/examples/cua-example.py",
    ),
    TemplateInfo(
        name="form-filling",
        url="https://raw.githubusercontent.com/browserbase/templates/refs/heads/dev/python/formFilling/index.py?token=GHSAT0AAAAAAC7F2JVDHB7PHQBEWCEXIM762G4ZJYA",
    ),
    TemplateInfo(
        name="gift-finder",
        url="https://raw.githubusercontent.com/browserbase/templates/refs/heads/dev/python/giftfinder/index.py?token=GHSAT0AAAAAAC7F2JVCKUTJOS2PJUTQRQ2Q2G4ZT4A",
    ),
    TemplateInfo(
        name="pickleball",
        url="https://raw.githubusercontent.com/browserbase/templates/refs/heads/dev/python/pickleball/index.py?token=GHSAT0AAAAAAC7F2JVDHB7PHQBEWCEXIM762G4ZJYA",
    ),
    TemplateInfo(
        name="real-estate-check",
        url="https://raw.githubusercontent.com/browserbase/templates/refs/heads/dev/python/realEstateCheck/index.py?token=GHSAT0AAAAAAC7F2JVDHB7PHQBEWCEXIM762G4ZJYA",
    ),
    TemplateInfo(
        name="context",
        url="https://raw.githubusercontent.com/browserbase/templates/refs/heads/dev/python/context/index.py?token=GHSAT0AAAAAAC7F2JVDHB7PHQBEWCEXIM762G4ZJYA",
    ),
]

def get_template_by_name(name: str) -> Optional[TemplateInfo]:
    """Get a specific template by name."""
    for template in GITHUB_TEMPLATES:
        if template.name == name:
            return template
    return None

def fetch_template_content(template: TemplateInfo) -> Optional[str]:
    """Fetch the content of a specific template from GitHub."""
    try:
        req = urllib.request.Request(template.url)
        req.add_header("User-Agent", "create-browser-app-py")

        with urllib.request.urlopen(req) as response:
            if response.status != 200:
                return None
            return response.read().decode("utf-8")
    except Exception:
        return None

def get_available_templates() -> List[str]:
    """Get a list of available template names."""
    default_templates = ["basic"]
    github_templates = [t.name for t in GITHUB_TEMPLATES]
    return default_templates + github_templates

def list_templates() -> List[str]:
    """Get a list of template names."""
    return get_available_templates()