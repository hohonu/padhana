Getting Started
===============

The Padhana framework is designed to enable you to work with PDF documents (and other types) in a
formal way.  By combining a simple document format (based on a node hierarchy) and then a
set of parsers and document analysis tools we parse and then structure/annotate document
content to enable rich interactions.

The platform is really based on a few concepts.

Document
--------

A document is a really a simple data structure comprising of metadata (a simple dictionary)
and then a root node (of type ContentNode).

The content node then has a structure based on how the information was parsed into the platform.

A document is used as the formal representation for a source file or binary object, and should contain
features (such as text, layout, visual elements) that can then be used in Padhana to try and
enable rich interaction with the document for re-structuring it, training or labelling etc.

Parsers
-------

Parsers basically take a source path to a file and then convert that file into a Document (see above)


Connectors
----------

Connectors basically take a source and provide a list of file locations (implementing the
iterator pattern).

Stores
-------

Once you have documents in parsed you can store them in a type of store to allow quick and easy access.

