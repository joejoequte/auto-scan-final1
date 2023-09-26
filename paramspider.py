import os

# 从 GitHub Actions 输入获取域名列表
domain_input = "${{ github.event.inputs.domain }}"

# 将域名字符串拆分为列表，假设域名之间使用逗号分隔
hosts = domain_input.split(',')

for host in hosts:
    os.system("python3 paramspider.py --domain " + host.strip() + " --output output/output.txt")
