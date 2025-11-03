import json
from pathlib import Path

import pytest

CHATFLOW_PATH = Path(__file__).resolve().parents[1] / "BuddyCall_Prototype Chatflow.json"


def load_chatflow():
    with CHATFLOW_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def test_conversation_chain_has_buddycall_system_prompt():
    chatflow = load_chatflow()
    nodes = chatflow.get("nodes", [])

    conversation_node = next(
        (node for node in nodes if node.get("id") == "conversationChain_0"),
        None,
    )

    assert conversation_node is not None, "conversationChain_0 node missing"

    prompt = conversation_node.get("data", {}).get("inputs", {}).get("systemMessagePrompt")
    assert prompt, "systemMessagePrompt is empty"
    assert "Du bist \"BuddyCall\"" in prompt
    assert "## STANDARD-AUSGABEFORMAT" in prompt
    assert "Wenn die Aufgabe unklar ist" in prompt


