from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	@property
	def rfOut(self):
		"""rfOut commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfOut'):
			from .RfOut import RfOutCls
			self._rfOut = RfOutCls(self._core, self._cmd_group)
		return self._rfOut

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import ChannelCls
			self._channel = ChannelCls(self._core, self._cmd_group)
		return self._channel

	def get_frequency(self) -> float:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:RFSettings:FREQuency \n
		Snippet: value: float = driver.source.avionics.generator.ils.gslope.rfSettings.get_frequency() \n
		Specifies the center frequency of the unmodulated RF carrier for the glide slope signal. \n
			:return: freq: Range: 100 kHz to 3 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, freq: float) -> None:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:RFSettings:FREQuency \n
		Snippet: driver.source.avionics.generator.ils.gslope.rfSettings.set_frequency(freq = 1.0) \n
		Specifies the center frequency of the unmodulated RF carrier for the glide slope signal. \n
			:param freq: Range: 100 kHz to 3 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(freq)
		self._core.io.write(f'SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:RFSettings:FREQuency {param}')

	def get_level(self) -> float:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:RFSettings:LEVel \n
		Snippet: value: float = driver.source.avionics.generator.ils.gslope.rfSettings.get_level() \n
		Specifies the RMS level of the unmodulated RF carrier. The allowed range depends on several other settings, for example
		on the selected connector, the frequency and the external attenuation. For supported output level ranges, refer to the
		data sheet. \n
			:return: level: Unit: dBm
		"""
		response = self._core.io.query_str('SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:RFSettings:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, level: float) -> None:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:RFSettings:LEVel \n
		Snippet: driver.source.avionics.generator.ils.gslope.rfSettings.set_level(level = 1.0) \n
		Specifies the RMS level of the unmodulated RF carrier. The allowed range depends on several other settings, for example
		on the selected connector, the frequency and the external attenuation. For supported output level ranges, refer to the
		data sheet. \n
			:param level: Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:RFSettings:LEVel {param}')

	def clone(self) -> 'RfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
