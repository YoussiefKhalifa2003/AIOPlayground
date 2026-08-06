#!/usr/bin/env python3
import os
from github import Github

def create_pr(token: str, repo_owner: str, repo_name: str,
              branch: str, title: str, body: str):
    """Create a PR from *branch* into the repo's default branch."""
    g = Github(token)
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    # Create the pull request
    pr = repo.create_pull(title=title, body=body, head=branch,
                          base=repo.default_branch)
    print(f"Created PR #{pr.number}: {pr.html_url}")

if __name__ == "__main__":
    token = os.getenv("GITHUB_TOKEN")
    repo_owner = os.getenv("REPO_OWNER")
    repo_name = os.getenv("REPO_NAME")
    branch = os.getenv("BRANCH")
    title = os.getenv("PR_TITLE", "Demo PR")
    body = os.getenv("PR_BODY", "This is a demo PR created by the script.")

    if not all([token, repo_owner, repo_name, branch]):
        raise ValueError(
            "Missing required environment variables: "
            "GITHUB_TOKEN, REPO_OWNER, REPO_NAME, BRANCH"
        )

    create_pr(token, repo_owner, repo_name, branch, title, body)
