import subprocess
from pathlib import Path
from typing import Optional


def get_repo_root() -> Optional[Path]:
    """Return the absolute path to the repository root, or None if not in a repo."""
    try:
        repo_root = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except subprocess.CalledProcessError:
        return None
    return Path(repo_root)


def get_git_dir() -> Optional[Path]:
    """Return the `.git` directory path (absolute) or None if not a repo."""
    try:
        git_dir_s = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except subprocess.CalledProcessError:
        return None

    git_dir = Path(git_dir_s)
    if not git_dir.is_absolute():
        repo_root = get_repo_root()
        if repo_root:
            git_dir = repo_root / git_dir

    return git_dir


def get_staged_diff() -> str:
    """
    Returns the diff of staged changes in the current Git repository.

    Runs the 'git diff --staged --unified=0' command to retrieve the differences
    between the staged changes and the last commit, with zero lines of context.
    Returns:
        str: The output of the git diff command as a string.
    Raises:
        subprocess.CalledProcessError: If the git command fails.
    """
    diff = subprocess.run(
        ["git", "diff", "--staged", "--unified=0"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    return diff


def commit_staged(message: str, edit: bool = False):
    """
    Commits staged changes to the git repository with the provided commit message.

    Args:
        message (str): The commit message to use for the commit.
        edit (bool, optional): If True, edit the commit message in editor.
            Defaults to False.

    Raises:
        subprocess.CalledProcessError: If the git commit command fails.
    """
    args = ["git", "commit", "--cleanup=strip", f"--message={message}"]
    if edit:
        args += ["--edit"]
    subprocess.run(args, check=True)
