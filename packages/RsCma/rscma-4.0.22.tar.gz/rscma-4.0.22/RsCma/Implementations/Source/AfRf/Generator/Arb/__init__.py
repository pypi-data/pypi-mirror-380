from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ArbCls:
	"""Arb commands group definition. 13 total commands, 3 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("arb", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_file'):
			from .File import FileCls
			self._file = FileCls(self._core, self._cmd_group)
		return self._file

	@property
	def marker(self):
		"""marker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import MarkerCls
			self._marker = MarkerCls(self._core, self._cmd_group)
		return self._marker

	@property
	def samples(self):
		"""samples commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_samples'):
			from .Samples import SamplesCls
			self._samples = SamplesCls(self._core, self._cmd_group)
		return self._samples

	def get_crate(self) -> float:
		"""SOURce:AFRF:GENerator<Instance>:ARB:CRATe \n
		Snippet: value: float = driver.source.afRf.generator.arb.get_crate() \n
		Queries the clock rate of the loaded ARB file. \n
			:return: clock_rate: Unit: Hz
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:ARB:CRATe?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_crc_protect(self) -> enums.YesNoStatus:
		"""SOURce:AFRF:GENerator<Instance>:ARB:CRCProtect \n
		Snippet: value: enums.YesNoStatus = driver.source.afRf.generator.arb.get_crc_protect() \n
		Queries whether the loaded ARB file contains a CRC checksum. \n
			:return: crc_protection: NO | YES
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:ARB:CRCProtect?')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)

	def get_foffset(self) -> float:
		"""SOURce:AFRF:GENerator<Instance>:ARB:FOFFset \n
		Snippet: value: float = driver.source.afRf.generator.arb.get_foffset() \n
		Defines a frequency offset to be imposed at the baseband during ARB generation. \n
			:return: frequency_offset: Range: -10 MHz to 10 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:ARB:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, frequency_offset: float) -> None:
		"""SOURce:AFRF:GENerator<Instance>:ARB:FOFFset \n
		Snippet: driver.source.afRf.generator.arb.set_foffset(frequency_offset = 1.0) \n
		Defines a frequency offset to be imposed at the baseband during ARB generation. \n
			:param frequency_offset: Range: -10 MHz to 10 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency_offset)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:ARB:FOFFset {param}')

	def get_loffset(self) -> float:
		"""SOURce:AFRF:GENerator<Instance>:ARB:LOFFset \n
		Snippet: value: float = driver.source.afRf.generator.arb.get_loffset() \n
		Queries the peak to average ratio (PAR) of the loaded ARB file. The PAR is also called level offset. \n
			:return: level_offset: Unit: dB
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:ARB:LOFFset?')
		return Conversions.str_to_float(response)

	def get_poffset(self) -> float:
		"""SOURce:AFRF:GENerator<Instance>:ARB:POFFset \n
		Snippet: value: float = driver.source.afRf.generator.arb.get_poffset() \n
		Queries the peak offset of the loaded ARB file. \n
			:return: peak_offset: Unit: dB
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:ARB:POFFset?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.RepeatMode:
		"""SOURce:AFRF:GENerator<Instance>:ARB:REPetition \n
		Snippet: value: enums.RepeatMode = driver.source.afRf.generator.arb.get_repetition() \n
		Defines how often the ARB file is processed. \n
			:return: repetition: CONTinuous | SINGle CONTinuous Cyclic continuous processing SINGle File is processed once
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:ARB:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.RepeatMode)

	def set_repetition(self, repetition: enums.RepeatMode) -> None:
		"""SOURce:AFRF:GENerator<Instance>:ARB:REPetition \n
		Snippet: driver.source.afRf.generator.arb.set_repetition(repetition = enums.RepeatMode.CONTinuous) \n
		Defines how often the ARB file is processed. \n
			:param repetition: CONTinuous | SINGle CONTinuous Cyclic continuous processing SINGle File is processed once
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.RepeatMode)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:ARB:REPetition {param}')

	def clone(self) -> 'ArbCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ArbCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
