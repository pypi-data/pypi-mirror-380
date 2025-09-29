from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Audio_Dev_Left: float or bool: Peak frequency deviation due to the left audio channel Unit: Hz
			- 3 Audio_Dev_Right: float or bool: Peak frequency deviation due to the right audio channel Unit: Hz
			- 4 Pilot_Deviation: float or bool: Peak frequency deviation due to the pilot tone Unit: Hz
			- 5 Pilot_Freq_Error: float or bool: Frequency error of the pilot tone Unit: Hz
			- 6 Rds_Deviation: float or bool: Peak frequency deviation due to the signal in the RDS band Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Audio_Dev_Left'),
			ArgStruct.scalar_float_ext('Audio_Dev_Right'),
			ArgStruct.scalar_float_ext('Pilot_Deviation'),
			ArgStruct.scalar_float_ext('Pilot_Freq_Error'),
			ArgStruct.scalar_float_ext('Rds_Deviation')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Audio_Dev_Left: float or bool = None
			self.Audio_Dev_Right: float or bool = None
			self.Pilot_Deviation: float or bool = None
			self.Pilot_Freq_Error: float or bool = None
			self.Rds_Deviation: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""CALCulate:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FMSTereo:CURRent \n
		Snippet: value: CalculateStruct = driver.afRf.measurement.multiEval.demodulation.fmStereo.current.calculate() \n
		Query the demodulation results for the individual components of an FM stereo signal. CALCulate commands return error
		indicators instead of measurement values. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FMSTereo:CURRent?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Audio_Dev_Left: float: Peak frequency deviation due to the left audio channel Unit: Hz
			- 3 Audio_Dev_Right: float: Peak frequency deviation due to the right audio channel Unit: Hz
			- 4 Pilot_Deviation: float: Peak frequency deviation due to the pilot tone Unit: Hz
			- 5 Pilot_Freq_Error: float: Frequency error of the pilot tone Unit: Hz
			- 6 Rds_Deviation: float: Peak frequency deviation due to the signal in the RDS band Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Audio_Dev_Left'),
			ArgStruct.scalar_float('Audio_Dev_Right'),
			ArgStruct.scalar_float('Pilot_Deviation'),
			ArgStruct.scalar_float('Pilot_Freq_Error'),
			ArgStruct.scalar_float('Rds_Deviation')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Audio_Dev_Left: float = None
			self.Audio_Dev_Right: float = None
			self.Pilot_Deviation: float = None
			self.Pilot_Freq_Error: float = None
			self.Rds_Deviation: float = None

	def fetch(self) -> ResultData:
		"""FETCh:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FMSTereo:CURRent \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.demodulation.fmStereo.current.fetch() \n
		Query the demodulation results for the individual components of an FM stereo signal. CALCulate commands return error
		indicators instead of measurement values. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FMSTereo:CURRent?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FMSTereo:CURRent \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.demodulation.fmStereo.current.read() \n
		Query the demodulation results for the individual components of an FM stereo signal. CALCulate commands return error
		indicators instead of measurement values. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:AFRF:MEASurement<Instance>:MEValuation:DEModulation:FMSTereo:CURRent?', self.__class__.ResultData())
