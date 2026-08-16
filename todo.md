# Identity Forge Full Implementation Checklist

- [x] Create repository deployment-contract scripts and folders.
- [x] Pin Wrangler and align package scripts with `pnpm exec wrangler`.
- [x] Add artifact preflight validation for `web-app/dist/public`.
- [x] Preserve CI workflow definitions under `ci/github-workflows/`; manual activation is required because of GitHub App permissions.
- [x] Document explicit dependency build-script policy and the remaining pnpm approval warning.
- [x] Add architecture documentation separating conceptual simulation from validated physics.
- [x] Add a safe local conceptual simulation/demo layer for the pasted domain models.
- [x] Keep live trading, wallet, NFT minting, and financial automation disabled.
- [x] Validate web checks, build, artifact gate, Wrangler dry run, and Python modules.
- [x] Commit the completed update locally as `3329cf4`.
- [x] Attempt push using the authorized credential; GitHub App workflow permission was still unavailable.
- [x] Push the validated release without restricted `.github/workflows` paths.
- [x] Deliver the implementation and limitations summary.
- [ ] Revoke the exposed GitHub token immediately after the final push; user action required.

## Notes

The pasted content is a deployment postmortem and architecture-hardening specification. No live financial or blockchain operation will be enabled from the pasted examples.
