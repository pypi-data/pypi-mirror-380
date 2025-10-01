"""write_hdf5.py: Class to write a resqml hdf5 file and functions for copying hdf5 data."""

# Nexus is a registered trademark of the Halliburton Company

# approach is to register the datasets (arrays) to be written; then write everything in a separate, single function call

import logging

log = logging.getLogger(__name__)

import os
import h5py
import numpy as np

import resqpy.olio.uuid as bu

resqml_path_head = '/RESQML/'  # note: latest fesapi code uses RESQML20
write_bool_as_uint8 = True  # Nexus read fails if bool used as hdf5 element dtype
write_int_as_int32 = True  # only applies if registered dtype is None
global_default_chunks = None
global_default_compression = None


class H5Register():
    """Class for registering arrays and then writing to an hdf5 file."""

    def __init__(self, model, default_chunks = None, default_compression = None):
        """Create a new, empty register of arrays to be written to an hdf5 file."""

        global global_default_chunks
        global global_default_compression

        assert default_chunks is None or (isinstance(default_chunks, str) and
                                          default_chunks in ['auto', 'all', 'slice', 'none'])
        if default_chunks is None:
            default_chunks = global_default_chunks
        assert default_compression is None or (isinstance(default_compression, str) and
                                               default_compression in ['gzip', 'lzf', 'none'])
        if default_compression is None:
            default_compression = global_default_compression
        if default_compression is not None and default_compression != 'none' and (default_chunks is None or
                                                                                  default_chunks == 'none'):
            default_chunks = 'auto'

        self.dataset_dict = {
        }  # dictionary mapping from (object_uuid, group_tail) to (numpy_array, dtype, chunks, compression)
        self.hdf5_path_dict = {}  # dictionary optionally mapping from (object_uuid, group_tail) to hdf5 internal path
        self.model = model
        self.default_chunks = default_chunks
        self.default_compression = default_compression

    def register_dataset(self,
                         object_uuid,
                         group_tail,
                         a,
                         dtype = None,
                         hdf5_internal_path = None,
                         copy = False,
                         chunks = None,
                         compression = None):
        """Register an array to be included as a dataset in the hdf5 file.

        arguments:
           object_uuid (uuid.UUID): the uuid of the object (part) that this array is for
           group_tail (string): the remainder of the hdf5 internal path (following RESQML and
              uuid elements)
           a (numpy array): the dataset (array) to be registered for writing
           dtype (type or string): the required type of the individual elements within the dataset;
              special value of 'pack' may be used to cause a bool array to be packed before writing
           hdf5_internal_path (string, optional): if present, a full hdf5 internal path to use
              instead of the default generated from the uuid
           copy (boolean, default False): if True, a copy of the array will be made at the time of
              registering, otherwise changes made to the array before the write() method is called
              are likely to be in the data that is written
           chunks (str or tuple of ints, optional): if not None, chunked hdf5 storage will be used;
              if str, options are 'auto', 'all', 'slice'
           compression (str, optional): if not None, either 'gzip' or 'lzf'

        returns:
           None

        notes:
           several arrays might belong to the same object;
           if a dtype is given and necessitates a conversion of the array data, the behaviour will
           be as if the copy argument is True regardless of its setting;
           the use of 'pack' as dtype will result in hdf5 data that will not generally be readable
           by non-resqpy applications; when reading packed data, the required shape must be specified;
           packing only takes place over the last axis; do not use packing if the array needs to be
           read or updated in slices, or read a single value at a time with index values;
           if chunks is set to a tuple, it must have the same ndim as a and the shape of a must be
           a mulitple of the entries in the chunks tuple, in each dimension; if chunks is 'all', the
           shape of a will be used as the tuple; if 'auto' then hdf5 auto chunking will be used; if
           'slice' and a has more than one dimension, then the chunks tuple will be the shape of a
           with the first entry replaced with 1
        """

        # log.debug('registering dataset with uuid ' + str(object_uuid) + ' and group tail ' + group_tail)
        assert (len(group_tail) > 0)
        assert a is not None
        assert isinstance(a, np.ndarray)
        assert chunks is None or isinstance(chunks, str) or isinstance(chunks, tuple)
        assert compression is None or (isinstance(compression, str) and compression in ['gzip', 'lzf', 'none'])
        if str(dtype) == 'pack':
            a = np.packbits(a, axis = -1)
            dtype = 'uint8'
        elif dtype is not None:
            a = a.astype(dtype, copy = copy)
        elif copy:
            a = a.copy()
        if chunks is None:
            chunks = self.default_chunks
        if isinstance(chunks, str):
            assert chunks in ['auto', 'all', 'slice', 'none']
            if chunks == 'none':
                chunks = None
            elif chunks == 'auto':
                chunks = True
            elif chunks == 'slice' and a.ndim > 1:
                chunks = tuple([1] + list(a.shape[1:]))
            else:
                chunks = a.shape
        if compression is None:
            compression = self.default_compression
        elif compression == 'none':
            compression = None
        if compression is not None and chunks is None:
            chunks = True
        if group_tail[0] == '/':
            group_tail = group_tail[1:]
        if group_tail[-1] == '/':
            group_tail = group_tail[:-1]
        if (object_uuid, group_tail) in self.dataset_dict.keys():
            log.warning(f'multiple hdf5 registrations for uuid: {object_uuid}; group: {group_tail}')
        self.dataset_dict[(object_uuid, group_tail)] = (a, dtype, chunks, compression)
        if hdf5_internal_path:
            self.hdf5_path_dict[(object_uuid, group_tail)] = hdf5_internal_path

    def write_fp(self, fp, use_int32 = None):
        """Write or append to an hdf5 file, writing the pre-registered datasets (arrays).

        arguments:
           fp: an already open h5py._hl.files.File object

        returns:
           None

        note:
           the file handle fp must have been opened with mode 'w' or 'a'
        """

        # note: in resqml, an established hdf5 file has a uuid and should therefore be immutable
        #       this function allows appending to any hdf5 file; calling code should set a new uuid when needed
        assert (fp is not None)
        if use_int32 is None:
            use_int32 = write_int_as_int32
        for (object_uuid, group_tail) in self.dataset_dict.keys():
            if (object_uuid, group_tail) in self.hdf5_path_dict.keys():
                internal_path = self.hdf5_path_dict[(object_uuid, group_tail)]
            else:
                internal_path = resqml_path_head + str(object_uuid) + '/' + group_tail
            (a, dtype, chunks, compression) = self.dataset_dict[(object_uuid, group_tail)]
            if dtype is None:
                dtype = a.dtype
                if use_int32 and str(dtype) == 'int64':
                    dtype = 'int32'
            if write_bool_as_uint8 and str(dtype).lower().startswith('bool'):
                dtype = 'uint8'
            # log.debug('Writing hdf5 dataset ' + internal_path + ' of size ' + str(a.size) + ' type ' + str(dtype))
            if chunks is None:
                fp.create_dataset(internal_path, data = a, dtype = dtype)
            elif compression is None:
                fp.create_dataset(internal_path, data = a, dtype = dtype, chunks = chunks)
            else:
                fp.create_dataset(internal_path, data = a, dtype = dtype, chunks = chunks, compression = compression)

    def write(self, file = None, mode = 'w', release_after = True, use_int32 = None):
        """Create or append to an hdf5 file, writing the pre-registered datasets (arrays).

        arguments:
           file: either a string being the file path, or an already open h5py._hl.files.File object;
              if None (recommended), the file is opened through the model object's hdf5 management
              functions
           mode (string, default 'w'): the mode to open the file in; only relevant if file is a path;
              must be 'w' or 'a' for (over)write or append
           release_after (bool, default True): if True, h5_release() is called after the write
           use_int32 (bool, optional): if True, int64 arrays will be written as int32; if None,
              global default will be used (currently True); if False, int64 arrays will be
              written as such

        returns:
           None
        """

        # note: in resqml, an established hdf5 file has a uuid and should therefore be immutable
        #       this function allows appending to any hdf5 file;
        #       strictly, calling code should set a new uuid when needed, in practice not essential
        if len(self.dataset_dict) == 0:
            return
        if file is None:
            file = self.model.h5_access(mode = mode)
        elif isinstance(file, str):
            # log.debug(f'writing to hdf5 file: {file}')
            file = self.model.h5_access(mode = mode, file_path = file)
        if mode == 'a' and isinstance(file, str) and not os.path.exists(file):
            mode = 'w'
        assert isinstance(file, h5py._hl.files.File)
        self.write_fp(file, use_int32 = use_int32)
        if release_after:
            self.model.h5_release()


def copy_h5(file_in, file_out, uuid_inclusion_list = None, uuid_exclusion_list = None, mode = 'w'):
    """Create a copy of an hdf5, optionally including or excluding arrays with specified uuids.

    arguments:
       file_in (string): path of existing hdf5 file to be duplicated
       file_out (string): path of output hdf5 file to be created or appended to (see mode)
       uuid_inclusion_list (list of uuid.UUID, optional): if present, the uuids to be included
          in the output file
       uuid_exclusion_list (list of uuid.UUID, optional): if present, the uuids to be excluded
          from the output file
       mode (string, default 'w'): mode to open output file with; must be 'w' or 'a' for
          (over)write or append respectively

    returns:
       number of hdf5 groups (uuid's) copied

    notes:
       at most one of uuid_inclusion_list and uuid_exclusion_list should be passed;
       if neither are passed, all the datasets (arrays) in the input file are copied to the
       output file
    """

    #  note: if both inclusion and exclusion lists are present, exclusion list is ignored
    assert file_out != file_in, 'identical input and output files specified for hdf5 copy'
    assert uuid_inclusion_list is None or uuid_exclusion_list is None,  \
       'inclusion and exclusion lists both specified for hdf5 copy; at most one allowed'
    checking_uuid = uuid_inclusion_list is not None or uuid_exclusion_list is not None
    assert mode in ['w', 'a']
    copy_count = 0
    with h5py.File(file_out, mode) as fp_out:
        assert fp_out is not None, 'failed to open output hdf5 file: ' + file_out
        with h5py.File(file_in, 'r') as fp_in:
            assert fp_in is not None, 'failed to open input hdf5 file: ' + file_in
            main_group_in = fp_in['RESQML']
            assert main_group_in is not None, 'failed to find RESQML group in hdf5 file: ' + file_in
            if mode == 'w':
                main_group_out = fp_out.create_group('RESQML')
            elif mode == 'a':
                try:
                    main_group_out = fp_out['RESQML']
                except Exception:
                    main_group_out = fp_out.create_group('RESQML')
            else:
                main_group_out = fp_out['RESQML']
            for group in main_group_in:
                if checking_uuid:
                    uuid = bu.uuid_from_string(group)
                    if uuid_inclusion_list is not None:
                        if uuid not in uuid_inclusion_list:
                            if uuid is None:
                                log.warning('RESQML group name in hdf5 file does not start with a uuid, skipping: ' +
                                            str(group))
                            continue
                    else:  # uuid_exclusion_list is not None
                        if uuid in uuid_exclusion_list:
                            continue
                        if uuid is None:  # will still be copied
                            log.warning('RESQML group name in hdf5 file does not start with a uuid: ' + str(group))
                if group in main_group_out:
                    log.warning('not copying hdf5 data due to pre-existence for: ' + str(group))
                    continue
                # log.debug('copying hdf5 data for uuid: ' + group)
                main_group_in.copy(group,
                                   main_group_out,
                                   expand_soft = True,
                                   expand_external = True,
                                   expand_refs = True)
                copy_count += 1
    return copy_count


def copy_h5_path_list(file_in, file_out, hdf5_path_list, mode = 'w', chunks = None, compression = None):
    """Create a copy of some hdf5 datasets (or groups), identified as a list of hdf5 internal paths.

    arguments:
       file_in (string): path of existing hdf5 file to be copied from
       file_out (string): path of output hdf5 file to be created or appended to (see mode)
       hdf5_path_list (list of string): the hdf5 internal paths of the datasets (or groups) to be copied
       mode (string, default 'w'): mode to open output file with; must be 'w' or 'a' for
          (over)write or append respectively
       chunks (string, optional): if present, one of 'auto', 'all', 'slice'; if None, global default
          will be used; any of the valid strings will actually be treated as 'auto'
       compression (string, optional): if present, either 'gzip' or 'lzf'; if None, global default
          will be used

    returns:
       number of hdf5 datasets (or groups) copied
    """

    global global_default_chunks
    global global_default_compression

    #  note: if both inclusion and exclusion lists are present, exclusion list is ignored
    assert file_out != file_in, 'identical input and output files specified for hdf5 copy'
    assert hdf5_path_list is not None
    assert mode in ['w', 'a']
    assert chunks is None or (isinstance(chunks, str) and chunks in ['auto', 'all', 'slice'])
    assert compression is None or (isinstance(compression, str) and compression in ['gzip', 'lzf'])
    if chunks is None:
        chunks = global_default_chunks
    if compression is None:
        compression = global_default_compression
    if compression is not None and chunks is None:
        chunks = 'auto'

    copy_count = 0
    with h5py.File(file_out, mode) as fp_out:
        assert fp_out is not None, f'failed to open output hdf5 file: {file_out}'
        with h5py.File(file_in, 'r') as fp_in:
            assert fp_in is not None, f'failed to open input hdf5 file: {file_in}'
            for path in hdf5_path_list:
                if path in fp_out:
                    log.warning(f'not copying hdf5 data due to pre-existence for: {path}')
                    continue
                assert path in fp_in, f'internal path {path} not found in hdf5 file {file_in}'
                # log.debug(f'copying hdf5 data for: {path}')
                build = ''
                group_list = list(path.split(sep = '/'))
                assert len(group_list) > 1, f'no hdf5 group(s) in internal path {path}'
                for w in group_list[:-1]:
                    if w:
                        build += '/' + w
                        if build not in fp_out:
                            fp_out.create_group(build)
                build += '/' + group_list[-1]
                if chunks is None or chunks == 'none':
                    fp_out.create_dataset(build, data = fp_in[path])
                elif compression is None or compression == 'none':
                    fp_out.create_dataset(build, data = fp_in[path], chunks = True)
                else:
                    fp_out.create_dataset(build, data = fp_in[path], chunks = True, compression = compression)
                # fp_in.copy(path, fp_out[path], expand_soft = True, expand_external = True, expand_refs = True)
                copy_count += 1
    return copy_count


def change_uuid(file, old_uuid, new_uuid):
    """Changes hdf5 internal path (group name) for part, switching from old to new uuid.

    notes:
       this is low level functionality not usually called directly;
       the function assumes that hdf5 internal path names conform to the format that resqpy uses
       when writing data, namely /RESQML/uuid/tail...
    """

    assert file, 'hdf5 file name missing'
    assert old_uuid is not None and new_uuid is not None, 'missing uuid'

    def change_uuid_fp(fp, old_uuid, new_uuid):
        main_group = fp[resqml_path_head.strip('/')]
        old_group = main_group[str(old_uuid)]
        main_group[str(new_uuid)] = old_group
        del main_group[str(old_uuid)]

    if isinstance(file, h5py._hl.files.File):
        change_uuid_fp(file, old_uuid, new_uuid)
    else:
        assert isinstance(file, str)
        with h5py.File(file, 'r+') as fp:
            change_uuid_fp(fp, old_uuid, new_uuid)


def set_global_default_chunks_and_compression(chunks, compression):
    """Set global default values for hdf5 chunks and compression.

    arguments:
        chunks (str, or None): if str, one of 'auto', 'all', or 'slice'
        compression (str, or None): if str, either 'gzip' or 'lzf'
    """

    global global_default_chunks
    global global_default_compression
    assert chunks is None or (isinstance(chunks, str) and chunks in ['auto', 'all', 'slice', 'none'])
    assert compression is None or (isinstance(compression, str) and compression in ['gzip', 'lzf', 'none'])
    global_default_chunks = chunks
    global_default_compression = compression
