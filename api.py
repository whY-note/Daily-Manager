from todo_collector import TodoCollector

def collect_todos(dir: str = "./"):
    collector = TodoCollector()
    collector.set_dir(dir = dir)
    collector.collect_write()

