from fastmcp import FastMCP
import httpx
import os

# Initialize the MCP server
mcp = FastMCP("My GitHub Tool")

# HARDCODE TOKEN FOR QUICK SETUP (or use os.getenv("GITHUB_TOKEN"))
GITHUB_TOKEN = "your_github_token_here"

@mcp.tool()
def get_commits(owner: str, repo: str, limit: int = 10, branch: str = "main") -> str:
    """
    Fetches the latest commit history for a GitHub repository.
    Useful for summarizing changes, finding bugs, or writing release notes.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {"per_page": limit, "sha": branch}

    try:
        response = httpx.get(url, headers=headers, params=params, timeout=10.0)
        response.raise_for_status()
        
        commits = response.json()
        result = []
        for c in commits:
            sha = c.get("sha", "")[:7]
            msg = c.get("commit", {}).get("message", "").split("\n")[0]
            date = c.get("commit", {}).get("author", {}).get("date", "")
            author = c.get("commit", {}).get("author", {}).get("name", "")
            result.append(f"[{date}] {sha} - {msg} ({author})")
            
        return "\n".join(result)
    except Exception as e:
        return f"Error fetching commits: {str(e)}"

if __name__ == "__main__":
    # This starts the server over stdio, which Perplexity connects to
    mcp.run()
