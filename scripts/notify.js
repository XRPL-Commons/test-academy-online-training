/**
 * Silent progress notification helper.
 * Called by exercise scripts after a successful transaction.
 * Posts to Google Chat webhook if GOOGLE_CHAT_WEBHOOK_URL is set.
 * Never throws — failures are silently ignored so exercises still work without the webhook.
 */

const fs = require("fs");
const path = require("path");

async function notifyProgress(stage) {
  const webhookUrl = process.env.GOOGLE_CHAT_WEBHOOK_URL || "";
  if (!webhookUrl.startsWith("https://chat.googleapis.com/")) return;

  const walletsFile = path.join(__dirname, "..", "wallets.json");
  let wallets;
  try {
    wallets = JSON.parse(fs.readFileSync(walletsFile, "utf8")).wallets;
  } catch {
    return;
  }

  const username = process.env.GITHUB_USER || process.env.CODESPACE_NAME || "unknown";
  const explorerBase = "https://testnet.xrpl.org/accounts/";

  const text = [
    "📣 *XRPL Academy Progress*",
    "",
    `👤 Participant: *${username}*`,
    `✅ Completed: *${stage}*`,
    "",
    `🔗 Wallet 1: ${explorerBase}${wallets[0].address}`,
    `🔗 Wallet 2: ${explorerBase}${wallets[1].address}`,
  ].join("\n");

  try {
    await fetch(webhookUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json; charset=UTF-8" },
      body: JSON.stringify({ text }),
    });
  } catch {
    // silent
  }
}

module.exports = { notifyProgress };
