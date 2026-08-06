#!/usr/bin/env python3
"""
Demo script to create a GitHub Pull Request (PR) from an AI assistant (AIO).
Requires a GitHub personal access token (PAT) and repository details.
"""

import os
import sys
import json
import requests

def create_pr(token, repo, head_branch, base_branch="main", title="Demo PR", body=""):
    """
    Create a pull request on GitHub.
    :param token: GitHub personal access token
    :param repo: Repository in format "owner/repo"
    :param head_branch: Source branch name
    :param base_branch: Target branch name (default: main)
    :param title: PR title
    :param body: PR description
    :return: Response JSON or raises exception
    """
    url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    payload = {
        "title": title,
        "head": head_branch,
        "base": base_branch,
        "body": body,
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Environment variables
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    if not token or not repo:
        print("Error: Set GITHUB_TOKEN and GITHUB_REPOSITORY environment variables.")
        sys.exit(1)

    # Command line arguments
    if len(sys.argv) < 2:
        print("Usage: python demo_pr.py <head_branch> [title] [body]")
        sys.exit(1)

    head_branch = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else "Demo PR from AIO"
    body = sys.argv[3] if len(sys.argv) > 3 else ""

    try:
        pr = create_pr(token, repo, head_branch, title=title, body=body)
        print(f"PR created: {pr['html_url']}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to create PR: {e}")
        sys.exit(1)
