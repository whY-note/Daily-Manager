import os
import re
from datetime import date, timedelta
from pathlib import Path

class TodoCollector:
    def __init__(self):
        self._unfinished_list = []
        self._start_date = None
        self._end_date = (date.today() - timedelta(days=1)).isoformat() # 默认将终止时间设定为昨天
        self._dir = "./" # 默认是在当前目录
        self._date_today = date.today().isoformat()

    def set_dir(self, dir):
        self._dir = dir

    def set_start_date(self, start_date):
        self._start_date = start_date
        
    def set_end_date(self, end_date):
        self._end_date = end_date
    
    def collect_write(self):
        md_list = self._find_md()

        os.makedirs(self._dir, exist_ok = True)
        self._today_md_path = os.path.join(self._dir, f"{self._date_today}.md")
        
        # 检查文件是否存在
        if not os.path.exists(self._today_md_path):
            # 情况1：文件不存在，则创建并写入TODO
            with open(self._today_md_path, "w", encoding="utf-8") as f:
                f.write(f"# TODO \n\n")
        else:
            # 情况2：文件已存在，则检查是否包含TODO
            with open(self._today_md_path, "r+", encoding="utf-8") as f:
                content = f.read()
                if "# TODO" not in content:
                    # 如果没有 'TODO'，则移到文件末尾，并追加 'TODO'
                    if content and not content.endswith('\n'):
                        f.write("\n")
                    f.write(f"# TODO \n\n")

        for md_path in md_list:

            # 如果文件不存在，就跳过
            if not md_path.exists():
                continue

            # 如果文件存在，则寻找其中未完成的Todo,然后写到今天的日程中
            todo_list = self._find_unfinished(md_path)
            self._write_todo(todo_list)

        
    def _find_md(self):
        # 找出指定目录下的所有Markdown文件
        return list(Path(self._dir).glob("*.md"))

    def _find_unfinished(self, md_path):
        '''收集md_path相应的文件里 未完成的todo'''
        pattern = re.compile(r'^-\s+\[\s*\]\s+(.*)')
        empty_pattern = re.compile(r"^\s*- \[ \]\s*$") # 只含有符号 '- [ ] '，但是后面没有内容

        todo_list = []
        with open(md_path, 'r', encoding='utf-8') as f:
            for lineno, line in enumerate(f, start=1):
                match = pattern.match(line)
                empty_match = empty_pattern.match(line)
                # print("match: ", match)
                # print("empty_match: ", empty_match)

                if match and not empty_match:
                    # 只含有符号'- [ ] '，但是后面没有内容 的行就不加到todo_list里面
                    todo_list.append({
                        "text": match.group(1).strip()
                    })
        return todo_list

    def _write_todo(self, todo_list):
        '''将未完成的todo_list写入今天的日程'''
        with open(self._today_md_path, "a", encoding="utf-8") as f:
            for todo in todo_list:
                f.write(f"- [ ] {todo['text']}\n")

    
if __name__ == "__main__":
    collector = TodoCollector()
    collector.set_dir("./")
    collector.collect_write()