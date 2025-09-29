from __future__ import annotations
from typing import List, Tuple
import pandas as pd
import numpy as np
import polars as pl
import pyarrow as pa
from datetime import date

BUSDAY_TYPES = pl.DataFrame | pl.Series | pd.DataFrame | pd.Series

def _busday_offset(dates: BUSDAY_TYPES, offsets, cal_name: str = None, **kwargs) -> pl.Series:
    import pandas_market_calendars as mcal
    if cal_name:
        kwargs['holidays'] = mcal.get_calendar(cal_name).holidays().holidays
    kwargs['roll'] = kwargs.get('roll', 'forward')
    res = np.busday_offset(dates, offsets, **kwargs) #TODO replace with polars-business-days
    return res

def busday_offset(dates: BUSDAY_TYPES, *args, **kwargs) -> pl.Series:
    res = _busday_offset(dates, *args, **kwargs)
    match type(dates):
        case pl.DataFrame:
            df = pl.from_numpy(res)
            df.columns = dates.columns
            return df
        case pd.DataFrame:
            return pd.DataFrame(res, dates.columns)
        case pl.Series:
            return pl.from_numpy(res).to_series()
        case pd.Series:
            return pd.Series(res)
        case _:
            return res

def start_end_pa_pred(col: str, start: date | str = None, end: date | str = None) -> List[Tuple[str, str, pa.Date32Scalar]]:
    date_filter = []
    if start:
        start = pd.Timestamp(start).date()
        date_filter.append((col, '>=', pa.scalar(start)))
    if end:
        end = pd.Timestamp(end).date()
        date_filter.append((col, '<=', pa.scalar(end)))
    return date_filter