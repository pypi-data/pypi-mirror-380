from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 410 total commands, 15 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def digital(self):
		"""digital commands group. 8 Sub-classes, 8 commands."""
		if not hasattr(self, '_digital'):
			from .Digital import DigitalCls
			self._digital = DigitalCls(self._core, self._cmd_group)
		return self._digital

	@property
	def delta(self):
		"""delta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delta'):
			from .Delta import DeltaCls
			self._delta = DeltaCls(self._core, self._cmd_group)
		return self._delta

	@property
	def voip(self):
		"""voip commands group. 7 Sub-classes, 5 commands."""
		if not hasattr(self, '_voip'):
			from .Voip import VoipCls
			self._voip = VoipCls(self._core, self._cmd_group)
		return self._voip

	@property
	def spdif(self):
		"""spdif commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_spdif'):
			from .Spdif import SpdifCls
			self._spdif = SpdifCls(self._core, self._cmd_group)
		return self._spdif

	@property
	def audioInput(self):
		"""audioInput commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_audioInput'):
			from .AudioInput import AudioInputCls
			self._audioInput = AudioInputCls(self._core, self._cmd_group)
		return self._audioInput

	@property
	def demodulation(self):
		"""demodulation commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_demodulation'):
			from .Demodulation import DemodulationCls
			self._demodulation = DemodulationCls(self._core, self._cmd_group)
		return self._demodulation

	@property
	def rfCarrier(self):
		"""rfCarrier commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfCarrier'):
			from .RfCarrier import RfCarrierCls
			self._rfCarrier = RfCarrierCls(self._core, self._cmd_group)
		return self._rfCarrier

	@property
	def searchRoutines(self):
		"""searchRoutines commands group. 10 Sub-classes, 6 commands."""
		if not hasattr(self, '_searchRoutines'):
			from .SearchRoutines import SearchRoutinesCls
			self._searchRoutines = SearchRoutinesCls(self._core, self._cmd_group)
		return self._searchRoutines

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def multiEval(self):
		"""multiEval commands group. 13 Sub-classes, 8 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEvalCls
			self._multiEval = MultiEvalCls(self._core, self._cmd_group)
		return self._multiEval

	@property
	def rfSettings(self):
		"""rfSettings commands group. 2 Sub-classes, 8 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettingsCls
			self._rfSettings = RfSettingsCls(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def cdefinition(self):
		"""cdefinition commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_cdefinition'):
			from .Cdefinition import CdefinitionCls
			self._cdefinition = CdefinitionCls(self._core, self._cmd_group)
		return self._cdefinition

	@property
	def audioOutput(self):
		"""audioOutput commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_audioOutput'):
			from .AudioOutput import AudioOutputCls
			self._audioOutput = AudioOutputCls(self._core, self._cmd_group)
		return self._audioOutput

	@property
	def sout(self):
		"""sout commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_sout'):
			from .Sout import SoutCls
			self._sout = SoutCls(self._core, self._cmd_group)
		return self._sout

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
