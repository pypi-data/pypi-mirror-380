from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AssemblyInfo:
    gc: float
    n50: int
    n_contigs: float
    length: int


def SimpleFastaParser(handle):
    """
    This method is a duplicate of biopython Bio.SeqIO.FastaIO.SimpleFastaParser
    We've copied it to avoid being dependant on biopython within the lib

    """
    # Skip any text before the first record (e.g. blank lines, comments)
    for line in handle:
        if line[0] == ">":
            title = line[1:].rstrip()
            break
    else:
        # no break encountered - probably an empty file
        return

    # Main logic
    # Note, remove trailing whitespace, and any internal spaces
    # (and any embedded \r which are possible in mangled files
    # when not opened in universal read lines mode)
    lines = []
    for line in handle:
        if line[0] == ">":
            yield title, "".join(lines).replace(" ", "").replace("\r", "")
            lines = []
            title = line[1:].rstrip()
            continue
        lines.append(line.rstrip())

    yield title, "".join(lines).replace(" ", "").replace("\r", "")


def compute_metrics(fasta: Path) -> AssemblyInfo:
    """
    Computes: GC content, n50, number of contigs, assembly length
    """
    gcs = 0
    assembly_length = 0
    number_of_contigs = 0
    lengths = []
    with open(fasta, encoding="utf-8") as reader:
        for _, seq in SimpleFastaParser(reader):
            length = len(seq)
            assembly_length += length
            lengths.append(length)
            counter = Counter(seq)
            gcs += counter.get("G", 0)
            gcs += counter.get("C", 0)
            number_of_contigs += 1
    sorted_lengths = sorted(lengths, reverse=True)
    n = assembly_length / 2
    cum_length = 0

    for length in sorted_lengths:
        cum_length += length
        if cum_length >= n:
            n50 = length
            break
    return AssemblyInfo(gcs / assembly_length, n50, number_of_contigs, assembly_length)
