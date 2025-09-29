from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BaseCls:
	"""Base commands group definition. 25 total commands, 11 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def reference(self):
		"""reference commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import ReferenceCls
			self._reference = ReferenceCls(self._core, self._cmd_group)
		return self._reference

	@property
	def gotsystem(self):
		"""gotsystem commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gotsystem'):
			from .Gotsystem import GotsystemCls
			self._gotsystem = GotsystemCls(self._core, self._cmd_group)
		return self._gotsystem

	@property
	def finish(self):
		"""finish commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_finish'):
			from .Finish import FinishCls
			self._finish = FinishCls(self._core, self._cmd_group)
		return self._finish

	@property
	def shutdown(self):
		"""shutdown commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_shutdown'):
			from .Shutdown import ShutdownCls
			self._shutdown = ShutdownCls(self._core, self._cmd_group)
		return self._shutdown

	@property
	def restart(self):
		"""restart commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_restart'):
			from .Restart import RestartCls
			self._restart = RestartCls(self._core, self._cmd_group)
		return self._restart

	@property
	def device(self):
		"""device commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_device'):
			from .Device import DeviceCls
			self._device = DeviceCls(self._core, self._cmd_group)
		return self._device

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import DateCls
			self._date = DateCls(self._core, self._cmd_group)
		return self._date

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	@property
	def option(self):
		"""option commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_option'):
			from .Option import OptionCls
			self._option = OptionCls(self._core, self._cmd_group)
		return self._option

	@property
	def password(self):
		"""password commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_password'):
			from .Password import PasswordCls
			self._password = PasswordCls(self._core, self._cmd_group)
		return self._password

	@property
	def display(self):
		"""display commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_display'):
			from .Display import DisplayCls
			self._display = DisplayCls(self._core, self._cmd_group)
		return self._display

	def get_reliability(self) -> int:
		"""SYSTem:BASE:RELiability \n
		Snippet: value: int = driver.system.base.get_reliability() \n
		Returns a reliability value, indicating errors detected by the base software. \n
			:return: value: See 'Reliability indicator'
		"""
		response = self._core.io.query_str('SYSTem:BASE:RELiability?')
		return Conversions.str_to_int(response)

	def get_did(self) -> str:
		"""SYSTem:BASE:DID \n
		Snippet: value: str = driver.system.base.get_did() \n
		No command help available \n
			:return: device_id: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:DID?')
		return trim_str_response(response)

	def get_klock(self) -> bool:
		"""SYSTem:BASE:KLOCk \n
		Snippet: value: bool = driver.system.base.get_klock() \n
		No command help available \n
			:return: klock: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:KLOCk?')
		return Conversions.str_to_bool(response)

	def set_klock(self, klock: bool) -> None:
		"""SYSTem:BASE:KLOCk \n
		Snippet: driver.system.base.set_klock(klock = False) \n
		No command help available \n
			:param klock: No help available
		"""
		param = Conversions.bool_to_str(klock)
		self._core.io.write(f'SYSTem:BASE:KLOCk {param}')

	def get_version(self) -> float:
		"""SYSTem:BASE:VERSion \n
		Snippet: value: float = driver.system.base.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:VERSion?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'BaseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BaseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
