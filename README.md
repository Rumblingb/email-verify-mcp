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

## Usage

### With Claude Desktop

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

### With Smithery

[![Smithery](https://smithery.ai/badge/email-verify-mcp)](https://smithery.ai/server/email-verify-mcp)

### From Command Line

```bash
pip install -r requirements.txt
python server.py
```

## Pricing

| Plan | Price | Includes |
|------|-------|----------|
| **Starter** | **$19/month** | 5,000 verifications/month, email support |
| Professional | $49/month | 25,000 verifications/month, priority support |
| Enterprise | Custom | Unlimited verifications, SLA, dedicated support |

[Subscribe Now — $19/month](https://buy.stripe.com/dRm6oJ4Hd2Jugek0wz1oI0m)

## Why Email Verification?

- **Reduce bounce rates** — Invalid emails damage your sender reputation
- **Save money** — Don't pay for emails that will never arrive
- **Improve deliverability** — ISPs reward clean lists with better inbox placement
- **Protect domain reputation** — High bounce rates can get you blacklisted

This is a proven business model generating **$400+/month** (see: IPWhois.io, VAT-Sense, TinyScreenshot).

## Requirements

- Python 3.8+
- `mcp>=1.0.0`
- No external APIs, no API keys, no subscriptions

## License

MIT
