from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeltaCls:
	"""Delta commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delta", core, parent)

	@property
	def user(self):
		"""user commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_user'):
			from .User import UserCls
			self._user = UserCls(self._core, self._cmd_group)
		return self._user

	@property
	def update(self):
		"""update commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .Update import UpdateCls
			self._update = UpdateCls(self._core, self._cmd_group)
		return self._update

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.DeltaMode:
		"""CONFigure:AFRF:MEASurement<Instance>:SIN:FREQuency:DELTa:MODE \n
		Snippet: value: enums.DeltaMode = driver.configure.afRf.measurement.spdif.frequency.delta.get_mode() \n
		Configures the AF frequency reference mode for SPDIF path. \n
			:return: mode: NONE | MEAS | USER
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SIN:FREQuency:DELTa:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DeltaMode)

	def set_mode(self, mode: enums.DeltaMode) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SIN:FREQuency:DELTa:MODE \n
		Snippet: driver.configure.afRf.measurement.spdif.frequency.delta.set_mode(mode = enums.DeltaMode.MEAS) \n
		Configures the AF frequency reference mode for SPDIF path. \n
			:param mode: NONE | MEAS | USER
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DeltaMode)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SIN:FREQuency:DELTa:MODE {param}')

	# noinspection PyTypeChecker
	class MeasuredStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Left_Val: float: Unit: Hz
			- Right_Val: float: Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Left_Val'),
			ArgStruct.scalar_float('Right_Val')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Left_Val: float=None
			self.Right_Val: float=None

	def get_measured(self) -> MeasuredStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:SIN:FREQuency:DELTa:MEASured \n
		Snippet: value: MeasuredStruct = driver.configure.afRf.measurement.spdif.frequency.delta.get_measured() \n
		Configures the AF frequency measured reference value for SPDIF path. \n
			:return: structure: for return value, see the help for MeasuredStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:AFRF:MEASurement<Instance>:SIN:FREQuency:DELTa:MEASured?', self.__class__.MeasuredStruct())

	def clone(self) -> 'DeltaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DeltaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
