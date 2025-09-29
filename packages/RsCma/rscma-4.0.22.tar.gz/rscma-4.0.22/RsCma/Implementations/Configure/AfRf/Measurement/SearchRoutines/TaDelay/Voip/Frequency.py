from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency_1: float, frequency_2: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:VOIP:FREQuency \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.taDelay.voip.frequency.set(frequency_1 = 1.0, frequency_2 = 1.0) \n
		No command help available \n
			:param frequency_1: No help available
			:param frequency_2: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('frequency_1', frequency_1, DataType.Float), ArgSingle('frequency_2', frequency_2, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:VOIP:FREQuency {param}'.rstrip())

	# noinspection PyTypeChecker
	class FrequencyStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Frequency_1: float: No parameter help available
			- 2 Frequency_2: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Frequency_1'),
			ArgStruct.scalar_float('Frequency_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency_1: float = None
			self.Frequency_2: float = None

	def get(self) -> FrequencyStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:VOIP:FREQuency \n
		Snippet: value: FrequencyStruct = driver.configure.afRf.measurement.searchRoutines.taDelay.voip.frequency.get() \n
		No command help available \n
			:return: structure: for return value, see the help for FrequencyStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TADelay:VOIP:FREQuency?', self.__class__.FrequencyStruct())
