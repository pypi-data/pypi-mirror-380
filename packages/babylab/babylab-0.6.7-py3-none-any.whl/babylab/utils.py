"""
Util functions for the app.
"""

from datetime import date, timedelta, datetime
from functools import singledispatch
from copy import deepcopy
import polars as pl
from babylab import api
from babylab.globals import COLNAMES, INT_FIELDS


@singledispatch
def fmt_labels(x: dict | pl.DataFrame, data_dict: dict[str, str]):
    """Reformat dataframe.

    Args:
        x (dict | DataFrame): Dataframe to reformat.
        data_dict (dict): Data dictionary to labels to use, as returned by ``api.get_data_dict``.
        prefixes (list[str]): List of prefixes to look for in variable names.

    Returns:
        DataFrame: A reformated Dataframe.
    """
    raise TypeError("`x` must be a dict or a DataFrame")


@fmt_labels.register(dict)
def _(x: dict, data_dict: dict) -> dict:
    """Reformat dictionary.

    Args:
        x (dict): dictionary to reformat.
        data_dict (dict): Data dictionary to labels to use, as returned by ``api.get_data_dict``.

    Returns:
        dict: A reformatted dictionary.
    """
    fields = ["participant_", "appointment_", "language_"]
    y = dict(x)
    for k, v in y.items():
        for f in fields:
            if f + k in data_dict and v:
                y[k] = data_dict[f + k][v]
        if "exp" in k:
            y[k] = round(float(v), None) if v else None
        for c in ["taxi_isbooked", "isdropout", "isestimated"]:
            if c in k:
                y[k] = y[c] == "1"
        y[k] = y[k] if y[k] != "" else None
    y = {k: (int(v) if v and k in INT_FIELDS else v) for k, v in y.items()}
    return y


@fmt_labels.register(pl.DataFrame)
def _(x: pl.DataFrame, data_dict: dict) -> pl.DataFrame:
    """Reformat DataFrame.

    Args:
        x (dict): dictionary to reformat.
        data_dict (dict): Data dictionary to labels to use, as returned by ``api.get_data_dict``.

    Returns:
        DataFrame: A reformatted DataFrame.
    """
    cols = {k.rsplit("_", 1)[1]: v for k, v in data_dict.items()}
    for k, v in {ck: cv for ck, cv in cols.items() if ck in x.columns}.items():
        x = x.with_columns(pl.col(k).replace_strict(v, default=None))
    for c in ["isestimated", "isdropout"]:
        if c in x.columns:
            x = x.with_columns(pl.col(c).eq("1"))
    x = x.with_columns(
        pl.when(pl.col(pl.String).str.len_chars() == 0)
        .then(None)
        .otherwise(pl.col(pl.String))
        .name.keep()
    ).cast({c: pl.Int64 for c in [f for f in INT_FIELDS if f in x.columns]})
    return x


def is_in_data_dict(x: list[str] | None, variable: str, data_dict: dict) -> list[str]:
    """Check that a value is an element in the data dictionary.

    Args:
        x (list[str] | None): Value to look up in the data dictionary.
        variable (str): Key in which to look for.
        data_dict (dict): Data dictionary as returned by ``api.get_data_dictionary``.

    Raises:
        ValueError: If `x` is not an option present in `data_dict`.

    Returns:
        list[str]: Values in data dict.
    """
    options = list(data_dict[variable].values())
    if x is None:
        return options
    out = x
    if isinstance(x, str):
        out = [out]
    for o in out:
        if o not in options:
            raise ValueError(f"{o} is not an option in {variable}")
    return out


def get_age_timestamp(
    months: int, days: int, timestamp: date | datetime
) -> tuple[str, str]:
    """Get age at timestamp in months and days.

    Args:
        apt_records (dict): Appointment records.
        ppt_records (dict): Participant records.
        date_type (str, optional): Timestamp at which to calculate age. Defaults to "date".

    Raises:
        ValueError: If timestamp is not "date" or "date_created".

    Returns:
        tuple[str, str]: Age at timestamp in months and days.
    """
    months_new, days_new = [], []
    for m, d, t in zip(months, days, timestamp):
        age_months, age_days = api.get_age(age=(m, d), ts=t)
        months_new.append(age_months)
        days_new.append(age_days)
    return months_new, days_new


def get_ppt_table(
    records: api.Records,
    data_dict: dict,
    relabel: bool = True,
    ppt_id: list[str] | str = None,
    study: list[str] | str = None,
) -> pl.DataFrame:
    """Get participants table

    Args:
        records (api.Records): REDCap records, as returned by ``api.Records``.
        data_dict (dict, optional): Data dictionary as returned by ``api.get_data_dictionary``.
        relabel (bool, optional): Should columns be relabeled? Defaults to True.
        ppt_id (list[str] | str): ID of participant to return. If None (default), all participants are returned.
        study (list[str] | str, optional): Study in which the participant in the records must have participated to be kept. Defaults to None.

    Returns:
        pl.DataFrame: Table of partcicipants.
    """  # pylint: disable=line-too-long
    if not records.participants.records:
        return pl.DataFrame(schema=COLNAMES["participants"])
    if isinstance(ppt_id, str):
        ppt_id = [ppt_id]
    if isinstance(study, str):
        study = [study]
    df = records.participants.to_df()
    if study:
        ppt_study = (
            records.appointments.to_df()
            .filter(pl.col("study").is_in(study))
            .unique("record_id")
            .get_column("record_id")
            .to_list()
        )
        df = df.filter(pl.col("record_id").is_in(ppt_study))
    if ppt_id:
        df = df.filter(pl.col("record_id").is_in(ppt_id))
    if relabel:
        df = fmt_labels(df, data_dict)
    return df


def get_apt_table(
    records: api.Records,
    data_dict: dict = None,
    ppt_id: list[str] | str = None,
    study: list[str] | str = None,
    relabel: bool = True,
) -> pl.DataFrame:
    """Get appointments table.

    Args:
        records (api.Records): REDCap records, as returned by ``api.Records``.
        data_dict (dict): Data dictionary as returned by ``api.get_data_dictionary``.
        ppt_id (list[str] | str): ID of participant to return. If None (default), all participants are returned.
        study (list[str] | str, optional): Study to filter for. If None (default) all studies are returned.
        relabel (bool): Reformat labels if True (default).

    Returns:
        DataFrame: Table of appointments.
    """  # pylint: disable=line-too-long
    df = deepcopy(records.appointments).to_df()
    if len(df) == 0:
        return pl.DataFrame(schema=COLNAMES["appointments"])
    if isinstance(study, str):
        study = [study]
    if isinstance(ppt_id, str):
        ppt_id = [ppt_id]
    if study:
        df = df.filter(pl.col("study").is_in(study))
    if ppt_id:
        df = df.filter(pl.col("record_id").is_in(ppt_id))
    if relabel:
        df = fmt_labels(df, data_dict)
    ppt_df = records.participants.to_df()
    df = df.join(
        ppt_df.select(["record_id", "age_now_months", "age_now_days"]), on="record_id"
    )
    age_apt = get_age_timestamp(df["age_now_days"], df["age_now_months"], df["date"])
    df.insert_column(-1, pl.Series("age_apt_months", age_apt[0]))
    df.insert_column(-1, pl.Series("age_apt_days", age_apt[1]))
    return df


def get_que_table(
    records: api.Records,
    data_dict: dict,
    ppt_id: list[str] | str = None,
    relabel: bool = True,
) -> pl.DataFrame:
    """Get questionnaires table.

    Args:
        records (api.Records): REDCap records, as returned by ``api.Records``.
        data_dict (dict): Data dictionary as returned by ``api.get_data_dictionary``.
        ppt_id (list[str] | str): ID of participant to return. If None (default), all participants are returned.
        relabel (bool): Reformat labels if True (default).

    Returns:
        DataFrame: A formated Pandas DataFrame.
    """  # pylint: disable=line-too-long
    df = deepcopy(records.questionnaires).to_df()
    if len(df) == 0:
        return pl.DataFrame(schema=COLNAMES["questionnaires"])
    if isinstance(ppt_id, str):
        ppt_id = [ppt_id]
    if ppt_id:
        df = df.filter(pl.col("record_id").is_in(ppt_id))
    if relabel:
        df = fmt_labels(df, data_dict)
    return df


def count_col(
    x: pl.DataFrame,
    col: str,
    values_sort: bool = False,
    cumulative: bool = False,
    missing_label: str = "Missing",
) -> dict:
    """Count frequencies of column in DataFrame.

    Args:
        x (DataFrame): DataFrame containing the target column.
        col (str): Name of the column.
        values_sort (str, optional): Should the resulting dict be ordered by values? Defaults to False.
        cumulative (bool, optional): Should the counts be cumulative? Defaults to False.
        missing_label (str, optional): Label to associate with missing values. Defaults to "Missing".

    Returns:
        dict: Counts of each category, sorted in descending order.
    """  # pylint: disable=line-too-long
    counts = x[col].value_counts().to_dict()
    counts = {missing_label if not k else k: v for k, v in counts.items()}
    if values_sort:
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    if cumulative:
        cumsum = 0
        for key in counts:
            cumsum += counts[key]
            counts[key] = cumsum
    return counts


def get_year_weeks(year: int):
    """Get week numbers of the year"""
    date_first = date(year, 1, 1)
    date_first += timedelta(days=6 - date_first.weekday())
    while date_first.year == year:
        yield date_first
        date_first += timedelta(days=7)


def get_week_n(timestamp: date):
    """Get current week number"""
    weeks = {}
    for wn, d in enumerate(get_year_weeks(timestamp.year)):
        weeks[wn + 1] = [(d + timedelta(days=k)).isoformat() for k in range(0, 7)]
    for k, v in weeks.items():
        if datetime.strftime(timestamp, "%Y-%m-%d") in v:
            return k
    return None


def get_weekly_apts(
    records: api.Records,
    data_dict: dict,
    study: list | None = None,
    status: list | None = None,
) -> dict:
    """Get weekly number of appointments.

    Args:
        records (api.Records): REDCap records, as returned by ``api.Records``.
        data_dict (dict): Data dictionary as returned by ``api.get_data_dictionary``.
        study (list | None, optional): Study to filter for. Defaults to None.
        status (list | None, optional): Status to filter for. Defaults to None.

    Raises:
        ValueError: If `study` or `status` is not available.

    Returns:
        dict: Weekly number of appointment with for a given study and/or status.
    """  # pylint: disable=line-too-long
    study = is_in_data_dict(study, "appointment_study", data_dict)
    status = is_in_data_dict(status, "appointment_status", data_dict)
    apts = records.appointments.records.values()
    return sum(
        get_week_n(v.data["date_created"]) == get_week_n(datetime.today())
        for v in apts
        if data_dict["appointment_status"][v.data["status"]] in status
        and data_dict["appointment_study"][v.data["study"]] in study
    )
