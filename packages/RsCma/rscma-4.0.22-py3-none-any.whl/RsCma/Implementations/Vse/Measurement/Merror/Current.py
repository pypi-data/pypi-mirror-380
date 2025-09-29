from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Rms: float: Unit: %
			- 3 Peak: float: Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Rms'),
			ArgStruct.scalar_float('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rms: float = None
			self.Peak: float = None

	def fetch(self) -> ResultData:
		"""FETCh:VSE:MEASurement<Instance>:MERRor:CURRent \n
		Snippet: value: ResultData = driver.vse.measurement.merror.current.fetch() \n
		Query the magnitude error results (part of the demodulation results) . \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:VSE:MEASurement<Instance>:MERRor:CURRent?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:VSE:MEASurement<Instance>:MERRor:CURRent \n
		Snippet: value: ResultData = driver.vse.measurement.merror.current.read() \n
		Query the magnitude error results (part of the demodulation results) . \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:VSE:MEASurement<Instance>:MERRor:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Rms: enums.ResultStatus: Unit: %
			- 3 Peak: enums.ResultStatus: Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Rms', enums.ResultStatus),
			ArgStruct.scalar_enum('Peak', enums.ResultStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rms: enums.ResultStatus = None
			self.Peak: enums.ResultStatus = None

	def calculate(self) -> CalculateStruct:
		"""CALCulate:VSE:MEASurement<Instance>:MERRor:CURRent \n
		Snippet: value: CalculateStruct = driver.vse.measurement.merror.current.calculate() \n
		Query the magnitude error results (part of the demodulation results) . \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:VSE:MEASurement<Instance>:MERRor:CURRent?', self.__class__.CalculateStruct())
