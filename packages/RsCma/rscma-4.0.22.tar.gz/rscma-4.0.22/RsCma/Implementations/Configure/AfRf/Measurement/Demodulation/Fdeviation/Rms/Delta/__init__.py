from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeltaCls:
	"""Delta commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delta", core, parent)

	@property
	def update(self):
		"""update commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .Update import UpdateCls
			self._update = UpdateCls(self._core, self._cmd_group)
		return self._update

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.DeltaMode:
		"""CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:MODE \n
		Snippet: value: enums.DeltaMode = driver.configure.afRf.measurement.demodulation.fdeviation.rms.delta.get_mode() \n
		Configures the reference mode of the RMS frequency deviation value for delta measurement. \n
			:return: mode: NONE | MEAS | USER
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DeltaMode)

	def set_mode(self, mode: enums.DeltaMode) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:MODE \n
		Snippet: driver.configure.afRf.measurement.demodulation.fdeviation.rms.delta.set_mode(mode = enums.DeltaMode.MEAS) \n
		Configures the reference mode of the RMS frequency deviation value for delta measurement. \n
			:param mode: NONE | MEAS | USER
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DeltaMode)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:MODE {param}')

	def get_user(self) -> float:
		"""CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:USER \n
		Snippet: value: float = driver.configure.afRf.measurement.demodulation.fdeviation.rms.delta.get_user() \n
		Configures the user RMS frequency deviation reference value for delta measurement. \n
			:return: user_val: Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:USER?')
		return Conversions.str_to_float(response)

	def set_user(self, user_val: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:USER \n
		Snippet: driver.configure.afRf.measurement.demodulation.fdeviation.rms.delta.set_user(user_val = 1.0) \n
		Configures the user RMS frequency deviation reference value for delta measurement. \n
			:param user_val: Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(user_val)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:USER {param}')

	def get_measured(self) -> float:
		"""CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:MEASured \n
		Snippet: value: float = driver.configure.afRf.measurement.demodulation.fdeviation.rms.delta.get_measured() \n
		Configures the measured RMS frequency deviation reference value for delta measurement. \n
			:return: meas_val: Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DEModulation:FDEViation:RMS:DELTa:MEASured?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'DeltaCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DeltaCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
