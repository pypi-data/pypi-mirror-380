"""JSON schema helpers for lean Bitbucket tools."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict

BITBUCKET_DEFS: Dict[str, Any] = {
    "$id": "bitbucket.defs",
    "$defs": {
        "Id": {"type": ["string", "integer"]},
        "Url": {"type": "string", "format": "uri"},
        "Cursor": {"type": ["string", "null"]},
        "Verbosity": {"enum": ["ids", "summary", "full"]},
        "PRItem": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {"$ref": "#/$defs/Id"},
                "title": {"type": "string"},
                "state": {"type": "string"},
                "approvals": {"type": "integer", "minimum": 0},
                "tasks_open": {"type": "integer", "minimum": 0},
                "updated": {"type": "string"},
                "url": {"$ref": "#/$defs/Url"},
            },
            "required": ["id", "title", "state"],
        },
        "CommentLite": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {"$ref": "#/$defs/Id"},
                "author": {"type": "string"},
                "short": {"type": "string"},
                "file": {"type": "string"},
                "line": {"type": "integer", "minimum": 1},
            },
            "required": ["id", "short"],
        },
        "User": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "uuid": {"$ref": "#/$defs/Id"},
                "display_name": {"type": "string"},
                "nickname": {"type": "string"},
                "account_id": {"type": "string"},
            },
            "required": ["uuid"],
        },
    },
}


def with_defs(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Attach the shared $defs to a schema copy."""

    combined = deepcopy(schema)
    combined.setdefault("$defs", BITBUCKET_DEFS["$defs"])
    return combined


TOOL_SPECS: Dict[str, Dict[str, Any]] = {
    "pr.list": {
        "description": "List PRs with compact metadata.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "anyOf": [
                                {"type": "string"},
                                {"$ref": "#/$defs/PRItem"},
                            ]
                        },
                    },
                    "next": {"$ref": "#/$defs/Cursor"},
                },
                "required": ["items"],
            }
        ),
    },
    "pr.overview": {
        "description": "Return PR digest: meta, blockers, comments, diffstat.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "pr": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "id": {"$ref": "#/$defs/Id"},
                            "title": {"type": "string"},
                            "state": {"type": "string"},
                            "author": {"type": "string"},
                            "updated": {"type": "string"},
                            "url": {"$ref": "#/$defs/Url"},
                            "source": {"type": "string"},
                            "destination": {"type": "string"},
                        },
                        "required": ["id", "title", "state"],
                    },
                    "blockers": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "checks_failing": {"type": "integer", "minimum": 0},
                            "required_approvals_left": {"type": "integer", "minimum": 0},
                            "pending_tasks": {"type": "integer", "minimum": 0},
                            "merge_conflicts": {"type": "boolean"},
                        },
                        "required": ["checks_failing", "required_approvals_left", "pending_tasks"],
                    },
                    "diffstat_top": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "path": {"type": "string"},
                                "add": {"type": "integer"},
                                "del": {"type": "integer"},
                            },
                            "required": ["path"],
                        },
                    },
                    "comments_recent": {
                        "type": "array",
                        "items": {"$ref": "#/$defs/CommentLite"},
                    },
                    "next": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "comments_cursor": {"$ref": "#/$defs/Cursor"},
                            "files_cursor": {"$ref": "#/$defs/Cursor"},
                        },
                    },
                },
                "required": ["pr", "blockers", "diffstat_top", "comments_recent"],
            }
        ),
    },
    "pr.review": {
        "description": "Return structured review guidance.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "summary": {"type": "string"},
                    "findings": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "severity": {"enum": ["high", "med", "low"]},
                                "title": {"type": "string"},
                                "why": {"type": "string"},
                                "file": {"type": "string"},
                                "line": {"type": "integer", "minimum": 1},
                                "suggest": {"type": "string"},
                            },
                            "required": ["severity", "title", "why"],
                        },
                    },
                    "suggested_inline_comments": {
                        "type": "array",
                        "items": {"$ref": "#/$defs/CommentLite"},
                    },
                },
                "required": ["summary", "findings", "suggested_inline_comments"],
            }
        ),
    },
    "pr.comment.add": {
        "description": "Add a PR comment (optional inline).",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "id": {"$ref": "#/$defs/Id"},
                    "url": {"$ref": "#/$defs/Url"},
                },
                "required": ["id", "url"],
            }
        ),
    },
    "pr.upsert": {
        "description": "Create or update a pull request.\n\nDefault reviewers list is available via \"workspace://{workspace}/default-reviewers\" resource.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "action": {"enum": ["created", "updated"]},
                    "id": {"$ref": "#/$defs/Id"},
                    "title": {"type": "string"},
                    "state": {"type": "string"},
                    "source": {"type": ["string", "null"]},
                    "destination": {"type": ["string", "null"]},
                    "url": {"$ref": "#/$defs/Url"},
                },
                "required": ["action", "id", "title", "state", "url"],
            }
        ),
    },
    "pr.tasks.sync": {
        "description": "Create and resolve PR tasks.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "created": {
                        "type": "array",
                        "items": {"$ref": "#/$defs/Id"},
                    },
                    "resolved": {
                        "type": "array",
                        "items": {"$ref": "#/$defs/Id"},
                    },
                    "remaining": {"type": "integer", "minimum": 0},
                },
                "required": ["created", "resolved", "remaining"],
            }
        ),
    },
    "pipe.run": {
        "description": "Start a pipeline for a branch/commit.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "pipeline_id": {"$ref": "#/$defs/Id"},
                    "url": {"$ref": "#/$defs/Url"},
                },
                "required": ["pipeline_id", "url"],
            }
        ),
    },
    "pipe.fail.summary": {
        "description": "Summarize failing pipeline steps.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "id": {"$ref": "#/$defs/Id"},
                                "step": {"type": "string"},
                                "error_kind": {"type": "string"},
                                "top_lines": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "maxItems": 20,
                                },
                                "suspected_commit": {"type": "string"},
                                "fix_hints": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                },
                                "url": {"$ref": "#/$defs/Url"},
                            },
                            "required": ["id", "step", "url"],
                        },
                    },
                },
                "required": ["items"],
            }
        ),
    },
    "workspace.list": {
        "description": "List repos, members, or projects.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "items": {"type": "array"},
                    "next": {"$ref": "#/$defs/Cursor"},
                },
                "required": ["items"],
            }
        ),
    },
    "repo.get": {
        "description": "Get repo basics and PR sample.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "slug": {"type": "string"},
                    "default_branch": {"type": "string"},
                    "perms": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "recent_prs": {
                        "type": "array",
                        "maxItems": 5,
                        "items": {"$ref": "#/$defs/PRItem"},
                    },
                    "url": {"$ref": "#/$defs/Url"},
                },
                "required": ["slug", "recent_prs"],
            }
        ),
    },
    "me.whoami": {
        "description": "Return identity and workspace slugs.",
        "output_schema": with_defs(
            {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "user": {"$ref": "#/$defs/User"},
                    "workspaces": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
                "required": ["user"],
            }
        ),
    },
}
