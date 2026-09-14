# 第 1 周学习计划：Python、Git 与日志分析器

> 日期：2026-09-14 ～ 2026-09-20  
> 计划投入：20 小时  
> 对应总路线：[plan.md](../plan.md) 第 1 周  
> 本周项目：`projects/log-analyzer`

---

## 1. 本周唯一目标

本周结束时，独立交付一个可以从命令行运行的日志分析器。它应当能够读取 JSON Lines 日志，统计请求量、错误量、状态码、热门接口和平均延迟，并具备自动化测试和使用文档。

本周不是为了“学完 Python”，而是完成下面这个闭环：

```text
理解需求 → 拆分模块 → 编写代码 → 制造异常 → 编写测试
       → 修复问题 → 整理 README → Git 提交与复盘
```

## 2. 本周完成标准

- [ ] 建立独立 Python 虚拟环境并安装 pytest、pytest-cov。
- [ ] 掌握本周所需的 Python 基础语法。
- [ ] 完成 `log-analyzer` 命令行程序。
- [ ] 自动化测试不少于 10 条。
- [ ] 行覆盖率达到 80% 以上。
- [ ] 完成 10 道数组、字符串、哈希题。
- [ ] README 能让其他人在 10 分钟内运行项目。
- [ ] 至少产生 5 个有意义的 Git commit。
- [ ] 完成一份周复盘。

## 3. 项目需求

### 输入格式

输入文件采用 JSON Lines 格式，一行代表一次请求：

```json
{"timestamp":"2026-09-14T10:00:00Z","level":"INFO","method":"GET","path":"/api/orders","status":200,"latency_ms":42}
{"timestamp":"2026-09-14T10:00:01Z","level":"ERROR","method":"POST","path":"/api/orders","status":500,"latency_ms":315}
```

### 必须输出的指标

- 日志总行数。
- 成功解析行数。
- 格式错误行数。
- 总请求数。
- HTTP 4xx 数量。
- HTTP 5xx 数量。
- 各状态码数量。
- 请求次数最多的 3 个接口。
- 全部有效请求的平均延迟。

建议输出：

```text
Total lines: 120
Valid records: 116
Malformed lines: 4
Requests: 116
4xx: 8
5xx: 3
Average latency: 85.32 ms
Status codes: 200=90, 201=15, 404=8, 500=3
Top endpoints:
1. GET /api/orders - 52
2. POST /api/orders - 31
3. GET /api/users - 18
```

### 错误处理要求

- 文件不存在：输出清晰错误信息并返回非零退出码。
- 空文件：正常结束，各项统计为 0。
- 某行不是合法 JSON：跳过并计入 `malformed_lines`。
- 字段缺失或类型错误：跳过并计入 `malformed_lines`。
- `latency_ms` 不能为负数。
- `status` 必须是 100～599 的整数。
- 一个坏行不能导致整个文件分析失败。

### 建议目录结构

```text
projects/log-analyzer/
├── pyproject.toml
├── README.md
├── examples/
│   ├── access.jsonl
│   ├── empty.jsonl
│   └── malformed.jsonl
├── src/
│   └── log_analyzer/
│       ├── __init__.py
│       ├── models.py
│       ├── parser.py
│       ├── statistics.py
│       └── cli.py
└── tests/
    ├── test_parser.py
    ├── test_statistics.py
    └── test_cli.py
```

职责建议：

- `models.py`：定义一条有效日志记录的数据结构。
- `parser.py`：读取文件并把每一行转换为记录。
- `statistics.py`：只负责统计，不负责文件读取和终端输出。
- `cli.py`：解析命令行参数、调用业务函数、输出结果。

---

## 3.1 Python 到哪里学

### 主课程：零基础视频

本周使用这一套作为唯一主课：

- [黑马程序员 Python + AI 零基础课程（Bilibili）](https://www.bilibili.com/video/BV1sHU9BmEne/)

它从安装、第一段程序、变量等内容开始，适合尚未建立编程概念的学习者。课程很长，本路线**不要求从头刷完整套视频**，只按每天列出的主题搜索对应章节。

### 查询资料：看不懂时查中文说明

- [廖雪峰 Python 教程](https://liaoxuefeng.com/books/python/introduction/index.html)：中文、示例短，适合第一次理解概念。
- [Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/)：作为字典查询，不作为零基础主课。官方教程本身假定读者已有基本编程概念。

### 练习平台

- [Python123](https://python123.io/)：用于基础语法练习。
- 算法题可以在 LeetCode 中国站或牛客完成，但本周只做文档列出的 10 道。

### 真正写代码的位置

视频只是讲解，真正的学习发生在本机仓库。所有示例代码都写入：

```text
E:\agent_learn\notes\python\week01\
```

项目代码写入：

```text
E:\agent_learn\projects\log-analyzer\
```

在 Git Bash 创建学习笔记目录：

```bash
cd /e/agent_learn
mkdir -p notes/python/week01
touch notes/python/week01/day01.py
touch notes/python/week01/day02.py
touch notes/python/week01/day03.py
touch notes/python/week01/day04.py
touch notes/python/week01/day05.py
```

用 VS Code 打开整个仓库：

```bash
code /e/agent_learn
```

以后不要把代码散落到桌面。视频中的临时代码写入当天的 `dayNN.py`，正式项目代码写入 `projects/log-analyzer`。

### 每个知识点的固定学习动作

每学一个概念，严格完成四步：

1. 看视频 10～20 分钟，暂停视频。
2. 不复制讲师代码，自己重新输入一个例子。
3. 修改输入，故意制造一个错误并阅读错误信息。
4. 关掉视频，再独立写一次。

在 Git Bash 中运行当天练习：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
python notes/python/week01/day01.py
```

学习时间比例：

```text
看视频/文档：最多 40%
自己敲代码：至少 50%
总结和复写：至少 10%
```

如果一个两小时学习块看了 90 分钟视频却没有运行代码，这个学习块视为未完成。

### 本周视频学习范围

只按标题寻找以下内容，不需要追求视频编号完全一致：

| 日期 | 在课程中学习的主题 | 观看上限 | 当天必须自己写的代码 |
|---|---|---:|---|
| Day 1 | 第一段 Python、变量、基本类型、字符串、输入输出 | 60 分钟 | 变量练习、状态码统计、平均延迟 |
| Day 2 | 列表、元组、字典、集合、函数、模块 | 45 分钟 | 三个统计函数和导入调用 |
| Day 3 | 文件读写、JSON、异常处理 | 45 分钟 | 逐行读文件、解析 JSON、捕获坏数据 |
| Day 4 | 命令行参数、包与模块 | 30 分钟 | `argparse` 示例和 CLI 入口 |
| Day 5 | pytest 部分以官方文档为主 | 30 分钟 | 6 条以上真实测试 |
| Day 6～7 | 不再追新课，补缺和完成项目 | 30 分钟/天 | 项目、测试、README |

如果视频中的 Python 版本与本机略有差异，以本机 Python 3.13 的实际运行结果和官方文档为准。

---

## 4. 每日计划

### 开始前先看：命令如何执行

本周统一使用 **Git Bash**，也就是终端标题中显示 `MINGW64` 的窗口。下面代码块中的命令需要一行一行执行：输入一行，按 Enter，等它结束后再输入下一行。

终端可能显示：

```text
15050@klikebe MINGW64 /e/agent_learn (main)
$
```

其中 `$` 是终端提示符，不需要输入。你只输入 `$` 后面的命令。例如文档写：

```bash
git status
```

你只需要输入 `git status`。

常用操作：

- 命令执行成功时可能没有任何输出，这是正常的。
- 命令长时间不结束时按 `Ctrl+C` 停止。
- 路径或文件名输入一半时，可以按 `Tab` 自动补全。
- 清屏使用 `clear`，不会删除任何文件。
- 查看当前目录使用 `pwd`。
- 查看当前目录内容使用 `ls -la`。
- 返回上一级目录使用 `cd ..`。
- 报错时不要连续尝试随机命令，复制“输入的命令 + 完整错误信息”发给 Codex。

每次重新打开 Git Bash，先执行：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
```

激活成功后，命令行最前面通常会出现 `(.venv)`。如果 `.venv` 尚未创建，只在 Day 1 执行创建步骤，不要提前运行第二行。

每天完成代码后的固定检查与提交步骤：

```bash
cd /e/agent_learn
git status --short
git diff
```

先阅读输出，确认改动正确且没有 `.venv`、`.env` 或密钥。然后执行：

```bash
git add projects/log-analyzer
git status --short
git diff --cached --stat
git commit -m "在这里填写当天实际完成的内容"
```

注意：最后一条中的中文只是占位说明，实际提交时换成文档每天建议的英文提交信息。若当天没有形成完整的小成果，可以不提交，不要为了凑数量提交空内容。

## Day 1｜环境、Git 与 Python 容器（2 小时）

### 0:00～0:20：建立环境

当前机器已检测到：

```text
Python 3.13.13
Git 2.53.0
```

#### 步骤 1：进入正确目录

打开 Git Bash，逐行执行：

```bash
cd /e/agent_learn
pwd
git status
```

`pwd` 预期输出：

```text
/e/agent_learn
```

如果不是这个目录，先不要继续。`git status` 应能看到 `On branch main`。它也可能显示 `plan.md` 和 `weekly/` 尚未提交，这是当前正常状态。

#### 步骤 2：创建并激活虚拟环境

只需创建一次：

```bash
python -m venv .venv
```

创建过程可能几十秒没有输出。完成后，执行：

```bash
source .venv/Scripts/activate
```

确认当前使用的是虚拟环境中的 Python：

```bash
which python
python --version
```

`which python` 的输出路径中应包含：

```text
/e/agent_learn/.venv/Scripts/python
```

如果你改用 PowerShell，激活命令才是：

```powershell
.\.venv\Scripts\Activate.ps1
```

两种终端的激活命令不要混用。

#### 步骤 3：安装本周依赖

确保命令行前面有 `(.venv)`，然后逐行执行：

```bash
python -m pip install --upgrade pip
python -m pip install pytest pytest-cov
python -m pytest --version
```

最后一条命令能显示 pytest 版本即为成功。如果下载失败，把完整错误发给 Codex；不要从不明网站手动下载包。

#### 步骤 4：创建 `.gitignore`

先检查文件是否已存在：

```bash
ls -la
```

使用 VS Code 打开当前目录：

```bash
code .
```

如果提示 `code: command not found`，直接使用资源管理器或其他编辑器，在 `E:\agent_learn` 下新建名为 `.gitignore` 的文件。注意文件名开头有英文句点，并且没有 `.txt` 后缀。

将以下内容加入 `.gitignore`：

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.coverage
htmlcov/
.env
```

不要提交 `.venv`、缓存、覆盖率文件或密钥。

保存后回到 Git Bash，检查忽略是否生效：

```bash
git status --short
```

输出中不应该出现成百上千个 `.venv/` 文件。如果出现，先停止，不要执行 `git add`。

### 0:20～1:20：Python 必学内容

- 基本类型：`int`、`float`、`str`、`bool`、`None`。
- 容器：`list`、`tuple`、`dict`、`set`。
- 控制流：`if`、`for`、`while`。
- 函数：参数、返回值、默认值、关键字参数。
- 推导式、`enumerate`、`zip`、`sorted`。

练习：

1. 输入状态码列表，返回每种状态码出现次数。
2. 输入接口路径列表，返回出现次数最多的 3 个。
3. 输入若干延迟，返回平均值；空列表返回 `0.0`。

### 1:20～1:50：Git 基础

#### 第一次提交

先查看将要提交的内容：

```bash
git status --short
git diff
```

然后只暂存计划文档和 `.gitignore`：

```bash
git add .gitignore plan.md weekly/week-01.md
git status --short
git diff --cached --stat
```

确认列表中没有 `.venv`、`.env`、密钥或陌生的大文件后再提交：

```bash
git commit -m "chore: initialize week 1 project"
git log --oneline -5
```

如果 Git 提示没有配置姓名和邮箱，把完整提示发给 Codex，不要随意填写别人的信息。

只提交 Day 1 实际完成的初始化内容，不创建空洞的大提交。

### 1:50～2:00：当日检查

- [ ] 虚拟环境可激活。
- [ ] pytest 可运行。
- [ ] 能解释 list、tuple、dict、set 的不同用途。
- [ ] 完成第一次 commit。

## Day 2｜函数、模块与数据模型（2 小时）

### 0:00～0:35：复习与算法

完成：

1. 两数之和。
2. 存在重复元素。

要求：先独立写，记录时间复杂度和空间复杂度，再看更优解。

### 0:35～1:15：Python 必学内容

- 模块、包、`import`。
- 作用域和纯函数。
- 类与 `dataclass`。
- 类型标注：`list[str]`、`dict[int, int]`、`Optional`。
- `collections.Counter` 和 `defaultdict`。

### 1:15～1:50：项目任务

先进入仓库根目录并激活环境：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
```

创建项目目录：

```bash
mkdir -p projects/log-analyzer/src/log_analyzer
mkdir -p projects/log-analyzer/tests
mkdir -p projects/log-analyzer/examples
cd projects/log-analyzer
touch pyproject.toml README.md
touch src/log_analyzer/__init__.py
touch src/log_analyzer/models.py
touch src/log_analyzer/parser.py
touch src/log_analyzer/statistics.py
touch src/log_analyzer/cli.py
touch tests/test_parser.py
touch tests/test_statistics.py
touch tests/test_cli.py
touch examples/access.jsonl
touch examples/empty.jsonl
touch examples/malformed.jsonl
find . -maxdepth 3 -type f | sort
```

最后一条命令应该列出刚创建的文件。`touch` 只创建空文件，不会自动写入代码。

在 `pyproject.toml` 中写入：

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "log-analyzer"
version = "0.1.0"
requires-python = ">=3.11"

[project.scripts]
log-analyzer = "log_analyzer.cli:main"

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.coverage.run]
source = ["log_analyzer"]
```

保存文件后安装当前项目：

```bash
python -m pip install -e .
```

`-e` 表示可编辑安装。以后修改 `src` 中的代码，不需要每次重新安装。

然后完成代码任务：

- 在 `models.py` 定义日志记录模型。
- 明确字段类型和校验规则。
- 在 `statistics.py` 写三个独立函数：状态码统计、热门接口、平均延迟。

写完后，从项目目录运行：

```bash
python -m pytest -q
git status --short
```

### 1:50～2:00：当日检查

- [ ] 数据模型能表示一条合法记录。
- [ ] 统计函数没有读取文件和打印输出。
- [ ] 完成第二次 commit，例如 `feat: add log record model and statistics`。

## Day 3｜文件、JSON 与异常处理（2 小时）

### 0:00～0:35：算法

完成：

3. 有效的字母异位词。
4. 两个数组的交集。

### 0:35～1:10：Python 必学内容

- `pathlib.Path`。
- `with` 上下文管理器。
- 文本编码和逐行读取。
- `json.loads`。
- `try/except/else/finally`。
- 捕获具体异常，不写裸 `except:`。

### 1:10～1:50：项目任务

- 在 `parser.py` 实现逐行读取 JSONL。
- 校验必需字段和字段类型。
- 返回有效记录与错误信息/错误计数。
- 为文件不存在、空文件、坏 JSON 写最小测试。

从仓库任意目录都可以先用下面三行回到正确位置：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
cd projects/log-analyzer
```

只运行解析器测试：

```bash
python -m pytest tests/test_parser.py -v
```

`-v` 会显示每个测试名称。成功时末尾应出现类似 `3 passed`；失败时从第一个红色 `FAILED` 开始阅读。

完成后提交：

```bash
cd /e/agent_learn
git add projects/log-analyzer/src/log_analyzer/parser.py projects/log-analyzer/tests/test_parser.py
git diff --cached --stat
git commit -m "feat: parse and validate jsonl logs"
```

### 1:50～2:00：当日检查

- [ ] 单行损坏不会中止整个文件。
- [ ] 文件使用 UTF-8 打开并能正确关闭。
- [ ] 完成第三次 commit，例如 `feat: parse and validate jsonl logs`。

## Day 4｜CLI 与端到端数据流（2 小时）

### 0:00～0:35：算法

完成：

5. 移动零。
6. 合并两个有序数组。

### 0:35～1:00：Python 必学内容

- `argparse` 基础。
- `python -m package.module` 的运行方式。
- 退出码和标准错误输出。
- 业务逻辑与展示逻辑分离。

### 1:00～1:50：项目任务

- 在 `cli.py` 接收日志文件路径。
- 串联 parser 和 statistics。
- 按项目需求打印结果。
- 文件不存在时输出明确错误并返回非零退出码。
- 准备至少三个 example 文件。

先回到项目目录：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
cd projects/log-analyzer
```

确认命令已被安装：

```bash
log-analyzer --help
```

如果你在 `argparse` 中把文件路径参数命名为 `log_file`，可以运行：

```bash
log-analyzer examples/access.jsonl
log-analyzer examples/empty.jsonl
log-analyzer examples/malformed.jsonl
```

也可以直接运行模块，但前提是 `cli.py` 中包含 `main()` 调用入口：

```bash
python -m log_analyzer.cli examples/access.jsonl
```

检查文件不存在时的退出码：

```bash
log-analyzer examples/not-exist.jsonl
echo $?
```

最后一行应为非零数字，通常为 `1` 或 `2`。`echo $?` 表示查看上一条命令的退出码。

运行 CLI 测试并提交：

```bash
python -m pytest tests/test_cli.py -v
cd /e/agent_learn
git add projects/log-analyzer
git diff --cached --stat
git commit -m "feat: add command-line report"
```

### 1:50～2:00：当日检查

- [ ] 可以从命令行分析正常日志。
- [ ] 可以正确处理空文件和坏文件。
- [ ] 完成第四次 commit，例如 `feat: add command-line report`。

## Day 5｜pytest 入门与测试设计（2 小时）

### 0:00～0:35：算法

完成：

7. 买卖股票的最佳时机。
8. 最长公共前缀。

### 0:35～1:05：pytest 必学内容

- 测试发现规则。
- Arrange、Act、Assert。
- `@pytest.mark.parametrize`。
- `pytest.raises`。
- `tmp_path` fixture。
- 测试命名应说明条件和预期。

### 1:05～1:50：项目任务

为以下场景设计测试，不必一天全部写完：

1. 单条合法日志。
2. 多条合法日志。
3. 空文件。
4. 文件不存在。
5. 非法 JSON。
6. 缺少必需字段。
7. 状态码不是整数。
8. 状态码超出范围。
9. 延迟为负数。
10. 多个 endpoint 排名。
11. 状态码分组统计。
12. 平均延迟精度。

运行全部测试：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
cd projects/log-analyzer
python -m pytest -v
```

只运行名称中包含 `status` 的测试：

```bash
python -m pytest -v -k status
```

显示覆盖率和未覆盖行：

```bash
python -m pytest --cov=log_analyzer --cov-report=term-missing
```

输出中的 `TOTAL` 行是总覆盖率，`Missing` 列会指出尚未执行到的代码行。

### 1:50～2:00：当日检查

- [ ] 已写至少 6 条测试。
- [ ] 测试名称能表达输入条件和预期。
- [ ] 完成第五次 commit，例如 `test: cover parser and statistics`。

## Day 6｜集中开发与边界测试（5 小时）

### 第 1 小时：算法与复盘

完成：

9. 验证回文串。
10. 同构字符串。

复写本周最不熟练的两道题，不看答案。

### 第 2～3 小时：完成项目功能

- 补齐全部统计指标。
- 保证错误行被统计但不终止处理。
- 统一函数名、变量名和类型标注。
- 消除明显重复逻辑。

### 第 4 小时：补齐测试

- 测试总数达到至少 10 条，建议达到 15 条。
- 覆盖 parser、statistics、cli 三层。
- 不只追求覆盖率数字，至少覆盖每项错误处理要求。

运行：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
cd projects/log-analyzer
python -m pytest -q
python -m pytest --cov=log_analyzer --cov-report=term-missing
```

如果看到 `ModuleNotFoundError: No module named 'log_analyzer'`，确认虚拟环境已激活，并在 `projects/log-analyzer` 下重新执行：

```bash
python -m pip install -e .
```

### 第 5 小时：调试和代码审查

- 删除调试用 `print`。
- 检查是否存在过大的函数。
- 检查异常是否过度捕获。
- 检查文件路径、空输入和类型边界。
- 提交第六次 commit：`refactor: improve validation and error handling`。

当日验收：

- [ ] 所有测试通过。
- [ ] 覆盖率达到 80% 以上。
- [ ] 正常、空、损坏三类示例均可运行。

## Day 7｜README、最终验收与复盘（5 小时）

### 第 1 小时：从零验证安装

模拟一个第一次看到项目的人：

1. 按 README 创建环境。
2. 安装依赖或以 editable 模式安装项目。
3. 运行 example。
4. 执行全部测试。
5. 查看覆盖率。

任何依赖“你脑中知道但 README 没写”的步骤都需要补充。

### 第 2 小时：完成 README

README 至少包含：

- 项目解决的问题。
- 输入格式。
- 安装方式。
- 运行命令。
- 输出示例。
- 测试命令。
- 项目结构。
- 错误处理策略。
- 当前限制与下一步计划。

### 第 3 小时：项目验收

执行并保存结果：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
cd projects/log-analyzer
python -m pytest -q
python -m pytest --cov=log_analyzer --cov-report=term-missing
cd /e/agent_learn
git status --short
git log --oneline -10
```

手工测试：

- 文件不存在。
- 空文件。
- 仅有坏行。
- 合法与坏行混合。
- 状态码 100、599、99、600。
- 延迟为 0 和负数。

### 第 4 小时：口头自测

不看资料回答：

1. 为什么用 JSON Lines，而不是一个大 JSON 数组？
2. list、tuple、set、dict 如何选择？
3. 为什么解析和统计要分成不同模块？
4. 为什么不能遇到一个坏行就让程序退出？
5. `try/except` 捕获范围为什么不应过大？
6. 单元测试和端到端测试分别在验证什么？
7. 覆盖率 100% 是否代表没有 Bug？
8. `git add`、`commit`、`push` 分别做了什么？

无法清晰回答的问题，回到代码或文档做一次最小实验。

### 第 5 小时：周复盘与最终提交

在本文件末尾填写周复盘。完成最终 commit，但在确认没有密钥和大文件前不要 push。

推荐提交信息：

```text
docs: complete log analyzer guide and week 1 review
```

提交前先执行完整检查：

```bash
cd /e/agent_learn
git status --short
git diff
git add .gitignore plan.md weekly/week-01.md projects/log-analyzer
git diff --cached --stat
git status --short
git commit -m "docs: complete log analyzer guide and week 1 review"
```

确认提交成功后推送。由于当前 `main` 可能还没有绑定上游分支，第一次使用：

```bash
git push -u origin main
```

以后只需要：

```bash
git push
```

如果 Git 显示 `nothing to commit, working tree clean`，表示没有新的未提交改动，不是错误。如果 push 失败，复制完整输出发给 Codex。

---

## 5. 算法题清单

| 序号 | 题型 | 题目 | 完成 | 独立复写 |
|---:|---|---|:---:|:---:|
| 1 | 哈希 | 两数之和 | [ ] | [ ] |
| 2 | 哈希 | 存在重复元素 | [ ] | [ ] |
| 3 | 哈希 | 有效的字母异位词 | [ ] | [ ] |
| 4 | 集合 | 两个数组的交集 | [ ] | [ ] |
| 5 | 数组/双指针 | 移动零 | [ ] | [ ] |
| 6 | 数组/双指针 | 合并两个有序数组 | [ ] | [ ] |
| 7 | 数组 | 买卖股票的最佳时机 | [ ] | [ ] |
| 8 | 字符串 | 最长公共前缀 | [ ] | [ ] |
| 9 | 字符串/双指针 | 验证回文串 | [ ] | [ ] |
| 10 | 哈希 | 同构字符串 | [ ] | [ ] |

每道题记录：

```text
第一次用时：
是否一次通过：
时间复杂度：
空间复杂度：
错误原因：
复写日期：
```

不要为了数量直接抄答案。超过 25 分钟仍无思路时，只看提示；再尝试 15 分钟后才看完整解法，并在 24 小时内独立复写。

---

## 6. 本周学习资源

只使用以下主资料，避免不停更换课程：

- Python 官方教程：https://docs.python.org/3/tutorial/
- Python `json`：https://docs.python.org/3/library/json.html
- Python `pathlib`：https://docs.python.org/3/library/pathlib.html
- Python `argparse`：https://docs.python.org/3/library/argparse.html
- pytest 入门：https://docs.pytest.org/en/stable/getting-started.html
- pytest fixtures：https://docs.pytest.org/en/stable/how-to/fixtures.html
- Git 基础：https://git-scm.com/book/zh/v2

资料使用顺序：看 15～25 分钟 → 立即写代码 → 制造一个错误 → 写测试验证。

---

## 7. 遇到时间不足时的裁剪顺序

按以下顺序从上到下裁剪，不能随意跳过核心交付：

1. 取消额外算法题，只保留表中的 10 道。
2. README 的“未来计划”可以简写。
3. 热门接口数量固定为 3，不做可配置参数。
4. 暂不增加 CSV、Nginx Common Log 等输入格式。
5. 不做彩色输出、进度条和界面。

不得裁剪：虚拟环境、核心统计、错误处理、10 条测试、README 运行步骤、周复盘。

---

## 8. 周末验收表

### 环境与 Git

- [ ] `.venv` 未提交。
- [ ] 没有提交 API Key、密码或个人隐私数据。
- [ ] `git status` 的变更均符合预期。
- [ ] 至少 5 个有意义的 commit。

### 项目

- [ ] 正常日志输出正确。
- [ ] 空文件不会崩溃。
- [ ] 文件不存在返回非零退出码。
- [ ] 坏行被跳过并计数。
- [ ] 状态码和延迟边界校验正确。
- [ ] 自动化测试不少于 10 条。
- [ ] 覆盖率达到 80% 以上。
- [ ] README 可指导从零运行。

### 学习

- [ ] 10 道算法题全部完成。
- [ ] 至少复写 2 道做错或卡住的题。
- [ ] 能回答 Day 7 的 8 个口头问题。

---

## 9. 周复盘（周日填写）

```text
计划完成率：
实际投入时间：

已完成：
- 

未完成：
- 

本周新增能力：
- 

最难的问题及解决过程：
- 

项目新增内容：
- 

算法完成数：
测试数量：
测试覆盖率：
Git commit 数：

下周需要调整的地方：
- 
```

## 10. 向 Codex 汇报进度

每天结束时可以使用：

```text
第 1 周 Day N 已结束。
今天完成：
运行/测试结果：
遇到的问题：
实际投入时间：
请检查结果并给出下一天的调整建议。
```

周日完成后使用：

```text
第 1 周已结束，请检查 weekly/week-01.md 的复盘和项目代码，
按照实际完成情况生成第 2 周计划。
```

---

## 11. 常见报错速查

### `bash: python: command not found`

先执行：

```bash
py --version
```

如果 `py` 可用，将创建环境的命令改为 `py -m venv .venv`。如果两者都不可用，需要重新安装 Python，并在安装界面勾选加入 PATH。

### `bash: .venv/Scripts/activate: No such file or directory`

通常是当前不在仓库根目录，或虚拟环境尚未创建。执行：

```bash
cd /e/agent_learn
ls -la
python -m venv .venv
source .venv/Scripts/activate
```

### `No module named pytest`

说明当前虚拟环境没有安装 pytest，执行：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
python -m pip install pytest pytest-cov
```

### `No module named log_analyzer`

重新执行可编辑安装：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
cd projects/log-analyzer
python -m pip install -e .
```

### `collected 0 items`

确认测试文件名以 `test_` 开头、测试函数名也以 `test_` 开头，然后检查当前位置：

```bash
pwd
find tests -maxdepth 2 -type f
```

### `Author identity unknown`

Git 尚未配置提交身份。先查看当前配置：

```bash
git config --get user.name
git config --get user.email
```

把错误和你准备使用的 GitHub 提交姓名、邮箱发给 Codex，再决定使用仓库级还是全局配置。

### 不小心退出虚拟环境

重新激活即可：

```bash
cd /e/agent_learn
source .venv/Scripts/activate
```

主动退出虚拟环境使用：

```bash
deactivate
```
