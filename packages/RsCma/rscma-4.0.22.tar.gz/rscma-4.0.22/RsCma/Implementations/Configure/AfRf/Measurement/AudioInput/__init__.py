from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AudioInputCls:
	"""AudioInput commands group definition. 34 total commands, 14 Subgroups, 0 group commands
	Repeated Capability: AudioInput, default value after init: AudioInput.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("audioInput", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_audioInput_get', 'repcap_audioInput_set', repcap.AudioInput.Nr1)

	def repcap_audioInput_set(self, audioInput: repcap.AudioInput) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AudioInput.Default.
		Default value after init: AudioInput.Nr1"""
		self._cmd_group.set_repcap_enum_value(audioInput)

	def repcap_audioInput_get(self) -> repcap.AudioInput:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import LevelCls
			self._level = LevelCls(self._core, self._cmd_group)
		return self._level

	@property
	def first(self):
		"""first commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_first'):
			from .First import FirstCls
			self._first = FirstCls(self._core, self._cmd_group)
		return self._first

	@property
	def second(self):
		"""second commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_second'):
			from .Second import SecondCls
			self._second = SecondCls(self._core, self._cmd_group)
		return self._second

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import DelayCls
			self._delay = DelayCls(self._core, self._cmd_group)
		return self._delay

	@property
	def sdecay(self):
		"""sdecay commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdecay'):
			from .Sdecay import SdecayCls
			self._sdecay = SdecayCls(self._core, self._cmd_group)
		return self._sdecay

	@property
	def counter(self):
		"""counter commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_counter'):
			from .Counter import CounterCls
			self._counter = CounterCls(self._core, self._cmd_group)
		return self._counter

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def mlevel(self):
		"""mlevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mlevel'):
			from .Mlevel import MlevelCls
			self._mlevel = MlevelCls(self._core, self._cmd_group)
		return self._mlevel

	@property
	def aranging(self):
		"""aranging commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aranging'):
			from .Aranging import ArangingCls
			self._aranging = ArangingCls(self._core, self._cmd_group)
		return self._aranging

	@property
	def icoupling(self):
		"""icoupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_icoupling'):
			from .Icoupling import IcouplingCls
			self._icoupling = IcouplingCls(self._core, self._cmd_group)
		return self._icoupling

	@property
	def gcoupling(self):
		"""gcoupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gcoupling'):
			from .Gcoupling import GcouplingCls
			self._gcoupling = GcouplingCls(self._core, self._cmd_group)
		return self._gcoupling

	@property
	def tmode(self):
		"""tmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmode'):
			from .Tmode import TmodeCls
			self._tmode = TmodeCls(self._core, self._cmd_group)
		return self._tmode

	@property
	def filterPy(self):
		"""filterPy commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	def clone(self) -> 'AudioInputCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AudioInputCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
