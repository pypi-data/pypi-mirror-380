# Introduction 
Design package for the company Envidan A/S intended for use with matplotlib and seaborn
- Hardcoded palettes and colormaps with company design colors
- Envidan logo in print and web form

# Getting Started
## Installation
You can install this package using
```
pip install ed_design
```
## Dependencies
Software dependencices are:
```
matplotlib
seaborn
pandas
numpy
```

## Use
### Palettes and colormaps for matplotlib and seaborn
```
import ed_design as edd

colors = edd.Colors()
colors.palette_show('all')

palette = colors.palette_get('blues')  # Use with categorical variabels
cmap = colors.cmap_get('BlGr')  # Use with continous variabels

my_own_camp = colors.create_cmap([color1, color2, color3], n_colors=256)
```

### Envidan logo
```
logo = edd.logo()
edd.logo2fig(fig)
```

### Set style
```
edd.style()  # Sets envidan style with color prop cycle "normal" from edd.Colors()
edd.style('default')  # sets matplotlib default style
```


# Build and Test
TODO:
- Nothing at the momement

# Contribute
Only employees in Envidan has access to the repositoryon Azure

# Author
Martin Vidkjær, mav@envidan.dk
