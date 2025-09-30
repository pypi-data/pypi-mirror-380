"""Command-line interface for the bsy-clippy Ollama client."""
from __future__ import annotations

import argparse
import json
import os
import sys
from importlib import resources
from pathlib import Path
from typing import IO, Iterable, List, Optional, Sequence, Tuple

import requests

YELLOW = "\033[93m"
ANSWER_COLOR = "\033[96m"
RESET = "\033[0m"

_DEFAULT_SYSTEM_PROMPT = "data/bsy-clippy.txt"


def _read_default_system_prompt() -> str:
    """Return the packaged default system prompt if it exists."""
    try:
        prompt_path = resources.files("bsy_clippy").joinpath(_DEFAULT_SYSTEM_PROMPT)
    except (FileNotFoundError, ModuleNotFoundError, AttributeError):
        return ""

    try:
        return prompt_path.read_text(encoding="utf-8").strip("\n")
    except OSError:
        return ""


def load_system_prompt(path: Optional[str], allow_default: bool = True) -> str:
    """Return the content of a system prompt file, or the packaged default."""
    if path:
        file_path = Path(path)
        if not file_path.exists():
            return _read_default_system_prompt() if allow_default else ""
        try:
            return file_path.read_text(encoding="utf-8").strip("\n")
        except OSError as exc:
            print(f"[Warning] Could not read system prompt file '{path}': {exc}", file=sys.stderr)
            return ""
    if allow_default:
        return _read_default_system_prompt()
    return ""


def compose_prompt(system_prompt: str, user_prompt: str, data: str) -> str:
    """Combine system prompt, user prompt, and data into a single message."""
    parts: List[str] = []
    for part in (system_prompt, user_prompt, data):
        if part and part.strip():
            parts.append(part.strip("\n"))
    return "\n\n".join(parts)


def strip_think_segments(text: str) -> str:
    """Return text with <think> sections removed."""
    if not text:
        return ""

    result: List[str] = []
    idx = 0
    in_think = False

    while idx < len(text):
        if in_think:
            close_idx = text.find("</think>", idx)
            if close_idx == -1:
                break
            idx = close_idx + len("</think>")
            in_think = False
        else:
            open_idx = text.find("<think>", idx)
            if open_idx == -1:
                result.append(text[idx:])
                break

            if open_idx > idx:
                result.append(text[idx:open_idx])
            idx = open_idx + len("<think>")
            in_think = True

    return "".join(result).strip()


def colorize_response(text: str) -> str:
    """Return the response string with ANSI colors applied to think segments."""
    if not text:
        return ""

    idx = 0
    in_think = False
    output: List[str] = []

    while idx < len(text):
        if in_think:
            close_idx = text.find("</think>", idx)
            if close_idx == -1:
                output.append(f"{YELLOW}{text[idx:]}{RESET}")
                break

            if close_idx > idx:
                output.append(f"{YELLOW}{text[idx:close_idx]}{RESET}")
            output.append(f"{YELLOW}</think>{RESET}")
            idx = close_idx + len("</think>")
            in_think = False
        else:
            open_idx = text.find("<think>", idx)
            if open_idx == -1:
                output.append(f"{ANSWER_COLOR}{text[idx:]}{RESET}")
                break

            if open_idx > idx:
                output.append(f"{ANSWER_COLOR}{text[idx:open_idx]}{RESET}")
            output.append(f"{YELLOW}<think>{RESET}")
            idx = open_idx + len("<think>")
            in_think = True

    return "".join(output)


def print_stream_chunk(text: str, in_think: bool) -> Tuple[bool, str]:
    """Stream a chunk of text with think/final color separation."""
    idx = 0
    final_parts: List[str] = []
    while idx < len(text):
        if in_think:
            close_idx = text.find("</think>", idx)
            if close_idx == -1:
                segment = text[idx:]
                if segment:
                    print(f"{YELLOW}{segment}{RESET}", end="", flush=True)
                idx = len(text)
            else:
                segment = text[idx:close_idx]
                if segment:
                    print(f"{YELLOW}{segment}{RESET}", end="", flush=True)
                print(f"{YELLOW}</think>{RESET}", end="", flush=True)
                idx = close_idx + len("</think>")
                in_think = False
        else:
            open_idx = text.find("<think>", idx)
            if open_idx == -1:
                segment = text[idx:]
                if segment:
                    print(f"{ANSWER_COLOR}{segment}{RESET}", end="", flush=True)
                    final_parts.append(segment)
                idx = len(text)
            else:
                segment = text[idx:open_idx]
                if segment:
                    print(f"{ANSWER_COLOR}{segment}{RESET}", end="", flush=True)
                    final_parts.append(segment)
                print(f"{YELLOW}<think>{RESET}", end="", flush=True)
                idx = open_idx + len("<think>")
                in_think = True
    return in_think, "".join(final_parts)


def call_ollama_batch(api_url: str, model: str, prompt: str, temperature: float) -> Tuple[str, str]:
    """Send a prompt to Ollama API and return response text (batch mode)."""
    try:
        response = requests.post(
            f"{api_url}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "temperature": temperature,
            },
            stream=True,
            timeout=600,
        )
        response.raise_for_status()

        output: List[str] = []
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    output.append(data.get("response", ""))
                except Exception:
                    pass
        raw_text = "".join(output)
        return colorize_response(raw_text), strip_think_segments(raw_text)

    except requests.RequestException as exc:
        error_text = f"[Error contacting Ollama API: {exc}]"
        return error_text, ""


def call_ollama_stream(api_url: str, model: str, prompt: str, temperature: float) -> str:
    """Send a prompt to Ollama API and stream response with color separation."""
    try:
        response = requests.post(
            f"{api_url}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "temperature": temperature,
            },
            stream=True,
            timeout=600,
        )
        response.raise_for_status()

        in_think = False
        final_parts: List[str] = []
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    text = data.get("response", "")
                    if text:
                        in_think, segment = print_stream_chunk(text, in_think)
                        if segment:
                            final_parts.append(segment)

                    if data.get("done", False):
                        break
                except Exception:
                    continue
        print()
        return strip_think_segments("".join(final_parts))

    except requests.RequestException as exc:
        print(f"[Error contacting Ollama API: {exc}]")
        return ""


def read_user_input(prompt_text: str, input_stream: Optional[IO[str]]) -> str:
    """Read a line of input, supporting non-tty streams."""
    if input_stream is None:
        return input(prompt_text)

    print(prompt_text, end="", flush=True)
    line = input_stream.readline()
    if not line:
        raise EOFError
    return line.rstrip("\r\n")


def interactive_mode(
    api_url: str,
    model: str,
    mode: str,
    temperature: float,
    system_prompt: str,
    user_prompt: str,
    memory_lines: int,
    memory_seed: Optional[Sequence[str]] = None,
    input_stream: Optional[IO[str]] = None,
) -> None:
    """Interactive chat mode with selectable output mode."""
    print(f"Interactive mode with model '{model}' at {api_url}")
    print(f"Mode: {mode}, Temperature: {temperature}")
    print("Type 'exit' or Ctrl+C to quit.")
    memory: List[str] = list(memory_seed) if memory_seed else []
    if memory_lines > 0 and memory:
        memory[:] = memory[-memory_lines:]
    local_stream = input_stream
    close_stream = False
    if local_stream is None:
        if sys.stdin.isatty():
            local_stream = None
        else:
            tty_paths = ["CONIN$"] if os.name == "nt" else ["/dev/tty"]
            for path in tty_paths:
                try:
                    local_stream = open(path, "r", encoding="utf-8", errors="ignore")
                    close_stream = True
                    break
                except OSError:
                    local_stream = None
            if local_stream is None and sys.stdin.isatty():
                local_stream = None
            elif local_stream is None:
                local_stream = sys.stdin

    try:
        while True:
            try:
                prompt = read_user_input("You: ", local_stream)
            except EOFError:
                if local_stream is sys.stdin and not sys.stdin.isatty():
                    print("\n[Warning] No interactive input available; exiting.")
                else:
                    print("\nExiting.")
                break
            except KeyboardInterrupt:
                print("\nExiting.")
                break

            user_text = prompt.strip()
            if user_text.lower() in {"exit", "quit"}:
                break
            history_block = ""
            if memory:
                history_block = "History of Past Interaction:\n" + "\n".join(memory)

            current_block = ""
            if user_text:
                current_block = f"Current User Message:\n{user_text}"

            conversation_parts = [part for part in (history_block, current_block) if part]
            conversation_input = "\n\n".join(conversation_parts)
            final_prompt = compose_prompt(system_prompt, user_prompt, conversation_input)
            if not final_prompt:
                continue
            final_text = ""
            if mode == "stream":
                print("LLM (thinking): ", end="", flush=True)
                final_text = call_ollama_stream(api_url, model, final_prompt, temperature)
            else:
                response_text, final_text = call_ollama_batch(api_url, model, final_prompt, temperature)
                print(response_text)

            if memory_lines > 0:
                if user_text:
                    memory.append(f"User: {user_text}")
                if final_text:
                    memory.append(f"Assistant: {final_text.strip()}")
                if len(memory) > memory_lines:
                    memory[:] = memory[-memory_lines:]
    finally:
        if close_stream and local_stream not in {None, sys.stdin}:
            try:
                local_stream.close()
            except OSError:
                pass


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="bsy-clippy: Ollama API Client")
    parser.add_argument("-i", "--ip", default="172.20.0.100", help="Ollama server IP (default: 172.20.0.100)")
    parser.add_argument("-p", "--port", default="11434", help="Ollama server port (default: 11434)")
    parser.add_argument("-M", "--model", default="qwen3:1.7b", help="Model name (default: qwen3:1.7b)")
    parser.add_argument("-m", "--mode", choices=["stream", "batch"], default="stream", help="Output mode: 'stream' = real-time, 'batch' = wait for final output")
    parser.add_argument("-t", "--temperature", type=float, default=0.7, help="Sampling temperature (default: 0.7, higher = more random)")
    parser.add_argument(
        "-s",
        "--system-file",
        default=None,
        help="Path to a system prompt file (default: packaged prompt)",
    )
    parser.add_argument("-u", "--user-prompt", default="", help="Additional user instructions to prepend before the data")
    parser.add_argument("-r", "--memory-lines", type=int, default=0, help="Remember this many lines of conversation in interactive mode")
    parser.add_argument("-c", "--chat-after-stdin", action="store_true", help="After processing stdin, continue in interactive chat mode")
    parser.add_argument("--no-default-system", action="store_true", help="Disable the packaged default system prompt")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    api_url = f"http://{args.ip}:{args.port}"
    allow_default = not args.no_default_system
    system_prompt = load_system_prompt(args.system_file, allow_default=allow_default)
    user_prompt = args.user_prompt
    memory_lines = max(0, args.memory_lines)
    chat_after_stdin = args.chat_after_stdin

    mode = args.mode
    if mode is None:
        if not sys.stdin.isatty():
            mode = "batch"
        else:
            mode = "stream"

    if not sys.stdin.isatty():
        data = sys.stdin.read()
        full_prompt = compose_prompt(system_prompt, user_prompt, data)

        if not full_prompt:
            interactive_mode(api_url, args.model, mode, args.temperature, system_prompt, user_prompt, memory_lines)
            return

        memory_seed: List[str] = []
        data_text = data.strip()
        if data_text:
            memory_seed.append(f"User: {data_text}")

        final_text = ""
        if mode == "stream":
            final_text = call_ollama_stream(api_url, args.model, full_prompt, args.temperature)
        else:
            response_text, final_text = call_ollama_batch(api_url, args.model, full_prompt, args.temperature)
            print(response_text)
        if chat_after_stdin:
            if final_text:
                memory_seed.append(f"Assistant: {final_text.strip()}")
            if memory_lines > 0 and memory_seed:
                memory_seed = memory_seed[-memory_lines:]
            interactive_mode(
                api_url,
                args.model,
                mode,
                args.temperature,
                system_prompt,
                user_prompt,
                memory_lines,
                memory_seed if memory_seed else None,
            )
        return

    interactive_mode(api_url, args.model, mode, args.temperature, system_prompt, user_prompt, memory_lines)
