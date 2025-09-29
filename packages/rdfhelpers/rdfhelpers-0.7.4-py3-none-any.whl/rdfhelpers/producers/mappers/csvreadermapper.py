import csv
from abc import ABC, abstractmethod
from rdfhelpers import Composable
from rdfhelpers.producers.common.interface import Mapper, FileReaderMixin

class CSVReaderMapper(Mapper, FileReaderMixin, ABC):
    def __init__(self, agent=None, **kwargs):
        super().__init__(agent=agent, **kwargs)
        self.header_row = None

    def openSourceFile(self, file, **kwargs):
        return open(file, newline='')

    def initialize(self, csv_reader_kwargs: dict = None, header_row=True, **kwargs) -> Composable:
        if self.source:
            self.source = csv.reader(self.source, **(csv_reader_kwargs or {}))
            if header_row:
                self.header_row = next(self.source)
        return super().initialize(**kwargs)

    def produce(self, data: Composable, **kwargs) -> Composable:
        for row in self.source:
            data = self.perRow(data, row)
        return data

    @abstractmethod
    def perRow(self, data: Composable, row) -> Composable:
        ...
