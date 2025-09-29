from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AfSettingsCls:
	"""AfSettings commands group definition. 12 total commands, 4 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("afSettings", core, parent)

	@property
	def audioOutput(self):
		"""audioOutput commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_audioOutput'):
			from .AudioOutput import AudioOutputCls
			self._audioOutput = AudioOutputCls(self._core, self._cmd_group)
		return self._audioOutput

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def fmoddepth(self):
		"""fmoddepth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmoddepth'):
			from .Fmoddepth import FmoddepthCls
			self._fmoddepth = FmoddepthCls(self._core, self._cmd_group)
		return self._fmoddepth

	@property
	def fly(self):
		"""fly commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_fly'):
			from .Fly import FlyCls
			self._fly = FlyCls(self._core, self._cmd_group)
		return self._fly

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.AudioConnector:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:CONNector \n
		Snippet: value: enums.AudioConnector = driver.source.avionics.generator.ils.localizer.afSettings.get_connector() \n
		Selects the output connector for the generated AF signal (AF1 OUT or AF2 OUT) . If you want to route both the localizer
		signal and the glide slope signal to an AF output, you must configure different connectors for the two signals. \n
			:return: connector: AF1O | AF2O
		"""
		response = self._core.io.query_str('SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.AudioConnector)

	def set_connector(self, connector: enums.AudioConnector) -> None:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:CONNector \n
		Snippet: driver.source.avionics.generator.ils.localizer.afSettings.set_connector(connector = enums.AudioConnector.AF1O) \n
		Selects the output connector for the generated AF signal (AF1 OUT or AF2 OUT) . If you want to route both the localizer
		signal and the glide slope signal to an AF output, you must configure different connectors for the two signals. \n
			:param connector: AF1O | AF2O
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.AudioConnector)
		self._core.io.write(f'SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:CONNector {param}')

	def get_enable(self) -> bool:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:ENABle \n
		Snippet: value: bool = driver.source.avionics.generator.ils.localizer.afSettings.get_enable() \n
		Enables or disables the modulation of the RF carrier with the audio tones for the two lobes. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:ENABle \n
		Snippet: driver.source.avionics.generator.ils.localizer.afSettings.set_enable(enable = False) \n
		Enables or disables the modulation of the RF carrier with the audio tones for the two lobes. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:ENABle {param}')

	def get_sdm(self) -> float:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:SDM \n
		Snippet: value: float = driver.source.avionics.generator.ils.localizer.afSettings.get_sdm() \n
		Sets the sum of depth of modulations (SDM) . \n
			:return: mod_depth: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:SDM?')
		return Conversions.str_to_float(response)

	def set_sdm(self, mod_depth: float) -> None:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:SDM \n
		Snippet: driver.source.avionics.generator.ils.localizer.afSettings.set_sdm(mod_depth = 1.0) \n
		Sets the sum of depth of modulations (SDM) . \n
			:param mod_depth: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(mod_depth)
		self._core.io.write(f'SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:SDM {param}')

	def get_ddm(self) -> float:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:DDM \n
		Snippet: value: float = driver.source.avionics.generator.ils.localizer.afSettings.get_ddm() \n
		Sets the difference in modulation depth between the two lobes. The maximum allowed absolute value is limited by the
		configured SDM value. \n
			:return: ddm: Range: -100 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:DDM?')
		return Conversions.str_to_float(response)

	def set_ddm(self, ddm: float) -> None:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:DDM \n
		Snippet: driver.source.avionics.generator.ils.localizer.afSettings.set_ddm(ddm = 1.0) \n
		Sets the difference in modulation depth between the two lobes. The maximum allowed absolute value is limited by the
		configured SDM value. \n
			:param ddm: Range: -100 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(ddm)
		self._core.io.write(f'SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:DDM {param}')

	def get_poffset(self) -> float:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:POFFset \n
		Snippet: value: float = driver.source.avionics.generator.ils.localizer.afSettings.get_poffset() \n
		Sets the phase offset between the audio signals of the two lobes. \n
			:return: poffset: Range: -60 deg to 120 deg, Unit: deg
		"""
		response = self._core.io.query_str('SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:POFFset?')
		return Conversions.str_to_float(response)

	def set_poffset(self, poffset: float) -> None:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:POFFset \n
		Snippet: driver.source.avionics.generator.ils.localizer.afSettings.set_poffset(poffset = 1.0) \n
		Sets the phase offset between the audio signals of the two lobes. \n
			:param poffset: Range: -60 deg to 120 deg, Unit: deg
		"""
		param = Conversions.decimal_value_to_str(poffset)
		self._core.io.write(f'SOURce:AVIonics:GENerator<Instance>:ILS:LOCalizer:AFSettings:POFFset {param}')

	def clone(self) -> 'AfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
