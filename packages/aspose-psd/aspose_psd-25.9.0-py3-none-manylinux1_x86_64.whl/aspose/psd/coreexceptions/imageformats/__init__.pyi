"""The namespace contains exceptions thrown by one of the file formats supported."""
from typing import List, Optional, Dict, Iterable
import enum
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

class BmpImageException(aspose.psd.coreexceptions.ImageException):
    '''The bmp image exception.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the  class.
        
        :param message: The exception message.'''
        ...
    
    ...

class GifImageException(aspose.psd.coreexceptions.ImageException):
    '''The Gif image exception.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the  class.
        
        :param message: The exception message.'''
        ...
    
    ...

class Jpeg2000Exception(aspose.psd.coreexceptions.ImageException):
    '''Exceptions for Jpeg files'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the  class.
        
        :param message: The exception message.'''
        ...
    
    ...

class JpegException(aspose.psd.coreexceptions.ImageException):
    '''Exceptions for Jpeg files'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the  class.
        
        :param message: The exception message.'''
        ...
    
    ...

class JpegLoadException(JpegException):
    '''Represents the JPEG image loading exception.'''
    
    @overload
    def __init__(self, message: str):
        '''Initializes a new instance of the  class.
        
        :param message: The exception message.'''
        ...
    
    @overload
    def __init__(self, message: str, reason: JpegLoadException.ErrorReason):
        ...
    
    @property
    def reason(self) -> JpegLoadException.ErrorReason:
        '''Gets the reason of error.'''
        ...
    
    @reason.setter
    def reason(self, value : JpegLoadException.ErrorReason):
        '''Sets the reason of error.'''
        ...
    
    ...

class PngImageException:
    '''The png image exception.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the  class.
        
        :param message: The message.'''
        ...
    
    ...

class PsdImageArgumentException(PsdImageException):
    '''The psd image argument exception.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the  class.
        
        :param message: The exception message.'''
        ...
    
    ...

class PsdImageException(aspose.psd.coreexceptions.ImageException):
    '''The psd image exception.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the  class.
        
        :param message: The exception message.'''
        ...
    
    ...

class PsdImageResourceException(PsdImageException):
    '''The psd image resource exception.'''
    
    def __init__(self, message: str, resource: aspose.psd.fileformats.psd.ResourceBlock):
        '''Initializes a new instance of the  class.
        
        :param message: The exception message.
        :param resource: The resource.'''
        ...
    
    @property
    def resource(self) -> aspose.psd.fileformats.psd.ResourceBlock:
        '''Gets the psd resource which caused this exception.'''
        ...
    
    ...

class TiffImageException(aspose.psd.coreexceptions.ImageException):
    '''The Tiff image exception'''
    
    @overload
    def __init__(self, message: str):
        '''Initializes a new instance of the  class.
        
        :param message: The exception message.'''
        ...
    
    @overload
    def __init__(self, message: str, error: aspose.psd.imageoptions.TiffOptionsError):
        '''Initializes a new instance of the  class.
        
        :param message: The message.
        :param error: The error.'''
        ...
    
    @overload
    def __init__(self, error: aspose.psd.imageoptions.TiffOptionsError):
        '''Initializes a new instance of the  class.
        
        :param error: The error.'''
        ...
    
    @property
    def options_error(self) -> aspose.psd.imageoptions.TiffOptionsError:
        ...
    
    ...

