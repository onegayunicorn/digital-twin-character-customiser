# Identity Forge Full Implementation Checklist

- [ ] Create repository deployment-contract scripts and folders.
- [ ] Pin Wrangler and align package scripts with `pnpm exec wrangler`.
- [ ] Add artifact preflight validation for `web-app/dist/public`.
- [ ] Add CI workflow for install, typecheck, tests, build, preflight, and dry run.
- [ ] Add explicit dependency build-script policy documentation.
- [ ] Add architecture documentation separating conceptual simulation from validated physics.
- [ ] Add a safe browser-only conceptual simulation/demo layer for the pasted domain models.
- [ ] Keep live trading, wallet, NFT minting, and financial automation disabled.
- [ ] Validate all repository workflows and Python modules.
- [x] Commit the completed update locally as `3329cf4`.
- [x] Attempt push using the authorized credential; GitHub App workflow permission was still unavailable.
- [ ] Push the validated release without restricted `.github/workflows` paths.
- [ ] Deliver the implementation and limitations summary.
- [ ] Revoke the exposed GitHub token immediately after the final push.

## Notes

The pasted content is a deployment postmortem and architecture-hardening specification. No live financial or blockchain operation will be enabled from the pasted examples.
