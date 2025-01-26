import json

# 读取 Singbox 规则集
with open('singbox_rules.json', 'r') as f:
    singbox_rules = json.load(f)

loon_rules = []

# 转换规则
for rule in singbox_rules['rules']:
    if rule['type'] == 'domain':
        loon_rules.append(f"DOMAIN,{rule['value']},{rule['action'].upper()}")
    elif rule['type'] == 'ip':
        loon_rules.append(f"IP-CIDR,{rule['value']}/32,{rule['action'].upper()}")

# 写入 Loon 规则集
with open('loon_rules.conf', 'w') as f:
    f.write("[Rule]\n")
    for rule in loon_rules:
        f.write(rule + "\n")

print("转换完成！")
