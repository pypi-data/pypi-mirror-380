#from typing import Union
from logging import Logger as PythonLogger
from .logger import SnakeLogger
from .processors.base import IProcessor, BaseProcessor
from .filters.base import IFilter, BaseFilter
#LoggingType = Union[SnakeLogger, PythonLogger]
LoggingType = SnakeLogger|PythonLogger
ProcessorsType = IProcessor|BaseProcessor
FiltersType  = IFilter|BaseFilter

