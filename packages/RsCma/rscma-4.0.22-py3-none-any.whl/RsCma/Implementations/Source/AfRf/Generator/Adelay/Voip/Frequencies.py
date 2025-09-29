from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequenciesCls:
	"""Frequencies commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequencies", core, parent)

	def set(self, frequency_1: int, frequency_2: int) -> None:
		"""SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:FREQuencies \n
		Snippet: driver.source.afRf.generator.adelay.voip.frequencies.set(frequency_1 = 1, frequency_2 = 1) \n
		No command help available \n
			:param frequency_1: No help available
			:param frequency_2: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('frequency_1', frequency_1, DataType.Integer), ArgSingle('frequency_2', frequency_2, DataType.Integer))
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:FREQuencies {param}'.rstrip())

	# noinspection PyTypeChecker
	class FrequenciesStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Frequency_1: int: No parameter help available
			- 2 Frequency_2: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Frequency_1'),
			ArgStruct.scalar_int('Frequency_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency_1: int = None
			self.Frequency_2: int = None

	def get(self) -> FrequenciesStruct:
		"""SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:FREQuencies \n
		Snippet: value: FrequenciesStruct = driver.source.afRf.generator.adelay.voip.frequencies.get() \n
		No command help available \n
			:return: structure: for return value, see the help for FrequenciesStruct structure arguments."""
		return self._core.io.query_struct(f'SOURce:AFRF:GENerator<Instance>:ADELay:VOIP:FREQuencies?', self.__class__.FrequenciesStruct())
