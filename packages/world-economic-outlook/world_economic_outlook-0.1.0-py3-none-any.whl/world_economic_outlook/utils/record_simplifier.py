"""Utility functions to simplify records for different IMF datasets."""

from world_economic_outlook.utils.iso_mappings import iso_alpha3_to_alpha2
from world_economic_outlook.utils.helpers import parse_imf_date


def simplify_fsicdm(records, use_iso_alpha2: bool = False):
    """Simplifies records for FSICDM dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "sector": r.get("SECTOR"),
            "indicator": r.get("INDICATOR"),
            "transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_qgdp_wca(records, use_iso_alpha2: bool = False):
    """Simplifies records for QGDP_WCA dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_icsd(records, use_iso_alpha2: bool = False):
    """Simplifies records for ICSD dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_spe(records, use_iso_alpha2: bool = False):
    """Simplifies records for SPE dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "bop_accounting_entry": r.get("BOP_ACCOUNTING_ENTRY"),
            "indicator": r.get("INDICATOR"),
            "unit": r.get("UNIT"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_eer(records, use_iso_alpha2: bool = False):
    """Simplifies records for EER dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_iipcc(records, use_iso_alpha2: bool = False):
    """Simplifies records for IIPCC dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "bop_accounting_entry": r.get("BOP_ACCOUNTING_ENTRY"),
            "indicator": r.get("INDICATOR"),
            "currency": r.get("CURRENCY"),
            "unit": r.get("UNIT"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_fsibsis(records, use_iso_alpha2: bool = False):
    """Simplifies records for FSIBSIS dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "sector": r.get("SECTOR"),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_gfs_ssuc(records, use_iso_alpha2: bool = False):
    """Simplifies records for GFS_SSUC dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "sector": r.get("SECTOR"),
            "gfs_grp": r.get("GFS_GRP"),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_itg_wca(records, use_iso_alpha2: bool = False):
    """Simplifies records for ITG_WCA dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_qnea(records, use_iso_alpha2: bool = False):
    """Simplifies records for QNEA dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "price_type": r.get("PRICE_TYPE"),
            "s_adjustment": r.get("S_ADJUSTMENT"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mfs_cbs(records, use_iso_alpha2: bool = False):
    """Simplifies records for MFS_CBS dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_fsic(records, use_iso_alpha2: bool = False):
    """Simplifies records for FSIC dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "sector": r.get("SECTOR"),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_wpcper(records, use_iso_alpha2: bool = False):
    """Simplifies records for WPCPER dataset."""
    return [
        {
            "currency": r.get("CURRENCY"),
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_whdreo(records, use_iso_alpha2: bool = False):
    """Simplifies records for WHDREO dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_fd(records, use_iso_alpha2: bool = False):
    """Simplifies records for FD dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "sector": r.get("SECTOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_fas(records, use_iso_alpha2: bool = False):
    """Simplifies records for FAS dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_ls(records, use_iso_alpha2: bool = False):
    """Simplifies records for LS dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_isora_2018_data_pub(records, use_iso_alpha2: bool = False):
    """Simplifies records for ISORA_2018_DATA_PUB dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("JURISDICTION"), r.get("JURISDICTION"))
                if use_iso_alpha2
                else r.get("JURISDICTION")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mfs_ofc(records, use_iso_alpha2: bool = False):
    """Simplifies records for MFS_OFC dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_fa(records, use_iso_alpha2: bool = False):
    """Simplifies records for FA dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mfs_nsrf(records, use_iso_alpha2: bool = False):
    """Simplifies records for MFS_NSRF dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "mfs_srvy": r.get("MFS_SRVY"),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_gfs_cofog(records, use_iso_alpha2: bool = False):
    """Simplifies records for GFS_COFOG dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "sector": r.get("SECTOR"),
            "gfs_grp": r.get("GFS_GRP"),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mcdreo(records, use_iso_alpha2: bool = False):
    """Simplifies records for MCDREO dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_fdi(records, use_iso_alpha2: bool = False):
    """Simplifies records for FDI dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_eq(records, use_iso_alpha2: bool = False):
    """Simplifies records for EQ dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "product": r.get("PRODUCT"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_fm(records, use_iso_alpha2: bool = False):
    """Simplifies records for FM dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_hpd(records, use_iso_alpha2: bool = False):
    """Simplifies records for HPD dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mfs_ir(records, use_iso_alpha2: bool = False):
    """Simplifies records for MFS_IR dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_anea(records, use_iso_alpha2: bool = False):
    """Simplifies records for ANEA dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "price_type": r.get("PRICE_TYPE"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_weo(records, use_iso_alpha2: bool = False):
    """Simplifies records for WEO dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_qgfs(records, use_iso_alpha2: bool = False):
    """Simplifies records for QGFS dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "accounts": r.get("ACCOUNTS"),
            "sector": r.get("SECTOR"),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_pip(records, use_iso_alpha2: bool = False):
    """Simplifies records for PIP dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "accounting_entry": r.get("ACCOUNTING_ENTRY"),
            "indicator": r.get("INDICATOR"),
            "sector": r.get("SECTOR"),
            "counterpart_sector": r.get("COUNTERPART_SECTOR"),
            "iso_star": (
                iso_alpha3_to_alpha2.get(
                    r.get("COUNTERPART_COUNTRY"), r.get("COUNTERPART_COUNTRY")
                )
                if use_iso_alpha2
                else r.get("COUNTERPART_COUNTRY")
            ),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mfs_odc(records, use_iso_alpha2: bool = False):
    """Simplifies records for MFS_ODC dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_bop_agg(records, use_iso_alpha2: bool = False):
    """Simplifies records for BOP_AGG dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_cofer(records, use_iso_alpha2: bool = False):
    """Simplifies records for COFER dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "fxr_currency": r.get("FXR_CURRENCY"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_gfs_soef(records, use_iso_alpha2: bool = False):
    """Simplifies records for GFS_SOEF dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "sector": r.get("SECTOR"),
            "gfs_grp": r.get("GFS_GRP"),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_sdg(records, use_iso_alpha2: bool = False):
    """Simplifies records for SDG dataset."""
    return [
        {
            "freq": r.get("FREQ"),
            "reporting_type": r.get("REPORTING_TYPE"),
            "series": r.get("SERIES"),
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("REF_AREA"), r.get("REF_AREA"))
                if use_iso_alpha2
                else r.get("REF_AREA")
            ),
            "sex": r.get("SEX"),
            "age": r.get("AGE"),
            "urbanisation": r.get("URBANISATION"),
            "income_wealth_quantile": r.get("INCOME_WEALTH_QUANTILE"),
            "education_lev": r.get("EDUCATION_LEV"),
            "occupation": r.get("OCCUPATION"),
            "cust_breakdown": r.get("CUST_BREAKDOWN"),
            "composite_breakdown": r.get("COMPOSITE_BREAKDOWN"),
            "disability_status": r.get("DISABILITY_STATUS"),
            "activity": r.get("ACTIVITY"),
            "product": r.get("PRODUCT"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_irfcl(records, use_iso_alpha2: bool = False):
    """Simplifies records for IRFCL dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "sector": r.get("SECTOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mfs_fmp(records, use_iso_alpha2: bool = False):
    """Simplifies records for MFS_FMP dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_pi(records, use_iso_alpha2: bool = False):
    """Simplifies records for PI dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "production_index": r.get("PRODUCTION_INDEX"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_its(records, use_iso_alpha2: bool = False):
    """Simplifies records for ITS dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_isora_latest_data_pub(records, use_iso_alpha2: bool = False):
    """Simplifies records for ISORA_LATEST_DATA_PUB dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("JURISDICTION"), r.get("JURISDICTION"))
                if use_iso_alpha2
                else r.get("JURISDICTION")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_il(records, use_iso_alpha2: bool = False):
    """Simplifies records for IL dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "unit": r.get("UNIT"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_afrreo(records, use_iso_alpha2: bool = False):
    """Simplifies records for AFRREO dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_dip(records, use_iso_alpha2: bool = False):
    """Simplifies records for DIP dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "dv_type": r.get("DV_TYPE"),
            "indicator": r.get("INDICATOR"),
            "iso_star": (
                iso_alpha3_to_alpha2.get(
                    r.get("COUNTERPART_COUNTRY"), r.get("COUNTERPART_COUNTRY")
                )
                if use_iso_alpha2
                else r.get("COUNTERPART_COUNTRY")
            ),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_pi_wca(records, use_iso_alpha2: bool = False):
    """Simplifies records for PI_WCA dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "production_index": r.get("PRODUCTION_INDEX"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_ctot(records, use_iso_alpha2: bool = False):
    """Simplifies records for CTOT dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "wgt_type": r.get("WGT_TYPE"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_taxfit(records, use_iso_alpha2: bool = False):
    """Simplifies records for TAXFIT dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "legal_spouse_presence": r.get("LEGAL_SPOUSE_PRESENCE"),
            "number_of_children": r.get("NUMBER_OF_CHILDREN"),
            "principal_employment_earnings": r.get("PRINCIPAL_EMPLOYMENT_EARNINGS"),
            "spouse_employment_earnings": r.get("SPOUSE_EMPLOYMENT_EARNINGS"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_nsdp(records, use_iso_alpha2: bool = False):
    """Simplifies records for NSDP dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "nsdp_cat": r.get("NSDP_CAT"),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_cpi(records, use_iso_alpha2: bool = False):
    """Simplifies records for CPI dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "index_type": r.get("INDEX_TYPE"),
            "coicop_1999": r.get("COICOP_1999"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_isora_2016_data_pub(records, use_iso_alpha2: bool = False):
    """Simplifies records for ISORA_2016_DATA_PUB dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("JURISDICTION"), r.get("JURISDICTION"))
                if use_iso_alpha2
                else r.get("JURISDICTION")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mfs_fc(records, use_iso_alpha2: bool = False):
    """Simplifies records for MFS_FC dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "unit": r.get("UNIT"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_gfs_soo(records, use_iso_alpha2: bool = False):
    """Simplifies records for GFS_SOO dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "sector": r.get("SECTOR"),
            "gfs_grp": r.get("GFS_GRP"),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mpft(records, use_iso_alpha2: bool = False):
    """Simplifies records for MPFT dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_iip(records, use_iso_alpha2: bool = False):
    """Simplifies records for IIP dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "bop_accounting_entry": r.get("BOP_ACCOUNTING_ENTRY"),
            "indicator": r.get("INDICATOR"),
            "unit": r.get("UNIT"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_gfs_sfcp(records, use_iso_alpha2: bool = False):
    """Simplifies records for GFS_SFCP dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "sector": r.get("SECTOR"),
            "gfs_grp": r.get("GFS_GRP"),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mfs_ma(records, use_iso_alpha2: bool = False):
    """Simplifies records for MFS_MA dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "unit": r.get("UNIT"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_gfs_bs(records, use_iso_alpha2: bool = False):
    """Simplifies records for GFS_BS dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "sector": r.get("SECTOR"),
            "gfs_grp": r.get("GFS_GRP"),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_pcps(records, use_iso_alpha2: bool = False):
    """Simplifies records for PCPS dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "data_transformation": r.get("DATA_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_er(records, use_iso_alpha2: bool = False):
    """Simplifies records for ER dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_ppi(records, use_iso_alpha2: bool = False):
    """Simplifies records for PPI dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_bop(records, use_iso_alpha2: bool = False):
    """Simplifies records for BOP dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "bop_accounting_entry": r.get("BOP_ACCOUNTING_ENTRY"),
            "indicator": r.get("INDICATOR"),
            "unit": r.get("UNIT"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_srd(records, use_iso_alpha2: bool = False):
    """Simplifies records for SRD dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_ed(records, use_iso_alpha2: bool = False):
    """Simplifies records for ED dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_imts(records, use_iso_alpha2: bool = False):
    """Simplifies records for IMTS dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "iso_star": (
                iso_alpha3_to_alpha2.get(
                    r.get("COUNTERPART_COUNTRY"), r.get("COUNTERPART_COUNTRY")
                )
                if use_iso_alpha2
                else r.get("COUNTERPART_COUNTRY")
            ),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_gdd(records, use_iso_alpha2: bool = False):
    """Simplifies records for GDD dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_itg(records, use_iso_alpha2: bool = False):
    """Simplifies records for ITG dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_mfs_dc(records, use_iso_alpha2: bool = False):
    """Simplifies records for MFS_DC dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "type_of_transformation": r.get("TYPE_OF_TRANSFORMATION"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]


def simplify_apdreo(records, use_iso_alpha2: bool = False):
    """Simplifies records for APDREO dataset."""
    return [
        {
            "iso": (
                iso_alpha3_to_alpha2.get(r.get("COUNTRY"), r.get("COUNTRY"))
                if use_iso_alpha2
                else r.get("COUNTRY")
            ),
            "indicator": r.get("INDICATOR"),
            "frequency": r.get("FREQUENCY"),
            "date": parse_imf_date(r.get("TIME_PERIOD")),
            "value": float(r.get("OBS_VALUE")) if r.get("OBS_VALUE") is not None else None,
        }
        for r in records
    ]
