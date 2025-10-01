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

class IXmlValue:
    '''Converts xmp values to the XML string representation.'''
    
    def get_xml_value(self) -> str:
        '''Converts XMP value to the XML representation.
        
        :returns: Returns the XMP value converted to the XML representation.'''
        ...
    
    ...

class LangAlt(IXmlValue):
    '''Represents XMP Language Alternative.'''
    
    def add_language(self, language : str, value : str):
        '''Adds the language.
        
        :param language: The language.
        :param value: The language value.'''
        ...
    
    def get_xml_value(self) -> str:
        '''Converts XMP value to the XML representation.
        
        :returns: Returns the XMP value converted to the XML representation.'''
        ...
    
    ...

class Namespaces:
    '''Contains namespaces used in RDF document.'''
    
    @classmethod
    @property
    def XML(cls) -> str:
        '''Xml namespace.'''
        ...
    
    @classmethod
    @property
    def RDF(cls) -> str:
        '''Resource definition framework namespace.'''
        ...
    
    @classmethod
    @property
    def DUBLIN_CORE(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_BASIC(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_RIGHTS(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_MM(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_DM(cls) -> str:
        ...
    
    @classmethod
    @property
    def PDF(cls) -> str:
        '''Adobe PDF namespace.'''
        ...
    
    @classmethod
    @property
    def PHOTOSHOP(cls) -> str:
        '''Adobe Photoshop namespace.'''
        ...
    
    @classmethod
    @property
    def XMP_GRAPHICS(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_GRAPHICS_THUMBNAIL(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_TYPE_FONT(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_TYPE_DIMENSIONS(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_TYPE_RESOURCE_REF(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_TYPE_RESOURCE_EVENT(cls) -> str:
        ...
    
    @classmethod
    @property
    def XMP_TYPE_VERSION(cls) -> str:
        ...
    
    ...

class XmpArray(IXmlValue):
    '''Represents Xmp Array in :py:class:`aspose.psd.xmp.XmpPackage`. TODO: Array may contain complex data.'''
    
    def add_item(self, item : str):
        '''Adds new item.
        
        :param item: The item to be added to list of items.'''
        ...
    
    def get_xml_value(self) -> str:
        '''Converts XMP value to the XML representation.
        
        :returns: Returns the XMP value converted to the XML representation.'''
        ...
    
    @property
    def values(self) -> List[str]:
        '''Gets array of values inside :py:class:`aspose.psd.xmp.XmpArray`.'''
        ...
    
    ...

class XmpArrayHelper:
    '''The helper class for processing RDF logic'''
    
    @staticmethod
    def get_rdf_code(xmp_array_type : aspose.psd.xmp.XmpArrayType) -> str:
        '''Gets the RDF code for specific :py:class:`aspose.psd.xmp.XmpArrayType`.
        
        :param xmp_array_type: Type of the XMP array.
        :returns: Returns the RDF code for specific :py:class:`aspose.psd.xmp.XmpArrayType`.'''
        ...
    
    ...

class XmpElementBase:
    '''Represents base xmp element contains attributes.'''
    
    def add_attribute(self, attribute : str, value : str):
        '''Adds the attribute.
        
        :param attribute: The attribute.
        :param value: The value.'''
        ...
    
    def get_attribute(self, attribute : str) -> str:
        '''Gets the attribute.
        
        :param attribute: The attribute.
        :returns: Returns the attribute for specified attribute name.'''
        ...
    
    def clear_attributes(self):
        '''Removes all attributes.'''
        ...
    
    def equals(self, other : aspose.psd.xmp.XmpElementBase) -> bool:
        '''Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the ``other`` parameter; otherwise, false.'''
        ...
    
    ...

class XmpHeaderPi(IXmlValue):
    '''Represents XMP header processing instruction.'''
    
    def get_xml_value(self) -> str:
        '''Converts XMP value to the XML representation.
        
        :returns: Returns the XMP value converted to the XML representation.'''
        ...
    
    def equals(self, other : aspose.psd.xmp.XmpHeaderPi) -> bool:
        '''Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the ``other`` parameter; otherwise, false.'''
        ...
    
    @property
    def guid(self) -> str:
        '''Represents Header Guid.'''
        ...
    
    @guid.setter
    def guid(self, value : str):
        '''Represents Header Guid.'''
        ...
    
    ...

class XmpMeta(XmpElementBase):
    '''Represents xmpmeta. Optional.
    The purpose of this element is to identify XMP metadata within general XML text that might contain other non-XMP uses of RDF.'''
    
    @overload
    def equals(self, other : aspose.psd.xmp.XmpMeta) -> bool:
        '''Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the ``other`` parameter; otherwise, false.'''
        ...
    
    @overload
    def equals(self, other : aspose.psd.xmp.XmpElementBase) -> bool:
        '''Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the ``other`` parameter; otherwise, false.'''
        ...
    
    def add_attribute(self, attribute : str, value : str):
        '''Adds the attribute.
        
        :param attribute: The attribute.
        :param value: The value.'''
        ...
    
    def get_attribute(self, attribute : str) -> str:
        '''Gets the attribute.
        
        :param attribute: The attribute.
        :returns: Returns the attribute for specified attribute name.'''
        ...
    
    def clear_attributes(self):
        '''Removes all attributes.'''
        ...
    
    def get_xml_value(self) -> str:
        '''Converts XMP value to the XML representation.
        
        :returns: Returns the XMP value converted to the XML representation.'''
        ...
    
    @property
    def adobe_xmp_toolkit(self) -> str:
        ...
    
    @adobe_xmp_toolkit.setter
    def adobe_xmp_toolkit(self, value : str):
        ...
    
    ...

class XmpPackage(IXmlValue):
    '''Defines the XmpPackage class that represents base abstraction for XMP package.'''
    
    def contains_key(self, key : str) -> bool:
        '''Determines whether the specified key contains key.
        
        :param key: The key to be checked.
        :returns: Returns true if the specified key contains key.'''
        ...
    
    def add_value(self, key : str, value : str):
        '''Adds the value.
        
        :param key: The string representation of key that is identified with added value.
        :param value: The value to add to.'''
        ...
    
    def remove(self, key : str) -> bool:
        '''Remove the value with the specified key.
        
        :param key: The string representation of key that is identified with removed value.
        :returns: Returns true if the value with the specified key was removed.'''
        ...
    
    def clear(self):
        '''Clears this instance.'''
        ...
    
    def set_value(self, key : str, value : aspose.psd.xmp.IXmlValue):
        '''Sets the value.
        
        :param key: The string representation of key that is identified with added value.
        :param value: The value to add to.'''
        ...
    
    def set_xmp_type_value(self, key : str, value : aspose.psd.xmp.types.XmpTypeBase):
        '''Sets the XMP type value.
        
        :param key: The string representation of key that is identified with set value.
        :param value: The value to set to.'''
        ...
    
    def get_xml_value(self) -> str:
        '''Converts XMP value to the XML representation.
        
        :returns: Returns the XMP value converted to the XML representation.'''
        ...
    
    @property
    def xml_namespace(self) -> str:
        ...
    
    @property
    def prefix(self) -> str:
        '''Gets the prefix.'''
        ...
    
    @property
    def namespace_uri(self) -> str:
        ...
    
    ...

class XmpPackageBaseCollection:
    '''Represents collection of :py:class:`aspose.psd.xmp.XmpPackage`.'''
    
    def add(self, package : aspose.psd.xmp.XmpPackage):
        '''Adds new instance of :py:class:`aspose.psd.xmp.XmpPackage`.
        
        :param package: The XMP package to add.'''
        ...
    
    def remove(self, package : aspose.psd.xmp.XmpPackage):
        '''Removes the specified XMP package.
        
        :param package: The XMP package to remove.'''
        ...
    
    def get_packages(self) -> List[aspose.psd.xmp.XmpPackage]:
        '''Get array of :py:class:`aspose.psd.xmp.XmpPackage`.
        
        :returns: Returns an array of XMP packages.'''
        ...
    
    def get_package(self, namespace_uri : str) -> aspose.psd.xmp.XmpPackage:
        '''Gets :py:class:`aspose.psd.xmp.XmpPackage` by it's namespaceURI.
        
        :param namespace_uri: The namespace URI to get package for.
        :returns: Returns XMP package for specified namespace Uri.'''
        ...
    
    def clear(self):
        '''Clear all :py:class:`aspose.psd.xmp.XmpPackage` inside collection.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements in the collection.'''
        ...
    
    ...

class XmpPacketWrapper:
    '''Contains serialized xmp package including header and trailer.'''
    
    def add_package(self, package : aspose.psd.xmp.XmpPackage):
        '''Adds the package.
        
        :param package: The package.'''
        ...
    
    def get_package(self, namespace_uri : str) -> aspose.psd.xmp.XmpPackage:
        '''Gets package by namespace URI.
        
        :param namespace_uri: The package schema URI.
        :returns: Returns the XMP package for specified namespace URI.'''
        ...
    
    def contains_package(self, namespace_uri : str) -> bool:
        '''Determines whethere package is exist in xmp wrapper.
        
        :param namespace_uri: Package schema uri.
        :returns: Returns true if package with specified namespace Uri exist in XMP wrapper.'''
        ...
    
    def remove_package(self, package : aspose.psd.xmp.XmpPackage):
        '''Removes the XMP package.
        
        :param package: The package.'''
        ...
    
    def clear_packages(self):
        '''Removes all :py:class:`aspose.psd.xmp.XmpPackage` inside XMP.'''
        ...
    
    @property
    def header_pi(self) -> aspose.psd.xmp.XmpHeaderPi:
        ...
    
    @property
    def meta(self) -> aspose.psd.xmp.XmpMeta:
        '''Gets the XMP meta. Optional.'''
        ...
    
    @meta.setter
    def meta(self, value : aspose.psd.xmp.XmpMeta):
        '''Gets the XMP meta. Optional.'''
        ...
    
    @property
    def trailer_pi(self) -> aspose.psd.xmp.XmpTrailerPi:
        ...
    
    @property
    def packages(self) -> List[aspose.psd.xmp.XmpPackage]:
        '''Gets array of :py:class:`aspose.psd.xmp.XmpPackage` inside XMP.'''
        ...
    
    @property
    def packages_count(self) -> int:
        ...
    
    ...

class XmpRdfRoot(XmpElementBase):
    '''Represents rdf:RDF element.
    A single XMP packet shall be serialized using a single rdf:RDF XML element. The rdf:RDF element content shall consist of only zero or more rdf:Description elements.'''
    
    def add_attribute(self, attribute : str, value : str):
        '''Adds the attribute.
        
        :param attribute: The attribute.
        :param value: The value.'''
        ...
    
    def get_attribute(self, attribute : str) -> str:
        '''Gets the attribute.
        
        :param attribute: The attribute.
        :returns: Returns the attribute for specified attribute name.'''
        ...
    
    def clear_attributes(self):
        '''Removes all attributes.'''
        ...
    
    def equals(self, other : aspose.psd.xmp.XmpElementBase) -> bool:
        '''Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the ``other`` parameter; otherwise, false.'''
        ...
    
    def register_namespace_uri(self, prefix : str, namespace_uri : str):
        '''Adds namespace uri by prefix. Prefix may start without xmlns.
        
        :param prefix: The prefix.
        :param namespace_uri: Package schema uri.'''
        ...
    
    def get_namespace_uri(self, prefix : str) -> str:
        '''Gets namespace URI by specific prefix. Prefix may start without xmlns.
        
        :param prefix: The prefix.
        :returns: Returns a package schema URI.'''
        ...
    
    def get_xml_value(self) -> str:
        '''Converts xmp value to the xml representation.
        
        :returns: Returns XMP value converted to XML string.'''
        ...
    
    ...

class XmpTrailerPi(IXmlValue):
    '''Represents XMP trailer processing instruction.'''
    
    def get_xml_value(self) -> str:
        '''Converts xmp value to the xml representation.
        
        :returns: Returns XML representation of XMP.'''
        ...
    
    def equals(self, other : aspose.psd.xmp.XmpTrailerPi) -> bool:
        '''Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the ``other`` parameter; otherwise, false.'''
        ...
    
    @property
    def is_writable(self) -> bool:
        ...
    
    @is_writable.setter
    def is_writable(self, value : bool):
        ...
    
    ...

class XmpArrayType:
    '''Represents array type in :py:class:`aspose.psd.xmp.XmpArray`.'''
    
    @classmethod
    @property
    def UNORDERED(cls) -> XmpArrayType:
        '''The unordered array.'''
        ...
    
    @classmethod
    @property
    def ORDERED(cls) -> XmpArrayType:
        '''The ordered array.'''
        ...
    
    @classmethod
    @property
    def ALTERNATIVE(cls) -> XmpArrayType:
        '''The alternative array.'''
        ...
    
    ...

