# Development Guide

## Contributing to the Strangeworks JupyterLab Theme

### Prerequisites

- Node.js >= 16
- Python >= 3.8
- JupyterLab >= 4.0.0

### Development Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd strangeworks-jupyterlab-theme
   ```

2. **Install dependencies**:
   ```bash
   # Install Node.js dependencies
   npm install

   # Install Python package in development mode
   pip install -e .
   ```

3. **Start development**:
   ```bash
   # Build and watch for changes
   npm run watch

   # In another terminal, start JupyterLab
   jupyter lab
   ```

### Project Structure

```
strangeworks-jupyterlab-theme/
├── src/
│   └── index.ts              # TypeScript extension code
├── style/
│   └── index.css            # Main theme CSS
├── docs/                    # Documentation
├── package.json             # Node.js configuration
├── pyproject.toml          # Python package configuration
├── tsconfig.json           # TypeScript configuration
└── README.md               # Project overview
```

### Key Files

- **`src/index.ts`**: Registers the theme with JupyterLab
- **`style/index.css`**: Contains all theme styles and color definitions
- **`package.json`**: Defines the extension metadata and build scripts
- **`pyproject.toml`**: Python packaging configuration

### Making Changes

#### Modifying Colors

The theme colors are defined as CSS variables in `style/index.css`:

```css
/* Strangeworks Brand Colors */
--jp-content-link-color: #4C90FE;        /* Primary Blue */
--jp-brand-color1: #4C90FE;              /* Primary Blue */
--jp-cell-inprompt-font-color: #4C90FE;  /* Primary Blue */
--jp-accent-color1: #7EE191;             /* Accent Green */
--jp-cell-outprompt-font-color: #7EE191; /* Accent Green */
--jp-editor-cursor-color: #7EE191;       /* Accent Green */
```

#### Modifying Theme Name or Metadata

Edit the theme registration in `src/index.ts`:

```typescript
manager.register({
  name: 'Strangeworks Dark',  // Theme name in UI
  isLight: false,             // Dark theme
  themeScrollbars: true,      // Style scrollbars
  load: () => manager.loadCSS(style),
  unload: () => Promise.resolve(undefined)
});
```

### Build Commands

```bash
# Development build (with source maps)
npm run build:labextension:dev

# Production build (optimized)
npm run build:prod

# Clean build artifacts
npm run clean:all

# Watch mode (rebuild on changes)
npm run watch
```

### Testing Changes

1. **Live reload during development**:
   ```bash
   npm run watch
   # Changes to CSS/TS will trigger rebuilds
   # Refresh JupyterLab browser tab to see changes
   ```

2. **Full rebuild test**:
   ```bash
   npm run build:prod
   jupyter lab build
   jupyter lab
   ```

3. **Package installation test**:
   ```bash
   python -m build
   pip uninstall strangeworks-jupyterlab-theme -y
   pip install dist/strangeworks_jupyterlab_theme-*.whl
   jupyter lab
   ```

### Debugging

#### Extension not loading
```bash
# Check extension status
jupyter labextension list

# Rebuild JupyterLab
jupyter lab build --dev-build=False

# Check browser console for errors
# Open Developer Tools → Console
```

#### Styles not applying
```bash
# Clear JupyterLab cache
jupyter lab clean
jupyter lab build

# Check CSS is loaded in browser DevTools
# Elements → Styles → look for @strangeworks styles
```

#### Build failures
```bash
# Clear all caches
npm run clean:all
rm -rf node_modules
rm -rf dist
rm -rf build

# Fresh install
npm install
python -m build
```

### Release Process

1. **Update version numbers**:
   - `package.json`: `"version": "0.1.1"`
   - `pyproject.toml`: `version = "0.1.1"`

2. **Test thoroughly**:
   ```bash
   npm run build:prod
   python -m build
   pip install dist/*.whl
   jupyter lab
   ```

3. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

4. **Create git tag**:
   ```bash
   git tag v0.1.1
   git push origin v0.1.1
   ```

### CSS Architecture

The theme extends JupyterLab's CSS variable system:

```css
/* Override JupyterLab variables */
:root {
  --jp-layout-color0: #2f3a50;      /* Background */
  --jp-ui-font-color0: rgb(245, 249, 255);  /* Text */
  --jp-brand-color1: #4C90FE;       /* Strangeworks Blue */
  --jp-accent-color1: #7EE191;      /* Strangeworks Green */
}

/* Specific component overrides */
.jp-Cell-inputArea .jp-InputArea-prompt {
  color: var(--jp-brand-color1);
}
```

### Browser Compatibility

The theme is tested on:
- Chrome/Chromium 90+
- Firefox 90+
- Safari 14+
- Edge 90+

### Performance Considerations

- CSS uses efficient selectors
- No JavaScript runtime overhead
- Minimal additional CSS payload (~50KB)

### Getting Help

- Check existing GitHub issues
- Review JupyterLab extension documentation
- Test changes in isolation before submitting PRs