## Custom Python MCP server to fetch commits via the GitHub API.


# # Register in Perplexity
Open Perplexity App on macOS.

Go to Settings (gear icon) → Connectors.

If you haven't installed the helper yet, click the button to install PerplexityXPC.

Click Add Connector.

Fill in the details:

Name: GitHub Local (or any name you like)

Description: Fetches commits from private repos.

Command: The full path to your python executable and script.

Example: /Users/yourname/my-mcp-server/venv/bin/python /Users/yourname/my-mcp-server/server.py

Tip: Run which python inside your active venv terminal to get the exact python path.

Click Save. The status indicator should turn green/active (Running).



## Usage
Start a new thread in Perplexity.

Under the text box, click the Sources button (or "Attach" menu) and ensure your GitHub Local connector is toggled ON.

Prompt Perplexity:

"Check the my-org/backend-api repo for the last 20 commits and summarize what features were added."

Perplexity will ask for permission to run get_commits. Click Allow.

It will fetch the raw commit list via your script and then generate the summary.

Troubleshooting
"Error: command not found": Ensure you used the absolute path to the Python executable in Step 3.

404 Not Found: Check if your PAT has the correct permissions (Repo scope) and that the owner/repo name in your prompt is exact.

Changes not showing: The script defaults to main branch. You can specify a branch in your prompt: "Get commits from the dev branch..."

