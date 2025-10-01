import base64
import warnings
import hashlib

from pathlib import Path
from typing import TypedDict, Literal, Optional, Iterable
from urllib.parse import quote_plus

from rich.console import Console

# noinspection PyProtectedMember
from playwright.sync_api import sync_playwright

CONSOLE = Console(force_terminal=True)


class LogMessage(TypedDict):
    type: Literal['log', 'warn', 'error', 'breakpoint', 'exit_code', 'say', 'think', 'did_not_run']
    content: Optional[str]


__file_path__ = Path(__file__).resolve()
run_html_path = (__file_path__ / '..' / "run.html").resolve()
tw_scaffolding_path = (__file_path__ / '..' / "scaffolding-with-music.js").resolve()


def get_exit_code(output: list[LogMessage], default: Optional[str] = None) -> Optional[str]:
    ret = output[-1]
    return ret["content"] if ret["type"] == "exit_code" else default


def output_msg(msg: LogMessage):
    """
    Print a log message to console with colored formatting. Automatically used by run()
    :param msg: Log message dictionary
    """
    cat = msg['type']
    content = msg.get('content')

    # noinspection PyUnreachableCode
    match cat:
        case 'log':
            CONSOLE.print(f"Log: {content!r}", style="green")
        case 'warn':
            CONSOLE.print(f"Warn: {content!r}", style="yellow")
        case 'error':
            CONSOLE.print(f"Error: {content!r}", style="red")
        case 'breakpoint':
            CONSOLE.print(f"Breakpoint", style="red")
        case 'exit_code':
            CONSOLE.print(f"Exited with code {content}", style="default")
        case 'say':
            CONSOLE.print(f"Say: {content!r}", style="purple")
        case 'think':
            CONSOLE.print(f"Think: {content!r}", style="purple")
        case 'did_not_run':
            CONSOLE.print(f"{content}", style="red")
        case _:
            warnings.warn(f"Unknown message: {msg!r}")
            CONSOLE.print(f"{msg['type']}: {msg.get('content', '')!r}")


def run(sb3_file: bytes,
        input_args: Iterable[str] = (),
        *,
        headless: bool = True,
        timeout: int = 1000,
        cloud_host: str = "wss://clouddata.turbowarp.org",
        username: str = "player",
        project_id: Optional[str] = None) -> list[LogMessage]:
    """
    Run a scratch project.
    :param sb3_file: Scratch project to run, in bytes
    :param input_args: arguments that are passed to any 'ask' ui. If these run out, then you will be prompted
    :param headless: Whether to run playwright in headless mode (whether to hide the window)
    :param timeout: How long to wait for the project to run, after being ready. This is usually only relevant for empty projects.
    :param cloud_host: Cloud host for the project. Defaults to TW
    :param project_id: Project ID for cloud connection. Defaults to the sha256 hash of the sb3 file
    :param username: Username for username block, and for cloud variables. Defaults to 'player'
    :return: List of log messages from scratch project
    """
    if project_id is None:
        project_id = hashlib.sha256(sb3_file).hexdigest() + ".sb3"

    input_args = list(input_args)

    for iarg in input_args:
        assert '\n' not in iarg, f"Input arg {iarg!r} should not contain newline."

    assert isinstance(timeout, int)
    assert timeout > 0

    def get_arg():
        get_output()
        if input_args:
            arg = input_args.pop(0)
            CONSOLE.print(f">> {arg!r}")
            return arg
        else:
            return input(">> ")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        page = browser.new_page()

        assert run_html_path.exists()
        assert tw_scaffolding_path.exists()

        page.goto(f"file://{run_html_path}"
                  f"?project={base64.urlsafe_b64encode(sb3_file).decode()}"
                  f"&timeout={timeout}"
                  f"&cloud_host={quote_plus(cloud_host.encode())}"
                  f"&project_id={quote_plus(project_id.encode())}"
                  f"&username={quote_plus(username.encode())}")

        while True:
            if not page.query_selector("#project"):
                warnings.warn("#project not found")
            else:
                break

        output_i = 0  # index of next message

        def get_output() -> list[LogMessage]:
            """
            Handle and return output. If new messages are received, print them.
            """
            nonlocal output_i
            output = page.evaluate("output")

            while len(output) > output_i:
                output_msg(output[output_i])
                output_i += 1

            return output

        while True:
            ret = get_output()
            if any(msg["type"] == "exit_code" for msg in ret):
                break

            # detect ask and wait block ui
            sc_input = page.query_selector(".sc-question-input")
            if sc_input is not None:
                sc_input.type(get_arg() + '\n')  # \n to actually send the message to the ask block

        browser.close()
        return ret
