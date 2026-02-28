# Daily Manager

Currently, Daily Manager is a program for manage your daily todos in **obsidian**.

## Main function
The main function of Daily Manager is to collect the unfinished todos in your past daily notes and then write them into today's daily note.

For example, if your daily note on Jan 23, 2026 and Jan 24, 2026 are like the following these:

```markdown
<!-- 2026-01-23.md -->
# TODO

- [x] 完成最优化大作业
- [ ] 完成绘图
- [ ] 
```

```markdown
<!-- 2026-01-24.md -->
# TODO

- [x] 写一个收集未完成的TODO的类
- [ ] 完成机械臂代码调试
- [ ] 写一篇博客
```

After running this program, you will get your daily note on Jan 25, 2026 like the following one:

```markdown
<!-- 2026-01-25.md -->
# TODO 

- [ ] 完成绘图
- [ ] 完成机械臂代码调试
- [ ] 写一篇博客
```

This is a very easy program, but it is very helpful for us to manage our daily routine.

## How to use?
```bash
python collect_todos.py --dir the directory of your daily schedule
```