from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RifBandwidthCls:
	"""RifBandwidth commands group definition. 16 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rifBandwidth", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def slevel(self):
		"""slevel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_slevel'):
			from .Slevel import SlevelCls
			self._slevel = SlevelCls(self._core, self._cmd_group)
		return self._slevel

	@property
	def nlevel(self):
		"""nlevel commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_nlevel'):
			from .Nlevel import NlevelCls
			self._nlevel = NlevelCls(self._core, self._cmd_group)
		return self._nlevel

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def coffset(self):
		"""coffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_coffset'):
			from .Coffset import CoffsetCls
			self._coffset = CoffsetCls(self._core, self._cmd_group)
		return self._coffset

	@property
	def signalQuality(self):
		"""signalQuality commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_signalQuality'):
			from .SignalQuality import SignalQualityCls
			self._signalQuality = SignalQualityCls(self._core, self._cmd_group)
		return self._signalQuality

	def clone(self) -> 'RifBandwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RifBandwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
