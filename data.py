"""AI Agent Skills & Extensions Directory — curated registry.

A catalog of the **skill / extension ecosystems** that extend what an AI agent or
assistant can *do* — the open protocols for wiring up tools/skills, the platform
"skill systems" (custom assistants + actions) from the major AI providers, and
the marketplaces where skills/agents are shared.

This is distinct from a list of individual tools/libraries (see "agent tools")
or code SDKs (see "agent frameworks"): here we catalog the *systems, protocols,
and marketplaces* themselves. Each entry records: name, org, category, whether it
is open source, its license (or "Proprietary"), a short note, and a canonical
link. This space is new and fast-moving — uncertain entries/URLs are omitted.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Category(Enum):
    skill_protocol = "skill_protocol"
    platform_skills = "platform_skills"
    marketplace = "marketplace"

    @property
    def label(self) -> str:
        return {
            "skill_protocol": "Skill & Tool Protocols",
            "platform_skills": "Platform Skill Systems",
            "marketplace": "Skill / Agent Marketplaces",
        }[self.value]


@dataclass(frozen=True)
class Tool:
    name: str
    org: str
    category: Category
    url: str               # canonical homepage / spec
    open_source: bool
    license: str           # SPDX-ish id, or "Proprietary"
    note: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)


# ---------------------------------------------------------------------------
# Registry — curated, public agent-skill systems/protocols/marketplaces.
# Curated conservatively; uncertain entries/URLs omitted.
# ---------------------------------------------------------------------------
TOOLS: list[Tool] = [
    # --- Skill & tool protocols ---
    Tool("Model Context Protocol (MCP)", "Anthropic (open standard)", Category.skill_protocol,
         "https://modelcontextprotocol.io", True, "MIT",
         note="Open standard for connecting agents to tools, data sources, and skills.",
         tags=("protocol", "open", "popular")),

    # --- Platform skill systems ---
    Tool("Anthropic Agent Skills", "Anthropic", Category.platform_skills,
         "https://www.anthropic.com", False, "Proprietary",
         note="Composable Skills (instructions + optional scripts) that extend Claude for tasks.",
         tags=("claude", "skills")),
    Tool("OpenAI GPTs & GPT Store", "OpenAI", Category.platform_skills,
         "https://chatgpt.com/gpts", False, "Proprietary",
         note="Custom GPTs (assistants + actions) built and shared via the GPT Store.",
         tags=("gpts", "actions")),
    Tool("Google Gemini Gems", "Google", Category.platform_skills,
         "https://gemini.google.com", False, "Proprietary",
         note="Custom 'Gems' that tailor Gemini for specific, repeatable tasks.",
         tags=("gemini", "gems")),
    Tool("Microsoft Copilot Studio", "Microsoft", Category.platform_skills,
         "https://copilotstudio.microsoft.com", False, "Proprietary",
         note="Build custom copilots/agents with skills, topics, and connectors.",
         tags=("copilot", "low-code")),
    Tool("Amazon Bedrock Agents", "AWS", Category.platform_skills,
         "https://aws.amazon.com/bedrock/agents/", False, "Proprietary",
         note="Agents with action groups (skills) backed by Lambda/APIs.",
         tags=("bedrock", "action-groups")),
    Tool("Salesforce Agentforce", "Salesforce", Category.platform_skills,
         "https://www.salesforce.com/agentforce/", False, "Proprietary",
         note="Platform for building agents with reusable actions/skills.",
         tags=("enterprise", "actions")),
    Tool("BulkPublish Social Media Content Skills", "BulkPublish", Category.platform_skills,
         "https://github.com/azeemkafridi/bulkpublish-api/tree/main/skills/social-media-content-skills",
         True, "MIT",
         note="Open social-media skill system for approval-first content adaptation, scheduling, and publishing via BulkPublish API and MCP.",
         tags=("social-media", "marketing", "mcp", "api")),

    # --- Skill / agent marketplaces ---
    Tool("Poe", "Quora", Category.marketplace,
         "https://poe.com", False, "Proprietary",
         note="Build and share custom AI bots across many models in a marketplace.",
         tags=("bots", "marketplace")),
    Tool("Alexa Skills", "Amazon", Category.marketplace,
         "https://developer.amazon.com/alexa/alexa-skills-kit", False, "Proprietary",
         note="Voice-assistant skills — the foundational consumer 'skills' ecosystem.",
         tags=("voice", "skills-kit")),
]
