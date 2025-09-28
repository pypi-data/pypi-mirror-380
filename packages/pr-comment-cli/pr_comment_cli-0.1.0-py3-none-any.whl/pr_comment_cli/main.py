# main.py
import os
import sys
import argparse
import requests
import base64
import hashlib
import json
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple

# 터미널 UI 라이브러리
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich.rule import Rule
from rich.text import Text

# --- 초기 설정 ---
console = Console()

# --- 설정 및 환경 변수 ---
AUTH_PATH = Path.home() / ".prcli_auth.json"
CONFIG_PATH = Path.home() / ".prcli_config.json"
API_ROOT = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
}

def save_token(token: str):
    """사용자 토큰을 JSON 파일에 저장합니다."""
    try:
        AUTH_PATH.write_text(json.dumps({"token": token}))
        console.print(f"[green]✔ GitHub token saved successfully to {AUTH_PATH}[/green]")
    except Exception as e:
        console.print(f"[red]Error saving token: {e}[/red]")
        sys.exit(1)

def load_token() -> Optional[str]:
    """저장된 토큰을 불러옵니다."""
    if not AUTH_PATH.exists():
        return None
    try:
        data = json.loads(AUTH_PATH.read_text())
        return data.get("token")
    except Exception:
        return None

# 전역 GITHUB_TOKEN 변수 설정
GITHUB_TOKEN = load_token()
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"

# 사용자별 색상 (rich 스타일)
USER_COLORS = [
    "cyan", "magenta", "yellow", "green", "blue", "red", "bright_cyan",
    "bright_magenta", "bright_yellow", "bright_green", "bright_blue", "bright_red"
]

def pick_color_for_user(username: str) -> str:
    h = hashlib.md5(username.encode()).digest()
    idx = h[0] % len(USER_COLORS)
    return USER_COLORS[idx]

# --- 설정 관리 함수 ---
def save_config(owner: str, repo: str):
    config = {"owner": owner, "repo": repo}
    try:
        CONFIG_PATH.write_text(json.dumps(config, indent=2))
        console.print(Panel(f"[green]✔ Config saved to {CONFIG_PATH}[/green]\nOwner: {owner}\nRepo:  {repo}", title="Config Saved", expand=False))
    except Exception as e:
        console.print(f"[red]Error saving config: {e}[/red]")

def load_config() -> Optional[Dict[str, str]]:
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text())
        except (json.JSONDecodeError, OSError) as e:
            console.print(f"[yellow]Warning: Could not load config file at {CONFIG_PATH}. Error: {e}[/yellow]")
            return None
    return None

# --- 데이터 클래스 ---
@dataclass
class Comment:
    id: int
    author: str
    body: str
    path: Optional[str]
    line: Optional[int]
    in_reply_to_id: Optional[int]
    created_at: str
    pr_number: int
    type: str  # "review" 또는 "issue"

# --- GitHub API 호출 헬퍼 ---
def gh_request(method: str, path: str, params=None, data=None, exit_on_error: bool = True):
    """API에 단일 요청을 보내고 전체 응답 객체를 반환합니다."""
    url = API_ROOT + path
    try:
        r = requests.request(method, url, headers=HEADERS, params=params, json=data, timeout=10)
        r.raise_for_status()
        return r
    except requests.exceptions.HTTPError as e:
        if exit_on_error:
            if e.response.status_code == 401:
                console.print("[bold red]API Error 401: Unauthorized. Check your GITHUB_TOKEN and its permissions.[/bold red]")
            else:
                console.print(f"[bold red]GitHub API Error {e.response.status_code}:[/bold red] {e.response.text}")
            sys.exit(1)
        return None
    except requests.exceptions.RequestException as e:
        if exit_on_error:
            console.print(f"[bold red]Network Error:[/bold red] {e}")
            sys.exit(1)
        return None

def gh_request_paginated(method: str, path: str, params=None):
    """gh_request를 사용해 페이지네이션을 처리하고 모든 아이템을 리스트로 반환합니다."""
    if params and 'per_page' not in params:
        params['per_page'] = 50
    elif not params:
        params = {'per_page': 50}

    res = gh_request(method, path, params=params)
    if res is None: return [] # 요청 실패 시 빈 리스트 반환
    all_items = res.json()
    
    if isinstance(all_items, dict) and 'items' in all_items:
        all_items = all_items['items']

    while 'next' in res.links.keys():
        next_url = res.links['next']['url']
        console.print(f"[dim]Fetching next page...[/dim]")
        
        try:
            res = requests.request(method, next_url, headers=HEADERS, timeout=10)
            res.raise_for_status()
            
            new_data = res.json()
            if isinstance(new_data, dict) and 'items' in new_data:
                all_items.extend(new_data['items'])
            else:
                 all_items.extend(new_data)
        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Pagination Error:[/bold red] {e}")
            break
            
    return all_items


_my_username = None
def get_my_username():
    """GITHUB_TOKEN을 이용해 현재 사용자의 GitHub 유저명을 가져옵니다 (결과 캐시)."""
    global _my_username
    if _my_username:
        return _my_username
    
    console.print("Fetching your GitHub username from token...")
    res = gh_request("GET", "/user")
    data = res.json()
    _my_username = data.get("login")
    if not _my_username:
        console.print("[bold red]Could not determine your username from GITHUB_TOKEN.[/bold red]")
        sys.exit(1)
    return _my_username

def list_my_prs(owner: str, repo: str, author: str, fetch_all_pages: bool = False):
    """특정 사용자가 작성한 PR 목록을 GitHub 검색 API를 이용해 최신순으로 가져옵니다."""
    console.print(f"Searching for PRs authored by [bold cyan]{author}[/bold cyan]...")
    query = f"is:pr repo:{owner}/{repo} author:{author}"
    params = {"q": query, "sort": "created", "order": "desc", "per_page": 50}
    
    if fetch_all_pages:
        console.print("[dim]Fetching all pages for your PRs...[/dim]")
        prs = gh_request_paginated("GET", "/search/issues", params=params)
    else:
        console.print("[dim]Fetching first page of your PRs... (use '--my-prs all' for all pages)[/dim]")
        res = gh_request("GET", "/search/issues", params=params)
        prs = res.json().get("items", [])
    
    if not prs:
        console.print(f"[yellow]No pull requests found for user '{author}'.[/yellow]")
        return

    table = Table(title=f"Pull Requests by {author} in {owner}/{repo}", show_lines=True)
    table.add_column("PR #", style="bold magenta", justify="right")
    table.add_column("Title", style="white")
    table.add_column("Created At", style="yellow")
    
    for pr in prs:
        table.add_row(
            str(pr['number']),
            pr['title'],
            pr['created_at'].split('T')[0]
        )
    console.print(table)

def get_review_comments(owner: str, repo: str, pr_number: int) -> List[Comment]:
    path = f"/repos/{owner}/{repo}/pulls/{pr_number}/comments"
    items = gh_request_paginated("GET", path)
    return [Comment(
        id=it["id"], author=it["user"]["login"], body=it.get("body", ""),
        path=it.get("path"), line=it.get("line"),
        in_reply_to_id=it.get("in_reply_to_id"), created_at=it.get("created_at"),
        pr_number=pr_number, type="review"
    ) for it in items]

def get_issue_comments(owner: str, repo: str, pr_number: int) -> List[Comment]:
    path = f"/repos/{owner}/{repo}/issues/{pr_number}/comments"
    items = gh_request_paginated("GET", path)
    return [Comment(
        id=it["id"], author=it["user"]["login"], body=it.get("body", ""),
        path=None, line=None, in_reply_to_id=None, created_at=it.get("created_at"),
        pr_number=pr_number, type="issue"
    ) for it in items]

def get_pr_refs(owner: str, repo: str, pr_numbers: List[int]) -> Dict[int, str]:
    mapping = {}
    for pr in pr_numbers:
        try:
            res = gh_request("GET", f"/repos/{owner}/{repo}/pulls/{pr}")
            j = res.json()
            mapping[pr] = j.get("head", {}).get("sha") or j.get("head", {}).get("ref")
        except Exception:
            mapping[pr] = None
    return mapping

def get_pr_changed_files(owner: str, repo: str, pr_number: int) -> set:
    """특정 PR에서 변경된 파일의 경로 목록을 set으로 반환합니다."""
    path = f"/repos/{owner}/{repo}/pulls/{pr_number}/files"
    files_data = gh_request_paginated("GET", path)
    return {file['filename'] for file in files_data}

def get_file_content(owner: str, repo: str, path_in_repo: str, ref: str) -> Optional[str]:
    api_path = f"/repos/{owner}/{repo}/contents/{path_in_repo}"
    try:
        res = gh_request("GET", api_path, params={"ref": ref}, exit_on_error=False)

        if res is None:
            return None

        j = res.json()
        content_b64 = j.get("content")
        if not content_b64 or j.get("encoding") != "base64":
            return None
        return base64.b64decode(content_b64).decode("utf-8", errors="replace")
    except Exception:
        return None

def list_prs(owner: str, repo: str, base: Optional[str], state: str = "open", fetch_all_pages: bool = False):
    path = f"/repos/{owner}/{repo}/pulls"
    params = {"state": state, "per_page": 50, "sort": "created", "direction": "desc"}
    
    title = f"All '{state.capitalize()}' PRs in {owner}/{repo}"
    if base:
        params["base"] = base
        title = f"'{state.capitalize()}' PRs targeting '{base}' in {owner}/{repo}"

    if fetch_all_pages:
        console.print("[dim]Fetching all pages for PRs...[/dim]")
        prs = gh_request_paginated("GET", path, params=params)
    else:
        console.print("[dim]Fetching first page of PRs... (use '--list-prs all' for all pages)[/dim]")
        res = gh_request("GET", path, params=params)
        prs = res.json()

    table = Table(title=title, show_lines=True)
    table.add_column("PR #", style="bold magenta")
    table.add_column("Title", style="white")
    table.add_column("Author", style="cyan")
    table.add_column("Created At", style="yellow")
    for pr in prs:
        table.add_row(str(pr['number']), pr['title'], pr['user']['login'], pr['created_at'].split('T')[0])
    console.print(table)

# --- 데이터 처리 유틸리티 ---
def build_reply_tree(comments: List[Comment]) -> Dict[int, List[Comment]]:
    tree = {}
    for c in comments:
        if pid := c.in_reply_to_id:
            tree.setdefault(pid, []).append(c)
    return tree

def group_comments_by_file(comments: List[Comment]) -> Dict[str, List[Comment]]:
    d = {}
    for c in comments:
        key = c.path if c.path else "__PR_TOP_LEVEL__"
        d.setdefault(key, []).append(c)
    return d

# --- 출력 함수 (rich 사용) ---
def print_comment_block(comment: Comment, color_map: Dict[str, str], indent: int = 0, prefix: str = ""):
    color = color_map.setdefault(comment.author, pick_color_for_user(comment.author))
    
    header_text = Text()
    header_text.append(" " * (indent * 2))
    header_text.append(prefix)
    header_text.append(comment.author, style=f"bold {color}")
    loc = f"{comment.path}:{comment.line}" if comment.path and comment.line else "PR General Comment"
    header_text.append(f" · {loc} · {comment.created_at.split('T')[0]}")
    
    console.print(header_text)
    
    body_panel = Panel(
        Text(comment.body, justify="left"),
        border_style="dim",
        padding=(0, 2),
        expand=False
    )
    console.print(Text(" " * (indent * 2 + 1)), body_panel)

def print_file_section(owner, repo, file_path, comments, pr_ref_map, cache, context_lines):
    console.print(Rule(f"[bold cyan]FILE: {file_path}", style="cyan"))
    
    color_map = {}
    content_lines = None

    if file_path != "__PR_TOP_LEVEL__":
        pr_numbers_to_check = sorted(pr_ref_map.keys(), reverse=True)
        for pr_num in pr_numbers_to_check:
            ref = pr_ref_map.get(pr_num)
            if ref:
                key = (file_path, ref)
                if key not in cache:
                    cache[key] = get_file_content(owner, repo, file_path, ref)
                if content := cache[key]:
                    content_lines = content.splitlines()
                    break
    
    comments_by_line = {}
    for c in comments:
        line_key = c.line if c.line is not None else "__GENERAL__"
        comments_by_line.setdefault(line_key, []).append(c)

    sorted_lines = sorted(comments_by_line.items(), key=lambda item: item[0] if isinstance(item[0], int) else float('inf'))
    
    for line_num, line_comments in sorted_lines:
        if isinstance(line_num, int) and content_lines:
            idx = line_num - 1
            start = max(0, idx - context_lines)
            end = min(len(content_lines), idx + context_lines + 1)
            
            lexer = file_path.split('.')[-1] if '.' in file_path else 'text'
            code_snippet = "\n".join(
                f"{'>' if i == idx else ' '} {i+1:4d} | {line}"
                for i, line in enumerate(content_lines[start:end], start=start)
            )
            console.print(
                Panel(
                    Syntax(code_snippet, lexer, theme="monokai", line_numbers=False),
                    title=f"Context Lines {start+1}-{end}",
                    border_style="green",
                    padding=(1, 2)
                )
            )
        
        reply_tree = build_reply_tree(line_comments)
        processed_ids = set()

        def print_thread_recursive(comment, indent_level, prefix=""):
            if comment.id in processed_ids:
                return
            processed_ids.add(comment.id)
            
            print_comment_block(comment, color_map, indent=indent_level, prefix=prefix)

            for reply in sorted(reply_tree.get(comment.id, []), key=lambda c: c.created_at):
                print_thread_recursive(reply, indent_level + 1, prefix="ㄴ ")

        for c in sorted(line_comments, key=lambda c: c.created_at):
            if not c.in_reply_to_id:
                print_thread_recursive(c, 0)

    if not comments:
        console.print("[yellow]No comments to select.[/yellow]")
        return

# --- 메인 실행 함수 ---
def main():
    parser = argparse.ArgumentParser(description="A CLI tool to review GitHub PR comments.")
    
    # 설정 관리
    parser.add_argument("--auth", type=str, metavar="TOKEN", help="Set and save your GitHub Personal Access Token.")
    parser.add_argument("--set-owner", type=str, help="Set and save the default GitHub owner/org.")
    parser.add_argument("--set-repo", type=str, help="Set and save the default GitHub repository.")
    
    # PR 조회 및 필터링
    parser.add_argument("--pr", type=int, help="The main PR number to inspect.")
    parser.add_argument("--about", type=int, nargs="*", help="Use PRs to identify files for filtering comments on the main PR.")
    parser.add_argument("--my-prs", nargs='?', const='default', default=None,
                        help="List your PRs. Shows 1st page by default. Use '--my-prs all' for all pages.")
    parser.add_argument("--list-prs", nargs='?', const='default', default=None, 
                        help="List PRs. Shows 1st page by default. Use '--list-prs all' to fetch all pages.")
    parser.add_argument("--state", type=str, choices=["open", "closed", "all"], default="open", help="State of the pull requests to list (used with --list-prs).")
    parser.add_argument("--base", type=str, help="Filter by base branch (e.g., develop). Omit to list PRs for all branches.")
    parser.add_argument("--files", type=str, nargs="*", help="Filter comments by file names (keywords).")
    
    # 출력
    parser.add_argument("--context", type=int, default=3, help="Number of context lines to show around a comment.")
    
    args = parser.parse_args()
    
    # 1. 인증 명령어 최우선 처리
    if args.auth:
        save_token(args.auth)
        return

    # 2. 토큰 존재 여부 확인 (인증 명령 제외 모든 경우)
    if not GITHUB_TOKEN:
        console.print("[bold red]ERROR: GitHub token not set.[/bold red]")
        console.print("Please run this command first to set your token:")
        console.print("  pr-comment-cli --auth <YOUR_GITHUB_TOKEN>")
        sys.exit(1)

    # 3. 설정 저장 명령어 처리
    if args.set_owner and args.set_repo:
        save_config(args.set_owner, args.set_repo)
        return
    
    # 4. 실제 기능 실행 전 설정 확인
    config = load_config()

    # 목록 조회 기능 실행
    if args.list_prs is not None or args.my_prs is not None:
        if not config:
            console.print("[bold red]ERROR: Repository config not set.[/bold red]")
            console.print("Please run this command first to set your target repository:")
            console.print("  pr-comment-cli --set-owner <OWNER> --set-repo <REPO>")
            sys.exit(1)
        
        owner, repo = config["owner"], config["repo"]
        console.print(f"Using repository: [bold cyan]{owner}/{repo}[/bold cyan]")
        
        if args.list_prs is not None:
            fetch_all = (args.list_prs == 'all')
            list_prs(owner, repo, args.base, args.state, fetch_all_pages=fetch_all)
        
        if args.my_prs is not None:
            fetch_all = (args.my_prs == 'all')
            my_username = get_my_username()
            list_my_prs(owner, repo, my_username, fetch_all_pages=fetch_all)
        return
    
    # 코멘트 조회 기능 실행
    if args.pr:
        if not config:
            console.print("[bold red]ERROR: Repository config not set.[/bold red]")
            console.print("Please run this command first to set your target repository:")
            console.print("  pr-comment-cli --set-owner <OWNER> --set-repo <REPO>")
            sys.exit(1)

        owner, repo = config["owner"], config["repo"]
        console.print(f"Using repository: [bold cyan]{owner}/{repo}[/bold cyan]")
    
        all_comments = []
        main_pr_num = args.pr
        about_pr_nums = args.about or []
        pr_refs = get_pr_refs(owner, repo, [main_pr_num] + about_pr_nums)

        if about_pr_nums:
            console.print(Rule("[bold yellow]Filtering Mode Activated by --about[/bold yellow]"))
            
            changed_files_from_about = set()
            with console.status("[green]Finding files from --about PRs...[/green]") as status:
                for pr_num in about_pr_nums:
                    status.update(f"Checking files in PR #{pr_num}...")
                    changed_files_from_about.update(get_pr_changed_files(owner, repo, pr_num))
            
            console.print(f"Found [bold cyan]{len(changed_files_from_about)}[/bold cyan] unique files to filter by from PRs: {about_pr_nums}")

            with console.status(f"[green]Fetching comments from main PR #{main_pr_num}...[/green]"):
                main_pr_comments = get_review_comments(owner, repo, main_pr_num) + get_issue_comments(owner, repo, main_pr_num)

            for comment in main_pr_comments:
                if comment.type == "issue" or (comment.path and comment.path in changed_files_from_about):
                    all_comments.append(comment)
            
            console.print(f"Filtered to [bold green]{len(all_comments)}[/bold green] relevant comments in PR #{main_pr_num}.")
        else:
            console.print(f"Fetching all comments from PR: [bold magenta]#{main_pr_num}[/bold magenta]")
            with console.status("[bold green]Collecting comments...[/bold green]"):
                all_comments.extend(get_review_comments(owner, repo, main_pr_num))
                all_comments.extend(get_issue_comments(owner, repo, main_pr_num))

        if not all_comments:
            console.print("[yellow]No comments found.[/yellow]")
            return
            
        console.print(f"Found [bold green]{len(all_comments)}[/bold green] total comments to display.")

        if args.files:
            keywords = [k.lower() for k in args.files]
            filtered_by_keyword = [
                c for c in all_comments
                if (c.type == "issue") or (c.path and any(kw in c.path.lower() for kw in keywords))
            ]
            console.print(f"Filtered down to [bold green]{len(filtered_by_keyword)}[/bold green] comments matching keywords: {keywords}")
            all_comments = filtered_by_keyword

            if not all_comments:
                console.print("[yellow]No comments matched the --files filters.[/yellow]")
                return
        
        grouped_by_file = group_comments_by_file(all_comments)
        file_contents_cache = {}
        
        for file_path, comments in sorted(grouped_by_file.items()):
            print_file_section(owner, repo, file_path, comments, pr_refs, file_contents_cache, args.context)

        console.print(Rule("[bold green]Done!", style="green"))
        return

    parser.print_help()

if __name__ == "__main__":
    main()