#!/usr/bin/env python3

## How to get and use?
# git clone "https://github.com/hezhijie0327/AdFilter.git" && python3 ./AdFilter/build.py

# Current Version: 1.2.2

import base64
import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
DIST_DIR = ROOT / "dist"

FILTER_ADBLOCK = (
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://filters.adtidy.org/extension/chromium/filters/1.txt",
    "https://filters.adtidy.org/extension/chromium/filters/101.txt",
    "https://filters.adtidy.org/extension/chromium/filters/102.txt",
    "https://filters.adtidy.org/extension/chromium/filters/103.txt",
    "https://filters.adtidy.org/extension/chromium/filters/104.txt",
    "https://filters.adtidy.org/extension/chromium/filters/105.txt",
    "https://filters.adtidy.org/extension/chromium/filters/106.txt",
    "https://filters.adtidy.org/extension/chromium/filters/107.txt",
    "https://filters.adtidy.org/extension/chromium/filters/108.txt",
    "https://filters.adtidy.org/extension/chromium/filters/109.txt",
    "https://filters.adtidy.org/extension/chromium/filters/11.txt",
    "https://filters.adtidy.org/extension/chromium/filters/110.txt",
    "https://filters.adtidy.org/extension/chromium/filters/111.txt",
    "https://filters.adtidy.org/extension/chromium/filters/112.txt",
    "https://filters.adtidy.org/extension/chromium/filters/113.txt",
    "https://filters.adtidy.org/extension/chromium/filters/114.txt",
    "https://filters.adtidy.org/extension/chromium/filters/115.txt",
    "https://filters.adtidy.org/extension/chromium/filters/116.txt",
    "https://filters.adtidy.org/extension/chromium/filters/117.txt",
    "https://filters.adtidy.org/extension/chromium/filters/118.txt",
    "https://filters.adtidy.org/extension/chromium/filters/119.txt",
    "https://filters.adtidy.org/extension/chromium/filters/12.txt",
    "https://filters.adtidy.org/extension/chromium/filters/120.txt",
    "https://filters.adtidy.org/extension/chromium/filters/121.txt",
    "https://filters.adtidy.org/extension/chromium/filters/122.txt",
    "https://filters.adtidy.org/extension/chromium/filters/123.txt",
    "https://filters.adtidy.org/extension/chromium/filters/13.txt",
    "https://filters.adtidy.org/extension/chromium/filters/14.txt",
    "https://filters.adtidy.org/extension/chromium/filters/15.txt",
    "https://filters.adtidy.org/extension/chromium/filters/16.txt",
    "https://filters.adtidy.org/extension/chromium/filters/17.txt",
    "https://filters.adtidy.org/extension/chromium/filters/2.txt",
    "https://filters.adtidy.org/extension/chromium/filters/200.txt",
    "https://filters.adtidy.org/extension/chromium/filters/201.txt",
    "https://filters.adtidy.org/extension/chromium/filters/203.txt",
    "https://filters.adtidy.org/extension/chromium/filters/204.txt",
    "https://filters.adtidy.org/extension/chromium/filters/205.txt",
    "https://filters.adtidy.org/extension/chromium/filters/206.txt",
    "https://filters.adtidy.org/extension/chromium/filters/207.txt",
    "https://filters.adtidy.org/extension/chromium/filters/208.txt",
    "https://filters.adtidy.org/extension/chromium/filters/209.txt",
    "https://filters.adtidy.org/extension/chromium/filters/210.txt",
    "https://filters.adtidy.org/extension/chromium/filters/211.txt",
    "https://filters.adtidy.org/extension/chromium/filters/212.txt",
    "https://filters.adtidy.org/extension/chromium/filters/213.txt",
    "https://filters.adtidy.org/extension/chromium/filters/214.txt",
    "https://filters.adtidy.org/extension/chromium/filters/215.txt",
    "https://filters.adtidy.org/extension/chromium/filters/216.txt",
    "https://filters.adtidy.org/extension/chromium/filters/217.txt",
    "https://filters.adtidy.org/extension/chromium/filters/218.txt",
    "https://filters.adtidy.org/extension/chromium/filters/219.txt",
    "https://filters.adtidy.org/extension/chromium/filters/220.txt",
    "https://filters.adtidy.org/extension/chromium/filters/221.txt",
    "https://filters.adtidy.org/extension/chromium/filters/222.txt",
    "https://filters.adtidy.org/extension/chromium/filters/223.txt",
    "https://filters.adtidy.org/extension/chromium/filters/224.txt",
    "https://filters.adtidy.org/extension/chromium/filters/225.txt",
    "https://filters.adtidy.org/extension/chromium/filters/226.txt",
    "https://filters.adtidy.org/extension/chromium/filters/227.txt",
    "https://filters.adtidy.org/extension/chromium/filters/228.txt",
    "https://filters.adtidy.org/extension/chromium/filters/229.txt",
    "https://filters.adtidy.org/extension/chromium/filters/230.txt",
    "https://filters.adtidy.org/extension/chromium/filters/231.txt",
    "https://filters.adtidy.org/extension/chromium/filters/232.txt",
    "https://filters.adtidy.org/extension/chromium/filters/233.txt",
    "https://filters.adtidy.org/extension/chromium/filters/234.txt",
    "https://filters.adtidy.org/extension/chromium/filters/235.txt",
    "https://filters.adtidy.org/extension/chromium/filters/236.txt",
    "https://filters.adtidy.org/extension/chromium/filters/237.txt",
    "https://filters.adtidy.org/extension/chromium/filters/238.txt",
    "https://filters.adtidy.org/extension/chromium/filters/239.txt",
    "https://filters.adtidy.org/extension/chromium/filters/240.txt",
    "https://filters.adtidy.org/extension/chromium/filters/241.txt",
    "https://filters.adtidy.org/extension/chromium/filters/242.txt",
    "https://filters.adtidy.org/extension/chromium/filters/243.txt",
    "https://filters.adtidy.org/extension/chromium/filters/244.txt",
    "https://filters.adtidy.org/extension/chromium/filters/245.txt",
    "https://filters.adtidy.org/extension/chromium/filters/246.txt",
    "https://filters.adtidy.org/extension/chromium/filters/247.txt",
    "https://filters.adtidy.org/extension/chromium/filters/249.txt",
    "https://filters.adtidy.org/extension/chromium/filters/3.txt",
    "https://filters.adtidy.org/extension/chromium/filters/4.txt",
    "https://filters.adtidy.org/extension/chromium/filters/5.txt",
    "https://filters.adtidy.org/extension/chromium/filters/6.txt",
    "https://filters.adtidy.org/extension/chromium/filters/7.txt",
    "https://filters.adtidy.org/extension/chromium/filters/8.txt",
    "https://filters.adtidy.org/extension/chromium/filters/9.txt",
    "https://gitee.com/xinggsf/Adblock-Rule/raw/master/mv.txt",
    "https://gitee.com/xinggsf/Adblock-Rule/raw/master/rule.txt",
    "https://raw.githubusercontent.com/AdguardTeam/cname-trackers/master/combined_disguised_trackers.txt",
    "https://raw.githubusercontent.com/VeleSila/VELE-SILA-List/gh-pages/KaFanList.txt",
    "https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt",
    "https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt",
    "https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjxlist.txt",
    "https://raw.githubusercontent.com/nextdns/cname-cloaking-blocklist/master/domains",
    "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad-edentw.txt",
    "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad-mo.txt",
    "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad-pc.txt",
    "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad.txt",
    "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad2.txt",
    "https://raw.githubusercontent.com/o0HalfLife0o/list/master/ad3.txt",
    "https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/ABP-FX.txt",
    "https://sub.adtchrome.com/adt-chinalist-easylist.txt",
    "https://www.fanboy.co.nz/enhancedstats.txt",
    "https://www.fanboy.co.nz/fanboy-annoyance.txt",
)
FILTER_DOMAIN = (
    "https://gitee.com/damengzhudamengzhu/guanggaoguolv/raw/master/jiekouAD.txt",
    "https://gitlab.com/ZeroDot1/CoinBlockerLists/-/raw/master/list_browser.txt",
    "https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/reject-list.txt",
    "https://raw.githubusercontent.com/examplecode/ad-rules-for-xbrowser/master/core-rule-cn.txt",
    "https://raw.githubusercontent.com/hezhijie0327/AdFilter/main/custom/block.txt",
    "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-domains.txt",
)
FILTER_HOSTS = (
    "https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts",
    "https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt",
    "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt",
    "https://raw.githubusercontent.com/ilpl/ad-hosts/master/hosts",
    "https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts",
    "https://raw.githubusercontent.com/neoFelhz/neohosts/gh-pages/full/hosts",
)
FILTER_OTHER = (
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list",
    "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list",
    "https://raw.githubusercontent.com/eHpo1/Rules/master/Surge4/Ruleset/Liby.list",
    "https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Reject.list",
)
FILTER_WHITE = (
    "https://easylist-downloads.adblockplus.org/exceptionrules.txt",
    "https://filters.adtidy.org/extension/chromium/filters/10.txt",
    "https://gitlab.com/ZeroDot1/CoinBlockerLists/-/raw/master/white_list.txt",
    "https://raw.githubusercontent.com/AdguardTeam/AdGuardSDNSFilter/master/Filters/exceptions.txt",
    "https://raw.githubusercontent.com/AdguardTeam/AdGuardSDNSFilter/master/Filters/exclusions.txt",
    "https://raw.githubusercontent.com/EnergizedProtection/unblock/master/basic/formats/domains.txt",
    "https://raw.githubusercontent.com/Ultimate-Hosts-Blacklist/whitelist/master/domains.list",
    "https://raw.githubusercontent.com/VeleSila/yhosts/master/whitelist.txt",
    "https://raw.githubusercontent.com/WildcardTech/Filter-Domain-List/master/whitelist.txt",
    "https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/optional-list.txt",
    "https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/whitelist.txt",
    "https://raw.githubusercontent.com/hezhijie0327/AdFilter/main/custom/allow.txt",
    "https://raw.githubusercontent.com/mkb2091/blockconvert/master/output/whitelist_domains.txt",
    "https://raw.githubusercontent.com/notracking/hosts-blocklists-scripts/master/hostnames.whitelist.txt",
    "https://raw.githubusercontent.com/privacy-protection-tools/dead-horse/master/anti-ad-white-list.txt",
)

DOMAIN_REGEX = re.compile(
    r"^(([a-z])|([a-z]{2})|([a-z][0-9])|([0-9][a-z])|([a-z0-9][-\.a-z0-9]{1,61}[a-z0-9]))"
    r"\.([a-z]{2,13}|[a-z0-9-]{2,30}\.[a-z]{2,3})$"
)

TITLE = "Zhijie's Ad Filter"
DESCRIPTION = (
    "Filter composed of several other filters can block ads from websites (especially Chinese websites); "
    "it can also improve privacy and security. Hey buddy, enjoy your fantastic web surfing experience~"
)
EXPIRES = "3 hours (update frequency)"
HOMEPAGE = "https://github.com/hezhijie0327/AdFilter"
VERSION_URL = "https://raw.githubusercontent.com/hezhijie0327/AdFilter/main/build.py"

HOSTS_LOCAL_BLOCK = (
    "# (DO NOT REMOVE)",
    "127.0.0.1 localhost",
    "255.255.255.255 broadcasthost",
    "::1 ip6-localhost ip6-loopback localhost",
    "fe00::0 ip6-localnet",
    "ff00::0 ip6-mcastprefix",
    "ff02::1 ip6-allnodes",
    "ff02::2 ip6-allrouters",
    "ff02::3 ip6-allhosts",
    "# (DO NOT REMOVE)",
)

# Output formats: (file name, comment prefix, title suffix, rule template)
FORMATS = (
    ("adblock.txt", "!", "Adblock (WEB-level)", "||{domain}^"),
    ("adguardhome.txt", "!", "AdGuard Home (DNS-level)", "|{domain}^"),
    ("clash.yaml", "#", "Clash (DNS-level)", "  - DOMAIN,{domain}"),
    ("dnsmasq.conf", "#", "Dnsmasq (DNS-level)", "address=/{domain}/"),
    ("domains.txt", "#", "Pi-hole (DNS-level)", "{domain}"),
    ("hosts.txt", "#", "AdAway (DNS-level)", "0.0.0.0 {domain}"),
    ("quantumult.yaml", "#", "Quantumult (DNS-level)", "DOMAIN,{domain},REJECT"),
    ("smartdns.conf", "#", "SmartDNS (DNS-level)", "address /{domain}/#"),
    ("surge.yaml", "#", "Surge (DNS-level)", "DOMAIN,{domain}"),
    ("unbound.conf", "#", "Unbound (DNS-level)", 'local-zone: "{domain}" always_nxdomain'),
)


## Function
# Download one URL, return decoded text (empty string on failure, like curl -s)
def download(url):
    try:
        request = Request(url, headers={"User-Agent": "curl/8"})
        with urlopen(request, timeout=15) as response:
            return response.read().decode("utf-8", errors="replace")
    except OSError:
        return ""


# Fetch all URLs in parallel and concatenate (raw append, like curl >> file)
def fetch(urls):
    with ThreadPoolExecutor(max_workers=32) as pool:
        return "".join(pool.map(download, urls))


# Get Data
def get_data():
    groups = (FILTER_ADBLOCK, FILTER_DOMAIN, FILTER_HOSTS, FILTER_OTHER, FILTER_WHITE)
    with ThreadPoolExecutor(max_workers=5) as pool:
        adblock, domain, hosts, other, white = pool.map(fetch, groups)
    return adblock, domain, hosts, other, white


# Strip hosts-file prefixes and rule syntax, keep valid domains.
# Substitutions run sequentially like the original sed chain: removing
# whitespace first can join "::" with a following "1..." into "::1...".
# ([^\S\n] = whitespace except newline: sed works line by line)
def clean(text, extra_patterns=(), drop_chars="^|"):
    for pattern in (r"[^\S\n]", r"0\.0\.0\.0", r"127\.0\.0\.1", r"::1", r"::") + extra_patterns:
        text = re.sub(pattern, "", text)
    text = text.translate(str.maketrans("", "", drop_chars)).lower()
    return sorted({line for line in text.split("\n") if DOMAIN_REGEX.fullmatch(line)})


# Analyse Data
def analyse_data(adblock, domain, hosts, other, white):
    filter_allow = set(clean(white, drop_chars="@^|"))
    filter_block = set(clean(
        adblock + domain + hosts + other,
        extra_patterns=(r"DOMAIN,", r"DOMAIN-SUFFIX,", r"domain:", r"full:"),
    ))
    return sorted(domain for domain in filter_block - filter_allow if ".." not in domain)


# Generate Information
def generate_information(total):
    now = time.time()
    checksum = base64.b64encode(f"{int(now)}\n".encode()).decode()
    updated = datetime.fromtimestamp(int(now), tz=timezone.utc)
    base_version = ""
    match = re.search(r"# Current Version: (.+)", download(VERSION_URL))
    if match:
        base_version = match.group(1).strip()
    return {
        "checksum": checksum,
        "version": f"{base_version}-{updated.strftime('%Y%m%d')}-{int(updated.strftime('%H')) // 3}",
        "timeupdated": updated.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "total": total,
    }


# Output Data
def output_data(filter_data, info):
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    for file_name, comment, suffix, template in FORMATS:
        lines = [
            f"{comment} Checksum: {info['checksum']}",
            f"{comment} Title: {TITLE} for {suffix}",
            f"{comment} Description: {DESCRIPTION}",
            f"{comment} Version: {info['version']}",
            f"{comment} TimeUpdated: {info['timeupdated']}",
            f"{comment} Expires: {EXPIRES}",
            f"{comment} Homepage: {HOMEPAGE}",
            f"{comment} Total: {info['total']}",
        ]
        if file_name == "hosts.txt":
            lines += HOSTS_LOCAL_BLOCK
        if file_name == "clash.yaml":
            lines.insert(0, "payload:")
        if file_name == "hosts.txt":
            # IPv4 and IPv6 lines interleave per domain in the original loop
            for domain in filter_data:
                lines.append(f"0.0.0.0 {domain}")
                lines.append(f":: {domain}")
        else:
            lines += [template.format(domain=domain) for domain in filter_data]
        (DIST_DIR / file_name).write_text("\n".join(lines) + "\n")


## Process
def main():
    filter_data = analyse_data(*get_data())
    # Skip regeneration when the domain list is unchanged
    domains_file = DIST_DIR / "domains.txt"
    if domains_file.exists():
        old = domains_file.read_text().split("\n")[8:-1]
        if old == filter_data:
            return
    output_data(filter_data, generate_information(len(filter_data)))


if __name__ == "__main__":
    main()
