# AdFilter

[![License](https://img.shields.io/badge/License-Apache%202.0--Commons%20Clause-blue)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

聚合多个广告过滤列表，生成适用于 10 种客户端/格式的广告屏蔽规则（Python 3.9+，仅标准库）。开发规范见 [AGENTS.md](AGENTS.md)。

## 特性

- **多源聚合**：整合 EasyList、AdGuard、anti-AD、yhosts 等数十个上游列表
- **白名单扣除**：自动从黑名单中剔除白名单域名，减少误伤
- **多格式输出**：Adblock、AdGuard Home、Clash、Dnsmasq、Pi-hole、AdAway、Quantumult、SmartDNS、Surge、Unbound
- **增量构建**：域名列表无变化时跳过重新生成
- **自动更新**：GitHub Actions 每日构建并提交

## 快速开始

### 方式一：直接使用生成的文件

```bash
# AdGuard Home（DNS 级）
curl -O https://raw.githubusercontent.com/hezhijie0327/AdFilter/main/dist/adguardhome.txt

# Clash 规则集
curl -O https://raw.githubusercontent.com/hezhijie0327/AdFilter/main/dist/clash.yaml

# hosts（AdAway）
curl -O https://raw.githubusercontent.com/hezhijie0327/AdFilter/main/dist/hosts.txt
```

### 方式二：本地构建

```bash
git clone https://github.com/hezhijie0327/AdFilter.git
cd AdFilter
python3 build.py
```

依赖：Python 3.9+（仅标准库）、网络访问。

## 文件说明（`dist/`）

| 文件 | 适用客户端 | 层级 |
| ---- | ---------- | ---- |
| `dist/adblock.txt` | Adblock / uBlock Origin | WEB 级 |
| `dist/adguardhome.txt` | AdGuard Home | DNS 级 |
| `dist/clash.yaml` | Clash | DNS 级 |
| `dist/dnsmasq.conf` | Dnsmasq | DNS 级 |
| `dist/domains.txt` | Pi-hole | DNS 级 |
| `dist/hosts.txt` | AdAway / hosts | DNS 级 |
| `dist/quantumult.yaml` | Quantumult | DNS 级 |
| `dist/smartdns.conf` | SmartDNS | DNS 级 |
| `dist/surge.yaml` | Surge | DNS 级 |
| `dist/unbound.conf` | Unbound | DNS 级 |

每个文件头部包含 Checksum、Title、Description、Version、TimeUpdated、Expires、Homepage、Total 元数据。

## 自定义规则

- `data/data_block.txt`：自定义黑名单域名（每行一个，`#` 开头为注释）
- `data/data_allow.txt`：自定义白名单域名（从结果中剔除）

两个文件经 main 分支 URL 自引用拉取，修改后推送即生效。

## 文档

- [AGENTS.md](AGENTS.md) — 开发规范与实现细节（英文）

## License

[Apache License 2.0 with Commons Clause v1.0](LICENSE)
