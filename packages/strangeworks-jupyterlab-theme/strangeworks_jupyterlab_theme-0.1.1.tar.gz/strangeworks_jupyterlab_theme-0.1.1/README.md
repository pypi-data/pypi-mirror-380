# Strangeworks JupyterLab Theme

A dark theme for JupyterLab featuring Strangeworks brand colors.

## Features

- Dark theme optimized for JupyterLab
- Strangeworks brand colors (blue and green accent colors)
- Improved code editor styling with syntax highlighting
- Custom cell styling and collapsers
- Enhanced UI elements and toolbars

## Installation

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```bash
# Clone the repo to your local environment
# Change directory to the strangeworks-jupyterlab-theme directory
# Install package in development mode
pip install -e "."
# Link your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite
# Rebuild extension Typescript source after making changes
jlpm build
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm watch
# Run JupyterLab in another terminal
jupyter lab
```

### Uninstall

```bash
pip uninstall strangeworks_jupyterlab_theme
```

## Theme Colors

The theme uses the Strangeworks brand palette:

- **Primary Blue**: #4C90FE (for accents and active elements)
- **Accent Green**: #7EE191 (for success states and output prompts)
- **Dark Backgrounds**: Various shades of dark blue/gray for panels and editors

## Contributing

### Development setup

See CONTRIBUTING.md for how to set up a local development environment.

## License

This project is licensed under the BSD-3-Clause License.