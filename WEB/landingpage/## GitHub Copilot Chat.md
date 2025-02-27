## GitHub Copilot Chat

- Extension Version: 0.24.1 (prod)
- VS Code: vscode/1.97.2
- OS: Windows

## Network

User Settings:
```json
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: 20.87.245.6 (5166 ms)
- DNS ipv6 Lookup: timed out after 10 seconds
- Proxy URL: None (6 ms)
- Electron fetch (configured): HTTP 200 (3948 ms)
- Node.js https: HTTP 200 (4670 ms)
- Node.js fetch: HTTP 200 (7664 ms)
- Helix fetch: HTTP 200 (4291 ms)

Connecting to https://api.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 140.82.112.22 (9935 ms)
- DNS ipv6 Lookup: Error (6809 ms): getaddrinfo ENOTFOUND api.individual.githubcopilot.com
- Proxy URL: None (9 ms)
- Electron fetch (configured): HTTP 200 (3171 ms)
- Node.js https: timed out after 10 seconds
- Node.js fetch: timed out after 10 seconds
- Helix fetch: HTTP 200 (7961 ms)

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).