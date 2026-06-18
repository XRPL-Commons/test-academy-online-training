"""
Silent progress notification helper.
Called by exercise scripts after a successful transaction.
Posts to Google Chat webhook if GOOGLE_CHAT_WEBHOOK_URL is set.
Never raises — failures are silently ignored.
"""

import json
import os
import urllib.request


def notify_progress(stage):
    webhook_url = os.environ.get("GOOGLE_CHAT_WEBHOOK_URL", "")
    if not webhook_url.startswith("https://chat.googleapis.com/"):
        return

    try:
        with open(os.path.join(os.path.dirname(__file__), "..", "wallets.json")) as f:
            wallets = json.load(f)["wallets"]
    except Exception:
        return

    username = os.environ.get("GITHUB_USER") or os.environ.get("CODESPACE_NAME") or "unknown"
    explorer = "https://testnet.xrpl.org/accounts/"

    text = "\n".join([
        "📣 *XRPL Academy Progress*",
        "",
        f"👤 Participant: *{username}*",
        f"✅ Completed: *{stage}*",
        "",
        f"🔗 Wallet 1: {explorer}{wallets[0]['address']}",
        f"🔗 Wallet 2: {explorer}{wallets[1]['address']}",
    ])

    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps({"text": text}).encode(),
            headers={"Content-Type": "application/json; charset=UTF-8"},
        )
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass
