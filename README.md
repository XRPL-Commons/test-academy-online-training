# XRPL Developer Training — June 22–23, 2026

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/XRPL-Commons/dev-training-june-2026?geo=EuropeWest)

This repository is the hands-on environment for the XRPL Commons developer training. Participants work from scaffolded exercises in their language of choice and verify their results live on the XRPL Testnet.

> ⏳ **Heads up:** Opening a Codespace for the first time can take several minutes. Click the button above as soon as you can and let it load in the background while the session intro is running.

---

## What is in this repo

```
.
├── .devcontainer/        Codespaces setup
├── scripts/              Wallet minting
├── exercises/
│   ├── js/               JavaScript exercises
│   ├── python/           Python exercises
│   └── java/             Java exercises
├── wallets.json          Auto-generated on Codespace start
└── README.md
```

Complete solutions live on the `solutions` branch.

---

## Getting started

Click the Codespaces button above and wait for the environment to finish starting. This can take **several minutes** on a cold start, it is normal.

> **Prebuild note:**
> - Dependencies are already installed, the environment loads faster than a standard Codespace
> - Wallet minting still runs only when your individual Codespace starts, so your wallets stay unique to you

The Codespace automatically:

- installs JavaScript, Python, and Java dependencies
- creates two funded XRPL Testnet wallets
- saves them to `wallets.json`

If wallet minting fails on startup, re-run it manually:

```bash
node scripts/mint-wallets.js
```

---

## Wallets

After startup, `wallets.json` contains two funded Testnet wallets:

- **Wallet 1:** sender, issuer, minter
- **Wallet 2:** receiver, holder

If your Codespace is stopped and restarted between exercises, it will re-mint wallets and overwrite `wallets.json`. To preserve continuity (trust lines, etc.), avoid restarting, or keep a copy of your previous `wallets.json` and restore it after restart.

> ⚠️ **Important:**
> - These are Testnet wallets only
> - Never reuse Testnet seeds on Mainnet
> - If you must re-mint, run `node scripts/mint-wallets.js`, but note this will reset your on-chain state (trust lines, AMM pools, etc.)

---

## Pick a language

Choose the language you are most comfortable with. All exercises cover the same content.

| Language | Folder | Run pattern |
|---|---|---|
| JavaScript | `exercises/js/` | `node exercises/js/file-name.js` |
| Python | `exercises/python/` | `python exercises/python/file_name.py` |
| Java | `exercises/java/` | `cd exercises/java && mvn compile exec:java -Dexec.mainClass="academy.xrpl.ClassName"` |

> Java dependencies are downloaded on the first `mvn compile`, which can take a few minutes. Run it once before the coding session starts.

> **Java users:** before running each exercise, reset your terminal to the repo root first:
> ```bash
> cd ~ && cd /workspaces/dev-training-june-2026
> ```

---

## Exercise commands

### Day 1: Send XRP

```bash
node exercises/js/day1-send-xrp.js
python exercises/python/day1_send_xrp.py
cd exercises/java && mvn compile exec:java -Dexec.mainClass="academy.xrpl.Day1SendXrp"
```

Success signal: `tesSUCCESS` and an Explorer link.

### Homework: NFT Lifecycle

```bash
node exercises/js/homework-nft.js
python exercises/python/homework_nft.py
cd exercises/java && mvn compile exec:java -Dexec.mainClass="academy.xrpl.HomeworkNft"
```

Success signal: NFT mint succeeds, appears on-chain, then is burned.

> Complete this between Day 1 and Day 2.

### Day 2 Step 1: Setup Account

```bash
node exercises/js/day2-step1-setup-account.js
python exercises/python/day2_step1_setup_account.py
cd exercises/java && mvn compile exec:java -Dexec.mainClass="academy.xrpl.Day2Step1SetupAccount"
```

Success signal: issuer account enables `Default Ripple`.

### Day 2 Step 2: Issue Token

```bash
node exercises/js/day2-step2-issue-token.js
python exercises/python/day2_step2_issue_token.py
cd exercises/java && mvn compile exec:java -Dexec.mainClass="academy.xrpl.Day2Step2IssueToken"
```

Success signal: holder trust line exists and receives the issued token.

### Day 2 Step 3: Create AMM

Prerequisite: complete Step 1 and Step 2 first.

```bash
node exercises/js/day2-step3-create-amm.js
python exercises/python/day2_step3_create_amm.py
cd exercises/java && mvn compile exec:java -Dexec.mainClass="academy.xrpl.Day2Step3CreateAmm"
```

Success signal: `AMMCreate` succeeds and the pool exists on Testnet.

---

## Workshop flow

### Day 1 — June 22, 2026

| Time (CEST) | Activity | Exercise |
|---|---|---|
| 15:00 – 15:30 | Welcome & intro | — |
| 15:30 – 16:30 | Blockchain 101 + quiz | — |
| 16:30 – 16:45 | Break | — |
| 16:45 – 17:30 | XRPL 101 + What's new + quiz | — |
| 17:30 – 18:00 | Coding session I | `day1-send-xrp` |
| 18:00 – 18:30 | Q&A + homework briefing | `homework-nft` |

### Day 2 — June 23, 2026

| Time (CEST) | Activity | Exercise |
|---|---|---|
| 15:00 – 15:30 | Greeting & homework review | — |
| 15:30 – 15:55 | Keynote: Spawning Liquidity on the XRP Ledger + quiz | — |
| 15:55 – 16:00 | Break | — |
| 16:00 – 17:30 | Coding session II — Step 1: setup account | `day2-step1-setup-account` |
| | Coding session II — Step 2: issue token | `day2-step2-issue-token` |
| | Coding session II — Step 3: create an AMM | `day2-step3-create-amm` |
| 17:30 – 17:45 | Break | — |
| 17:45 – 18:00 | Alumni testimonial | — |
| 18:00 – 18:30 | Q&A + closing remarks | — |

---

## Stuck? Get help

If you are blocked at any point:

- Post your question in the **training Google Chat space**, mentors are monitoring it throughout both days.
- Mentors can see your on-chain activity and will be able to tell which step you are on and help you debug.
- If needed, a mentor will invite you to a Zoom breakout room for 1-on-1 support.

---

## Troubleshooting

| Problem | What to do |
|---|---|
| Codespace takes a long time to start | This is normal, it can take several minutes on a cold start. Wait it out. |
| Wallet minting fails | Retry `node scripts/mint-wallets.js` after a short wait. |
| Java build is slow on first run | Run `mvn compile` once and wait for dependencies to download. |
| Java `cd` error between exercises | Reset your terminal to the repo root: `cd ~ && cd /workspaces/dev-training-june-2026` |
| WebSocket connection fails | Retry on a different network, corporate firewalls sometimes block WebSockets. |
| Day 2 Step 3 fails | Make sure you completed Step 1 and Step 2 first, using the same wallets. |

---

## Solutions

If you are truly stuck after asking for help, complete solutions are available on the `solutions` branch. Try the exercise first, solutions are a last resort.

```bash
git checkout solutions -- solutions/
```

This copies the solution files into your `solutions/` folder without overwriting your work in `exercises/`.

---

## Network reference

| Item | Value |
|---|---|
| Network | XRPL Testnet |
| WebSocket | `wss://s.altnet.rippletest.net:51233` |
| JSON-RPC | `https://s.altnet.rippletest.net:51234` |
| Explorer | `https://testnet.xrpl.org` |
| Faucet | `https://faucet.altnet.rippletest.net/accounts` |

---

## Reference materials

### Start here

- [XRPL Commons Learning Portal](https://learn.xrpl-commons.org/), guided courses and workshop-friendly explanations
- [Intro to the XRPL](https://learn.xrpl-commons.org/course/intro-to-the-xrpl/), broad protocol overview
- [XRPL Docs](https://xrpl.org/docs), official transaction, API, and network references
- [XRPLF GitHub Organization](https://github.com/XRPLF), SDKs, examples, and core project source
- [XRPL Testnet Explorer](https://testnet.xrpl.org), confirm your results on-chain after each exercise

### Exercise-by-exercise links

| Exercise | Learning Portal | XRPL Docs | SDKs |
|---|---|---|---|
| `day1-send-xrp` | [Create Accounts and Send XRP](https://learn.xrpl-commons.org/course/blockchain-foundations-for-web2-developers/lesson/create-accounts-and-send-xrp/) | [Payment transaction](https://xrpl.org/docs/references/protocol/transactions/types/payment) | [xrpl.js](https://js.xrpl.org), [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/) |
| `homework-nft` | [Mint and Burn NFTs](https://learn.xrpl-commons.org/course/code-with-the-xrpl/lesson/mint-and-burn-nfts/) | [NFTokenMint](https://xrpl.org/docs/references/protocol/transactions/types/nftokenmint), [NFTokenBurn](https://xrpl.org/docs/references/protocol/transactions/types/nftokenburn) | [xrpl.js](https://js.xrpl.org), [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/) |
| `day2-step1-setup-account` | [Code with XRPL](https://learn.xrpl-commons.org/course/code-with-the-xrpl/) | [AccountSet transaction](https://xrpl.org/docs/references/protocol/transactions/types/accountset) | [xrpl.js](https://js.xrpl.org), [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/), [xrpl4j](https://github.com/XRPLF/xrpl4j) |
| `day2-step2-issue-token` | [Create Trust Line and Send Currency](https://learn.xrpl-commons.org/course/code-with-the-xrpl/lesson/create-trustline-and-send-currency/) | [TrustSet](https://xrpl.org/docs/references/protocol/transactions/types/trustset), [Payment](https://xrpl.org/docs/references/protocol/transactions/types/payment) | [xrpl.js](https://js.xrpl.org), [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/), [xrpl4j](https://github.com/XRPLF/xrpl4j) |
| `day2-step3-create-amm` | [What is an AMM?](https://learn.xrpl-commons.org/course/deep-dive-into-xrpl-defi/lesson/what-is-an-automated-market-maker-amm/) | [AMMCreate](https://xrpl.org/docs/references/protocol/transactions/types/ammcreate), [amm_info](https://xrpl.org/docs/references/http-websocket-apis/public-api-methods/path-and-order-book-methods/amm_info) | [xrpl.js](https://js.xrpl.org), [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/), [xrpl4j](https://github.com/XRPLF/xrpl4j) |

### SDKs

- [xrpl.js docs](https://js.xrpl.org) and [xrpl.js repo](https://github.com/XRPLF/xrpl.js)
- [xrpl-py docs](https://xrpl-py.readthedocs.io/en/stable/) and [xrpl-py repo](https://github.com/XRPLF/xrpl-py)
- [xrpl4j repo](https://github.com/XRPLF/xrpl4j), Java library and examples
- [xrpl-connect](https://github.com/XRPL-Commons/xrpl-connect), XRPL Commons' wallet connection toolkit
- [XRPLF GitHub](https://github.com/XRPLF), SDKs, examples, and core project source

---

## Further reading

- [XRPL Commons Learning Portal](https://learn.xrpl-commons.org/)
- [XRPL Docs](https://xrpl.org/docs)
- [xrpl.js](https://js.xrpl.org)
- [xrpl-py](https://xrpl-py.readthedocs.io/en/stable/)
- [xrpl4j](https://github.com/XRPLF/xrpl4j)
- [XRPLF GitHub Organization](https://github.com/XRPLF)
- [XRPL Dev Portal Repo](https://github.com/XRPLF/xrpl-dev-portal)
- [XRPL Testnet Explorer](https://testnet.xrpl.org)
