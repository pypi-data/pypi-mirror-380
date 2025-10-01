from typing import List, Optional, Dict, Iterable
import aspose.pycore
import aspose.pydrawing
import aspose.psd
import aspose.psd.asynctask
import aspose.psd.brushes
import aspose.psd.coreexceptions
import aspose.psd.coreexceptions.compressors
import aspose.psd.coreexceptions.imageformats
import aspose.psd.customfonthandler
import aspose.psd.dithering
import aspose.psd.evalute
import aspose.psd.exif
import aspose.psd.exif.enums
import aspose.psd.extensions
import aspose.psd.fileformats
import aspose.psd.fileformats.ai
import aspose.psd.fileformats.bmp
import aspose.psd.fileformats.core
import aspose.psd.fileformats.core.blending
import aspose.psd.fileformats.core.vectorpaths
import aspose.psd.fileformats.jpeg
import aspose.psd.fileformats.jpeg2000
import aspose.psd.fileformats.pdf
import aspose.psd.fileformats.png
import aspose.psd.fileformats.psd
import aspose.psd.fileformats.psd.core
import aspose.psd.fileformats.psd.core.rawcolor
import aspose.psd.fileformats.psd.layers
import aspose.psd.fileformats.psd.layers.adjustmentlayers
import aspose.psd.fileformats.psd.layers.animation
import aspose.psd.fileformats.psd.layers.filllayers
import aspose.psd.fileformats.psd.layers.fillsettings
import aspose.psd.fileformats.psd.layers.gradient
import aspose.psd.fileformats.psd.layers.layereffects
import aspose.psd.fileformats.psd.layers.layerresources
import aspose.psd.fileformats.psd.layers.layerresources.strokeresources
import aspose.psd.fileformats.psd.layers.layerresources.typetoolinfostructures
import aspose.psd.fileformats.psd.layers.smartfilters
import aspose.psd.fileformats.psd.layers.smartfilters.rendering
import aspose.psd.fileformats.psd.layers.smartobjects
import aspose.psd.fileformats.psd.layers.text
import aspose.psd.fileformats.psd.layers.warp
import aspose.psd.fileformats.psd.resources
import aspose.psd.fileformats.psd.resources.enums
import aspose.psd.fileformats.psd.resources.resolutionenums
import aspose.psd.fileformats.tiff
import aspose.psd.fileformats.tiff.enums
import aspose.psd.fileformats.tiff.filemanagement
import aspose.psd.flatarray
import aspose.psd.flatarray.exceptions
import aspose.psd.imagefilters
import aspose.psd.imagefilters.filteroptions
import aspose.psd.imageloadoptions
import aspose.psd.imageoptions
import aspose.psd.interfaces
import aspose.psd.memorymanagement
import aspose.psd.multithreading
import aspose.psd.palettehelper
import aspose.psd.progressmanagement
import aspose.psd.shapes
import aspose.psd.shapesegments
import aspose.psd.sources
import aspose.psd.xmp
import aspose.psd.xmp.schemas
import aspose.psd.xmp.schemas.dublincore
import aspose.psd.xmp.schemas.pdf
import aspose.psd.xmp.schemas.photoshop
import aspose.psd.xmp.schemas.xmpbaseschema
import aspose.psd.xmp.schemas.xmpdm
import aspose.psd.xmp.schemas.xmpmm
import aspose.psd.xmp.schemas.xmprm
import aspose.psd.xmp.types
import aspose.psd.xmp.types.basic
import aspose.psd.xmp.types.complex
import aspose.psd.xmp.types.complex.colorant
import aspose.psd.xmp.types.complex.dimensions
import aspose.psd.xmp.types.complex.font
import aspose.psd.xmp.types.complex.resourceevent
import aspose.psd.xmp.types.complex.resourceref
import aspose.psd.xmp.types.complex.thumbnail
import aspose.psd.xmp.types.complex.version
import aspose.psd.xmp.types.derived

class AsyncTask:
    '''The static factory class for creating the asynchronous tasks'''
    
    ...

class AsyncTaskException:
    '''The exception for the asynchronous task.'''
    
    ...

class AsyncTaskProgress:
    '''Provides progress info for the asynchronous task.'''
    
    @property
    def DURATION(self) -> TimeSpan:
        '''The duration of the asynchronous task.'''
        ...
    
    @property
    def PROGRESS_PERCENTAGE(self) -> int:
        ...
    
    ...

class IAsyncTask:
    '''The asynchronous task.'''
    
    def run_async(self):
        '''Runs this task.'''
        ...
    
    def cancel(self):
        '''Cancels this task.
        The task is completed safely by the controlled stopping of the algorithm.'''
        ...
    
    def abort(self):
        '''Aborts this task.
        The task is completed immediately, with the risk of not freeing internal unmanaged resources.'''
        ...
    
    @property
    def progress(self) -> aspose.psd.asynctask.AsyncTaskProgress:
        '''Gets the progress of the asynchronous task.'''
        ...
    
    @property
    def is_busy(self) -> bool:
        ...
    
    @property
    def is_canceled(self) -> bool:
        ...
    
    @property
    def is_faulted(self) -> bool:
        ...
    
    @property
    def result(self) -> any:
        '''Gets the result of this task.'''
        ...
    
    ...

class IAsyncTaskState:
    '''Provides access to the state of the asynchronous task.'''
    
    def set_progress(self, progress_percentage : int):
        '''Sets the progress of the asynchronous task.
        
        :param progress_percentage: The progress percentage.'''
        ...
    
    @property
    def is_canceled(self) -> bool:
        ...
    
    @property
    def progress(self) -> aspose.psd.asynctask.AsyncTaskProgress:
        '''Gets the progress of the asynchronous task.'''
        ...
    
    ...

