from dataclasses import dataclass, field
from datetime import datetime

from py_mdr.ocsf_models.objects.base_model import BaseModel
from py_mdr.ocsf_models.objects.geolocation import GeoLocation


# FIXME: Circular dependency
# from py_mdr.ocsf_models.objects.user import User


@dataclass
class LDAPPerson(BaseModel):
    """
    The LDAPPerson class encapsulates detailed information about an individual within an LDAP or Active Directory system. It is designed to model both the professional and personal attributes of a person, including their role, contact information, and organizational context.

    Attributes:
    - Cost Center (cost_center) [Optional]: Associated cost center for budgeting and financial analysis.
    - Created Time (created_time) [Optional]: Timestamp of when the user account was created.
    - Deleted Time (deleted_time) [Optional]: Timestamp indicating when the user was deleted, useful in AD environments.
    - Email Addresses (email_addrs) [Optional]: list of additional email addresses.
    - Employee ID (employee_uid) [Optional]: Unique identifier assigned by the organization.
    - Geo Location (location) [Optional]: Usual work location of the user.
    - Given Name (given_name) [Optional]: First name of the user.
    - Hire Time (hire_time) [Optional]: Timestamp when the user was hired.
    - Job Title (job_title) [Optional]: Official job title.
    - LDAP Common Name (ldap_cn) [Optional]: Full name as per LDAP cn attribute.
    - LDAP Distinguished Name (ldap_dn) [Optional]: Unique DN in the LDAP directory.
    - Labels (labels) [Optional]: Array of labels or tags associated with the user.
    - Last Login (last_login_time) [Optional]: Last login timestamp.
    - Leave Time (leave_time) [Optional]: When the user left or will leave the organization.
    - Manager (manager) [Optional]: Direct manager, supports org hierarchy.
    - Modified Time (modified_time) [Optional]: Last modification timestamp of the user entry.
    - Office Location (office_location) [Optional]: Primary office location, not necessarily a specific address.
    - Surname (surname) [Optional]: Family or last name.
    """

    cost_center: str = None
    created_time: datetime = None
    deleted_time: datetime = None
    email_addrs: list[str] = field(default_factory=list)
    employee_uid: str = None
    location: GeoLocation = field(default_factory=GeoLocation)
    given_name: str = None
    hire_time: datetime = None
    job_title: str = None
    ldap_cn: str = None
    ldap_dn: str = None
    labels: list[str] = field(default_factory=list)
    last_login_time: datetime = None
    leave_time: datetime = None
    # FIXME: Circular dependency
    # manager: User = field(default_factory=User)
    manager = None
    modified_time: datetime = None
    office_location: str = None
    surname: str = None
