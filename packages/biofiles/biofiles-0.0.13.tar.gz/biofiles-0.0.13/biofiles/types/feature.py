from dataclasses import dataclass

from biofiles.common import Strand


__all__ = ["Feature", "Gene", "Transcript", "Exon", "UTR", "ThreePrimeUTR"]


@dataclass(frozen=True)
class Feature:
    sequence_id: str
    source: str
    type_: str

    start_original: int
    end_original: int
    # Original values as they were present in the file (1-based inclusive for .gff and .gtf).

    start_c: int
    end_c: int
    # Standardized ("C-style") 0-based values, start inclusive, end exclusive.

    score: float | None
    strand: Strand | None
    phase: int | None
    attributes: dict[str, str]

    id: str | None
    parent: "Feature | None"
    children: tuple["Feature", ...]


# Custom types for particular kinds of features:


@dataclass(frozen=True)
class Gene(Feature):
    name: str
    biotype: str
    transcripts: tuple["Transcript", ...]


@dataclass(frozen=True)
class Transcript(Feature):
    gene: Gene
    exons: tuple["Exon", ...]


@dataclass(frozen=True)
class Exon(Feature):
    gene: Gene
    transcript: Transcript
    cds: "CDS | None"


@dataclass(frozen=True)
class UTR(Feature):
    gene: Gene
    transcript: Transcript


@dataclass(frozen=True)
class ThreePrimeUTR(UTR):
    pass


@dataclass(frozen=True)
class CDS(Feature):
    gene: Gene
    transcript: Transcript
    exon: Exon
