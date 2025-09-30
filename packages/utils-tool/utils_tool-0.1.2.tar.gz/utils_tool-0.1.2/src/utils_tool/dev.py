"""开发支持工具 black path"""

import functools
from itertools import islice
import subprocess
from contextlib import contextmanager
import traceback
import os


## locust 压力测试


def struct():
    """
    一个装饰器，用于在运行时校验函数的输入参数和返回值的类型。

    此装饰器通过检查函数注解来确保传入的参数类型和函数返回值的类型符合预期。
    如果类型不匹配，将抛出 AssertionError。

    推荐在工程化项目中使用，以增强代码的健壮性和可维护性。

    用法示例:
        >>> @struct()
        >>> def add(a: int, b: int) -> int:
        >>>     return a + b
        >>> add(1, 2) # 正常执行
        3
        >>> add(1, "2") # 抛出 AssertionError

    Returns:
        Callable: 一个包装函数，用于执行类型校验。
    """

    def outer_packing(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            ann_dict = func.__annotations__

            if len(args) != 0:
                remaining_items = islice(ann_dict.items(), None, len(args))
                args_result_dict = dict(remaining_items)
                args_result_list = list(args_result_dict.values())
                try:
                    for i, j in enumerate(args_result_list):
                        assert isinstance(args[i], j)
                except AssertionError as e:
                    raise AssertionError(f"位置: {i} 预期的输入是: {j}") from e

            try:
                for k, v in kwargs.items():
                    assert isinstance(v, ann_dict[k])
            except AssertionError as e:
                raise AssertionError(f"位置: {k} 预期的输入是: {v}") from e
            try:
                assert isinstance(result, ann_dict.get("return", object))
            except AssertionError as e:
                raise AssertionError("返回值格式不准确") from e

            return result

        return wrapper

    return outer_packing


@contextmanager
def safe_operation():
    """
    一个上下文管理器，用于安全地执行代码块并捕获其中的异常。

    当代码块中发生异常时，此上下文管理器会捕获异常，打印详细的错误信息（包括堆栈跟踪），
    并重新抛出一个通用的异常。这有助于在不中断程序流程的情况下处理预期之外的错误，
    并提供统一的错误日志记录机制。

    用法示例:
        >>> with safe_operation():
        >>>     # 可能会抛出异常的代码
        >>>     result = 1 / 0
        >>> # 异常会被捕获并处理
    """
    try:
        yield
    except Exception as e:
        error_info = traceback.format_exc()
        print(e, error_info)  # 详细信息
        raise Exception(" exception!") from e
        # log记录


####
class GitHubManager:
    """
    一个用于管理和获取 GitHub 仓库提交历史的工具类。

    此类能够执行 Git 命令来获取指定 GitHub 仓库的提交历史，
    并将其格式化为 Mermaid Git Graph 语法，以便于可视化。
    主要用于获取仓库的 Git 记录，并可将这些记录用于其他目的。
    """

    def __init__(self):
        """
        初始化 GitHubManager 实例。

        设置 Mermaid 图的格式字符串。
        """
        self.mermaid_format = """
        ```mermaid
        {mermaid_code}
        ```
        """

    def _get_origin(self):
        """
        获取并推送指定 GitHub 仓库的 Git 记录。

        此方法遍历预定义的 GitHub 仓库列表，并对每个仓库执行 `git push origin main` 命令。
        主要用于确保本地仓库与远程主分支同步。

        注意:
            此方法包含硬编码的本地路径和仓库列表，可能需要根据实际环境进行调整。
            目前包含一个 TODO 标记，表示可能需要进一步完善。
        """
        home = "/Users/zhaoxuefeng/GitHub/"

        for repo in [
            "toolsz",
            "llmada",
            "clientz",
            "commender",
            "mermaidz",
            "kanbanz",
            "querypipz",
            "appscriptz",
            "reallife-client-mac",
            "designerz",
            "algorithmz",
            "reallife",
            "promptlibz",
        ]:
            os.system(f"git -C {os.path.join(home,repo)} push origin main")

    def generate_mermaid_git_graph(self, simulated_git_log: str) -> str:
        """
        将模拟的 Git 日志输出转换为 Mermaid Git Graph 语法。

        此方法解析 Git 日志的简化输出，并将其转换为 Mermaid 图所需的 `gitGraph` 格式。
        它能够识别提交哈希、分支引用和提交消息，并将其转换为 Mermaid 图的节点和标签。

        Args:
            simulated_git_log (str): 模拟的 Git 日志字符串，通常是 `git log --all --graph --pretty=format:%h,%d,%s` 的输出。

        Returns:
            str: 格式化为 Mermaid Git Graph 语法的字符串。
        """

        mermaid_code = "gitGraph\n"
        commits_seen = {}  # To track commits and avoid duplicates if needed

        for line in simulated_git_log.strip().split("\n"):
            line = line.strip()
            if line.startswith("*"):
                # Parse the commit line
                # Handle potential extra space after * and split by the first two commas
                parts = line[1:].strip().split(",", 2)
                if len(parts) >= 2:
                    hash_val = parts[0].strip()
                    refs = parts[1].strip()
                    message = parts[2].strip() if len(parts) > 2 else ""

                    commit_line = f'    commit id: "{hash_val}"'

                    # Process references (branches, tags)
                    if refs:
                        # Remove parentheses and split by comma
                        ref_list = [
                            r.strip()
                            for r in refs.replace("(", "").replace(")", "").split(",")
                            if r.strip()
                        ]
                        processed_refs = []
                        for ref in ref_list:
                            if "->" in ref:
                                ref = ref.split("->")[
                                    -1
                                ].strip()  # Get the branch name after ->
                            if (
                                ref and ref != "HEAD"
                            ):  # Exclude the simple HEAD reference
                                processed_refs.append(f'"{ref}"')
                        if processed_refs:
                            # Join with comma and space as it's a single tag attribute
                            commit_line += f' tag: {", ".join(processed_refs)}'

                    if message:
                        # Escape double quotes in message
                        message = message.replace('"', '\\"')
                        commit_line += f' msg: "{message}"'

                    mermaid_code += commit_line + "\n"
                    commits_seen[hash_val] = True

            # Note: Handling merge lines (|/ \) is more complex and not fully covered
            # in this simple parser, requires analyzing the graph structure.

        # print(mermaid_code)
        return mermaid_code

    def work(self) -> str:
        """
        执行 Git 命令以获取当前仓库的完整提交历史。

        此方法运行 `git log --all --graph --pretty=format:%h,%d,%s` 命令，
        捕获其标准输出，并打印出来。它还处理命令执行过程中可能出现的错误，
        例如 Git 命令未找到或执行失败。

        Returns:
            str: Git 命令的标准输出，包含格式化的提交历史。

        Raises:
            FileNotFoundError: 如果 'git' 命令未找到。
            subprocess.CalledProcessError: 如果 Git 命令执行失败。
        """
        # 将命令拆分成一个列表，这是更安全的方式
        command = ["git", "log", "--all", "--graph", "--pretty=format:%h,%d,%s"]

        try:
            # 执行命令
            # capture_output=True: 捕获标准输出和标准错误
            # text=True: 将捕获到的输出(bytes)解码为文本(str)
            # check=True: 如果命令返回非零退出码（表示有错误），则会抛出异常
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
                encoding="utf-8",  # 明确指定编码，避免乱码问题
            )

            # 捕获的输出存储在 result.stdout 属性中
            git_log_output = result.stdout

            # 现在你可以对这个字符串做任何你想做的事情了
            print("--- 捕获到的 Git Log 输出 ---")
            print(git_log_output)

            # 你甚至可以把它按行分割成一个列表
            log_lines = git_log_output.strip().split("\n")
            print("\n--- 输出的第一行 ---")
            print(log_lines[0])

        except FileNotFoundError:
            print(
                "错误: 'git' 命令未找到。请确保 Git 已经安装并且在系统的 PATH 环境变量中。"
            )
        except subprocess.CalledProcessError as e:
            # 如果 git 命令执行失败 (例如，不在一个 git 仓库中)
            print(f"执行 Git 命令时出错，返回码: {e.returncode}")
            print(f"错误信息 (stderr):\n{e.stderr}")
        return git_log_output

    def run(self) -> str:
        """
        执行完整的 Git 历史获取和 Mermaid 图生成流程。

        此方法首先调用 `work()` 获取 Git 日志输出，然后使用 `generate_mermaid_git_graph()`
        将日志转换为 Mermaid 语法，最后将 Mermaid 代码嵌入到预定义的格式字符串中。

        Returns:
            str: 包含 Mermaid Git Graph 的完整格式化字符串，可以直接在支持 Mermaid 的环境中渲染。
        """
        git_log_output = self.work()
        mermaid_code = self.generate_mermaid_git_graph(git_log_output)
        return self.mermaid_format.format(mermaid_code=mermaid_code)



"""抓包和反编译 pyshark"""

import time
import pyshark

# !pip install pyshark
# 使用过滤器捕获 HTTP 流量
capture = pyshark.LiveCapture(interface="Wi-Fi", display_filter="http")

# 捕获流量，设置超时时间为50秒
capture.sniff(timeout=5)

# 打印捕获到的 HTTP 数据包
print("start")
for packet in capture:
    print(packet)
    # print('Packet Number:', packet.number)
    # print('Timestamp:', packet.sniff_time)
    # print('Source IP:', packet.ip.src)
    # print('Destination IP:', packet.ip.dst)
    time.sleep(0.1)


# 捕获网络接口上的流量
capture = pyshark.LiveCapture(interface="eth0")

# 捕获流量，设置超时时间为50秒
capture.sniff(timeout=50)

# 访问数据包内容
for packet in capture:
    print("Packet Number:", packet.number)
    print("Timestamp:", packet.sniff_time)
    print("Source IP:", packet.ip.src)
    print("Destination IP:", packet.ip.dst)
    if "http" in packet:
        print("HTTP Method:", packet.http.request_method)
        print("HTTP Host:", packet.http.host)



# 多轮对话
import asyncio
from fastapi import FastAPI, HTTPException
from pyppeteer import launch
from pydantic import BaseModel
from contextlib import asynccontextmanager
import os


# 存储浏览器实例和页面对象
browser = None
page = None

userDataDir = '/Users/zhaoxuefeng/GitHub/test1/userdata'
# userDataDir = "~/Library/Application Support/Google/Chrome"
# 启动浏览器并初始化页面
async def init_browser():
    global browser, page, i
    browser = await launch(headless=False,
                        #    args=['--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage'],
                           userDataDir=userDataDir,
                           executable_path='/Applications/Google Chrome',
                           devtools=False,
                          )
    i = 1                     
    page = await browser.newPage()
    await page.goto('https://kimi.moonshot.cn/chat')
    await page.waitForSelector('.chat-input')


# 编写类似with 的功能
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # 启动时执行的逻辑
        await init_browser()
        if not page:
            raise HTTPException(status_code=500, detail="Failed to initialize browser")
        yield

    finally:
        # 确保浏览器关闭
        if browser:
            await browser.close()

app = FastAPI(lifespan=lifespan)


# 定义请求体模型
class ChatRequest(BaseModel):
    message: str

# 多轮对话 API
@app.post("/chat")
async def chat(request: ChatRequest):
    global page,i
    print('start')
    if not page:
        raise HTTPException(status_code=500, detail="Browser not initialized")
    user_input = request.message.strip()
    if not user_input:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    if user_input.lower() == 'exit':
        raise HTTPException(status_code=400, detail="Conversation ended")
    try:
        # 输入用户消息并发送
        await page.type('.chat-input', user_input)
        await page.evaluate('''() => {
        document.querySelector('.send-button').click();
        }''')
        
        # 等待回复
        x = 1 + 2 * i
        print(x)
        xpath_expression2 = f'//*[@id="app"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[{x}]/div/div[2]/div[2]'
        await page.waitForXPath(xpath_expression2, timeout=60000)
        
        # 获取回复内容
        xpath_expression = f'//*[@id="app"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[{x}]/div/div[2]/div[1]/div[1]/div[2]/div'
        elements = await page.xpath(xpath_expression)
        text_contents = []
        for element in elements:
            text_content = await (await element.getProperty('textContent')).jsonValue()
            text_contents.append(text_content)
        
        response = '\n'.join(text_contents)
        i +=1
        return {"response": response}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8093,loop="asyncio") # loop 是有效果的
# loop="asyncio"