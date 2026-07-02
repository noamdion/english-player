import json, re
from pathlib import Path

base = Path("/mnt/c/01_English/01_Hermes生成英语计划/The_article_I_am_learning/13_Chapter13/13_Chapter13_02_rule1_joan_sales")
srt_path = base / "13_Chapter13_02_rule1_joan_sales.srt"
out_path = base / "13_Chapter13_02_rule1_joan_sales_template.json"

text = srt_path.read_text(encoding="utf-8")
blocks = re.split(r'\n\s*\n', text.strip())
ts_re = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}')

items = {}
for idx, block in enumerate(blocks):
    sub_text = ""
    for line in block.splitlines():
        if '-->' in line:
            after = line.split('-->', 1)[1]
            sub_text = ts_re.sub("", after).strip()
            break
    items[str(idx)] = {
        "original": sub_text,
        "b1": "",
        "cn": "",
        "ai_notes": "",
        "remarks": "",
        "play_count": 0
    }

out_path.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Template written: {out_path}")
print(f"Items: {len(items)}")
