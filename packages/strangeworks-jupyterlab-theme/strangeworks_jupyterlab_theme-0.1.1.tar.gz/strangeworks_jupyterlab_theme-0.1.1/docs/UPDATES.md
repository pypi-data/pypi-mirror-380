# Updating the Strangeworks JupyterLab Theme

## For End Users

### Update to Latest Version

```bash
pip install --upgrade strangeworks-jupyterlab-theme
```

### Check Current Version

```bash
pip show strangeworks-jupyterlab-theme
```

### Force Reinstall

If you encounter issues, force a clean reinstall:

```bash
pip uninstall strangeworks-jupyterlab-theme -y
pip install strangeworks-jupyterlab-theme
```

After updating, restart JupyterLab for changes to take effect.

## For Developers/Maintainers

### Making Updates to the Theme

1. **Make your changes** to the theme files:
   - CSS: `style/index.css`
   - TypeScript: `src/index.ts`
   - Configuration: `package.json`, `pyproject.toml`

2. **Update version number** in both:
   - `package.json` (line 3): `"version": "0.1.1"`
   - `pyproject.toml` (line 7): `version = "0.1.1"`

3. **Test your changes locally**:
   ```bash
   # Install in development mode
   pip install -e .

   # Start JupyterLab and test
   jupyter lab
   ```

4. **Build the updated package**:
   ```bash
   # Clean previous builds
   rm -rf dist/ build/

   # Build new distribution
   python -m build
   ```

5. **Upload to PyPI**:
   ```bash
   # Upload to TestPyPI first (optional)
   twine upload --repository testpypi dist/*

   # Test install from TestPyPI
   pip install --index-url https://test.pypi.org/simple/ strangeworks-jupyterlab-theme

   # Upload to production PyPI
   twine upload dist/*
   ```

### Version History

- **v0.1.0**: Initial release with Strangeworks brand colors
  - Blue accent (`#4C90FE`) for primary elements
  - Green accent (`#7EE191`) for secondary elements
  - Based on Darkside theme foundation

### Development Workflow

```bash
# 1. Create development environment
git clone <repo-url>
cd strangeworks-jupyterlab-theme
npm install
pip install -e .

# 2. Make changes to theme files
# Edit style/index.css, src/index.ts, etc.

# 3. Build and test
npm run build:labextension:dev
jupyter lab

# 4. When ready to release
# Update version numbers
npm run build:prod
python -m build
twine upload dist/*
```

### Color Customization

The theme uses these primary Strangeworks colors:

```css
/* Primary Blue - Used for links, brand elements */
--jp-content-link-color: #4C90FE;
--jp-brand-color1: #4C90FE;
--jp-cell-inprompt-font-color: #4C90FE;

/* Accent Green - Used for outputs, highlights */
--jp-accent-color1: #7EE191;
--jp-cell-outprompt-font-color: #7EE191;
--jp-editor-cursor-color: #7EE191;
```

To modify colors, edit these variables in `style/index.css`.

### Troubleshooting Development

**Build Issues:**
```bash
# Clear all caches and rebuild
npm run clean:all
yarn install
npm run build:prod
```

**Extension Not Loading:**
```bash
# Check extension is properly installed
jupyter labextension list

# Rebuild JupyterLab
jupyter lab build --dev-build=False --minimize=False
```

**Version Conflicts:**
```bash
# Uninstall all versions
pip uninstall strangeworks-jupyterlab-theme -y
jupyter labextension uninstall @strangeworks/jupyterlab-theme

# Clean install
pip install -e .
```