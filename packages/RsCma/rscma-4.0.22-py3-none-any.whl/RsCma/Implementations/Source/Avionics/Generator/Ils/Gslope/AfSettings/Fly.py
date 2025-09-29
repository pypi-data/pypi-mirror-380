from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FlyCls:
	"""Fly commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fly", core, parent)

	def get_idirection(self) -> bool:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:AFSettings:FLY:IDIRection \n
		Snippet: value: bool = driver.source.avionics.generator.ils.gslope.afSettings.fly.get_idirection() \n
		Inverts the current direction towards the ideal line (fly up or fly down) . \n
			:return: invert_direction: OFF | ON
		"""
		response = self._core.io.query_str('SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:AFSettings:FLY:IDIRection?')
		return Conversions.str_to_bool(response)

	def set_idirection(self, invert_direction: bool) -> None:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:AFSettings:FLY:IDIRection \n
		Snippet: driver.source.avionics.generator.ils.gslope.afSettings.fly.set_idirection(invert_direction = False) \n
		Inverts the current direction towards the ideal line (fly up or fly down) . \n
			:param invert_direction: OFF | ON
		"""
		param = Conversions.bool_to_str(invert_direction)
		self._core.io.write(f'SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:AFSettings:FLY:IDIRection {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.UpDownDirection:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:AFSettings:FLY \n
		Snippet: value: enums.UpDownDirection = driver.source.avionics.generator.ils.gslope.afSettings.fly.get_value() \n
		Sets the direction towards the ideal line (fly up or fly down) and the sign of the configured DDM value. \n
			:return: direction: UP | DOWN
		"""
		response = self._core.io.query_str('SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:AFSettings:FLY?')
		return Conversions.str_to_scalar_enum(response, enums.UpDownDirection)

	def set_value(self, direction: enums.UpDownDirection) -> None:
		"""SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:AFSettings:FLY \n
		Snippet: driver.source.avionics.generator.ils.gslope.afSettings.fly.set_value(direction = enums.UpDownDirection.DOWN) \n
		Sets the direction towards the ideal line (fly up or fly down) and the sign of the configured DDM value. \n
			:param direction: UP | DOWN
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.UpDownDirection)
		self._core.io.write(f'SOURce:AVIonics:GENerator<Instance>:ILS:GSLope:AFSettings:FLY {param}')
