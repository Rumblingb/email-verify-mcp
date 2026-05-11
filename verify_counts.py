with open('/mnt/d/Projects/pickaxes/email-verify-mcp/server.py') as f:
    source = f.read()

in_set = False
count = 0
for line in source.split('\n'):
    stripped = line.strip()
    if 'DISPOSABLE_DOMAINS = frozenset({' in stripped:
        in_set = True
        continue
    if in_set:
        if stripped == '})':
            break
        if stripped.endswith('",') or stripped.endswith('",  #'):
            count += 1

print(f'Disposable domains: {count}')

in_map = False
typo_count = 0
for line in source.split('\n'):
    stripped = line.strip()
    if 'TYPO_MAP = {' in stripped:
        in_map = True
        continue
    if in_map:
        if stripped == '}':
            break
        if ':"' in stripped:
            typo_count += 1

print(f'Typo entries: {typo_count}')
print(f'Cost: ${19}/mo in README: {"$19/month" in open("/mnt/d/Projects/pickaxes/email-verify-mcp/README.md").read()}')
print(f'Stripe link: {"buy.stripe.com/dRm6oJ4Hd2Jugek0wz1oI0m" in open("/mnt/d/Projects/pickaxes/email-verify-mcp/README.md").read()}')
