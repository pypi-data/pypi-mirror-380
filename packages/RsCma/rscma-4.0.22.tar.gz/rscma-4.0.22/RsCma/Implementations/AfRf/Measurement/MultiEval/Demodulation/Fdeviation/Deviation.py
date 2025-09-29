from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeviationCls:
	"""Deviation commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("deviation", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Rms: float or bool: RMS average value Unit: Hz
			- 3 Rms_Sqrt_2: float or bool: RMS result multiplied with the square root of 2 Unit: Hz
			- 4 Ppeak: float or bool: Positive peak value Unit: Hz
			- 5 Mpeak: float or bool: Negative peak value Unit: Hz
			- 6 Mp_Peak_Average: enums.ResultStatus: Peak-to-peak value divided by 2 Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Rms_Sqrt_2'),
			ArgStruct.scalar_float_ext('Ppeak'),
			ArgStruct.scalar_float_ext('Mpeak'),
			ArgStruct.scalar_enum('Mp_Peak_Average', enums.ResultStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rms: float or bool = None
			self.Rms_Sqrt_2: float or bool = None
			self.Ppeak: float or bool = None
			self.Mpeak: float or bool = None
			self.Mp_Peak_Average: enums.ResultStatus = None

	def calculate(self) -> CalculateStruct:
		"""CALCulate:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FDEViation:DEViation \n
		Snippet: value: CalculateStruct = driver.afRf.measurement.multiEval.demodulation.fdeviation.deviation.calculate() \n
		Queries the demodulation results for FM or FM stereo demodulation. A statistical evaluation of the frequency deviation or
		multiplex deviation is returned. CALCulate commands return error indicators instead of measurement values. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FDEViation:DEViation?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Rms: float: RMS average value Unit: Hz
			- 3 Rms_Sqrt_2: float: RMS result multiplied with the square root of 2 Unit: Hz
			- 4 Ppeak: float: Positive peak value Unit: Hz
			- 5 Mpeak: float: Negative peak value Unit: Hz
			- 6 Mp_Peak_Average: float: Peak-to-peak value divided by 2 Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Rms'),
			ArgStruct.scalar_float('Rms_Sqrt_2'),
			ArgStruct.scalar_float('Ppeak'),
			ArgStruct.scalar_float('Mpeak'),
			ArgStruct.scalar_float('Mp_Peak_Average')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rms: float = None
			self.Rms_Sqrt_2: float = None
			self.Ppeak: float = None
			self.Mpeak: float = None
			self.Mp_Peak_Average: float = None

	def fetch(self) -> ResultData:
		"""FETCh:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FDEViation:DEViation \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.demodulation.fdeviation.deviation.fetch() \n
		Queries the demodulation results for FM or FM stereo demodulation. A statistical evaluation of the frequency deviation or
		multiplex deviation is returned. CALCulate commands return error indicators instead of measurement values. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FDEViation:DEViation?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FDEViation:DEViation \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.demodulation.fdeviation.deviation.read() \n
		Queries the demodulation results for FM or FM stereo demodulation. A statistical evaluation of the frequency deviation or
		multiplex deviation is returned. CALCulate commands return error indicators instead of measurement values. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FDEViation:DEViation?', self.__class__.ResultData())
