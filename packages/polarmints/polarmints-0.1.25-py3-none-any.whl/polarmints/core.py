from __future__ import annotations

import logging
from collections.abc import Sequence
from typing import Union, Callable, List, Dict
import polars as pl
from polars import exclude, Series, DataFrame as DF, Expr, Struct
from polarmints.sugar import c
from polarmints.utils import dict2pred

logger = logging.getLogger(__name__)

class PolarsBase:
    def __init__(self, df: DF):
        self._df = df




class PolarMints(PolarsBase):

    def get(self, col: str, default=None) -> Series:
        if col in self._df:
            return self._df[col]
        return default

    def filter_dict(self, pred: dict) -> DF:
        return self._df.filter(dict2pred(pred))

    def todict(self, key: str | List[str], val: str | List[str]) -> dict:
        kvpair = [self._df.select(
            (c[v] if isinstance(v, str) else pl.coalesce(v))
        ).to_series() for v in (key, val)]
        return dict(zip(*kvpair))

    def replace_pred(self, *pairs, cols=pl.all()) -> DF:
        """
        Experimental TODO: must be a betterway
        """
        res = self._df.with_columns(where(
            pairs + [(None, cols)]
        ).keep_name())
        return res

    def safe_rename(self, mapping: dict) -> DF:
        excs = [v for k, v in mapping.items() if k != v]
        return self._df.select(exclude(excs)
        ).rename(mapping)

    def with_cols(self, inputs: List[Union[List, dict]]) -> DF:
        res = self._df
        for args in inputs:
            res = res.with_columns(**args) if isinstance(args, dict) else res.with_columns(args)
        return res

    def join(self, other: DF, on: str | Sequence[str], *args, **kwargs):
        """
        infers type of on columns and casts other df to match
        """
        if isinstance(on, str):
            on = [on]
        other_cast = other.with_columns([
            c[col].cast(self._df[col].dtype)
        for col in on])
        return self._df.join(other_cast, on, *args, **kwargs)

    def convert_schema(self, schema: dict, strict=False) -> DF:
        """
        convert schema to polars schema
        """
        fn = self._df.select if strict else self._df.with_columns
        return fn(
            c[col].cast(dtype) for col, dtype in schema.items() if strict or col in self._df.columns
        )

    def renamefn(self, fn: Callable) -> DF:
        return self._df.rename({k: fn(k) for k in self._df.columns})

    def unnest_all(self):
        df = self._df
        return df.unnest(*[col for col, typ in df.schema.items() if typ == Struct])

    ######################## Convenience Shortcuts #####################


    def tsc(self, samplesize=100000):
        df = self._df
        if len(df) > samplesize:
            print(f'truncating {len(df)} rows to {samplesize}')
            df = df.sample(samplesize)
        df.to_pandas().to_clipboard(index=False)


    @property
    def tc(self):
        self.tsc()


    def infer_date_range(self, on: str, range_fn=None, **kwargs) -> dict:
        import pandas as pd
        df = self._df
        params = dict(
            start=df[on].min(),
            end=df[on].max(),
            freq=pd.infer_freq(df[on].unique().sort()),
        ) | kwargs
        range_fn = range_fn or pd.date_range
        dr = pl.from_pandas(range_fn(**params)).to_frame(on)
        return dr

    ################################## Data integrity ##################################

    def ts_holes(self, on: str | Expr, pk: List = None, how='anti', **kwargs):
        df = self._df
        dr = self.infer_date_range(on, **kwargs)
        if pk:
            dr = df[pk].unique().sort(pk).join(dr, how='cross')
        missing = dr.pm.join(df, [on] + (pk or []), how)
        return missing

    def _null_counts(self) -> Dict[str, int]:
        """
        by columns
        """
        counts = self._df.select(pl.all().is_null().sum()).to_dicts()[0]
        return {k: v for k, v in counts.items() if v}

    def check_nulls(self):
        nulls = self._null_counts()
        assert not nulls, f"found nulls in cols {nulls}"

####################### MAIN examples #######################

if __name__ == '__main__':
    dfpl = pl.DataFrame({'a': [1, 2, 3]})
    c = PolarsCol()
    expr = c.a == 1
    expr2 = c['a'] > 2
    filtered = dfpl.filter(expr | expr2)

    dfs = {
        'd1': pl.DataFrame({
            'd': [1, 2, 3],
            'a': [1, 2, 3],
            'b': [1, 2, 3],
            'c': [1, 2, 3],
        }),
        'd2': pl.DataFrame({
            'd': [1, 2, 3],
            'a': [2, 2, 2],
            'c': [2, 2, 2],
        }),
        'd3': pl.DataFrame({
            'a': [3, 2, 1],
            'b': [3, 2, 1],
        }),
    }
    combined = combine_struct(dfs, ['d'])

    df = dfs['d1']
    df.index = ['a', 'b']
    res = df.pd.replace({1: 11})

    df['a'].pd.abs()


