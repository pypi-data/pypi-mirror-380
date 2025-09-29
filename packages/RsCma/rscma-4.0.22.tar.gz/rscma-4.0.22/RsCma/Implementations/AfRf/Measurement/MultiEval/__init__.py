from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 537 total commands, 14 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	@property
	def audioInput(self):
		"""audioInput commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_audioInput'):
			from .AudioInput import AudioInputCls
			self._audioInput = AudioInputCls(self._core, self._cmd_group)
		return self._audioInput

	@property
	def spdifLeft(self):
		"""spdifLeft commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_spdifLeft'):
			from .SpdifLeft import SpdifLeftCls
			self._spdifLeft = SpdifLeftCls(self._core, self._cmd_group)
		return self._spdifLeft

	@property
	def spdifRight(self):
		"""spdifRight commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_spdifRight'):
			from .SpdifRight import SpdifRightCls
			self._spdifRight = SpdifRightCls(self._core, self._cmd_group)
		return self._spdifRight

	@property
	def voip(self):
		"""voip commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_voip'):
			from .Voip import VoipCls
			self._voip = VoipCls(self._core, self._cmd_group)
		return self._voip

	@property
	def demodLeft(self):
		"""demodLeft commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_demodLeft'):
			from .DemodLeft import DemodLeftCls
			self._demodLeft = DemodLeftCls(self._core, self._cmd_group)
		return self._demodLeft

	@property
	def demodRight(self):
		"""demodRight commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_demodRight'):
			from .DemodRight import DemodRightCls
			self._demodRight = DemodRightCls(self._core, self._cmd_group)
		return self._demodRight

	@property
	def demodulation(self):
		"""demodulation commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_demodulation'):
			from .Demodulation import DemodulationCls
			self._demodulation = DemodulationCls(self._core, self._cmd_group)
		return self._demodulation

	@property
	def rfCarrier(self):
		"""rfCarrier commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfCarrier'):
			from .RfCarrier import RfCarrierCls
			self._rfCarrier = RfCarrierCls(self._core, self._cmd_group)
		return self._rfCarrier

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def oscilloscope(self):
		"""oscilloscope commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_oscilloscope'):
			from .Oscilloscope import OscilloscopeCls
			self._oscilloscope = OscilloscopeCls(self._core, self._cmd_group)
		return self._oscilloscope

	@property
	def spdif(self):
		"""spdif commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spdif'):
			from .Spdif import SpdifCls
			self._spdif = SpdifCls(self._core, self._cmd_group)
		return self._spdif

	@property
	def signalQuality(self):
		"""signalQuality commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_signalQuality'):
			from .SignalQuality import SignalQualityCls
			self._signalQuality = SignalQualityCls(self._core, self._cmd_group)
		return self._signalQuality

	@property
	def tones(self):
		"""tones commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_tones'):
			from .Tones import TonesCls
			self._tones = TonesCls(self._core, self._cmd_group)
		return self._tones

	@property
	def fft(self):
		"""fft commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_fft'):
			from .Fft import FftCls
			self._fft = FftCls(self._core, self._cmd_group)
		return self._fft

	def initiate(self, opc_timeout_ms: int = -1) -> None:
		"""INITiate:AFRF:MEASurement<Instance>:MEValuation \n
		Snippet: driver.afRf.measurement.multiEval.initiate() \n
		Starts or continues the analyzer. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:AFRF:MEASurement<Instance>:MEValuation', opc_timeout_ms)
		# OpcSyncAllowed = true

	def stop(self) -> None:
		"""STOP:AFRF:MEASurement<Instance>:MEValuation \n
		Snippet: driver.afRf.measurement.multiEval.stop() \n
		Pauses the analyzer. \n
		"""
		self._core.io.write(f'STOP:AFRF:MEASurement<Instance>:MEValuation')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""STOP:AFRF:MEASurement<Instance>:MEValuation \n
		Snippet: driver.afRf.measurement.multiEval.stop_with_opc() \n
		Pauses the analyzer. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCma.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:AFRF:MEASurement<Instance>:MEValuation', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""ABORt:AFRF:MEASurement<Instance>:MEValuation \n
		Snippet: driver.afRf.measurement.multiEval.abort() \n
		Stops the analyzer. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:AFRF:MEASurement<Instance>:MEValuation', opc_timeout_ms)
		# OpcSyncAllowed = true

	def clone(self) -> 'MultiEvalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEvalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
