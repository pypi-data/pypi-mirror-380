from enumerific import Enumeration, auto


class Context(Enumeration):
    """List of XML contexts, to denote the XML context currently being processed."""

    Unknown = auto()
    Root = auto(description="Document root node")
    Prolog = auto(description="Document declaration (prolog)")
    Instruction = auto(description="Document processing instruction")
    DocType = auto(description="Document type")
    Element = auto(description="Element comprising opening/closing or self-closing tag")
    TagOpen = auto(description="Opening tag of an element (maybe self-closing)")
    TagClose = auto(description="Closing tag of an element")
    Attribute = auto(description="Attribute held by an element's tag")
    Text = auto(description="Text held between an element's opening and closing tags")
    Data = auto(description="Data held in a CDATA section")
    Comment = auto(description="Comment held in a comment section")


class Escape(Enumeration):
    """List of XML special character escape modes."""

    All = auto(description="Escape all XML special characters")
    Required = auto(description="Escpae only required XML special characters")
