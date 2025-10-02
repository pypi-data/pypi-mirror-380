"""High-level user-friendly API functions for IMF data."""


def _infer_file_format(save_path):
    if save_path.endswith(".json"):
        return "json"
    elif save_path.endswith(".csv"):
        return "csv"
    elif save_path.endswith(".txt"):
        return "txt"
    else:
        raise ValueError(
            f"Unknown file format for '{save_path}'. Please use .json, .csv, or .txt."
        )


def fsicdm(
    isos: str | list[str],
    sector: str | list[str] = "*",
    indicator: str | list[str] = "*",
    transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Financial Soundness Indicators (FSI), Concentration and Distribution Measures data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        sector (str or list): S12CFSI
        indicator (str or list): AQ14, NPF4NSPTK, NPF4TF4, ...
        transformation (str or list): HI, WGTK, WGTS, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. fsicdm
        save_path (str, optional): e.g. fsicdm.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(transformation, list):
        transformation = "+".join(transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.fsicdm import FSICDMAPI
    from world_economic_outlook.models.fsicdm_options import FSICDMOptions
    from world_economic_outlook.utils.record_simplifier import simplify_fsicdm

    options = FSICDMOptions(
        country=isos,
        sector=sector,
        indicator=indicator,
        transformation=transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = FSICDMAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_fsicdm(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def qgdp_wca(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Quarterly Gross Domestic Product (GDP), World and Country Aggregates data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): B1GQ_S1_PD, B1GQ_S1_Q, B1GQ_S1_V
        type_of_transformation (str or list): IX, POP_PCH_PT, SA_PU
        frequency (str or list): Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. qgdp_wca
        save_path (str, optional): e.g. qgdp_wca.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.qgdp_wca import QGDP_WCAAPI
    from world_economic_outlook.models.qgdp_wca_options import QGDP_WCAOptions
    from world_economic_outlook.utils.record_simplifier import simplify_qgdp_wca

    options = QGDP_WCAOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = QGDP_WCAAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_qgdp_wca(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def icsd(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Investment and Capital Stock Dataset (ICSD) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): B1GQ_Q_PU_RY2017, B1GQ_V_XDC, CAPSTCK_PS_Q_POGDP_PT, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. icsd
        save_path (str, optional): e.g. icsd.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.icsd import ICSDAPI
    from world_economic_outlook.models.icsd_options import ICSDOptions
    from world_economic_outlook.utils.record_simplifier import simplify_icsd

    options = ICSDOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ICSDAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_icsd(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def spe(
    isos: str | list[str],
    bop_accounting_entry: str | list[str] = "*",
    indicator: str | list[str] = "*",
    unit: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Special Purpose Entities (SPEs) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        bop_accounting_entry (str or list): A_NFA_T, A_P, CD_T, ...
        indicator (str or list): CAB, D, D1_F5, ...
        unit (str or list): EUR, USD, XDC
        frequency (str or list): A, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. spe
        save_path (str, optional): e.g. spe.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(bop_accounting_entry, list):
        bop_accounting_entry = "+".join(bop_accounting_entry)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(unit, list):
        unit = "+".join(unit)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.spe import SPEAPI
    from world_economic_outlook.models.spe_options import SPEOptions
    from world_economic_outlook.utils.record_simplifier import simplify_spe

    options = SPEOptions(
        country=isos,
        bop_accounting_entry=bop_accounting_entry,
        indicator=indicator,
        unit=unit,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = SPEAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_spe(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def eer(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Effective Exchange Rate (EER) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): NEER_IX_RY2010_ACW, NEER_IX_RY2010_AEW, REER_IX_RY2010_ACW_RCPI, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. eer
        save_path (str, optional): e.g. eer.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.eer import EERAPI
    from world_economic_outlook.models.eer_options import EEROptions
    from world_economic_outlook.utils.record_simplifier import simplify_eer

    options = EEROptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = EERAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_eer(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def iipcc(
    isos: str | list[str],
    bop_accounting_entry: str | list[str] = "*",
    indicator: str | list[str] = "*",
    currency: str | list[str] = "*",
    unit: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Currency Composition of the International Investment Position (IIPCC) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        bop_accounting_entry (str or list): A_P, L_P
        indicator (str or list): DCNRESICL_DIC, DCNRESICL_DIC_S, DCNRES_DIC, ...
        currency (str or list): EUR, FC, JPY, ...
        unit (str or list): EUR, USD, XDC
        frequency (str or list): A, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. iipcc
        save_path (str, optional): e.g. iipcc.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(bop_accounting_entry, list):
        bop_accounting_entry = "+".join(bop_accounting_entry)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(currency, list):
        currency = "+".join(currency)
    if isinstance(unit, list):
        unit = "+".join(unit)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.iipcc import IIPCCAPI
    from world_economic_outlook.models.iipcc_options import IIPCCOptions
    from world_economic_outlook.utils.record_simplifier import simplify_iipcc

    options = IIPCCOptions(
        country=isos,
        bop_accounting_entry=bop_accounting_entry,
        indicator=indicator,
        currency=currency,
        unit=unit,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = IIPCCAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_iipcc(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def fsibsis(
    isos: str | list[str],
    sector: str | list[str] = "*",
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Financial Soundness Indicators (FSI), Balance Sheet, Income Statement and Memorandum Series data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        sector (str or list): S1, S11, S123, ...
        indicator (str or list): AASF_EUR, AASF_USD, AASF_XDC, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. fsibsis
        save_path (str, optional): e.g. fsibsis.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.fsibsis import FSIBSISAPI
    from world_economic_outlook.models.fsibsis_options import FSIBSISOptions
    from world_economic_outlook.utils.record_simplifier import simplify_fsibsis

    options = FSIBSISOptions(
        country=isos,
        sector=sector,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = FSIBSISAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_fsibsis(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def gfs_ssuc(
    isos: str | list[str],
    sector: str | list[str] = "*",
    gfs_grp: str | list[str] = "*",
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download GFS Statement of Sources and Uses of Cash data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        sector (str or list): S13, S1311, S13112, ...
        gfs_grp (str or list): BI, G1, G2M, ...
        indicator (str or list): CIOA_TCB_CAB, CSDA_TCB_CAB, DC_L_TCB_CAB, ...
        type_of_transformation (str or list): POGDP_PT, XDC
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. gfs_ssuc
        save_path (str, optional): e.g. gfs_ssuc.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(gfs_grp, list):
        gfs_grp = "+".join(gfs_grp)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.gfs_ssuc import GFS_SSUCAPI
    from world_economic_outlook.models.gfs_ssuc_options import GFS_SSUCOptions
    from world_economic_outlook.utils.record_simplifier import simplify_gfs_ssuc

    options = GFS_SSUCOptions(
        country=isos,
        sector=sector,
        gfs_grp=gfs_grp,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = GFS_SSUCAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_gfs_ssuc(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def itg_wca(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download International Trade in Goods, World and Country Aggregates data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): XG_SA
        type_of_transformation (str or list): FOB_POP_PCH_PT, FOB_USD
        frequency (str or list): M
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. itg_wca
        save_path (str, optional): e.g. itg_wca.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.itg_wca import ITG_WCAAPI
    from world_economic_outlook.models.itg_wca_options import ITG_WCAOptions
    from world_economic_outlook.utils.record_simplifier import simplify_itg_wca

    options = ITG_WCAOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ITG_WCAAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_itg_wca(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def qnea(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    price_type: str | list[str] = "*",
    s_adjustment: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download National Economic Accounts (NEA), Quarterly Data data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): B11, B1G, B1GQ, ...
        price_type (str or list): PD, Q, V
        s_adjustment (str or list): NSA, SA
        type_of_transformation (str or list): IX, USD, XDC
        frequency (str or list): Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. qnea
        save_path (str, optional): e.g. qnea.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(price_type, list):
        price_type = "+".join(price_type)
    if isinstance(s_adjustment, list):
        s_adjustment = "+".join(s_adjustment)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.qnea import QNEAAPI
    from world_economic_outlook.models.qnea_options import QNEAOptions
    from world_economic_outlook.utils.record_simplifier import simplify_qnea

    options = QNEAOptions(
        country=isos,
        indicator=indicator,
        price_type=price_type,
        s_adjustment=s_adjustment,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = QNEAAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_qnea(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mfs_cbs(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary and Financial Statistics (MFS), Central Bank Data data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): S121_A_ACO_DCORP_EAWR_CBS, S121_A_ACO_NRES_CBS, S121_A_ACO_NRES_EAWR_CBS, ...
        type_of_transformation (str or list): EUR, PCH_CP_A_PT, USD, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mfs_cbs
        save_path (str, optional): e.g. mfs_cbs.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mfs_cbs import MFS_CBSAPI
    from world_economic_outlook.models.mfs_cbs_options import MFS_CBSOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mfs_cbs

    options = MFS_CBSOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MFS_CBSAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mfs_cbs(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def fsic(
    isos: str | list[str],
    sector: str | list[str] = "*",
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Financial Soundness Indicators (FSI), Core and Additional Indicators data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        sector (str or list): REM, S1, S11, ...
        indicator (str or list): AQ12_CFSI_PT, AQ12_NPF4_EUR, AQ12_NPF4_USD, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. fsic
        save_path (str, optional): e.g. fsic.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.fsic import FSICAPI
    from world_economic_outlook.models.fsic_options import FSICOptions
    from world_economic_outlook.utils.record_simplifier import simplify_fsic

    options = FSICOptions(
        country=isos,
        sector=sector,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = FSICAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_fsic(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def wpcper(
    isos: str | list[str],
    currency: str | list[str] = "*",
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Crypto-based Parallel Exchange Rates (Working Paper dataset WP-CPER) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        currency (str or list): AED, ALL, ARS, ...
        indicator (str or list): BIT_SHD_PT, BIT_SHD_RT, TVBIT, ...
        frequency (str or list): M
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. wpcper
        save_path (str, optional): e.g. wpcper.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(currency, list):
        currency = "+".join(currency)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.wpcper import WPCPERAPI
    from world_economic_outlook.models.wpcper_options import WPCPEROptions
    from world_economic_outlook.utils.record_simplifier import simplify_wpcper

    options = WPCPEROptions(
        currency=currency,
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = WPCPERAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_wpcper(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def whdreo(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Western Hemisphere Regional Economic Outlook (WHDREO) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): BCA_GDP_BP6, GGXGGEI_GDP, GGXONLB_GDP, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. whdreo
        save_path (str, optional): e.g. whdreo.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.whdreo import WHDREOAPI
    from world_economic_outlook.models.whdreo_options import WHDREOOptions
    from world_economic_outlook.utils.record_simplifier import simplify_whdreo

    options = WHDREOOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = WHDREOAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_whdreo(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def fd(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    sector: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Fiscal Decentralization (FD) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): CS_S13ESHR_PT, DEFICIT_POOS_PT, G111_S13RSHR_PT, ...
        sector (str or list): S1311MIXED, S1312X, S1313X, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. fd
        save_path (str, optional): e.g. fd.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.fd import FDAPI
    from world_economic_outlook.models.fd_options import FDOptions
    from world_economic_outlook.utils.record_simplifier import simplify_fd

    options = FDOptions(
        country=isos,
        indicator=indicator,
        sector=sector,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = FDAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_fd(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def fas(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Financial Access Survey (FAS) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): COMBANK, CUCC, DTMFI, ...
        type_of_transformation (str or list): NUM, PHTADLT_NUM, POGDP, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. fas
        save_path (str, optional): e.g. fas.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.fas import FASAPI
    from world_economic_outlook.models.fas_options import FASOptions
    from world_economic_outlook.utils.record_simplifier import simplify_fas

    options = FASOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = FASAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_fas(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def ls(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Labor Statistics (LS) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): E, LF, U, ...
        type_of_transformation (str or list): IX, PE, POP_PCH_PT, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. ls
        save_path (str, optional): e.g. ls.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.ls import LSAPI
    from world_economic_outlook.models.ls_options import LSOptions
    from world_economic_outlook.utils.record_simplifier import simplify_ls

    options = LSOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = LSAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_ls(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def isora_2018_data_pub(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download ISORA 2018 Data data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): 337_001, 337_002, 337_003, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. isora_2018_data_pub
        save_path (str, optional): e.g. isora_2018_data_pub.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.isora_2018_data_pub import (
        ISORA_2018_DATA_PUBAPI,
    )
    from world_economic_outlook.models.isora_2018_data_pub_options import (
        ISORA_2018_DATA_PUBOptions,
    )
    from world_economic_outlook.utils.record_simplifier import (
        simplify_isora_2018_data_pub,
    )

    options = ISORA_2018_DATA_PUBOptions(
        jurisdiction=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ISORA_2018_DATA_PUBAPI()
    data = api.get_data(options)
    result = (
        data
        if full_output
        else simplify_isora_2018_data_pub(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mfs_ofc(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary and Financial Statistics (MFS), Other Financial Corporations data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): S12R_A_ACO_DCORP_OFCS, S12R_A_ACO_NRES_OFCS, S12R_A_ACO_PS_OFCS, ...
        type_of_transformation (str or list): EUR, USD, XDC
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mfs_ofc
        save_path (str, optional): e.g. mfs_ofc.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mfs_ofc import MFS_OFCAPI
    from world_economic_outlook.models.mfs_ofc_options import MFS_OFCOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mfs_ofc

    options = MFS_OFCOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MFS_OFCAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mfs_ofc(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def fa(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Fund Accounts (FA) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): CLIMF_POQT_PT_A_PT, CLIMF_USD, CLIMF_XDR, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. fa
        save_path (str, optional): e.g. fa.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.fa import FAAPI
    from world_economic_outlook.models.fa_options import FAOptions
    from world_economic_outlook.utils.record_simplifier import simplify_fa

    options = FAOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = FAAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_fa(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mfs_nsrf(
    isos: str | list[str],
    mfs_srvy: str | list[str] = "*",
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary and Financial Statistics (MFS),  Non-Standard Data data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        mfs_srvy (str or list): CBS, DCS, FCS, ...
        indicator (str or list): NSRF_10RA, NSRF_11, NSRF_12A, ...
        type_of_transformation (str or list): EUR, PT, USD, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mfs_nsrf
        save_path (str, optional): e.g. mfs_nsrf.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(mfs_srvy, list):
        mfs_srvy = "+".join(mfs_srvy)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mfs_nsrf import MFS_NSRFAPI
    from world_economic_outlook.models.mfs_nsrf_options import MFS_NSRFOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mfs_nsrf

    options = MFS_NSRFOptions(
        country=isos,
        mfs_srvy=mfs_srvy,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MFS_NSRFAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mfs_nsrf(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def gfs_cofog(
    isos: str | list[str],
    sector: str | list[str] = "*",
    gfs_grp: str | list[str] = "*",
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download GFS Government Expenditures by Function data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        sector (str or list): S13, S1311, S13112, ...
        gfs_grp (str or list): G2MF
        indicator (str or list): F6N_G33_L_T, GF011_T, GF012_T, ...
        type_of_transformation (str or list): POGDP_PT, POTO_PT, XDC
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. gfs_cofog
        save_path (str, optional): e.g. gfs_cofog.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(gfs_grp, list):
        gfs_grp = "+".join(gfs_grp)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.gfs_cofog import GFS_COFOGAPI
    from world_economic_outlook.models.gfs_cofog_options import GFS_COFOGOptions
    from world_economic_outlook.utils.record_simplifier import simplify_gfs_cofog

    options = GFS_COFOGOptions(
        country=isos,
        sector=sector,
        gfs_grp=gfs_grp,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = GFS_COFOGAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_gfs_cofog(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mcdreo(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Middle East and Central Asia Regional Economic Outlook (MCDREO)  data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): BCA, BCA_GDP, BM, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mcdreo
        save_path (str, optional): e.g. mcdreo.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mcdreo import MCDREOAPI
    from world_economic_outlook.models.mcdreo_options import MCDREOOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mcdreo

    options = MCDREOOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MCDREOAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mcdreo(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def fdi(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Financial Development Index (FDI) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): FDA_IX, FDD_IX, FDE_IX, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. fdi
        save_path (str, optional): e.g. fdi.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.fdi import FDIAPI
    from world_economic_outlook.models.fdi_options import FDIOptions
    from world_economic_outlook.utils.record_simplifier import simplify_fdi

    options = FDIOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = FDIAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_fdi(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def eq(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    product: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Export Quality (EQ) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): EXPRGDP_PERCAPITA_USD, MQ_MEAN_USD, MUV_MEAN_USD, ...
        product (str or list): 0, 1, 2, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. eq
        save_path (str, optional): e.g. eq.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(product, list):
        product = "+".join(product)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.eq import EQAPI
    from world_economic_outlook.models.eq_options import EQOptions
    from world_economic_outlook.utils.record_simplifier import simplify_eq

    options = EQOptions(
        country=isos,
        indicator=indicator,
        product=product,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = EQAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_eq(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def fm(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Fiscal Monitor (FM) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): CAB_S13_POPGDP_PT, CAPB_S13_POPGDP_PT, G1_S13_POGDP_PT, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. fm
        save_path (str, optional): e.g. fm.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.fm import FMAPI
    from world_economic_outlook.models.fm_options import FMOptions
    from world_economic_outlook.utils.record_simplifier import simplify_fm

    options = FMOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = FMAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_fm(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def hpd(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Historical Public Debt (HPD) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): G63G_S13_POFYGDP
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. hpd
        save_path (str, optional): e.g. hpd.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.hpd import HPDAPI
    from world_economic_outlook.models.hpd_options import HPDOptions
    from world_economic_outlook.utils.record_simplifier import simplify_hpd

    options = HPDOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = HPDAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_hpd(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mfs_ir(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary and Financial Statistics (MFS), Interest Rate data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): DISR_FC_RT_PT_A_PT, DISR_RT_PT_A_PT, GBYMIN_RT_PT_A_PT, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mfs_ir
        save_path (str, optional): e.g. mfs_ir.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mfs_ir import MFS_IRAPI
    from world_economic_outlook.models.mfs_ir_options import MFS_IROptions
    from world_economic_outlook.utils.record_simplifier import simplify_mfs_ir

    options = MFS_IROptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MFS_IRAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mfs_ir(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def anea(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    price_type: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download National Economic Accounts (NEA), Annual Data data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): B11, B1G, B1GQ, ...
        price_type (str or list): PD, Q, V
        type_of_transformation (str or list): IX, USD, XDC
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. anea
        save_path (str, optional): e.g. anea.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(price_type, list):
        price_type = "+".join(price_type)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.anea import ANEAAPI
    from world_economic_outlook.models.anea_options import ANEAOptions
    from world_economic_outlook.utils.record_simplifier import simplify_anea

    options = ANEAOptions(
        country=isos,
        indicator=indicator,
        price_type=price_type,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ANEAAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_anea(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def weo(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download World Economic Outlook (WEO) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): BCA, BCA_NGDPD, BF, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. weo
        save_path (str, optional): e.g. weo.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.weo import WEOAPI
    from world_economic_outlook.models.weo_options import WEOOptions
    from world_economic_outlook.utils.record_simplifier import simplify_weo

    options = WEOOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = WEOAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_weo(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def qgfs(
    isos: str | list[str],
    accounts: str | list[str] = "*",
    sector: str | list[str] = "*",
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Quarterly Government Finance Statistics (QGFS) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        accounts (str or list): BS, SOO, SSUC
        sector (str or list): S13, S1311B, S1321
        indicator (str or list): 6M2_NETAL_SP_XDC, CIO_CA_TCB_XDC, CR_OA_TCB_XDC, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. qgfs
        save_path (str, optional): e.g. qgfs.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(accounts, list):
        accounts = "+".join(accounts)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.qgfs import QGFSAPI
    from world_economic_outlook.models.qgfs_options import QGFSOptions
    from world_economic_outlook.utils.record_simplifier import simplify_qgfs

    options = QGFSOptions(
        country=isos,
        accounts=accounts,
        sector=sector,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = QGFSAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_qgfs(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def pip(
    isos: str | list[str],
    isos_star: str | list[str] = "*",
    accounting_entry: str | list[str] = "*",
    indicator: str | list[str] = "*",
    sector: str | list[str] = "*",
    counterpart_sector: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Portfolio Investment Positions by Counterpart Economy (formerly CPIS) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        isos_star (str or list): Counterpart ISO country code(s) or '*' for all
        accounting_entry (str or list): A, L
        indicator (str or list): P_F3SNP_L_P_USD, P_F3SNP_P_USD, P_F3SNP_S_P_USD, ...
        sector (str or list): OFM, S1, S11, ...
        counterpart_sector (str or list): S1, S12, S121, ...
        frequency (str or list): A, S
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. pip
        save_path (str, optional): e.g. pip.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    isos_star = normalise(isos_star)
    if isinstance(accounting_entry, list):
        accounting_entry = "+".join(accounting_entry)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(counterpart_sector, list):
        counterpart_sector = "+".join(counterpart_sector)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos_star == "*":
        isos_star = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos_star = "+".join(
            [iso_alpha2_to_alpha3.get(code, code) for code in isos_star]
        )

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.pip import PIPAPI
    from world_economic_outlook.models.pip_options import PIPOptions
    from world_economic_outlook.utils.record_simplifier import simplify_pip

    options = PIPOptions(
        country=isos,
        accounting_entry=accounting_entry,
        indicator=indicator,
        sector=sector,
        counterpart_sector=counterpart_sector,
        counterpart_country=isos_star,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = PIPAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_pip(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mfs_odc(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary and Financial Statistics (MFS), Other Depository Corporations data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): ODCORP_A_ACO_EWRN_EAWR_ODCS, ODCORP_A_ACO_NRES_EAWR_ODCS, ODCORP_A_ACO_NRES_ODCS, ...
        type_of_transformation (str or list): EUR, USD, XDC
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mfs_odc
        save_path (str, optional): e.g. mfs_odc.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mfs_odc import MFS_ODCAPI
    from world_economic_outlook.models.mfs_odc_options import MFS_ODCOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mfs_odc

    options = MFS_ODCOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MFS_ODCAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mfs_odc(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def bop_agg(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Balance of Payments and International Investment Position Statistics (BOP/IIP), World and Country Group Aggregates data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): CAB_NETCD, D_NFA_A, D_NIL_L, ...
        type_of_transformation (str or list): POGCAT_PT, POGCT_PT, POGDP_PT, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. bop_agg
        save_path (str, optional): e.g. bop_agg.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.bop_agg import BOP_AGGAPI
    from world_economic_outlook.models.bop_agg_options import BOP_AGGOptions
    from world_economic_outlook.utils.record_simplifier import simplify_bop_agg

    options = BOP_AGGOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = BOP_AGGAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_bop_agg(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def cofer(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    fxr_currency: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Currency Composition of Official Foreign Exchange Reserves (COFER) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): AFXRA, TFXRA, UFXRA
        fxr_currency (str or list): CI_AUD, CI_CAD, CI_CHF, ...
        type_of_transformation (str or list): NV_USD, SHRO_PT
        frequency (str or list): A, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. cofer
        save_path (str, optional): e.g. cofer.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(fxr_currency, list):
        fxr_currency = "+".join(fxr_currency)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.cofer import COFERAPI
    from world_economic_outlook.models.cofer_options import COFEROptions
    from world_economic_outlook.utils.record_simplifier import simplify_cofer

    options = COFEROptions(
        country=isos,
        indicator=indicator,
        fxr_currency=fxr_currency,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = COFERAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_cofer(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def gfs_soef(
    isos: str | list[str],
    sector: str | list[str] = "*",
    gfs_grp: str | list[str] = "*",
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download GFS Statement of Other Economic Flows data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        sector (str or list): S13, S1311, S13112, ...
        gfs_grp (str or list): BI, OEF
        indicator (str or list): G91_A_OEF, G92_A_OEF, G93_L_OEF, ...
        type_of_transformation (str or list): POGDP_PT, XDC
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. gfs_soef
        save_path (str, optional): e.g. gfs_soef.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(gfs_grp, list):
        gfs_grp = "+".join(gfs_grp)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.gfs_soef import GFS_SOEFAPI
    from world_economic_outlook.models.gfs_soef_options import GFS_SOEFOptions
    from world_economic_outlook.utils.record_simplifier import simplify_gfs_soef

    options = GFS_SOEFOptions(
        country=isos,
        sector=sector,
        gfs_grp=gfs_grp,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = GFS_SOEFAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_gfs_soef(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def sdg(
    isos: str | list[str],
    freq: str | list[str] = "*",
    reporting_type: str | list[str] = "*",
    series: str | list[str] = "*",
    sex: str | list[str] = "*",
    age: str | list[str] = "*",
    urbanisation: str | list[str] = "*",
    income_wealth_quantile: str | list[str] = "*",
    education_lev: str | list[str] = "*",
    occupation: str | list[str] = "*",
    cust_breakdown: str | list[str] = "*",
    composite_breakdown: str | list[str] = "*",
    disability_status: str | list[str] = "*",
    activity: str | list[str] = "*",
    product: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download IMF Reported SDG Data data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        freq (str or list): A
        reporting_type (str or list): G
        series (str or list): FB_ATM_TOTL, FB_CBK_BRCH, FI_FSI_FSANL, ...
        sex (str or list): _T
        age (str or list): _T
        urbanisation (str or list): _T
        income_wealth_quantile (str or list): _T
        education_lev (str or list): _T
        occupation (str or list): _T
        cust_breakdown (str or list): _T
        composite_breakdown (str or list): _T
        disability_status (str or list): _T
        activity (str or list): _T
        product (str or list): _T
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. sdg
        save_path (str, optional): e.g. sdg.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(freq, list):
        freq = "+".join(freq)
    if isinstance(reporting_type, list):
        reporting_type = "+".join(reporting_type)
    if isinstance(series, list):
        series = "+".join(series)
    if isinstance(sex, list):
        sex = "+".join(sex)
    if isinstance(age, list):
        age = "+".join(age)
    if isinstance(urbanisation, list):
        urbanisation = "+".join(urbanisation)
    if isinstance(income_wealth_quantile, list):
        income_wealth_quantile = "+".join(income_wealth_quantile)
    if isinstance(education_lev, list):
        education_lev = "+".join(education_lev)
    if isinstance(occupation, list):
        occupation = "+".join(occupation)
    if isinstance(cust_breakdown, list):
        cust_breakdown = "+".join(cust_breakdown)
    if isinstance(composite_breakdown, list):
        composite_breakdown = "+".join(composite_breakdown)
    if isinstance(disability_status, list):
        disability_status = "+".join(disability_status)
    if isinstance(activity, list):
        activity = "+".join(activity)
    if isinstance(product, list):
        product = "+".join(product)

    if isinstance(isos, list):
        isos = "+".join(isos)

    from world_economic_outlook.api.endpoints.sdg import SDGAPI
    from world_economic_outlook.models.sdg_options import SDGOptions
    from world_economic_outlook.utils.record_simplifier import simplify_sdg

    options = SDGOptions(
        freq=freq,
        reporting_type=reporting_type,
        series=series,
        ref_area=isos,
        sex=sex,
        age=age,
        urbanisation=urbanisation,
        income_wealth_quantile=income_wealth_quantile,
        education_lev=education_lev,
        occupation=occupation,
        cust_breakdown=cust_breakdown,
        composite_breakdown=composite_breakdown,
        disability_status=disability_status,
        activity=activity,
        product=product,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = SDGAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_sdg(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def irfcl(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    sector: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download International Reserves and Foreign Currency Liquidity (IRFCL) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): IRFCLDT1_IRFCL121_USD_IRFCL13, IRFCLDT1_IRFCL31_BOFIORCLA_USD_IRFCL13, IRFCLDT1_IRFCL31_BOFIORC_USD_IRFCL13, ...
        sector (str or list): S1311, S1X, S1XS1311
        frequency (str or list): A, D, M, ...
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. irfcl
        save_path (str, optional): e.g. irfcl.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.irfcl import IRFCLAPI
    from world_economic_outlook.models.irfcl_options import IRFCLOptions
    from world_economic_outlook.utils.record_simplifier import simplify_irfcl

    options = IRFCLOptions(
        country=isos,
        indicator=indicator,
        sector=sector,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = IRFCLAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_irfcl(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mfs_fmp(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary and Financial Statistics (MFS): Financial Market Prices data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): EI, EMN, EPAMEX, ...
        type_of_transformation (str or list): EOP_IX, PA_IX
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mfs_fmp
        save_path (str, optional): e.g. mfs_fmp.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mfs_fmp import MFS_FMPAPI
    from world_economic_outlook.models.mfs_fmp_options import MFS_FMPOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mfs_fmp

    options = MFS_FMPOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MFS_FMPAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mfs_fmp(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def pi(
    isos: str | list[str],
    production_index: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Production Indexes (PI) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        production_index (str or list): B, B06, C, ...
        type_of_transformation (str or list): IX, POP_PCH_PT, SA_IX, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. pi
        save_path (str, optional): e.g. pi.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(production_index, list):
        production_index = "+".join(production_index)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.pi import PIAPI
    from world_economic_outlook.models.pi_options import PIOptions
    from world_economic_outlook.utils.record_simplifier import simplify_pi

    options = PIOptions(
        country=isos,
        production_index=production_index,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = PIAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_pi(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def its(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download International Trade in Services (ITS) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): G_CD, SAOTH_CD_CA, SAY_CD_CA, ...
        type_of_transformation (str or list): 1DIGITPT, 2DIGITPT, PERCAPITAR, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. its
        save_path (str, optional): e.g. its.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.its import ITSAPI
    from world_economic_outlook.models.its_options import ITSOptions
    from world_economic_outlook.utils.record_simplifier import simplify_its

    options = ITSOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ITSAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_its(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def isora_latest_data_pub(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download ISORA Latest Data data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): 111_200, 111_201, 111_202, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. isora_latest_data_pub
        save_path (str, optional): e.g. isora_latest_data_pub.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.isora_latest_data_pub import (
        ISORA_LATEST_DATA_PUBAPI,
    )
    from world_economic_outlook.models.isora_latest_data_pub_options import (
        ISORA_LATEST_DATA_PUBOptions,
    )
    from world_economic_outlook.utils.record_simplifier import (
        simplify_isora_latest_data_pub,
    )

    options = ISORA_LATEST_DATA_PUBOptions(
        jurisdiction=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ISORA_LATEST_DATA_PUBAPI()
    data = api.get_data(options)
    result = (
        data
        if full_output
        else simplify_isora_latest_data_pub(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def il(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    unit: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download International Liquidity (IL) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): GOLD35P_REVS, NFAOFA_ACO_NRES_S121, NFAOFL_LT_NRES_S121, ...
        unit (str or list): FTO, USD, XDR
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. il
        save_path (str, optional): e.g. il.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(unit, list):
        unit = "+".join(unit)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.il import ILAPI
    from world_economic_outlook.models.il_options import ILOptions
    from world_economic_outlook.utils.record_simplifier import simplify_il

    options = ILOptions(
        country=isos,
        indicator=indicator,
        unit=unit,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ILAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_il(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def afrreo(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Sub-Saharan Africa Regional Economic Outlook (AFRREO) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): BCA_BP6_GDP_PT, BFD_BP6_GDP_PT, BG_BP6_GDP_PT, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. afrreo
        save_path (str, optional): e.g. afrreo.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.afrreo import AFRREOAPI
    from world_economic_outlook.models.afrreo_options import AFRREOOptions
    from world_economic_outlook.utils.record_simplifier import simplify_afrreo

    options = AFRREOOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = AFRREOAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_afrreo(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def dip(
    isos: str | list[str],
    isos_star: str | list[str] = "*",
    dv_type: str | list[str] = "*",
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Direct Investment Positions by Counterpart Economy (formerly CDIS) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        isos_star (str or list): Counterpart ISO country code(s) or '*' for all
        dv_type (str or list): O, SCC
        indicator (str or list): INWD_D_AG_FALL_FE, INWD_D_AG_FL_ALL, INWD_D_LG_FALL_FE, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. dip
        save_path (str, optional): e.g. dip.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    isos_star = normalise(isos_star)
    if isinstance(dv_type, list):
        dv_type = "+".join(dv_type)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos_star == "*":
        isos_star = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos_star = "+".join(
            [iso_alpha2_to_alpha3.get(code, code) for code in isos_star]
        )

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.dip import DIPAPI
    from world_economic_outlook.models.dip_options import DIPOptions
    from world_economic_outlook.utils.record_simplifier import simplify_dip

    options = DIPOptions(
        country=isos,
        dv_type=dv_type,
        indicator=indicator,
        counterpart_country=isos_star,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = DIPAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_dip(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def pi_wca(
    isos: str | list[str],
    production_index: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Production Indexes, World and Country Group Aggregates data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        production_index (str or list): IND
        type_of_transformation (str or list): SA_IX, SA_POP_PCH_PT
        frequency (str or list): M
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. pi_wca
        save_path (str, optional): e.g. pi_wca.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(production_index, list):
        production_index = "+".join(production_index)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.pi_wca import PI_WCAAPI
    from world_economic_outlook.models.pi_wca_options import PI_WCAOptions
    from world_economic_outlook.utils.record_simplifier import simplify_pi_wca

    options = PI_WCAOptions(
        country=isos,
        production_index=production_index,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = PI_WCAAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_pi_wca(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def ctot(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    wgt_type: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Commodity Terms of Trade (CTOT) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): CEMPI_CTOTNX_TT, CEMPI_CTOTXM_GDP, CEPI_CTOTX_GDP, ...
        wgt_type (str or list): H_FW_IX, H_RW_IX, R_FW_IX, ...
        frequency (str or list): A, M
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. ctot
        save_path (str, optional): e.g. ctot.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(wgt_type, list):
        wgt_type = "+".join(wgt_type)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.ctot import CTOTAPI
    from world_economic_outlook.models.ctot_options import CTOTOptions
    from world_economic_outlook.utils.record_simplifier import simplify_ctot

    options = CTOTOptions(
        country=isos,
        indicator=indicator,
        wgt_type=wgt_type,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = CTOTAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_ctot(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def taxfit(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    legal_spouse_presence: str | list[str] = "*",
    number_of_children: str | list[str] = "*",
    principal_employment_earnings: str | list[str] = "*",
    spouse_employment_earnings: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Tax and Benefits Analysis Tool (TAXFIT) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): aw, care, earn_p, ...
        legal_spouse_presence (str or list): 0, 1
        number_of_children (str or list): 0, 1, 2, ...
        principal_employment_earnings (str or list): 0, 100, 120, ...
        spouse_employment_earnings (str or list): 0, 100, 120, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. taxfit
        save_path (str, optional): e.g. taxfit.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(legal_spouse_presence, list):
        legal_spouse_presence = "+".join(legal_spouse_presence)
    if isinstance(number_of_children, list):
        number_of_children = "+".join(number_of_children)
    if isinstance(principal_employment_earnings, list):
        principal_employment_earnings = "+".join(principal_employment_earnings)
    if isinstance(spouse_employment_earnings, list):
        spouse_employment_earnings = "+".join(spouse_employment_earnings)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.taxfit import TAXFITAPI
    from world_economic_outlook.models.taxfit_options import TAXFITOptions
    from world_economic_outlook.utils.record_simplifier import simplify_taxfit

    options = TAXFITOptions(
        country=isos,
        indicator=indicator,
        legal_spouse_presence=legal_spouse_presence,
        number_of_children=number_of_children,
        principal_employment_earnings=principal_employment_earnings,
        spouse_employment_earnings=spouse_employment_earnings,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = TAXFITAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_taxfit(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def nsdp(
    isos: str | list[str],
    nsdp_cat: str | list[str] = "*",
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download National Summary Data Page (NSDP) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        nsdp_cat (str or list): BOP00, CPI00, ILV00, ...
        indicator (str or list): AIP, AIPMA, AIPMA_SA, ...
        type_of_transformation (str or list): EUR, IX, NUM, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. nsdp
        save_path (str, optional): e.g. nsdp.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(nsdp_cat, list):
        nsdp_cat = "+".join(nsdp_cat)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.nsdp import NSDPAPI
    from world_economic_outlook.models.nsdp_options import NSDPOptions
    from world_economic_outlook.utils.record_simplifier import simplify_nsdp

    options = NSDPOptions(
        country=isos,
        nsdp_cat=nsdp_cat,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = NSDPAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_nsdp(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def cpi(
    isos: str | list[str],
    index_type: str | list[str] = "*",
    coicop_1999: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Consumer Price Index (CPI) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        index_type (str or list): CPI, HICP
        coicop_1999 (str or list): CP01, CP02, CP03, ...
        type_of_transformation (str or list): IX, POP_PCH_PA_PT, SRP_IX, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. cpi
        save_path (str, optional): e.g. cpi.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(index_type, list):
        index_type = "+".join(index_type)
    if isinstance(coicop_1999, list):
        coicop_1999 = "+".join(coicop_1999)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.cpi import CPIAPI
    from world_economic_outlook.models.cpi_options import CPIOptions
    from world_economic_outlook.utils.record_simplifier import simplify_cpi

    options = CPIOptions(
        country=isos,
        index_type=index_type,
        coicop_1999=coicop_1999,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = CPIAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_cpi(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def isora_2016_data_pub(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download ISORA 2016 Data data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): 10010, 10020, 10030, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. isora_2016_data_pub
        save_path (str, optional): e.g. isora_2016_data_pub.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.isora_2016_data_pub import (
        ISORA_2016_DATA_PUBAPI,
    )
    from world_economic_outlook.models.isora_2016_data_pub_options import (
        ISORA_2016_DATA_PUBOptions,
    )
    from world_economic_outlook.utils.record_simplifier import (
        simplify_isora_2016_data_pub,
    )

    options = ISORA_2016_DATA_PUBOptions(
        jurisdiction=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ISORA_2016_DATA_PUBAPI()
    data = api.get_data(options)
    result = (
        data
        if full_output
        else simplify_isora_2016_data_pub(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mfs_fc(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    unit: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary and Financial Statistics (MFS), Financial Corporations data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): ODCORP_A_ACO_NRES, ODCORP_A_ACO_PS, ODCORP_A_ACO_S11001, ...
        unit (str or list): EUR, USD, XDC, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mfs_fc
        save_path (str, optional): e.g. mfs_fc.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(unit, list):
        unit = "+".join(unit)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mfs_fc import MFS_FCAPI
    from world_economic_outlook.models.mfs_fc_options import MFS_FCOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mfs_fc

    options = MFS_FCOptions(
        country=isos,
        indicator=indicator,
        unit=unit,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MFS_FCAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mfs_fc(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def gfs_soo(
    isos: str | list[str],
    sector: str | list[str] = "*",
    gfs_grp: str | list[str] = "*",
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download GFS Statement of Operations  data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        sector (str or list): S13, S1311, S13112, ...
        gfs_grp (str or list): BI, BS, G1, ...
        indicator (str or list): DC_L_T, DD_A_SP, DMV_G33_L_T_MI, ...
        type_of_transformation (str or list): POGDP_PT, XDC
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. gfs_soo
        save_path (str, optional): e.g. gfs_soo.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(gfs_grp, list):
        gfs_grp = "+".join(gfs_grp)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.gfs_soo import GFS_SOOAPI
    from world_economic_outlook.models.gfs_soo_options import GFS_SOOOptions
    from world_economic_outlook.utils.record_simplifier import simplify_gfs_soo

    options = GFS_SOOOptions(
        country=isos,
        sector=sector,
        gfs_grp=gfs_grp,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = GFS_SOOAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_gfs_soo(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mpft(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary Policy Frameworks Toolkit (MPFT) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): COM, COM_1, COM_2, ...
        type_of_transformation (str or list): IX, IX_PCH
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mpft
        save_path (str, optional): e.g. mpft.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mpft import MPFTAPI
    from world_economic_outlook.models.mpft_options import MPFTOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mpft

    options = MPFTOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MPFTAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_mpft(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def iip(
    isos: str | list[str],
    bop_accounting_entry: str | list[str] = "*",
    indicator: str | list[str] = "*",
    unit: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download International Investment Position (IIP) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        bop_accounting_entry (str or list): A_P, L_P, NETAL_P
        indicator (str or list): D, D1_F3, D1_F5, ...
        unit (str or list): EUR, USD, XDC
        frequency (str or list): A, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. iip
        save_path (str, optional): e.g. iip.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(bop_accounting_entry, list):
        bop_accounting_entry = "+".join(bop_accounting_entry)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(unit, list):
        unit = "+".join(unit)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.iip import IIPAPI
    from world_economic_outlook.models.iip_options import IIPOptions
    from world_economic_outlook.utils.record_simplifier import simplify_iip

    options = IIPOptions(
        country=isos,
        bop_accounting_entry=bop_accounting_entry,
        indicator=indicator,
        unit=unit,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = IIPAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_iip(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def gfs_sfcp(
    isos: str | list[str],
    sector: str | list[str] = "*",
    gfs_grp: str | list[str] = "*",
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download GFS Stocks and Flows by Counterparty data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        sector (str or list): S13, S1311, S13112, ...
        gfs_grp (str or list): BS, TFAL
        indicator (str or list): DC_L_T, DD_A_SP, FA_A_SP, ...
        type_of_transformation (str or list): POGDP_PT, XDC
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. gfs_sfcp
        save_path (str, optional): e.g. gfs_sfcp.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(gfs_grp, list):
        gfs_grp = "+".join(gfs_grp)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.gfs_sfcp import GFS_SFCPAPI
    from world_economic_outlook.models.gfs_sfcp_options import GFS_SFCPOptions
    from world_economic_outlook.utils.record_simplifier import simplify_gfs_sfcp

    options = GFS_SFCPOptions(
        country=isos,
        sector=sector,
        gfs_grp=gfs_grp,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = GFS_SFCPAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_gfs_sfcp(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mfs_ma(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    unit: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary and Financial Statistics (MFS), Monetary Aggregates data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): BMM5_SI, BM_MAI, BM_SA_SI, ...
        unit (str or list): EUR, IX, USD, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mfs_ma
        save_path (str, optional): e.g. mfs_ma.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(unit, list):
        unit = "+".join(unit)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mfs_ma import MFS_MAAPI
    from world_economic_outlook.models.mfs_ma_options import MFS_MAOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mfs_ma

    options = MFS_MAOptions(
        country=isos,
        indicator=indicator,
        unit=unit,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MFS_MAAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mfs_ma(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def gfs_bs(
    isos: str | list[str],
    sector: str | list[str] = "*",
    gfs_grp: str | list[str] = "*",
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download GFS Balance Sheet data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        sector (str or list): S13, S1311, S13112, ...
        gfs_grp (str or list): BI, BS, G1, ...
        indicator (str or list): ADJ_D_A_SP, CONTLIB_L_SP_MI, F12_FC_L_SP, ...
        type_of_transformation (str or list): POGDP_PT, XDC
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. gfs_bs
        save_path (str, optional): e.g. gfs_bs.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(sector, list):
        sector = "+".join(sector)
    if isinstance(gfs_grp, list):
        gfs_grp = "+".join(gfs_grp)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.gfs_bs import GFS_BSAPI
    from world_economic_outlook.models.gfs_bs_options import GFS_BSOptions
    from world_economic_outlook.utils.record_simplifier import simplify_gfs_bs

    options = GFS_BSOptions(
        country=isos,
        sector=sector,
        gfs_grp=gfs_grp,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = GFS_BSAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_gfs_bs(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def pcps(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    data_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Primary Commodity Price System (PCPS) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): LMICS, PAGRI, PALLFNF, ...
        data_transformation (str or list): INDEX, INDEX_PCH, INDEX_PCHY, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. pcps
        save_path (str, optional): e.g. pcps.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(data_transformation, list):
        data_transformation = "+".join(data_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.pcps import PCPSAPI
    from world_economic_outlook.models.pcps_options import PCPSOptions
    from world_economic_outlook.utils.record_simplifier import simplify_pcps

    options = PCPSOptions(
        country=isos,
        indicator=indicator,
        data_transformation=data_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = PCPSAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_pcps(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def er(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Exchange Rates (ER) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): ECU_XDC, EUR_XDC, USD_XDC, ...
        type_of_transformation (str or list): EOP_RT, PA_RT
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. er
        save_path (str, optional): e.g. er.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.er import ERAPI
    from world_economic_outlook.models.er_options import EROptions
    from world_economic_outlook.utils.record_simplifier import simplify_er

    options = EROptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ERAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_er(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def ppi(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Producer Price Index (PPI) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): PPI, WPI
        type_of_transformation (str or list): IX, POP_PCH_PT, YOY_PCH_PT
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. ppi
        save_path (str, optional): e.g. ppi.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.ppi import PPIAPI
    from world_economic_outlook.models.ppi_options import PPIOptions
    from world_economic_outlook.utils.record_simplifier import simplify_ppi

    options = PPIOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = PPIAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_ppi(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def bop(
    isos: str | list[str],
    bop_accounting_entry: str | list[str] = "*",
    indicator: str | list[str] = "*",
    unit: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Balance of Payments (BOP) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        bop_accounting_entry (str or list): A_NFA_T, A_T, CD_T, ...
        indicator (str or list): ANPNFA, CAB, CABXEF, ...
        unit (str or list): EUR, USD, XDC
        frequency (str or list): A, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. bop
        save_path (str, optional): e.g. bop.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(bop_accounting_entry, list):
        bop_accounting_entry = "+".join(bop_accounting_entry)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(unit, list):
        unit = "+".join(unit)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.bop import BOPAPI
    from world_economic_outlook.models.bop_options import BOPOptions
    from world_economic_outlook.utils.record_simplifier import simplify_bop

    options = BOPOptions(
        country=isos,
        bop_accounting_entry=bop_accounting_entry,
        indicator=indicator,
        unit=unit,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = BOPAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_bop(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def srd(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Structural Reform Database (SRD) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): DOMFIN_CREDIT_NUM, DOMFIN_ENTRY_NUM, DOMFIN_INT_NUM, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. srd
        save_path (str, optional): e.g. srd.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.srd import SRDAPI
    from world_economic_outlook.models.srd_options import SRDOptions
    from world_economic_outlook.utils.record_simplifier import simplify_srd

    options = SRDOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = SRDAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_srd(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def ed(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Export Diversification (ED) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): BETWEEN_THEIL_IX, TOTAL_THEIL_IX, WITHIN_THEIL_IX
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. ed
        save_path (str, optional): e.g. ed.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.ed import EDAPI
    from world_economic_outlook.models.ed_options import EDOptions
    from world_economic_outlook.utils.record_simplifier import simplify_ed

    options = EDOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = EDAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_ed(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def imts(
    isos: str | list[str],
    isos_star: str | list[str] = "*",
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download International Trade in Goods (by partner country) (IMTS) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        isos_star (str or list): Counterpart ISO country code(s) or '*' for all
        indicator (str or list): MG_CIF_USD, MG_FOB_USD, TBG_USD, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. imts
        save_path (str, optional): e.g. imts.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    isos_star = normalise(isos_star)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos_star == "*":
        isos_star = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos_star = "+".join(
            [iso_alpha2_to_alpha3.get(code, code) for code in isos_star]
        )

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.imts import IMTSAPI
    from world_economic_outlook.models.imts_options import IMTSOptions
    from world_economic_outlook.utils.record_simplifier import simplify_imts

    options = IMTSOptions(
        country=isos,
        indicator=indicator,
        counterpart_country=isos_star,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = IMTSAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_imts(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def gdd(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Global Debt Database (GDD) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): B1GQ_V_XDC, F3T4_PS_POGDP_PT, F3T4_S11_POGDP_PT, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. gdd
        save_path (str, optional): e.g. gdd.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.gdd import GDDAPI
    from world_economic_outlook.models.gdd_options import GDDOptions
    from world_economic_outlook.utils.record_simplifier import simplify_gdd

    options = GDDOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = GDDAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_gdd(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def itg(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download International Trade in Goods (ITG) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): EPI, MG, MG_PD, ...
        type_of_transformation (str or list): CIF_IX, CIF_POP_PCH_PT, CIF_USD, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. itg
        save_path (str, optional): e.g. itg.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.itg import ITGAPI
    from world_economic_outlook.models.itg_options import ITGOptions
    from world_economic_outlook.utils.record_simplifier import simplify_itg

    options = ITGOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = ITGAPI()
    data = api.get_data(options)
    result = data if full_output else simplify_itg(data, use_iso_alpha2=use_iso_alpha2)
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def mfs_dc(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    type_of_transformation: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Monetary and Financial Statistics (MFS), Depository Corporations data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): DCORP_A_ACO_NRES, DCORP_A_ACO_NRES_EAWR, DCORP_A_ACO_PS, ...
        type_of_transformation (str or list): EUR, PCH_CP_A_PT, RMBBMPT_A_PT, ...
        frequency (str or list): A, M, Q
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. mfs_dc
        save_path (str, optional): e.g. mfs_dc.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(type_of_transformation, list):
        type_of_transformation = "+".join(type_of_transformation)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.mfs_dc import MFS_DCAPI
    from world_economic_outlook.models.mfs_dc_options import MFS_DCOptions
    from world_economic_outlook.utils.record_simplifier import simplify_mfs_dc

    options = MFS_DCOptions(
        country=isos,
        indicator=indicator,
        type_of_transformation=type_of_transformation,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = MFS_DCAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_mfs_dc(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def apdreo(
    isos: str | list[str],
    indicator: str | list[str] = "*",
    frequency: str | list[str] = "*",
    start_date: str = None,
    end_date: str = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
) -> list[dict]:
    """
    Download Asia and Pacific Regional Economic Outlook (APDREO) data.

    Args:
        isos (str or list): ISO country code(s) or '*' for all
        indicator (str or list): BCA_GDP_BP6, GGXCNL_GDP, LUR, ...
        frequency (str or list): A
        start_date (str, optional): e.g. 2020-01-01
        end_date (str, optional): e.g. 2028-01-01
        database (str, optional): e.g. database.db
        table (str, optional): e.g. apdreo
        save_path (str, optional): e.g. apdreo.json
        full_output (str, optional): True/False
        use_iso_alpha2 (str, optional): True/False

    Returns:
        list[dict]: List of simplified or raw records
    """

    def normalise(val):
        if val == "*" or val == ["*"]:
            return "*"
        if isinstance(val, str):
            return [val]
        return val

    isos = normalise(isos)
    if isinstance(indicator, list):
        indicator = "+".join(indicator)
    if isinstance(frequency, list):
        frequency = "+".join(frequency)

    if isos == "*":
        isos = "*"
    else:
        from world_economic_outlook.utils.iso_mappings import iso_alpha2_to_alpha3

        isos = "+".join([iso_alpha2_to_alpha3.get(code, code) for code in isos])

    from world_economic_outlook.api.endpoints.apdreo import APDREOAPI
    from world_economic_outlook.models.apdreo_options import APDREOOptions
    from world_economic_outlook.utils.record_simplifier import simplify_apdreo

    options = APDREOOptions(
        country=isos,
        indicator=indicator,
        frequency=frequency,
        **{
            k: v
            for k, v in {"start_date": start_date, "end_date": end_date}.items()
            if v is not None
        },
    )
    api = APDREOAPI()
    data = api.get_data(options)
    result = (
        data if full_output else simplify_apdreo(data, use_iso_alpha2=use_iso_alpha2)
    )
    if len(data) == 0:
        return []
    if database and table:
        from simple_sqlite3 import Database

        with Database(database) as db:
            db.table(table).insert(result)
    if save_path:
        from world_economic_outlook.utils.save_helpers import save_records

        fmt = _infer_file_format(save_path)
        save_records(result, save_path, fmt)
    return result


def vweo(
    vintage: str | list[str],
    isos: list[str] = None,
    indicator: list[str] = None,
    start_year: str | int = None,
    end_year: str | int = None,
    database: str = None,
    table: str = None,
    save_path: str = None,
    full_output: bool = False,
    use_iso_alpha2: bool = False,
):
    # Lazy import <vweo> for speed efficiency
    from .vweo import vweo

    start_year = int(start_year) if start_year is not None else None
    end_year = int(end_year) if end_year is not None else None

    return vweo(
        vintage,
        isos,
        indicator,
        start_year,
        end_year,
        database,
        table,
        save_path,
        full_output,
        use_iso_alpha2,
    )
