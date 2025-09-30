# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

# %%


class Colors(object):

    def __init__(self):

        self.colors = {'blues': ['#003778', '#006EB7', '#A3CCEE', '#DFEAF8'],
                       'greens': ['#125428', '#1D893A', '#B5D8AF', '#E1EFE3'],
                       'reds': ['#7B282E', '#C14246', '#F7BCBB', '#FCE4E0'],
                       'yellows': ['#6D4104', '#F7A823', '#FDD5A5', '#FEEBDA'],
                       'browns': ['#4A372C', '#7D604B', '#D4C1B2', '#F1E9E4'],
                       'purples': ['#53234e', '#82387B', '#DBBFDD', '#F2E1F0']
                       }

        self.palettes = {'dark': [self.colors[key][0] for key in self.colors.keys()],
                         'normal': [self.colors[key][1] for key in self.colors.keys()],
                         'pastel': [self.colors[key][2] for key in self.colors.keys()],
                         'light': [self.colors[key][3] for key in self.colors.keys()],

                         'pair1': [val for sublist in [v[:2] for v in self.colors.values()] for val in sublist],
                         'triple1': [val for sublist in [v[:3] for v in self.colors.values()] for val in sublist],
                         'seq': [val for sublist in [v[:4] for v in self.colors.values()] for val in sublist],

                         'pair2': [val for sublist in [v[1:3] for v in self.colors.values()] for val in sublist],
                         'triple2': [val for sublist in [v[1:4] for v in self.colors.values()] for val in sublist],

                         'pair3': [val for sublist in [v[2:4] for v in self.colors.values()] for val in sublist],
                         }

        self.colormaps = {'BlWh': mcolors.LinearSegmentedColormap.from_list('BlWh',
                                                                            [self.colors['blues'][1],
                                                                             '#FFFFFF'],
                                                                            N=256),
                          'GrWh': mcolors.LinearSegmentedColormap.from_list('GrWh',
                                                                            [self.colors['greens'][1],
                                                                             '#FFFFFF'],
                                                                            N=256),
                          'BlGr': mcolors.LinearSegmentedColormap.from_list('BlGr',
                                                                            [self.colors['blues'][1],
                                                                             '#FFFFFF',
                                                                             self.colors['greens'][1]],
                                                                            N=256),
                          'BlRe': mcolors.LinearSegmentedColormap.from_list('BlRe',
                                                                            [self.colors['blues'][1],
                                                                             '#FFFFFF',
                                                                             self.colors['reds'][1]],
                                                                            N=256)}

    def palette_get(self, palette='normal'):
        if palette in self.colors.keys():
            pal = self.colors[palette]
        elif palette in self.palettes.keys():
            pal = self.palettes[palette]
        else:
            raise ValueError(f'Palette {palette} not valid found. Valid palettes are {self.palettes.keys()}')
        return pal

    def cmap_get(self, cmap='BlGr', plot=False):
        if cmap in self.colormaps.keys():
            cmap_obj = self.colormaps[cmap]
            if plot is True:
                self._plot(cmap_obj, label=cmap)
            return cmap_obj
        else:
            raise ValueError('Colormap not found. Valid colormaps are {self.colormaps.keys()}')

    def cmap_create(self, c_lst, n_colors=256, plot=True):
        """
        Create a custom colormap from a sequence of colors.

        This function generates a colormap using the provided colors. The colormap will be a linear interpolation
        between the given colors. You can specify the number of colors (steps) in the colormap with the `n_colors`
        parameter.

        Parameters
        ----------
        *colors : str or list of str
            A sequence of color names or color codes (e.g., 'red', '#FF5733') to define the colormap.
            Colors can be passed as separate arguments (e.g., 'red', 'yellow', 'green') or as a list.
        n_colors : int, optional
            The number of color steps in the resulting colormap. Default is 256.

        Returns
        -------
        cmap : matplotlib.colors.LinearSegmentedColormap
            A colormap object that can be used in Matplotlib plots.

        Raises
        ------
        ValueError
            If fewer than two colors are provided or if `n_colors` is not a positive integer.

        Example
        -------
        ```python
        cmap = cmap_create('red', 'yellow', 'green')
        plt.imshow(data, cmap=cmap)

        cmap = cmap_create(['blue', 'purple', 'pink'])  # Also works
        ```
        """
        # if len(c) == 1 and isinstance(c[0], list):
        #     c = c[0]  # Unpack list if passed as a single argument

        # if len(c) < 2:
        #     raise ValueError("At least two colors must be provided to create a colormap.")

        # if not isinstance(n_colors, int) or n_colors <= 0:
        #     raise ValueError("n_colors must be a positive integer.")

        cmap = mcolors.LinearSegmentedColormap.from_list('custom_cmap', c_lst, N=n_colors)
        if plot is True:
            self._plot(cmap, 'My colormap')
        return cmap

    def _plot(self, palette, label):
        """
        Plot a horizontal color bar using the specified color palette.

        This function creates a small horizontal color bar using the given
        color palette (`palette`) and labels it with the provided `label`.

        Parameters
        ----------
        palette : matplotlib.colors.Colormap
            The colormap to be used for the color bar.
        label : str
            The title of the color bar.

        Returns
        -------
        None
            This function does not return a value but displays the plot.

        Example
        -------
        ```python
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm

        my_palette = cm.get_cmap("viridis")
        obj = MyClass()
        obj._plot(my_palette, "Color Scale")
        ```
        """
        fig, ax = plt.subplots(figsize=(4, 0.5))
        plt.colorbar(
            mpl.cm.ScalarMappable(cmap=palette),
            cax=ax,
            orientation='horizontal',
        )
        plt.title(f'{label}')
        ax.set_xticks([]),
        ax.set_xticklabels([])
        plt.show()
        return

    def palette_show(self, palette='all'):
        if palette != 'all' and palette not in self.colors.keys() and palette not in self.palettes.keys():
            raise NameError('Palette does not exist!')

        elif palette in self.colors.keys():
            cmap = mcolors.ListedColormap(self.colors[palette])
            self._plot(cmap, label=palette)

        elif palette in self.palettes.keys():
            cmap = mcolors.ListedColormap(self.palettes[palette])
            self._plot(cmap, label=palette)

        elif palette == 'all':
            for palette in self.colors.keys():
                cmap = mcolors.ListedColormap(self.colors[palette])
                self._plot(cmap, label=palette)

            for palette in self.palettes.keys():
                cmap = mcolors.ListedColormap(self.palettes[palette])
                self._plot(cmap, label=palette)
        return

    def cmap_show(self, cmap='all'):
        if cmap != 'all' and cmap not in self.colormaps.keys():
            raise NameError('Colormap not found')
        elif cmap in self.colormaps.keys():
            colormap = self.colormaps[cmap]
            self._plot(colormap, label=cmap)
        elif cmap == 'all':
            for cmap in self.colormaps.keys():
                colormap = self.colormaps[cmap]
                self._plot(colormap, label=cmap)
        return

    def show_all(self):
        self.show_palette('all')
        self.show_cmap('all')
        return
