import itertools
from typing import Any
import pandas
from rdflib import URIRef
from rdfhelpers import Composable
from rdfhelpers.producers.mappers.tinyrmlmapper import TinyRMLMapper

class PandasMapper(TinyRMLMapper):

    def readSource(self, source: pandas.DataFrame =None, **kwargs) -> Any:
        columns = source.columns
        return ({column: value for column, value in itertools.zip_longest(columns, row)}
                for row in source.itertuples(index=False, name=None))

class ExcelMapper(PandasMapper):

    def run(self, source=None, pandas_kwargs=None, **kwargs) -> Composable:
        return super().run(source=pandas.read_excel(source, **(pandas_kwargs or {})),
                           **kwargs)
