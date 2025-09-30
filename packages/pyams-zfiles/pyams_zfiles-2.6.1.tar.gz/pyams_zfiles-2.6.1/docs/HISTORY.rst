Changelog
=========

2.6.1
-----
 - allow unknown images formats to be stored as standard files

2.6.0
-----
 - added mode to documents synchronizer to handle two-ways synchronizations
 - updated scheduler task execution log format

2.5.3
-----
 - updated scheduler task execution result format

2.5.2
-----
 - updated scheduler task principal ID

2.5.1
-----
 - packaging issue
 - added conditional include on pyams_alchemy to pyams_zfiles.task

2.5.0
-----
 - added scheduler task to check for orphaned documents
 - updated application_name search argument to allow multiple values search
 - use new PyAMS_workflow method to apply first publication date on published content

2.4.4
-----
 - updated Gitlab-CI for Python 3.12

2.4.3
-----
 - updated Gitlab-CI for Python 3.12

2.4.2
-----
 - avoid document content extraction without any matching filter

2.4.1
-----
 - added columns to display index size in indexed properties view

2.4.0
-----
 - allow setting of document title or filename from properties or from current datetime
   using formatting strings

2.3.1
-----
 - update RPC API permissions checker methods to return a boolean value instead of an ACL
 - added support for Python 3.12

2.3.0
-----
 - added document properties extractors, which can be used to extract some of a document properties
   from it's associated file content

2.2.1
-----
 - updated doctests

2.2.0
-----
 - added support for custom catalog indexes for selected documents properties

2.1.0
-----
 - added optional "created_time" argument to document creation API

2.0.7
-----
 - switched default timezone to UTC

2.0.6
-----
 - added missing documents container label provider

2.0.5
-----
 - corrected faulty import

2.0.4
-----
 - updated REST API route name and configuration setting name
 - moved objects finder helper to new module
 - updated doctests

2.0.3
-----
 - updated properties index values getter to correctly split values

2.0.2
-----
 - version mismatch

2.0.1
-----
 - updated modal forms title
 - small updates in documents workflow

2.0.0
-----
 - upgraded to Pyramid 2.0
 - updated tests for unauthenticated requests

1.4.6
-----
 - updated REST document search API schema

1.4.5
-----
 - updated access and update modes management

1.4.4
-----
 - updated Colander API schemas for better OpenAPI specifications
 - added enums for workflow states

1.4.3
-----
 - updated translations

1.4.2
-----
 - updated workflow delete view

1.4.1
-----
 - updated generation evolve

1.4.0
-----
 - added multiple synchronizer configurations
 - added synchronizer access to REST API

1.3.4
-----
 - updated synchronizer call result to return enums values instead of enums, which can't be
   converted to JSON

1.3.3
-----
 - removed permission check for CORS OPTIONS request on document data

1.3.2
-----
 - added new PyAMS_security CORS validators to REST services

1.3.1
-----
 - updated CORS support in REST API
 - added support for Python 3.10

1.3.0
-----
 - added support for CORS preflight OPTIONS verb used by REST services
 - updated support for search params in URL
 - updated Gitlab-CI configuration
 - small ZMI updates

1.2.1
-----
 - added enumeration to handle synchronizer status
 - PyAMS_security interfaces refactoring

1.2.0
-----
 - added workflow label
 - added "NOT_FOUND" status to documents synchronizer if given OID doesn't match an existing
   document
 - added "NO_DATA" status to documents synchronizer if a POSError occurs when reading
   document data

1.1.0
-----
 - add index on properties to make them searchable

1.0.6
-----
 - updated document properties widget template

1.0.5
-----
 - added option to display menu to access documents container from ZMI home page

1.0.4
-----
 - added missing "context" argument to permission check

1.0.3
-----
 - added title to applications vocabulary terms

1.0.2
-----
 - updated application manager permissions

1.0.1
-----
 - updated context of permissions checks in REST and GraphQL APIs

1.0.0
-----
 - initial release
