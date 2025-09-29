from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsensitivityCls:
	"""Rsensitivity commands group definition. 10 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsensitivity", core, parent)

	@property
	def rfLevel(self):
		"""rfLevel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfLevel'):
			from .RfLevel import RfLevelCls
			self._rfLevel = RfLevelCls(self._core, self._cmd_group)
		return self._rfLevel

	@property
	def signalQuality(self):
		"""signalQuality commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_signalQuality'):
			from .SignalQuality import SignalQualityCls
			self._signalQuality = SignalQualityCls(self._core, self._cmd_group)
		return self._signalQuality

	@property
	def sensitivity(self):
		"""sensitivity commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_sensitivity'):
			from .Sensitivity import SensitivityCls
			self._sensitivity = SensitivityCls(self._core, self._cmd_group)
		return self._sensitivity

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Sensitivity_Level: float: Measured RX sensitivity level (RF level) Unit: dBm
			- 3 Signal_Quality: float: Audio signal quality value measured at the RX sensitivity level Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Sensitivity_Level'),
			ArgStruct.scalar_float('Signal_Quality')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Sensitivity_Level: float = None
			self.Signal_Quality: float = None

	def fetch(self) -> ResultData:
		"""FETCh:AFRF:MEASurement<Instance>:SROutines:RSENsitivity \n
		Snippet: value: ResultData = driver.afRf.measurement.searchRoutines.rsensitivity.fetch() \n
		Query the single results of the RX sensitivity search routine. CALCulate commands return error indicators instead of
		measurement values. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:SROutines:RSENsitivity?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Sensitivity_Level: enums.ResultStatus: Measured RX sensitivity level (RF level) Unit: dBm
			- 3 Signal_Quality: enums.ResultStatus: Audio signal quality value measured at the RX sensitivity level Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Sensitivity_Level', enums.ResultStatus),
			ArgStruct.scalar_enum('Signal_Quality', enums.ResultStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Sensitivity_Level: enums.ResultStatus = None
			self.Signal_Quality: enums.ResultStatus = None

	def calculate(self) -> CalculateStruct:
		"""CALCulate:AFRF:MEASurement<Instance>:SROutines:RSENsitivity \n
		Snippet: value: CalculateStruct = driver.afRf.measurement.searchRoutines.rsensitivity.calculate() \n
		Query the single results of the RX sensitivity search routine. CALCulate commands return error indicators instead of
		measurement values. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:AFRF:MEASurement<Instance>:SROutines:RSENsitivity?', self.__class__.CalculateStruct())

	def read(self) -> ResultData:
		"""READ:AFRF:MEASurement<Instance>:SROutines:RSENsitivity \n
		Snippet: value: ResultData = driver.afRf.measurement.searchRoutines.rsensitivity.read() \n
		Query the single results of the RX sensitivity search routine. CALCulate commands return error indicators instead of
		measurement values. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:AFRF:MEASurement<Instance>:SROutines:RSENsitivity?', self.__class__.ResultData())

	def clone(self) -> 'RsensitivityCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RsensitivityCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
