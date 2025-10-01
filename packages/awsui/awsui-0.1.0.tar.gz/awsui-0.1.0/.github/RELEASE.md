# Release Process

This document describes how to release a new version of awsui to PyPI using GitHub Actions.

## Prerequisites

1. **PyPI Account**: You must have a PyPI account at https://pypi.org
2. **API Token**: Generate an API token at https://pypi.org/manage/account/token/
3. **GitHub Secret**: Add the token to GitHub repository secrets

## Setup (One-time)

### 1. Create PyPI API Token

1. Log in to https://pypi.org
2. Go to https://pypi.org/manage/account/token/
3. Click "Add API token"
4. Set token name: `awsui-github-actions`
5. Scope: "Entire account" (or specific to awsui after first release)
6. Copy the token (starts with `pypi-`)

### 2. Add GitHub Secret

1. Go to your GitHub repository
2. Navigate to: **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Name: `PYPI_API_TOKEN`
5. Value: Paste your PyPI token
6. Click **"Add secret"**

## Release Process

### Option 1: Automatic Release (Recommended)

1. **Update version in `pyproject.toml`**
   ```toml
   [project]
   version = "0.1.1"  # Increment version
   ```

2. **Commit and push changes**
   ```bash
   git add pyproject.toml
   git commit -m "chore: bump version to 0.1.1"
   git push origin main
   ```

3. **Create and push a git tag**
   ```bash
   git tag -a v0.1.1 -m "Release v0.1.1"
   git push origin v0.1.1
   ```

4. **GitHub Actions will automatically:**
   - Run tests
   - Build the package
   - Publish to PyPI
   - Create a GitHub Release with release notes

5. **Monitor the workflow**
   - Go to: **Actions** tab in your repository
   - Watch the "Publish to PyPI" workflow
   - Check for any errors

### Option 2: Manual Trigger

1. Go to **Actions** tab
2. Select **"Publish to PyPI"** workflow
3. Click **"Run workflow"**
4. Enter the tag (e.g., `v0.1.1`)
5. Click **"Run workflow"**

## Version Naming Convention

- Format: `vMAJOR.MINOR.PATCH` (e.g., `v0.1.0`, `v1.0.0`)
- Follow [Semantic Versioning](https://semver.org/):
  - **MAJOR**: Breaking changes
  - **MINOR**: New features (backward compatible)
  - **PATCH**: Bug fixes (backward compatible)

## What Happens During Release

The GitHub Actions workflow will:

1. ✅ Extract version from git tag
2. ✅ Verify version matches `pyproject.toml`
3. ✅ Build wheel and source distribution
4. ✅ Validate built packages with `twine check`
5. ✅ Test wheel installation
6. ✅ Publish to PyPI
7. ✅ Create GitHub Release with auto-generated notes
8. ✅ Upload build artifacts

## Verify Release

After the workflow completes:

1. **Check PyPI**: Visit https://pypi.org/project/awsui/
2. **Test installation**:
   ```bash
   # Install from PyPI
   uv tool install awsui

   # Verify version
   awsui --version
   ```

3. **Check GitHub Release**: Visit https://github.com/junminhong/awsui/releases

## Troubleshooting

### Version Mismatch Error

If you see: "Error: Version mismatch!"

**Solution**: Make sure the version in `pyproject.toml` matches the git tag:
- Tag: `v0.1.1` → Version in pyproject.toml: `0.1.1`

### PyPI Token Invalid

If you see: "Error: Invalid credentials"

**Solution**:
1. Generate a new token at https://pypi.org/manage/account/token/
2. Update GitHub secret `PYPI_API_TOKEN`

### Package Already Exists

If you see: "Error: File already exists"

**Solution**:
- PyPI doesn't allow re-uploading the same version
- Increment the version number and create a new tag

### Workflow Not Triggering

**Check:**
1. Tag format: Must start with `v` (e.g., `v0.1.0`)
2. Tag pushed: `git push origin v0.1.0`
3. Workflow file: `.github/workflows/publish.yml` exists in main branch

## Rolling Back a Release

If you need to remove a version from PyPI:

1. Go to https://pypi.org/manage/project/awsui/releases/
2. Select the version
3. Click "Options" → "Yank release"
4. Note: You cannot delete a release, only "yank" it

## Future: Trusted Publishing (Recommended)

After your first release, consider upgrading to Trusted Publishing (no token needed):

1. Go to PyPI project settings: https://pypi.org/manage/project/awsui/settings/publishing/
2. Add a new publisher:
   - **Owner**: junminhong
   - **Repository**: awsui
   - **Workflow**: publish.yml
   - **Environment**: (leave empty or `release`)
3. Update `.github/workflows/publish.yml`:
   - Remove `UV_PUBLISH_TOKEN`
   - Keep `id-token: write` permission
4. Delete `PYPI_API_TOKEN` from GitHub secrets

## References

- [uv documentation](https://docs.astral.sh/uv/)
- [PyPI Help](https://pypi.org/help/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Actions](https://docs.github.com/en/actions)
