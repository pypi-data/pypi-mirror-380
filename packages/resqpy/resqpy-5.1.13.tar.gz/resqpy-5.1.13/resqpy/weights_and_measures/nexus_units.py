"""Functions specific to Nexus units of measure."""

# Nexus is a trademark of Halliburton


def nexus_uom_for_quantity(nexus_unit_system, quantity, english_volume_flavour = None):
    """Returns RESQML uom string expected by Nexus for given quantity class and unit system.

    arguments:
        nexus_unit_system (str): one of 'METRIC', 'METKG/CM2', 'METBAR', 'LAB', or 'ENGLISH'
        quantity (str): the RESQML quantity class of interest; currently suppported:
            'length', 'area', 'volume', 'volume per volume', 'permeability rock',
            'time', 'thermodynamic temperature', 'mass per volume', 'pressure',
            'volume per time'
        english_volume_flavour (str, optional): only needed for ENGLISH unit system and volume,
            volume per volume, or volume per time quantity; one of 'PV', 'OVER PV', 'FVF', 'GOR',
            'surface gas rate', or 'saturation'; see notes regarding FVF, also regarding flow
            rates

    returns:
        str: the RESQML uom string for the units required by Nexus

    notes:
        transmissibility not yet catered for here, as RESQML has transmissibility units without a
        viscosity component;
        Nexus volume unit expectations vary depending on the data being handled, and sometimes also
        where in the Nexus input dataset the data is being entered;
        resqpy.weights_and_measures.valid_quantities() and valid_uoms() may also be of interest;
        in the ENHLISH unit system, Nexus expacts gas formation volume factors in bbl / 1000 ft3
        but that is not a valid RESQML uom – this function will return bbl/bbl for ENGLISH FVF;
        also be wary of pore volume units when using the medieval ENGLISH unit system: the OVER
        keyword expects different units than GRID or recurrent override input; ENGLISH fluid flow
        rates will be returned as bbl/d unless the flavour is specified as 'surface gas rate'
    """

    nexus_unit_system = nexus_unit_system.upper()
    assert nexus_unit_system in ['METRIC', 'METKG/CM2', 'METBAR', 'LAB', 'ENGLISH']
    # todo: add other quantities as needed
    assert quantity in [
        'length', 'area', 'volume', 'volume per volume', 'permeability rock', 'rock permeability', 'time',
        'thermodynamic temperature', 'mass per volume', 'pressure', 'volume per time'
    ]
    if quantity == 'permeability rock':
        quantity = 'rock permeability'

    if (nexus_unit_system == 'ENGLISH' and english_volume_flavour is not None):
        english_volume_flavour = english_volume_flavour.lower()
        if english_volume_flavour == 'pv':
            assert quantity == 'volume'
            return 'ft3'  # correct for main GRID array input or recurrent override
        elif english_volume_flavour == 'over pv':
            assert quantity == 'volume'
            return 'bbl'  # for static override of pv (Nexus OVER)
        elif english_volume_flavour == 'surface gas rate':
            assert quantity == 'volume per time'
            return '1000 ft3/d'
        assert quantity == 'volume per volume'
        if english_volume_flavour == 'fvf':
            return 'bbl/bbl'
        elif english_volume_flavour == 'gor':
            return '1000 ft3/bbl'
        else:
            assert english_volume_flavour == 'saturation'  # handled by default in dictionary

    d = {
        'METRIC': {
            'length': 'm',
            'area': 'm2',
            'volume': 'm3',
            'volume per volume': 'm3/m3',
            'rock permeability': 'mD',
            'time': 'd',
            'thermodynamic temperature': 'degC',
            'mass per volume': 'kg/m3',
            'pressure': 'kPa',
            'volume per time': 'm3/d'
        },
        'METKG/CM2': {
            'length': 'm',
            'area': 'm2',
            'volume': 'm3',
            'volume per volume': 'm3/m3',
            'rock permeability': 'mD',
            'time': 'd',
            'thermodynamic temperature': 'degC',
            'mass per volume': 'kg/m3',
            'pressure': 'kgf/cm2',
            'volume per time': 'm3/d'
        },
        'METBAR': {
            'length': 'm',
            'area': 'm2',
            'volume': 'm3',
            'volume per volume': 'm3/m3',
            'rock permeability': 'mD',
            'time': 'd',
            'thermodynamic temperature': 'degC',
            'mass per volume': 'kg/m3',
            'pressure': 'bar',
            'volume per time': 'm3/d'
        },
        'LAB': {
            'length': 'cm',
            'area': 'cm2',
            'volume': 'cm3',
            'volume per volume': 'cm3/cm3',
            'rock permeability': 'mD',
            'time': 'h',
            'thermodynamic temperature': 'degC',
            'mass per volume': 'g/cm3',
            'pressure': 'psi',
            'volume per time': 'cm3/h'
        },
        'ENGLISH': {
            'length': 'ft',
            'area': 'ft2',
            'volume': 'ft3',  # NB. Nexus expects bbl in some situations!
            'volume per volume': 'ft3/ft3',  # note: some special cases dealt with above
            'rock permeability': 'mD',
            'time': 'd',
            'thermodynamic temperature': 'degF',
            'mass per volume': 'lbm/ft3',
            'pressure': 'psi',
            'volume per time': 'bbl/d'  # surface gas is special case handled above
        }
    }

    return d[nexus_unit_system][quantity]
