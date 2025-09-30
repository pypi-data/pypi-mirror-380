import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';

/**
 * Initialization data for the @strangeworks/jupyterlab-theme extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: '@strangeworks/jupyterlab-theme:plugin',
  description: 'Strangeworks dark theme for JupyterLab',
  autoStart: true,
  requires: [IThemeManager],
  activate: (app: JupyterFrontEnd, manager: IThemeManager) => {
    console.log('JupyterLab extension @strangeworks/jupyterlab-theme is activated!');
    const style = '@strangeworks/jupyterlab-theme/index.css';

    manager.register({
      name: 'Strangeworks Dark',
      isLight: false,
      themeScrollbars: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  }
};

export default plugin;