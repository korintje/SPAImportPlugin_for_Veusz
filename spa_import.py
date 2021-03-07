# -*- coding: utf-8 -*-
import numpy as np
from veusz.plugins import (
    ImportPlugin,
    ImportDataset1D,
    ImportFieldText,
    importpluginregistry,
    )

class ImportSPA(ImportPlugin):
    """A plugin for reading Thermo Scientific OMNIC SPA file."""
    name = 'OMNIC SPA import'
    author = 'Takuro Hosomi'
    description = 'Read a spectrum from Thermo Scientific OMNIC SPA file'
    file_extensions = set(['.spa', '.SPA'])

    def __init__(self):
        ImportPlugin.__init__(self)
        #self.spadata = SPAData(params.filename)
        self.fields = [
            ImportFieldText("x_name", descr="X-axis name", default="wavenumber"),
            ImportFieldText("y_name", descr="Y-axis name", default=r"{auto}")
        ]
    
    def doImport(self, params):
        """Actually import data"""
        try:
            self.spadata = SPAData(params.filename)
            x_name = params.field_results["x_name"]
            y_name = params.field_results["y_name"]
            if y_name == r"{auto}":
                y_name = self.spadata.title
            return [
                ImportDataset1D(x_name, self.spadata.wavenumbers),
                ImportDataset1D(y_name, self.spadata.data),
            ]
        except IOError as e:
            raise e
        except Exception as e:
            raise ImportPluginException(str(e))


class SPAData():

    def __init__(self, filepath):
        self.datanum = 1
        self.title = ""
        self.max_wavenum = 0
        self.min_wavenum = 0
        self.wavenumbers = np.zeros(1)
        self.data = np.zeros(1)
        self.loadfromFile(filepath)
    
    def loadfromFile(self, filepath):
        with open(filepath, 'rb') as f:
            # Get spectrum title
            f.seek(30)
            title = np.fromfile(f, np.uint8,255)
            self.title = ''.join([chr(x) for x in title if x!=0])

            # Get number of datapoints in wavenumber array
            f.seek(564)
            self.datanum = np.fromfile(f, np.int32,1)[0]
            
            # Get wavenumber array
            f.seek(576)
            self.max_wavenum = np.fromfile(f, np.single, 1)[0]
            self.min_wavenum = np.fromfile(f, np.single, 1)[0]
            self.wavenumbers = np.linspace(self.max_wavenum, self.min_wavenum, self.datanum)

            # Search and move start address of data
            f.seek(288)
            flag = 0
            while flag != 3:
                flag = np.fromfile(f, np.uint16, 1)
            data_position=np.fromfile(f,np.uint16, 1)[0]
            f.seek(data_position)

            # Get spectrum data
            self.data = np.fromfile(f, np.single, self.datanum)

# add the class to the registry.
importpluginregistry.append(ImportSPA)
