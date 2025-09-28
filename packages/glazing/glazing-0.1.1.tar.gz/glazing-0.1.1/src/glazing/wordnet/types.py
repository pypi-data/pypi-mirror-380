"""WordNet-specific type definitions.

Defines type aliases and literal types specific to WordNet 3.1 data structures
including synsets, senses, relations, and morphological processing.

Constants
---------
WordNetPOS : type[Literal]
    WordNet part-of-speech tags (n, v, a, r, s).
PointerSymbol : type[Literal]
    All WordNet relation symbols (40+ types).
LexFileName : type[Literal]
    Lexical file names for 45 semantic categories.
VerbFrameNumber : type[Literal]
    Valid verb frame numbers (1-35).
AdjPosition : type[Literal]
    Adjective positions (attributive, predicative, postnominal).
SynsetOffset : type[Annotated[str, Field]]
    8-digit synset identifier with validation.
SenseKey : type[Annotated[str, Field]]
    WordNet sense key with format validation.
LexID : type[Annotated[int, Field]]
    Lexical ID (0-15) for distinguishing words in synsets.
SenseNumber : type[Annotated[int, Field]]
    Sense number for frequency-based ordering.
TagCount : type[Annotated[int, Field]]
    Semantic concordance tag count.
WORDNET_OFFSET_PATTERN : str
    Regex pattern for 8-digit synset offsets.
WORDNET_SENSE_KEY_PATTERN : str
    Regex pattern for sense key validation.
PERCENTAGE_NOTATION_PATTERN : str
    Regex pattern for VerbNet percentage notation.

Examples
--------
>>> from glazing.wordnet.types import WordNetPOS, SynsetOffset
>>> pos: WordNetPOS = "v"
>>> offset: SynsetOffset = "00001740"
"""

from typing import Annotated, Literal

from pydantic import Field

# WordNet part-of-speech categories
type WordNetPOS = Literal[
    "n",  # noun
    "v",  # verb
    "a",  # adjective
    "r",  # adverb
    "s",  # satellite adjective
]

# All WordNet pointer symbols (semantic and lexical relations)
type PointerSymbol = Literal[
    "!",  # Antonym
    "@",  # Hypernym (is-a)
    "@i",  # Instance Hypernym
    "~",  # Hyponym
    "~i",  # Instance Hyponym
    "#m",  # Member holonym
    "#s",  # Substance holonym
    "#p",  # Part holonym
    "%m",  # Member meronym
    "%s",  # Substance meronym
    "%p",  # Part meronym
    "=",  # Attribute
    "+",  # Derivationally related form
    ";c",  # Domain of synset - TOPIC
    "-c",  # Member of this domain - TOPIC
    ";r",  # Domain of synset - REGION
    "-r",  # Member of this domain - REGION
    ";u",  # Domain of synset - USAGE
    "-u",  # Member of this domain - USAGE
    "*",  # Entailment (verbs)
    ">",  # Cause (verbs)
    "^",  # Also see
    "$",  # Verb Group
    "&",  # Similar to (adjectives)
    "<",  # Participle of verb (adjectives)
    "\\",  # Pertainym (pertains to noun) (adjectives)
]

# WordNet lexical file names (45 categories)
type LexFileName = Literal[
    # Noun files
    "noun.Tops",
    "noun.act",
    "noun.animal",
    "noun.artifact",
    "noun.attribute",
    "noun.body",
    "noun.cognition",
    "noun.communication",
    "noun.event",
    "noun.feeling",
    "noun.food",
    "noun.group",
    "noun.location",
    "noun.motive",
    "noun.object",
    "noun.person",
    "noun.phenomenon",
    "noun.plant",
    "noun.possession",
    "noun.process",
    "noun.quantity",
    "noun.relation",
    "noun.shape",
    "noun.state",
    "noun.substance",
    "noun.time",
    # Verb files
    "verb.body",
    "verb.change",
    "verb.cognition",
    "verb.communication",
    "verb.competition",
    "verb.consumption",
    "verb.contact",
    "verb.creation",
    "verb.emotion",
    "verb.motion",
    "verb.perception",
    "verb.possession",
    "verb.social",
    "verb.stative",
    "verb.weather",
    # Adjective files
    "adj.all",
    "adj.pert",
    "adj.ppl",
    # Adverb files
    "adv.all",
]

# Valid verb frame numbers (1-35)
type VerbFrameNumber = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
]

# Adjective position markers
type AdjPosition = Literal[
    "a",  # attributive (prenominal)
    "p",  # predicative
    "ip",  # immediately postnominal
]

# Regex patterns for WordNet identifier formats

# WordNet synset offset (8-digit zero-padded)
WORDNET_OFFSET_PATTERN = r"^[0-9]{8}$"

# WordNet sense key format
WORDNET_SENSE_KEY_PATTERN = r"^[a-z0-9_.-]+%[1-5]:[0-9]{2}:[0-9]{2}:[a-z0-9_.-]*:[0-9]*$"

# VerbNet percentage notation (WordNet reference format)
PERCENTAGE_NOTATION_PATTERN = r"^[a-z_-]+%[1-5]:[0-9]{2}:[0-9]{2}$"

# Validated string types with constraints

# 8-digit synset identifier
type SynsetOffset = Annotated[
    str,
    Field(
        pattern=WORDNET_OFFSET_PATTERN,
        description="8-digit zero-padded synset offset (e.g., '00001740')",
    ),
]

# WordNet sense key with full format validation
type SenseKey = Annotated[
    str,
    Field(
        pattern=WORDNET_SENSE_KEY_PATTERN,
        description="WordNet sense key (e.g., 'abandon%2:40:01::')",
    ),
]

# Lexical ID for distinguishing words in same synset
type LexID = Annotated[
    int,
    Field(
        ge=0,
        le=15,
        description="Lexical ID (0-15) for word disambiguation in synset",
    ),
]

# Sense number for frequency-based ordering
type SenseNumber = Annotated[
    int,
    Field(
        ge=1,
        description="1-based sense number for frequency ordering",
    ),
]

# Semantic concordance tag count
type TagCount = Annotated[
    int,
    Field(
        ge=0,
        description="Number of times sense appears in semantic concordances",
    ),
]
