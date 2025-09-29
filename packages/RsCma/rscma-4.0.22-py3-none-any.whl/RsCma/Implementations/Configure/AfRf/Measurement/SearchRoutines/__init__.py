from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SearchRoutinesCls:
	"""SearchRoutines commands group definition. 50 total commands, 10 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("searchRoutines", core, parent)

	@property
	def taDelay(self):
		"""taDelay commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_taDelay'):
			from .TaDelay import TaDelayCls
			self._taDelay = TaDelayCls(self._core, self._cmd_group)
		return self._taDelay

	@property
	def limit(self):
		"""limit commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import LimitCls
			self._limit = LimitCls(self._core, self._cmd_group)
		return self._limit

	@property
	def lrfLevel(self):
		"""lrfLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lrfLevel'):
			from .LrfLevel import LrfLevelCls
			self._lrfLevel = LrfLevelCls(self._core, self._cmd_group)
		return self._lrfLevel

	@property
	def dialing(self):
		"""dialing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dialing'):
			from .Dialing import DialingCls
			self._dialing = DialingCls(self._core, self._cmd_group)
		return self._dialing

	@property
	def rx(self):
		"""rx commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_rx'):
			from .Rx import RxCls
			self._rx = RxCls(self._core, self._cmd_group)
		return self._rx

	@property
	def tx(self):
		"""tx commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_tx'):
			from .Tx import TxCls
			self._tx = TxCls(self._core, self._cmd_group)
		return self._tx

	@property
	def rifBandwidth(self):
		"""rifBandwidth commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rifBandwidth'):
			from .RifBandwidth import RifBandwidthCls
			self._rifBandwidth = RifBandwidthCls(self._core, self._cmd_group)
		return self._rifBandwidth

	@property
	def rsquelch(self):
		"""rsquelch commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_rsquelch'):
			from .Rsquelch import RsquelchCls
			self._rsquelch = RsquelchCls(self._core, self._cmd_group)
		return self._rsquelch

	@property
	def ssnr(self):
		"""ssnr commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_ssnr'):
			from .Ssnr import SsnrCls
			self._ssnr = SsnrCls(self._core, self._cmd_group)
		return self._ssnr

	@property
	def tsensitivity(self):
		"""tsensitivity commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_tsensitivity'):
			from .Tsensitivity import TsensitivityCls
			self._tsensitivity = TsensitivityCls(self._core, self._cmd_group)
		return self._tsensitivity

	def get_mrf_level(self) -> float:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:MRFLevel \n
		Snippet: value: float = driver.configure.afRf.measurement.searchRoutines.get_mrf_level() \n
		Configures the maximum RF level for the signal generator. Set a maximum RF level value that matches with the maximum
		input power of your DUT. A too high value of the RF level can damage your DUT. \n
			:return: max_level: Range: -130 dBm to -30 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:MRFLevel?')
		return Conversions.str_to_float(response)

	def set_mrf_level(self, max_level: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:MRFLevel \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.set_mrf_level(max_level = 1.0) \n
		Configures the maximum RF level for the signal generator. Set a maximum RF level value that matches with the maximum
		input power of your DUT. A too high value of the RF level can damage your DUT. \n
			:param max_level: Range: -130 dBm to -30 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(max_level)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:MRFLevel {param}')

	def get_sq_value(self) -> float:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:SQValue \n
		Snippet: value: float = driver.configure.afRf.measurement.searchRoutines.get_sq_value() \n
		Configures the target value for the audio signal quality parameters. \n
			:return: target_par_val: Range: 1 dB to 46 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:SQValue?')
		return Conversions.str_to_float(response)

	def set_sq_value(self, target_par_val: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:SQValue \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.set_sq_value(target_par_val = 1.0) \n
		Configures the target value for the audio signal quality parameters. \n
			:param target_par_val: Range: 1 dB to 46 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(target_par_val)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:SQValue {param}')

	# noinspection PyTypeChecker
	def get_sq_type(self) -> enums.TargetParType:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:SQTYpe \n
		Snippet: value: enums.TargetParType = driver.configure.afRf.measurement.searchRoutines.get_sq_type() \n
		Selects the type of audio signal quality to be measured. \n
			:return: target_par_type: SINad | SNRatio | SNNRatio | SNDNratio SINad Signal to noise and distortion SNRatio Signal-to-noise ratio S/N SNNRatio (S+N) /N SNDNratio (S+N+D) /N
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:SQTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.TargetParType)

	def set_sq_type(self, target_par_type: enums.TargetParType) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:SQTYpe \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.set_sq_type(target_par_type = enums.TargetParType.SINad) \n
		Selects the type of audio signal quality to be measured. \n
			:param target_par_type: SINad | SNRatio | SNNRatio | SNDNratio SINad Signal to noise and distortion SNRatio Signal-to-noise ratio S/N SNNRatio (S+N) /N SNDNratio (S+N+D) /N
		"""
		param = Conversions.enum_scalar_to_str(target_par_type, enums.TargetParType)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:SQTYpe {param}')

	def get_stolerance(self) -> float:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:STOLerance \n
		Snippet: value: float = driver.configure.afRf.measurement.searchRoutines.get_stolerance() \n
		Configures the maximum allowed deviation of the current signal quality from the average signal quality. \n
			:return: tolerance: Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:STOLerance?')
		return Conversions.str_to_float(response)

	def set_stolerance(self, tolerance: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:STOLerance \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.set_stolerance(tolerance = 1.0) \n
		Configures the maximum allowed deviation of the current signal quality from the average signal quality. \n
			:param tolerance: Unit: dB
		"""
		param = Conversions.decimal_value_to_str(tolerance)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:STOLerance {param}')

	# noinspection PyTypeChecker
	def get_path(self) -> enums.SearchRoutinePath:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:PATH \n
		Snippet: value: enums.SearchRoutinePath = driver.configure.afRf.measurement.searchRoutines.get_path() \n
		Configures the path from where the test instrument receives the audio input by the connector or by 'VoIP'. \n
			:return: path: AFI1 | AFI2 | VOIP
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:PATH?')
		return Conversions.str_to_scalar_enum(response, enums.SearchRoutinePath)

	def set_path(self, path: enums.SearchRoutinePath) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:PATH \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.set_path(path = enums.SearchRoutinePath.AFI1) \n
		Configures the path from where the test instrument receives the audio input by the connector or by 'VoIP'. \n
			:param path: AFI1 | AFI2 | VOIP
		"""
		param = Conversions.enum_scalar_to_str(path, enums.SearchRoutinePath)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:PATH {param}')

	def get_timeout(self) -> float:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:TOUT \n
		Snippet: value: float = driver.configure.afRf.measurement.searchRoutines.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated via the graphical user interface. The timer is reset after the first
		measurement cycle. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped and the reliability indicator is set to 1. Still running READ, FETCh or CALCulate commands are completed,
		returning the available results. At least for some results, there are no values at all or the statistical depth has not
		been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:return: tcd_timeout: Unit: s
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SROutines:TOUT \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.set_timeout(tcd_timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated via the graphical user interface. The timer is reset after the first
		measurement cycle. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped and the reliability indicator is set to 1. Still running READ, FETCh or CALCulate commands are completed,
		returning the available results. At least for some results, there are no values at all or the statistical depth has not
		been reached. A timeout of 0 s corresponds to an infinite measurement timeout. \n
			:param tcd_timeout: Unit: s
		"""
		param = Conversions.decimal_value_to_str(tcd_timeout)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TOUT {param}')

	def clone(self) -> 'SearchRoutinesCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SearchRoutinesCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
