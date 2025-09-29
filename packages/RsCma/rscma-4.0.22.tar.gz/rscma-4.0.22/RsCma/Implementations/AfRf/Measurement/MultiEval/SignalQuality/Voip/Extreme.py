from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Thd_Percent: enums.ResultStatus: Total harmonic distortion in percent Unit: %
			- 3 Thd: float or bool: Total harmonic distortion in dB Unit: dB
			- 4 Thd_Plus_Noise: float or bool: Total harmonic distortion and noise Unit: %
			- 5 Sinad: enums.ResultStatus: Signal to noise and distortion Unit: dB
			- 6 Snr: enums.ResultStatus: Signal-to-noise ratio S/N Unit: dB
			- 7 Snr_Plus_Noise: float or bool: (S+N) /N Unit: dB
			- 8 Snr_Plus_Noinse_Plus_Dist: float or bool: (S+N+D) /N Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Thd_Percent', enums.ResultStatus),
			ArgStruct.scalar_float_ext('Thd'),
			ArgStruct.scalar_float_ext('Thd_Plus_Noise'),
			ArgStruct.scalar_enum('Sinad', enums.ResultStatus),
			ArgStruct.scalar_enum('Snr', enums.ResultStatus),
			ArgStruct.scalar_float_ext('Snr_Plus_Noise'),
			ArgStruct.scalar_float_ext('Snr_Plus_Noinse_Plus_Dist')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Thd_Percent: enums.ResultStatus = None
			self.Thd: float or bool = None
			self.Thd_Plus_Noise: float or bool = None
			self.Sinad: enums.ResultStatus = None
			self.Snr: enums.ResultStatus = None
			self.Snr_Plus_Noise: float or bool = None
			self.Snr_Plus_Noinse_Plus_Dist: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""CALCulate:AFRF:MEASurement<Instance>:MEValuation:SQUality:VOIP:EXTReme \n
		Snippet: value: CalculateStruct = driver.afRf.measurement.multiEval.signalQuality.voip.extreme.calculate() \n
		Query the signal quality results measured for the VoIP path. CALCulate commands return error indicators instead of
		measurement values. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:AFRF:MEASurement<Instance>:MEValuation:SQUality:VOIP:EXTReme?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Thd_Percent: float: Total harmonic distortion in percent Unit: %
			- 3 Thd: float: Total harmonic distortion in dB Unit: dB
			- 4 Thd_Plus_Noise: float: Total harmonic distortion and noise Unit: %
			- 5 Sinad: float: Signal to noise and distortion Unit: dB
			- 6 Snr: float: Signal-to-noise ratio S/N Unit: dB
			- 7 Snr_Plus_Noise: float: (S+N) /N Unit: dB
			- 8 Snr_Plus_Noinse_Plus_Dist: float: (S+N+D) /N Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Thd_Percent'),
			ArgStruct.scalar_float('Thd'),
			ArgStruct.scalar_float('Thd_Plus_Noise'),
			ArgStruct.scalar_float('Sinad'),
			ArgStruct.scalar_float('Snr'),
			ArgStruct.scalar_float('Snr_Plus_Noise'),
			ArgStruct.scalar_float('Snr_Plus_Noinse_Plus_Dist')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Thd_Percent: float = None
			self.Thd: float = None
			self.Thd_Plus_Noise: float = None
			self.Sinad: float = None
			self.Snr: float = None
			self.Snr_Plus_Noise: float = None
			self.Snr_Plus_Noinse_Plus_Dist: float = None

	def fetch(self) -> ResultData:
		"""FETCh:AFRF:MEASurement<Instance>:MEValuation:SQUality:VOIP:EXTReme \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.signalQuality.voip.extreme.fetch() \n
		Query the signal quality results measured for the VoIP path. CALCulate commands return error indicators instead of
		measurement values. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:MEValuation:SQUality:VOIP:EXTReme?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:AFRF:MEASurement<Instance>:MEValuation:SQUality:VOIP:EXTReme \n
		Snippet: value: ResultData = driver.afRf.measurement.multiEval.signalQuality.voip.extreme.read() \n
		Query the signal quality results measured for the VoIP path. CALCulate commands return error indicators instead of
		measurement values. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:AFRF:MEASurement<Instance>:MEValuation:SQUality:VOIP:EXTReme?', self.__class__.ResultData())
