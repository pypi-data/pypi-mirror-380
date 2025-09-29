from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	# noinspection PyTypeChecker
	def fetch(self) -> enums.ResourceState:
		"""FETCh:AFRF:MEASurement<Instance>:SROutines:STATe \n
		Snippet: value: enums.ResourceState = driver.afRf.measurement.searchRoutines.state.fetch() \n
		Queries the main search routine state. \n
			:return: meas_state: OFF | RDY | RUN OFF Measurement is off RDY Measurement has been paused or is finished RUN Measurement is running"""
		response = self._core.io.query_str(f'FETCh:AFRF:MEASurement<Instance>:SROutines:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.ResourceState)

	def clone(self) -> 'StateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
