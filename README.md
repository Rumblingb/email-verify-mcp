# Email Verify MCP Server

**Validate emails without sending a single message.** Reduce bounce rates, protect sender reputation, and clean your mailing lists — all from your MCP-compatible client (Claude Desktop, Cursor, VS Code + Continue, etc.).

## Features

| Tool | Description |
|------|-------------|
| `verify_email` | Full email validation: format check, MX record lookup, disposable email detection, typo suggestion, deliverability score |
| `verify_email_batch` | Batch verify multiple emails in a single call |
| `is_disposable_email` | Check if a domain is a known disposable/temporary email provider |

## How It Works

Zero external API dependencies. Everything runs locally using:
- **Python `re`** — RFC-compliant format validation
- **Python `socket`** — MX record and domain resolution
- **Hardcoded disposable domain list** — 200+ known disposable email providers
- **Typo detection engine** — Catches common typos (gmial.com → gmail.com, hotmal.com → hotmail.com, etc.)

## Response Format

```json
{
  "email": "test@example.com",
  "valid_format": true,
  "has_mx_record": true,
  "is_disposable": false,
  "typo_suggestion": null,
  "score": 0.95,
  "details": "Email has valid format, MX records found, not a disposable provider"
}
```

## Pricing & Rate Limits

| Plan | Price | Limit |
|------|-------|-------|
| **Free** | $0 | 50 verifications per server instance |
| **Pro** | **$19/month** | Unlimited verifications |

## Usage

### With Claude Desktop (Free Tier)

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "email-verify": {
      "command": "python",
      "args": ["path/to/email-verify-mcp/server.py"]
    }
  }
}
```

### With Claude Desktop (Pro Tier)

```json
{
  "mcpServers": {
    "email-verify": {
      "command": "python",
      "args": ["path/to/email-verify-mcp/server.py", "--pro-key", "PROL_AGENTPAY_DEMO"]
    }
  }
}
```

### With Smithery

[![Smithery](https://smithery.ai/badge/email-verify-mcp)](https://smithery.ai/server/email-verify-mcp)

On Smithery, configure the `proKey` environment variable to use Pro mode.

### From Command Line

```bash
pip install -r requirements.txt

# Free tier (50 calls)
python server.py

# Pro tier (unlimited)
python server.py --pro-key PROL_AGENTPAY_DEMO
```

## Get a Pro Key

[Subscribe Now — $19/month](https://buy.stripe.com/5kQ3cxflRabW9PW1AD1oI0r)

After purchase, you'll receive a Pro key (PROL_XXX) to unlock unlimited email verifications.

## Why Email Verification?

- **Reduce bounce rates** — Invalid emails damage your sender reputation
- **Save money** — Don't pay for emails that will never arrive
- **Improve deliverability** — ISPs reward clean lists with better inbox placement
- **Protect domain reputation** — High bounce rates can get you blacklisted

## Requirements

- Python 3.8+
- `mcp>=1.0.0`
- No external APIs, no API keys, no subscriptions needed for free tier

## License

MIT
