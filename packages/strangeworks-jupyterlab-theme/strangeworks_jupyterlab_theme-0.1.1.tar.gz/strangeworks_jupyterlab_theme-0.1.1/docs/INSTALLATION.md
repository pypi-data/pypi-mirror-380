# Installation Guide

## Installing the Strangeworks JupyterLab Theme

### Method 1: Install from PyPI (Recommended)

```bash
pip install strangeworks-jupyterlab-theme
```

### Method 2: Install from Wheel File

If you have the wheel file locally:

```bash
pip install path/to/strangeworks_jupyterlab_theme-0.1.0-py3-none-any.whl
```

### Method 3: Install from Source (Development)

```bash
git clone <repository-url>
cd strangeworks-jupyterlab-theme
pip install -e .
```

## Verification

After installation, verify the theme is available:

```bash
# Check Python package
pip list | grep strangeworks

# Check JupyterLab extension
jupyter labextension list | grep strangeworks
```

You should see:
- `strangeworks_jupyterlab_theme` in pip list
- `@strangeworks/jupyterlab-theme` as enabled in JupyterLab extensions

## Activating the Theme

1. Start JupyterLab:
   ```bash
   jupyter lab
   ```

2. Navigate to **Settings > Theme**

3. Select **"Strangeworks Dark"** from the theme list

4. The theme will be applied immediately

## Requirements

- Python >= 3.8
- JupyterLab >= 4.0.0

## Troubleshooting

### Theme Not Appearing in Settings

If "Strangeworks Dark" doesn't appear in Settings > Theme:

1. Verify installation:
   ```bash
   jupyter labextension list
   ```

2. Rebuild JupyterLab:
   ```bash
   jupyter lab build
   ```

3. Restart JupyterLab

### Extension Conflicts

If you experience conflicts with other themes:

1. List all installed themes:
   ```bash
   jupyter labextension list | grep theme
   ```

2. Disable conflicting themes if needed:
   ```bash
   jupyter labextension disable theme-name
   ```

### Cache Issues

Clear JupyterLab cache if theme changes don't appear:

```bash
jupyter lab clean
jupyter lab build
```