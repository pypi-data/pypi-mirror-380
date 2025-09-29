import logging
from copy import deepcopy

from ..utils.format import format_chr

# Logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Change to DEBUG for more verbosity
if not logger.handlers:
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        level=logging.INFO,
    )


class GenomicRangeMixin:
    """
    Mixin class providing genomic range filtering functionality for PyMutation objects.
    
    This mixin adds the ability to filter by genomic coordinates and gene names,
    following the same architectural pattern as other mixins in the project.
    """

    def region(self, chrom, start: int, end: int):
        """
        Filter this PyMutation by a genomic range using the CHROM and POS columns.
        Supports one or multiple chromosomes. Attempts to use pandas' PyArrow engine
        for improved performance when available.

        Parameters
        ----------
        chrom : str | list[str] | tuple[str, ...] | set[str]
            Chromosome(s) to filter by (e.g., 'chr1', '1', 'X', 'Y').
            You can pass a single chromosome as a string, a list/tuple/set of
            chromosomes, or a comma-separated string like '1,2,X'.
        start : int
            Start position of the range (inclusive).
        end : int
            End position of the range (inclusive).

        Returns
        -------
        PyMutation
            A new instance of PyMutation containing only the rows that fall within
            the specified genomic region(s). The metadata is copied and updated to
            record the applied filter.

        Raises
        ------
        KeyError
            If the DataFrame does not contain the required 'CHROM' or 'POS' columns.
        """
        df = self.data

        # Verify required columns exist
        if "CHROM" not in df.columns:
            logger.error("Column 'CHROM' does not exist in the DataFrame")
            raise KeyError("Column 'CHROM' does not exist in the DataFrame")
        if "POS" not in df.columns:
            logger.error("Column 'POS' does not exist in the DataFrame")
            raise KeyError("Column 'POS' does not exist in the DataFrame")

        # Normalize chromosome input to a list and format for consistency
        if isinstance(chrom, (list, tuple, set)):
            chrom_list = list(chrom)
        elif isinstance(chrom, str):
            # Allow comma/semicolon separated values e.g., "1,2,X" or "1;2;X"
            if "," in chrom or ";" in chrom:
                sep = "," if "," in chrom else ";"
                chrom_list = [c.strip() for c in chrom.split(sep) if c.strip()]
            else:
                chrom_list = [chrom]
        else:
            chrom_list = [str(chrom)]

        chroms_formatted = [format_chr(str(c)) for c in chrom_list]
        if len(chroms_formatted) == 1:
            logger.info(f"Chromosome formatted: '{chrom_list[0]}' -> '{chroms_formatted[0]}'")
        else:
            logger.info(f"Chromosomes formatted: {chrom_list} -> {chroms_formatted}")

        # Try to use pyarrow if available
        try:
            logger.info("Attempting to use PyArrow optimization")

            # Convert relevant columns to pyarrow types for optimization
            df_work = df.copy(deep=True)

            # Format CHROM column before optimization
            df_work["CHROM"] = df_work["CHROM"].astype(str).map(format_chr)

            # Optimize CHROM with string[pyarrow] if not already
            if not str(df_work["CHROM"].dtype).startswith("string"):
                df_work["CHROM"] = df_work["CHROM"].astype("string[pyarrow]")

            # Optimize POS with int64[pyarrow] if not already
            if not str(df_work["POS"].dtype).startswith("int") or "pyarrow" not in str(df_work["POS"].dtype):
                df_work["POS"] = df_work["POS"].astype("int64[pyarrow]")

            # Comparison operations now use pyarrow engine internally
            # This is more efficient than standard pandas operations
            if len(chroms_formatted) == 1:
                chrom_mask = df_work["CHROM"] == chroms_formatted[0]  # Uses pyarrow string comparison
            else:
                chrom_mask = df_work["CHROM"].isin(chroms_formatted)  # Membership comparison
            pos_start_mask = df_work["POS"] >= start  # Uses pyarrow int comparison
            pos_end_mask = df_work["POS"] <= end  # Uses pyarrow int comparison

            # Combine masks (also optimized with pyarrow)
            mask = chrom_mask & pos_start_mask & pos_end_mask

            # Filtering maintains pyarrow types
            new_df = df_work[mask].copy(deep=True)
            logger.info("PyArrow optimization successful")

        except ImportError:
            logger.warning("PyArrow not available, using standard pandas operations")
            # pyarrow is not available, use standard pandas operations
            # Format CHROM column in original DataFrame
            df_formatted = df.copy()
            df_formatted["CHROM"] = df_formatted["CHROM"].astype(str).map(format_chr)

            if len(chroms_formatted) == 1:
                chrom_mask = df_formatted["CHROM"] == chroms_formatted[0]
            else:
                chrom_mask = df_formatted["CHROM"].isin(chroms_formatted)

            mask = (
                    chrom_mask &
                    (df_formatted["POS"] >= start) &
                    (df_formatted["POS"] <= end)
            )
            new_df = df_formatted[mask].copy()

        except Exception as e:
            logger.warning(f"PyArrow optimization failed: {e}, falling back to standard operations")
            # Any other error with pyarrow, use standard operations
            # Format CHROM column in original DataFrame
            df_formatted = df.copy()
            df_formatted["CHROM"] = df_formatted["CHROM"].astype(str).map(format_chr)

            if len(chroms_formatted) == 1:
                chrom_mask = df_formatted["CHROM"] == chroms_formatted[0]
            else:
                chrom_mask = df_formatted["CHROM"].isin(chroms_formatted)

            mask = (
                    chrom_mask &
                    (df_formatted["POS"] >= start) &
                    (df_formatted["POS"] <= end)
            )
            new_df = df_formatted[mask].copy()

        # Create updated metadata with information about the applied filter
        updated_metadata = deepcopy(self.metadata)

        # Create filter description using the formatted chromosome(s)
        chroms_desc = ",".join(chroms_formatted)
        filter_description = f"genomic_region:{chroms_desc}:{start}-{end}"

        # Add the filter to the existing filters list
        if hasattr(updated_metadata, 'filters') and updated_metadata.filters:
            updated_metadata.filters = updated_metadata.filters + [filter_description]
        else:
            updated_metadata.filters = [filter_description]

        # Log information
        original_count = len(df)
        filtered_count = len(new_df)
        logger.info(f"Genomic filter applied: {chroms_desc}:{start}-{end}")
        logger.info(f"Variants before filter: {original_count}")
        logger.info(f"Variants after filter: {filtered_count}")
        logger.info(f"Variants filtered out: {original_count - filtered_count}")

        if filtered_count == 0:
            logger.warning(f"No variants found in region(s) {chroms_desc}:{start}-{end}")
        elif filtered_count == original_count:
            logger.warning("Filter did not remove any variants - check region coordinates")
        else:
            logger.info(f"Successfully filtered genomic region(s): {chroms_desc}:{start}-{end}")

        # Return new instance of the same type with updated metadata
        return type(self)(data=new_df, metadata=updated_metadata, samples=self.samples)

    def gen_region(self, gen_name: str):
        """
        Filter data by a specific gene and return a new PyMutation instance.

        If source_format is MAF, searches in the Hugo_Symbol column (case-insensitive).
        For other formats, searches in available gene columns.

        Parameters
        ----------
        gen_name : str
            Name of the gene to filter by (e.g., 'KRAS', 'TP53', 'BRCA1').

        Returns
        -------
        PyMutation
            A new instance of PyMutation containing only the rows that match
            the specified gene. The metadata is copied and updated to
            record the applied filter.

        Raises
        ------
        ValueError
            If no gene columns are found in the data or if the Hugo_Symbol
            column is not found in MAF format data.
        """
        logger.info(f"Applying gene filter for: {gen_name}")
        logger.info(f"Source format detected: {self.metadata.source_format}")

        # Check if source_format is MAF
        if self.metadata.source_format.upper() == "MAF":
            logger.info("Processing MAF format - looking for Hugo_Symbol column")

            # Search for Hugo_Symbol column (case-insensitive)
            hugo_column = None
            for col in self.data.columns:
                if col.lower() == "hugo_symbol":
                    hugo_column = col
                    break

            if hugo_column is None:
                logger.error("Hugo_Symbol column not found in MAF data")
                raise ValueError("Hugo_Symbol column not found in MAF data")

            logger.info(f"Found Hugo_Symbol column: {hugo_column}")

            # Filter by the specified gene (case-insensitive)
            # Strip whitespace from gene name for proper comparison
            gen_name_clean = gen_name.strip()
            filtered_data = self.data[
                self.data[hugo_column].str.upper() == gen_name_clean.upper()
                ]

            # Create filter description using the found column
            filter_description = f"gene_filter:{hugo_column}:{gen_name}"

        else:
            pass

        # Create updated metadata with information about the applied filter
        updated_metadata = deepcopy(self.metadata)

        # Add the filter to the existing filters list
        if hasattr(updated_metadata, 'filters') and updated_metadata.filters:
            updated_metadata.filters = updated_metadata.filters + [filter_description]
        else:
            updated_metadata.filters = [filter_description]

        # Log filtering information
        original_count = len(self.data)
        filtered_count = len(filtered_data)

        logger.info(f"Gene filter applied: {gen_name}")
        logger.info(f"Variants before filter: {original_count}")
        logger.info(f"Variants after filter: {filtered_count}")
        logger.info(f"Variants filtered out: {original_count - filtered_count}")

        if filtered_count == 0:
            logger.warning(f"No variants found for gene: {gen_name}")
        elif filtered_count == original_count:
            logger.warning(f"Filter did not remove any variants - check gene name: {gen_name}")
        else:
            logger.info(f"Successfully filtered data for gene: {gen_name}")

        # Return new PyMutation instance with filtered data and updated metadata
        return type(self)(data=filtered_data.copy(), metadata=updated_metadata, samples=self.samples)
