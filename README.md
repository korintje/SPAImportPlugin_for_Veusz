# SPAImportPlugin_for_Veusz
A plugin for importing Thermo Scientific OMNIC .SPA file into [Veusz](https://veusz.github.io/).　　

SPA is the default file type of Thermo Scientific(TM) OMNIC Series Software(TM), which stores infrared (IR) spectral data in a binary format.

# How it works
Extracting a spectrum from .SPA file and importing as two Dataset1D (x and y). The x-axis is wavenumber. The y-azis is absorbance or transmittance.

# How to install
1. Download [the plugin file](https://github.com/korintje/SPAImportPlugin_for_Veusz/releases/tag/v1.0)
2. Extract the compressed folder
3. Move the `spa_import.py` to anywhere (e.g. C:\Program Files (x86)\Veusz\plugins)
4. Start Veusz
5. `Edit` -> `Preferences` -> `Plugins` -> `Add`, and choose the `spa_import.py`
6. Restart Veusz

# How to use
In veusz
1. `Data` -> `Import` -> `Plugins`, and select "OMNIC SPA import" in the plugin select box.
2. Set X and Y axis name (By default, the Y axis name is automatically set as the "title" of SPA data.) 
3. Import

# Requirements
- [Veusz](https://veusz.github.io/)

# License
GNU General Public License v3.0 or later  

See [LICNESE](https://github.com/korintje/SPAImportPlugin_for_Veusz/blob/main/LICENSE) for the full text.
