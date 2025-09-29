"""Functions for reading DICOM files ith dicomity"""

from typing import Optional

import numpy as np
from pydicom import filereader, FileDataset

from dicomity.dictionary import DicomDictionary
from dicomity.types import GroupingMetadata


def read_dicom_image(file_name: str) -> np.array:
    meta = filereader.dcmread(file_name, stop_before_pixels=False)
    return meta.pixel_array


def read_dicom_tags(
        file_name: str,
        dictionary: Optional[DicomDictionary] = None,
        specific_tags: Optional[list[str]] = None
) -> FileDataset:
    # ToDo: reading of specific tags is not currently supported
    # if dictionary:
    #     specific_tags = dictionary.allTags()

    meta = filereader.dcmread(
        file_name,
        stop_before_pixels=True
    #     specific_tags=specific_tags
    )
    return meta


def read_grouping_metadata(file_name: str) -> GroupingMetadata:
    meta = filereader.dcmread(fp=file_name,
                              stop_before_pixels=True,
                              specific_tags=GroupingMetadata.groupingTags())
    return GroupingMetadata.fromPyDicom(meta)


def dicomInfo(file_name):
    """Reads the metaheader data from a Dicom file"""
    return filereader.dcmread(file_name, stop_before_pixels=True)


def DMdicominfo(file_name, dictionary=None):
    """Read metadata from a Dicom file

    Usage:
        metadata = DMdicominfo(fileName)

        fileName: path and filename of the file to test

     Returns:
        a structure containing the metadata from a Dicom file
    """

    if not dictionary:
        dictionary = DicomDictionary.essential_dictionary_without_pixel_data()

    metadata = read_dicom_tags(file_name, dictionary)

    # The filename is not really part of the metadata but is included for
    # compatibility with Matlab's image processing toolbox
    # metadata["Filename"] = file_name
    return metadata


def is_dicom(file_name: str) -> bool:
    """Test whether a file is in DICOM format

    Uses a simple test for the DICM preamble - this is very fast but
    may occasionally produce false positives.

    For a more robust guarantee that a file really is DICOM, first call this
    function and if True, try to parse the file - if the tag data cannot be
    parsed then it is likely not a DICOM file

    Args:
        file_name: path and filename of the file to test

    Returns:
        True if the file appears to be a Dicom file
    """

    with open(file_name, "rb") as f:
        f.seek(128)
        preamble = f.read(4)
        return preamble == b"DICM"


def is_dicom_image_file(file_name: str) -> bool:
    """Tests if a file is a DICOM file but not a DICOMDIR file

    Args:
        file_name: Full path to file

    Returns:
        True if the file is DICOM and not a DICOMDIR
    """
    return file_name != 'DICOMDIR' and is_dicom(file_name)
