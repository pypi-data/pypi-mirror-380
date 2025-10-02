# AEGIS: Annotation Extraction Genomic Integration Suite

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-brightgreen.svg)](https://www.python.org/downloads/)

**AEGIS** is a powerful and flexible Python-based suite for the manipulation, analysis, and integration of genomic annotations. It provides a robust, object-oriented framework for working with genomic data, enabling complex analyses and data transformations with intuitive, high-level commands.

## Key Features

- **Object-Oriented Design**: AEGIS represents genomic features (genes, transcripts, exons, etc.) as a hierarchical system of Python classes, providing a clean and intuitive API for data manipulation.
- **Comprehensive Annotation Handling**: Seamlessly parse, process, and export genomic annotations in GFF3 format.
- **Sequence Extraction**: Easily extract sequences for any genomic feature, including genes, transcripts, CDS, proteins, and promoters.
- **Comparative Genomics**: Perform comparative analyses, such as identifying orthologs and syntenic regions between different species.
- **Extensible and Modular**: The modular design of AEGIS allows for easy extension and integration with other bioinformatics tools and pipelines.

## The AEGIS Class System

The core of AEGIS is its sophisticated class system, which models the hierarchical nature of genomic annotations. This object-oriented approach provides several key advantages over traditional, line-by-line processing of annotation files:

- **Intuitive Data Representation**: Genomic features are not just lines in a file; they are objects with properties and relationships. A `Gene` object contains `Transcript` objects, which in turn contain `Exon` and `CDS` objects. This makes the code more readable, maintainable, and less error-prone.
- **Data Integrity**: The class system enforces data consistency. For example, when a `Gene` object is updated, all its associated `Transcript` and sub-feature objects are updated accordingly, ensuring that the annotation remains coherent.
- **Complex Queries and Manipulations**: The object-oriented structure allows for complex queries and manipulations that would be difficult to perform with traditional text-based tools. For example, you can easily retrieve all coding transcripts for a specific gene, or calculate the total length of all exons in a given transcript.
- **Code Reusability**: The class-based design promotes code reusability. Once you have defined a class for a specific genomic feature, you can reuse it in different parts of your analysis pipeline.

### Core Classes

- **`Genome`**: Represents a genome, containing a collection of `Scaffold` objects.
- **`Scaffold`**: Represents a chromosome or scaffold, containing the sequence and a collection of `Gene` objects.
- **`Annotation`**: The main container for genomic annotations, holding a collection of `Gene` objects.
- **`Gene`**: Represents a gene, containing one or more `Transcript` objects.
- **`Transcript`**: Represents a transcript, containing `Exon`, `CDS`, and `UTR` objects.
- **`Exon`**, **`CDS`**, **`UTR`**, **`Intron`**: Represent the sub-features of a transcript.
- **`Protein`**, **`Promoter`**: Represent other biological features of interest.

## Installation

You can install and run AEGIS in several ways. Using a container (Docker or Singularity) is the recommended approach as it handles all dependencies automatically.

### Using Docker (Recommended)

If you have Docker installed, you can easily pull and run the pre-built AEGIS image from Docker Hub. This image includes AEGIS and all third-party software used for orthology analyses.

**1. Pull the image from Docker Hub:**

```bash
docker pull tomsbiolab/aegis
```

**2. Run an AEGIS command:**
The following command runs `aegis-extract` on a test dataset. The `-v` flag is crucial as it makes your current directory accessible inside the container.

```bash
docker run --rm -ti -v `pwd`:`pwd` -w `pwd` tomsbiolab/aegis aegis-extract -f protein test_data/arabidopsis_araport11.gff3 test_data/arabidopsis_tair10.fasta
```

**3. (Optional) Build the image locally:**
If you want to build the image from the source code in this repository, you can use the provided `Dockerfile`.

```bash
docker build -t aegis-local .
```
You can then run your local image by replacing `tomsbiolab/aegis` with `aegis-local`.

### Using Singularity

For high-performance computing (HPC) environments where Docker is not available, Singularity is an excellent alternative.

**1. Build the Singularity image from Docker Hub:**

```bash
singularity build aegis.sif docker://tomsbiolab/aegis
```

This will create a single `aegis.sif` file in your current directory.

**2. Run an AEGIS command:**
Use the `singularity run` command to execute AEGIS. The `-B` flag mounts your current directory into the container.

```bash
singularity run -B `pwd`:`pwd` aegis.sif aegis-extract -f protein test_data/arabidopsis_tair10.gff3 test_data/arabidopsis_tair10.fasta
```

### From PyPI (Python Package Index)

Easiest way to install, however, some dependencies will be missing (such as Liftoff, LiftOn, MCScan, Orthofinder, Diamond...). If you are planning to use aegis-orthology you will require these, so to avoid having to install the dependencies yourself see docker and singularity options above. 

```bash
pip3 install aegis-bio
```

### From Source

Alternatively, you can install AEGIS directly from the source by cloning the repository and installing the required Python dependencies.

```bash
git clone https://github.com/Tomsbiolab/aegis.git
cd aegis
pip3 install -r requirements.txt
pip3 install -e .
```

## Usage

Aegis is designed to be used as a library in your Python scripts or directly through the CLI

### CLI commands

All of the commands are called with aegis-{subcommand} in a terminal:

- Extract
	- Extracts all kinds of fasta features from an annotation.
- Overlap
	- Overlap quantification of gene models (and their subfeatures) between any number of gffs associated to same genome
- Rename
	- Rename gff feature ids.
- Orthology
	- Comprehensive multi-tool comparison of gene ids from different genomes. All evidence is summarised and converted to a qualitative scale, allowing to select orthologues by confidence level.
- Summary
	- Outputs tabular annotation stats as well as a series of plots.
- Tidy
	- Cleans annotation files, fixes errors, issues warnings, and provides custom formatting options for extra flexibility/compatibility with third party tools.
- Tidy-genome
	- Allows removal and/or renaming of genome features.
- Merge
	- Custom merge of any number of gffs, prevent id clashes and control redundancy in same loci.
- Symbols
	- Allows to add gene symbols into an annotation file based on tabular input
- Motifs
	- Plots frequency of a particular DNA motif (allowing regular expressions) in promoter regions of chosen gene lists, all genome’s genes, and random gene lists.
- Subset
	- Make all sorts of subsets of an annotation file, select by desired features (coding/non-coding) or even create lite versions for debugging/testing.
- Prune
	- Removes features based on id lists (transcript or gene level) and solves any derived issues, i.e. remove a gene if all of its transcripts are removed
- Reformat:
	- Converts between gtf and gff formats.

### As a Python library

Here is a simple example of how to load an annotation and extract the sequences of all genes:

```python
from aegis.annotation import Annotation
from aegis.genome import Genome

# Load the genome and annotation
genome = Genome(name = "my_genome", genome_file_path = "path/to/genome.fasta")
annotation = Annotation(name = "my_annotation", annot_file_path = "path/to/annotation.gff3", genome)

# Generate and export gene sequences
annotation.generate_sequences(genome)
annotation.export_genes()
```
## Documentation
For further and more detailed information on how to use the **AEGIS** package, including **Jupyter Notebook examples**, please refer to the **GitHub Wiki**. The wiki provides comprehensive guides and tutorials to help you get the most out of the suite.

**Link to Wiki:** https://github.com/Tomsbiolab/aegis/wiki

## Contributing

Contributions to AEGIS are welcome! Please feel free to submit a pull request or open an issue on the GitHub repository.

## License

AEGIS is licensed under the GNU General Public License v3.0. See the `LICENSE.md` file for more details. Third-party tools included in the Docker image are distributed under their respective licenses.
