"""WellboreFrame class."""

# Nexus is a registered trademark of the Halliburton Company
# RMS and ROXAR are registered trademarks of Roxar Software Solutions AS, an Emerson company

import logging

log = logging.getLogger(__name__)

import numpy as np

import resqpy.olio.uuid as bu
import resqpy.olio.write_hdf5 as rwh5
import resqpy.olio.xml_et as rqet
import resqpy.organize as rqo
import resqpy.property as rqp
import resqpy.well as rqw
import resqpy.well.well_utils as rqwu
from resqpy.olio.base import BaseResqpy
from resqpy.olio.xml_namespaces import curly_namespace as ns


class WellboreFrame(BaseResqpy):
    """Class for RESQML WellboreFrameRepresentation objects (supporting well log Properties)

    RESQML documentation:

       Representation of a wellbore that is organized along a wellbore trajectory by its MD values.
       RESQML uses MD values to associate properties on points and to organize association of
       properties on intervals between MD points.

    Roughly equivalent to a Techlog "dataset" object with a given depth reference.

    The `logs` attribute is a :class:`resqpy.property.WellLogCollection` of all logs in the frame.
    """

    resqml_type = 'WellboreFrameRepresentation'

    def __init__(self,
                 parent_model,
                 uuid = None,
                 trajectory = None,
                 mds = None,
                 represented_interp = None,
                 title = None,
                 originator = None,
                 extra_metadata = None):
        """Creates a new wellbore frame object and optionally loads it from xml or list of measured depths.

        arguments:
           parent_model (model.Model object): the model which the new wellbore frame belongs to
           uuid (optional): the uuid of an existing wellbore frame; if present, remaining arguments are
              ignored
           trajectory (Trajectory object, optional): the trajectory of the well; required if loading from
              list of measured depths
           mds (optional numpy 1D array, tuple or list of floats): ordered list of measured depths which
              will constitute the frame; ignored if uuid is not None; units are those of trajectory mds
           represented_interp (wellbore interpretation object, optional): if present, is noted as the wellbore
              interpretation object which this frame relates to; ignored if uuid is not None
           title (str, optional): the citation title to use for a new wellbore frame;
              ignored if uuid is not None
           originator (str, optional): the name of the person creating the wellbore frame, defaults to login id;
              ignored if uuid is not None
           extra_metadata (dict, optional): string key, value pairs to add as extra metadata for the wellbore frame;
              ignored if uuid is not None

        returns:
           the newly created wellbore frame object

        note:
           if initialising from a list of measured depths, the wellbore trajectory object must already exist

        :meta common:
        """

        #: associated wellbore trajectory, an instance of :class:`resqpy.well.Trajectory`.
        self.trajectory = trajectory
        self.trajectory_uuid = None if trajectory is None else trajectory.uuid

        #: instance of :class:`resqpy.organize.WellboreInterpretation`
        self.wellbore_interpretation = represented_interp
        self.wellbore_feature = None
        self.feature_and_interpretation_to_be_written = False

        #: number of measured depth nodes, each being an entry or exit point of trajectory with a cell
        self.node_count = None

        #: node_count measured depths (in same units and datum as trajectory) of cell entry and/or exit points
        self.node_mds = None

        #: all properties, including indexable of nodes or intervals; an instance of :class:`resqpy.property.PropertyCollection`
        self.property_collection = None
        #: all logs associated with the wellbore frame; an instance of :class:`resqpy.property.WellLogCollection`
        self.logs = None

        super().__init__(model = parent_model,
                         uuid = uuid,
                         title = title,
                         originator = originator,
                         extra_metadata = extra_metadata)

        if self.root is None and trajectory is not None and mds is not None:
            assert len(mds) > 1, 'at least two measured depth nodes needed for wellbore frame'
            self.node_count = len(mds)
            self.node_mds = np.array(mds)
            assert self.node_mds is not None and self.node_mds.ndim == 1

    def _load_from_xml(self):
        """Loads the wellbore frame object from an xml node.

        Also loads the associated data either from an hdf5 file or generated from a
        lattice array definition.
        """

        # NB: node is the root level xml node, not a node in the md list!

        node = self.root
        assert node is not None

        trajectory_uuid = bu.uuid_from_string(rqet.find_nested_tags_text(node, ['Trajectory', 'UUID']))
        assert trajectory_uuid is not None, 'wellbore frame trajectory reference not found in xml'
        if self.trajectory is None:
            self.trajectory = rqw.Trajectory(self.model, uuid = trajectory_uuid)
        else:
            assert bu.matching_uuids(self.trajectory.uuid, trajectory_uuid), 'wellbore frame trajectory uuid mismatch'

        self.node_count = rqet.find_tag_int(node, 'NodeCount')
        assert self.node_count is not None, 'node count not found in xml for wellbore frame'
        assert self.node_count > 1, 'fewer than 2 nodes for wellbore frame'

        mds_node = rqet.find_tag(node, 'NodeMd')
        assert mds_node is not None, 'wellbore frame measured depths hdf5 reference not found in xml'
        if rqet.node_type(mds_node) == "DoubleLatticeArray":
            rqwu.load_lattice_array(self, mds_node, "node_mds", self.trajectory)
            self.node_count = self.node_mds.size
        else:
            rqwu.load_hdf5_array(self, mds_node, "node_mds")

        assert self.node_mds is not None and self.node_mds.ndim == 1 and self.node_mds.size == self.node_count

        interp_uuid = rqet.find_nested_tags_text(node, ['RepresentedInterpretation', 'UUID'])
        if interp_uuid is None:
            self.wellbore_interpretation = None
        else:
            self.wellbore_interpretation = rqo.WellboreInterpretation(self.model, uuid = interp_uuid)

        self.extract_property_collection()
        self.logs = rqp.WellLogCollection(frame = self)

    def extract_crs_uuid(self):
        """Returns the uuid of the coordinate reference system used by the related trajectory."""

        if self.trajectory is None:
            return None
        return self.trajectory.crs_uuid

    def extract_property_collection(self):
        """Returns property collection for the frame, creating attribute if not already established."""
        if self.property_collection is None:
            self.property_collection = rqp.PropertyCollection(support = self)
        return self.property_collection

    def extract_log_collection(self, refresh = False):
        """Returns collection of well logs (nodes properties) for this frame, creating if refresh or not already established."""
        if refresh:
            self.logs = None
        if self.logs is None:
            self.logs = rqp.WellLogCollection(frame = self)
        return self.logs

    def interval_for_md(self, md):
        """Returns wellbore frame interval index and fractional way along interval, for given md.

        arguments:
            md (float): measured depth, in units used by trajectory mds

        returns:
            (int, float) where int is the index of the wellbore frame interval containing md, and float is a fraction
                way through that interval of md, in range 0.0 to 1.0

        note:
            if md is outside the range covered by the wellbore frame intervals, an index of -1 is returned and
            the fraction will be 0.0 for an md shallower than the frame intervals, 1.0 for deeper
        """
        if md < self.node_mds[0]:
            return -1, 0.0  # -1 indicates md is not in any frame interval, 0.0 indicates too shallow
        for i in range(self.node_count - 1):
            if md <= self.node_mds[i + 1]:
                return i, (md - self.node_mds[i]) / (self.node_mds[i + 1] - self.node_mds[i])
        return -1, 1.0  # 1.0 indicates md is deeper than the intervals covered by the frame

    def create_feature_and_interpretation(self):
        """Instantiate new empty WellboreFeature and WellboreInterpretation objects, if a wellboreinterpretation does

        not already exist.

        Uses the wellboreframe citation title as the well name
        """

        if self.wellbore_interpretation is None:
            log.info(f"Creating WellboreInterpretation and WellboreFeature with name {self.title}")
            self.wellbore_feature = rqo.WellboreFeature(parent_model = self.model, feature_name = self.title)
            self.wellbore_interpretation = rqo.WellboreInterpretation(parent_model = self.model,
                                                                      wellbore_feature = self.wellbore_feature)
            self.feature_and_interpretation_to_be_written = True
        else:
            log.debug("WellboreInterpretation for {self.title} already exists")

    def write_hdf5(self, file_name = None, mode = 'a'):
        """Create or append to an hdf5 file, writing datasets for the measured depths."""

        # NB: array data must have been set up prior to calling this function

        if self.uuid is None:
            self.uuid = bu.new_uuid()

        h5_reg = rwh5.H5Register(self.model)
        h5_reg.register_dataset(self.uuid, 'NodeMd', self.node_mds)
        h5_reg.write(file = file_name, mode = mode)

    def create_xml(self,
                   ext_uuid = None,
                   add_as_part = True,
                   add_relationships = True,
                   title = None,
                   originator = None):
        """Create a wellbore frame representation node from this WellboreFrame object, optionally add as part.

        note:
           trajectory xml node must be in place before calling this function
        """

        assert self.trajectory is not None, 'trajectory object missing'
        assert self.trajectory.root is not None, 'trajectory xml not established'

        self.__create_wellbore_feature_and_interpretation_xml(add_as_part = add_as_part,
                                                              add_relationships = add_relationships,
                                                              originator = originator)

        if ext_uuid is None:
            ext_uuid = self.model.h5_uuid()

        if title:
            self.title = title
        if not self.title:
            self.title = 'wellbore frame'

        wf_node = super().create_xml(originator = originator, add_as_part = False)

        # wellbore frame elements

        nc_node, mds_node, mds_values_node = self.__add_sub_elements_to_root_node(wf_node = wf_node)

        self.model.create_hdf5_dataset_ref(ext_uuid, self.uuid, 'NodeMd', root = mds_values_node)

        traj_root = self.trajectory.root
        self.model.create_ref_node('Trajectory',
                                   rqet.find_nested_tags_text(traj_root, ['Citation', 'Title']),
                                   bu.uuid_from_string(traj_root.attrib['uuid']),
                                   content_type = 'obj_WellboreTrajectoryRepresentation',
                                   root = wf_node)

        if self.wellbore_interpretation is not None:
            interp_root = self.wellbore_interpretation.root
            self.model.create_ref_node('RepresentedInterpretation',
                                       rqet.find_nested_tags_text(interp_root, ['Citation', 'Title']),
                                       bu.uuid_from_string(interp_root.attrib['uuid']),
                                       content_type = 'obj_WellboreInterpretation',
                                       root = wf_node)

        self.__add_as_part_and_add_relationships(wf_node = wf_node,
                                                 ext_uuid = ext_uuid,
                                                 add_as_part = add_as_part,
                                                 add_relationships = add_relationships)

        return wf_node

    def __create_wellbore_feature_and_interpretation_xml(self,
                                                         add_as_part = True,
                                                         add_relationships = True,
                                                         originator = None):
        """ Return root node for WellboreFeature and WellboreInterpretation objects"""

        if self.feature_and_interpretation_to_be_written:
            if self.wellbore_interpretation is None:
                self.create_feature_and_interpretation()
            if self.wellbore_feature is not None:
                self.wellbore_feature.create_xml(add_as_part = add_as_part, originator = originator)
            self.wellbore_interpretation.create_xml(add_as_part = add_as_part,
                                                    add_relationships = add_relationships,
                                                    originator = originator)

    def __add_sub_elements_to_root_node(self, wf_node):
        """Appends sub-elements to the WellboreFrame object's root node."""

        nc_node = rqet.SubElement(wf_node, ns['resqml2'] + 'NodeCount')
        nc_node.set(ns['xsi'] + 'type', ns['xsd'] + 'positiveInteger')
        nc_node.text = str(self.node_count)

        mds_node = rqet.SubElement(wf_node, ns['resqml2'] + 'NodeMd')
        mds_node.set(ns['xsi'] + 'type', ns['resqml2'] + 'DoubleHdf5Array')
        mds_node.text = rqet.null_xml_text

        mds_values_node = rqet.SubElement(mds_node, ns['resqml2'] + 'Values')
        mds_values_node.set(ns['xsi'] + 'type', ns['resqml2'] + 'Hdf5Dataset')
        mds_values_node.text = rqet.null_xml_text

        return nc_node, mds_node, mds_values_node

    def __add_as_part_and_add_relationships(self, wf_node, ext_uuid, add_as_part, add_relationships):
        """Add the newly created WellborFrame object's root node as a part in the model and add reciprocal relationships.."""

        if add_as_part:
            self.model.add_part('obj_WellboreFrameRepresentation', self.uuid, wf_node)
            if add_relationships:
                self.model.create_reciprocal_relationship(wf_node, 'destinationObject', self.trajectory.root,
                                                          'sourceObject')
                ext_part = rqet.part_name_for_object('obj_EpcExternalPartReference', ext_uuid, prefixed = False)
                ext_node = self.model.root_for_part(ext_part)
                self.model.create_reciprocal_relationship(wf_node, 'mlToExternalPartProxy', ext_node,
                                                          'externalPartProxyToMl')
                if self.wellbore_interpretation is not None:
                    interp_root = self.wellbore_interpretation.root
                    self.model.create_reciprocal_relationship(wf_node, 'destinationObject', interp_root, 'sourceObject')
