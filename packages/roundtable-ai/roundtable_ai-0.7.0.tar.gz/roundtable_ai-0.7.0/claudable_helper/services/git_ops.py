import subprocess
from typing import List, Optional
import os


def _run(cmd: list[str], cwd: str) -> str:
    res = subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)
    return res.stdout.strip()


def list_commits(repo_path: str, limit: int = 50) -> list[dict]:
    fmt = "%H%x01%P%x01%an%x01%ad%x01%s"
    out = _run(["git", "log", f"-n{limit}", f"--pretty=format:{fmt}", "--date=iso"], cwd=repo_path)
    commits: list[dict] = []
    if not out:
        return commits
    for line in out.splitlines():
        sha, parents, author, date, subject = line.split("\x01")
        commits.append({
            "commit_sha": sha,
            "parent_sha": parents.split()[0] if parents else None,
            "author": author,
            "date": date,
            "message": subject,
        })
    return commits


def show_diff(repo_path: str, commit_sha: str) -> str:
    return _run(["git", "show", "--format=", commit_sha], cwd=repo_path)


def current_head(repo_path: str) -> str:
    return _run(["git", "rev-parse", "HEAD"], cwd=repo_path)


# Legacy function for backward compatibility
def commit_all_legacy(repo_path: str, message: str) -> str:
    _run(["git", "add", "-A"], cwd=repo_path)
    _run(["git", "commit", "-m", message], cwd=repo_path)
    return current_head(repo_path)


def hard_reset(repo_path: str, commit_sha: str) -> None:
    _run(["git", "reset", "--hard", commit_sha], cwd=repo_path)


def add_remote(repo_path: str, remote_name: str, remote_url: str) -> None:
    """Add a remote repository"""
    try:
        # Check if remote already exists
        existing_url = _run(["git", "remote", "get-url", remote_name], cwd=repo_path)
        
        # Compare URLs without authentication credentials for proper comparison
        def normalize_url(url):
            # Remove credentials from URL for comparison
            import re
            return re.sub(r'https://[^@]+@github.com/', 'https://github.com/', url)
        
        if normalize_url(existing_url) != normalize_url(remote_url):
            # Different repository - remove existing remote and add new one
            _run(["git", "remote", "remove", remote_name], cwd=repo_path)
            _run(["git", "remote", "add", remote_name, remote_url], cwd=repo_path)
            
            # Unset any existing upstream to avoid conflicts
            try:
                _run(["git", "branch", "--unset-upstream"], cwd=repo_path)
            except subprocess.CalledProcessError:
                pass  # No upstream set, that's fine
        else:
            # Same repository but potentially different credentials - update URL
            _run(["git", "remote", "set-url", remote_name, remote_url], cwd=repo_path)
    except subprocess.CalledProcessError:
        # Remote doesn't exist, add it
        _run(["git", "remote", "add", remote_name, remote_url], cwd=repo_path)


def push_to_remote(repo_path: str, remote_name: str = "origin", branch: str = "main") -> dict:
    """Push to remote repository"""
    try:
        # First try normal push with upstream
        try:
            result = _run(["git", "push", "-u", remote_name, branch], cwd=repo_path)
        except subprocess.CalledProcessError:
            # If push fails (e.g., different histories), try force push
            # This is safe for initial connection to a new empty repo
            result = _run(["git", "push", "-u", "--force", remote_name, branch], cwd=repo_path)
            
        return {
            "success": True,
            "output": result,
            "remote": remote_name,
            "branch": branch
        }
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": e.stderr if e.stderr else str(e),
            "remote": remote_name,
            "branch": branch
        }


def get_remote_url(repo_path: str, remote_name: str = "origin") -> str:
    """Get remote URL"""
    try:
        return _run(["git", "remote", "get-url", remote_name], cwd=repo_path)
    except subprocess.CalledProcessError:
        return ""


def get_current_branch(repo_path: str) -> str:
    """Get current branch name"""
    try:
        return _run(["git", "branch", "--show-current"], cwd=repo_path)
    except subprocess.CalledProcessError:
        return "main"  # fallback to main


def set_git_config(repo_path: str, name: str, email: str) -> None:
    """Set git config for the repository"""
    # Set local repository config (not global)
    _run(["git", "config", "--local", "user.name", name], cwd=repo_path)
    _run(["git", "config", "--local", "user.email", email], cwd=repo_path)


def initialize_main_branch(repo_path: str) -> None:
    """Initialize main branch if not exists"""
    try:
        # Check if we have any commits
        _run(["git", "rev-parse", "HEAD"], cwd=repo_path)
    except subprocess.CalledProcessError:
        # No commits yet, create initial commit
        _run(["git", "add", "."], cwd=repo_path)
        try:
            _run(["git", "commit", "-m", "Initial commit"], cwd=repo_path)
        except subprocess.CalledProcessError:
            # Nothing to commit, create empty commit
            _run(["git", "commit", "--allow-empty", "-m", "Initial commit"], cwd=repo_path)
    
    # Ensure we're on main branch
    try:
        current_branch = get_current_branch(repo_path)
        if current_branch != "main":
            try:
                _run(["git", "branch", "-M", "main"], cwd=repo_path)
            except subprocess.CalledProcessError:
                # Branch rename failed, checkout main
                try:
                    _run(["git", "checkout", "-b", "main"], cwd=repo_path)
                except subprocess.CalledProcessError:
                    pass  # Already on main or other issue
    except subprocess.CalledProcessError:
        pass


def commit_all(repo_path: str, message: str) -> dict:
    """Stage all changes and commit, return commit info"""
    try:
        _run(["git", "add", "-A"], cwd=repo_path)
        _run(["git", "commit", "-m", message], cwd=repo_path)
        commit_sha = current_head(repo_path)
        return {
            "success": True,
            "commit_hash": commit_sha,
            "message": message
        }
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": str(e),
            "message": message
        }
