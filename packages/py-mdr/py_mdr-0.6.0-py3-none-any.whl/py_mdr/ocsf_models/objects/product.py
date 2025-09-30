from dataclasses import dataclass, field

from py_mdr.ocsf_models.objects.base_model import BaseModel


@dataclass
class Feature(BaseModel):
    """
    The Feature object provides information about the software product feature that generated a specific event. It encompasses details related to the capabilities, components, user interface (UI) design, and performance upgrades associated with the feature.

    Attributes:
    - Name (name) [Optional]: The name of the feature.
    - Unique ID (uid) [Optional]: The unique identifier for the feature.
    - Version (version) [Optional]: The version of the feature.
    """

    name: str = None
    uid: str = None
    version: str = None


@dataclass
class Product(BaseModel):
    """
    The Product object describes characteristics of a software product.

    Attributes:
    - Feature (name) [Optional]: The feature that reported the event.
    - Language (lang) [Optional]: The two letter lower case language codes, as defined by ISO 639-1. For example: en (English), de (German), or fr (French).
    - Name (name) [Optional]: The name of the product.
    - Path (path) [Optional]: The installation path of the product.
    - The product CPE identifier (cpe_name) [Optional]: The Common Platform Enumeration (CPE) name as described by (NIST) For example: cpe:/a:apple:safari:16.2.
    - URL String (url_string) [Optional]: The URL pointing towards the product.
    - Unique ID (uid) [Optional]: The unique identifier of the product.
    - Vendor Name (vendor_name) [Optional]: The name of the vendor of the product.
    - Version (version) [Optional]: The version of the product, as defined by the event source. For example: 2013.1.3-beta.
    """

    feature: Feature = field(default_factory=Feature)
    lang: str = None
    name: str = None
    path: str = None
    cpe_name: str = None
    url_string: str = None
    uid: str = None
    vendor_name: str = None
    version: str = None
