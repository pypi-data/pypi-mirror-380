"""_add_surfaces.py: Module to import a list of surfaces into a RESQML model, as triangulatedsets or mesh objects."""

# RMS and GOCAD are trademarks of Emerson

import logging

log = logging.getLogger(__name__)

import os

import resqpy.model as rq
import resqpy.olio.xml_et as rqet
import resqpy.organize as rqo
import resqpy.surface as rqs


def add_surfaces(
        epc_file,  # existing resqml model
        crs_uuid = None,  # optional crs uuid, defaults to crs associated with model (usually main grid crs)
        surface_file_format = 'zmap',  # zmap, rms (roxar) or GOCAD-Tsurf only formats currently supported
        rq_class = 'surface',  # 'surface' or 'mesh': the class of object to be created
        surface_role = 'map',  # 'map' or 'pick'
        quad_triangles = False,  # if True, 4 triangles per quadrangle will be used for mesh formats, otherwise 2
        surface_file_list = None,  # list of full file names (paths), each holding one surface
        make_horizon_interpretations_and_features = True,  # if True, feature and interpretation objects are created
        interpretation_type = 'horizon',
        fault_is_normal = True):
    """Process a list of surface files, adding each surface as a new part in the resqml model.

    Arguments:
        epc_file (str): file name and path to an existing resqml model
        crs_uuid (uuid.UUID, default None): uuid for a coordinate reference system. Defaults to crs associated with model (usually the main grid crs)
        surface_file_format (str, default 'zmap'): 'zmap', 'rms', 'roxar' or 'GOCAD-Tsurf'. The format of the input file
        rq_class (str, default 'surface'): 'surface' or 'mesh'. The class of object ot be
        surface_role (str, default 'map'): 'map' or 'pick'
        quad_triangles (bool, default False): if True, 4 triangles per quadrangle will be used for mesh formats, otherwise 2
        surface_file_list (list, default None): list of full file names (paths), each holding one surface
        make_horizon_interpretations_and_features (bool, default True): if True, feature and interpretation objects are created
        interpretation_type (str, default 'horizon'): if 'make_horizon_interpretations_and_features' is True, feature and interpretation objects are added. Default is 'horizon', other options are 'fault' and 'geobody'
        fault_is_normal (bool, default True): if 'interpretation_type' is 'fault', define if the fault is a normal fault. Default True

    Returns:
        resqml model object with added surfaces
    """

    assert surface_file_list, 'surface file list is empty or missing'
    assert surface_file_format in ['zmap', 'rms', 'roxar',
                                   'GOCAD-Tsurf'], 'unsupported surface file format: ' + str(surface_file_format)
    assert interpretation_type in ['horizon', 'fault', 'geobody']
    rq_class = _get_rq_class(rq_class)

    model, crs_uuid = _get_model_details(epc_file, crs_uuid)

    for surf_file in surface_file_list:
        model = _add_single_surface(model, surf_file, surface_file_format, surface_role, quad_triangles, crs_uuid,
                                    rq_class, make_horizon_interpretations_and_features, interpretation_type,
                                    fault_is_normal)

    # mark model as modified
    model.set_modified()

    # store new version of model
    log.info('storing model with additional parts in epc file: ' + epc_file)
    model.store_epc(epc_file)

    return model


def _add_single_surface(model, surf_file, surface_file_format, surface_role, quad_triangles, crs_uuid, rq_class,
                        make_horizon_interpretations_and_features, interpretation_type, fault_is_normal):
    _, short_name = os.path.split(surf_file)
    dot = short_name.rfind('.')
    if dot > 0:
        short_name = short_name[:dot]

    em = {'source': surf_file}

    log.info('surface ' + short_name + ' processing file: ' + surf_file + ' using format: ' + surface_file_format)
    if rq_class == 'surface':
        if surface_file_format == 'GOCAD-Tsurf':
            surface = rqs.Surface(model,
                                  tsurf_file = surf_file,
                                  surface_role = surface_role,
                                  quad_triangles = quad_triangles,
                                  crs_uuid = crs_uuid,
                                  extra_metadata = em)
        else:
            surface = rqs.Surface(model,
                                  mesh_file = surf_file,
                                  mesh_format = surface_file_format,
                                  surface_role = surface_role,
                                  quad_triangles = quad_triangles,
                                  crs_uuid = crs_uuid,
                                  extra_metadata = em)
    elif rq_class == 'mesh':
        if surface_file_format == 'GOCAD-Tsurf':
            log.info(f"Cannot convert a GOCAD-Tsurf to mesh, only to TriangulatedSurface - skipping file {surf_file}")
            return model
        else:
            surface = rqs.Mesh(model,
                               mesh_file = surf_file,
                               mesh_format = surface_file_format,
                               mesh_flavour = 'reg&z',
                               surface_role = surface_role,
                               crs_uuid = crs_uuid,
                               extra_metadata = em)
    else:
        log.critical('this is impossible')
    # NB. surface may be either a Surface object or a Mesh object

    log.debug('appending to hdf5 file for surface file: ' + surf_file)
    surface.write_hdf5()

    if make_horizon_interpretations_and_features:
        if interpretation_type == 'horizon':
            feature = rqo.GeneticBoundaryFeature(model, kind = 'horizon', feature_name = short_name)
            feature.create_xml()
            interp = rqo.HorizonInterpretation(model, genetic_boundary_feature = feature, domain = 'depth')
            interp_root = interp.create_xml()
        elif interpretation_type == 'fault':
            feature = rqo.TectonicBoundaryFeature(model, kind = 'fault', feature_name = short_name)
            feature.create_xml()
            interp = rqo.FaultInterpretation(model,
                                             tectonic_boundary_feature = feature,
                                             domain = 'depth',
                                             is_normal = fault_is_normal)
            interp_root = interp.create_xml()
        else:
            feature = rqo.GeobodyFeature(model, feature_name = short_name)
            feature.create_xml()
            interp = rqo.GeobodyInterpretation(model, geobody_feature = feature, domain = 'depth')
            interp_root = interp.create_xml()
        surface.set_represented_interpretation_root(interp_root)

    surface.create_xml(add_as_part = True, add_relationships = True, title = short_name, originator = None)

    return model


def _get_rq_class(rq_class):
    if 'TriangulatedSet' in rq_class:
        rq_class = 'surface'
    elif 'Grid2d' in rq_class:
        rq_class = 'mesh'
    assert rq_class in ['surface', 'mesh']
    return rq_class


def _get_model_details(epc_file, crs_uuid):
    log.info('accessing existing resqml model from: ' + epc_file)
    model = rq.Model(epc_file = epc_file)
    assert model, 'failed to read existing resqml model from file: ' + epc_file

    if crs_uuid is None:
        assert model.crs_uuid is not None, 'no crs uuid given and no default in model'
        crs_uuid = model.crs_uuid

    return model, crs_uuid
