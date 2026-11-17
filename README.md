# AdFilter

[![License](https://img.shields.io/badge/License-Apache%202.0--Commons%20Clause-blue)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)

AdFilter 聚合 EasyList、AdGuard、anti-AD、yhosts 等多个广告过滤列表，生成适用于 10 种客户端/格式的广告屏蔽规则；Python 3.9+ 标准库实现，GitHub Actions 每日更新。开发规范见 [AGENTS.md](AGENTS.md)。

## 特性

- **多源聚合**：整合 EasyList、AdGuard、anti-AD、yhosts 等数十个上游列表
- **白名单扣除**：自动从黑名单中剔除白名单域名，减少误伤
- **多格式输出**：Adblock、AdGuard Home、Clash、Dnsmasq、Pi-hole、AdAway、Quantumult、SmartDNS、Surge、Unbound
- **增量构建**：域名列表无变化时跳过重新生成
- **自动更新**：GitHub Actions 每日构建并提交

## 快速开始

### 直接下载

| 文件 | 适用客户端 | 层级 |
| ---- | ---------- | ---- |
| [adblock.txt](dist/adblock.txt) | Adblock / uBlock Origin | WEB 级 |
| [adguardhome.txt](dist/adguardhome.txt) | AdGuard Home | DNS 级 |
| [clash.yaml](dist/clash.yaml) | Clash | DNS 级 |
| [dnsmasq.conf](dist/dnsmasq.conf) | Dnsmasq | DNS 级 |
| [domains.txt](dist/domains.txt) | Pi-hole | DNS 级 |
| [hosts.txt](dist/hosts.txt) | AdAway / hosts | DNS 级 |
| [quantumult.yaml](dist/quantumult.yaml) | Quantumult | DNS 级 |
| [smartdns.conf](dist/smartdns.conf) | SmartDNS | DNS 级 |
| [surge.yaml](dist/surge.yaml) | Surge | DNS 级 |
| [unbound.conf](dist/unbound.conf) | Unbound | DNS 级 |

每个文件头部包含 Checksum、Title、Description、Version、TimeUpdated、Expires、Homepage、Total 元数据。

### 本地构建

```bash
git clone https://github.com/hezhijie0327/AdFilter.git
cd AdFilter
python3 build.py
```

依赖：Python 3.9+（仅标准库）、网络访问。

## 用法

### 自定义规则

- `custom/block.txt`：自定义黑名单域名（每行一个，`#` 开头为注释）
- `custom/allow.txt`：自定义白名单域名（从结果中剔除）

两个文件经 main 分支 URL 自引用拉取，修改后推送即生效。

## 文档

- [AGENTS.md](AGENTS.md) — 开发规范与实现细节（英文）

## License

[Apache License 2.0 with Commons Clause v1.0](LICENSE)
