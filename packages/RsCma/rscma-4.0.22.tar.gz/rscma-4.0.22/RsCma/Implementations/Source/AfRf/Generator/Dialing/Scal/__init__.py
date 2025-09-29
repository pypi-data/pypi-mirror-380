from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScalCls:
	"""Scal commands group definition. 9 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scal", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def userDefined(self):
		"""userDefined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_userDefined'):
			from .UserDefined import UserDefinedCls
			self._userDefined = UserDefinedCls(self._core, self._cmd_group)
		return self._userDefined

	@property
	def ttime(self):
		"""ttime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttime'):
			from .Ttime import TtimeCls
			self._ttime = TtimeCls(self._core, self._cmd_group)
		return self._ttime

	# noinspection PyTypeChecker
	def get_standard(self) -> enums.SelCalStandard:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:STANdard \n
		Snippet: value: enums.SelCalStandard = driver.source.afRf.generator.dialing.scal.get_standard() \n
		Selects the SELCAL standard. Selecting the standard also determines the dual-tone frequencies that the CMA generates when
		generating a SELCAL dialing signal. \n
			:return: standard: SCAL16 | SCAL32 | UDEFined SCAL16 SELCAL16 standard and corresponding frequencies SCAL32 SELCAL32 standard and corresponding frequencies UDEFined User-defined dual-tone frequencies
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.SelCalStandard)

	def set_standard(self, standard: enums.SelCalStandard) -> None:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:STANdard \n
		Snippet: driver.source.afRf.generator.dialing.scal.set_standard(standard = enums.SelCalStandard.SCAL16) \n
		Selects the SELCAL standard. Selecting the standard also determines the dual-tone frequencies that the CMA generates when
		generating a SELCAL dialing signal. \n
			:param standard: SCAL16 | SCAL32 | UDEFined SCAL16 SELCAL16 standard and corresponding frequencies SCAL32 SELCAL32 standard and corresponding frequencies UDEFined User-defined dual-tone frequencies
		"""
		param = Conversions.enum_scalar_to_str(standard, enums.SelCalStandard)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:STANdard {param}')

	def get_sequence(self) -> str:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SEQuence \n
		Snippet: value: str = driver.source.afRf.generator.dialing.scal.get_sequence() \n
		Specifies the SELCAL code (without the hyphen) . \n
			:return: scal_sequence: String with four letters The allowed letters are A to H, J to M and P to S. A letter must not appear twice. The first two letters and the last two letters must be ordered alphabetically.
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SEQuence?')
		return trim_str_response(response)

	def set_sequence(self, scal_sequence: str) -> None:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SEQuence \n
		Snippet: driver.source.afRf.generator.dialing.scal.set_sequence(scal_sequence = 'abc') \n
		Specifies the SELCAL code (without the hyphen) . \n
			:param scal_sequence: String with four letters The allowed letters are A to H, J to M and P to S. A letter must not appear twice. The first two letters and the last two letters must be ordered alphabetically.
		"""
		param = Conversions.value_to_quoted_str(scal_sequence)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SEQuence {param}')

	def get_srepeat(self) -> int:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SREPeat \n
		Snippet: value: int = driver.source.afRf.generator.dialing.scal.get_srepeat() \n
		Defines how often a SELCAL sequence (two dual tones) is repeated. \n
			:return: sequence_repeat: Range: 1 to 100
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SREPeat?')
		return Conversions.str_to_int(response)

	def set_srepeat(self, sequence_repeat: int) -> None:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SREPeat \n
		Snippet: driver.source.afRf.generator.dialing.scal.set_srepeat(sequence_repeat = 1) \n
		Defines how often a SELCAL sequence (two dual tones) is repeated. \n
			:param sequence_repeat: Range: 1 to 100
		"""
		param = Conversions.decimal_value_to_str(sequence_repeat)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SREPeat {param}')

	def get_spause(self) -> float:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SPAuse \n
		Snippet: value: float = driver.source.afRf.generator.dialing.scal.get_spause() \n
		Defines the duration of a pause between two repetitions of a SELCAL sequence. \n
			:return: sequence_pause: Range: 0.1 s to 10 s, Unit: s
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SPAuse?')
		return Conversions.str_to_float(response)

	def set_spause(self, sequence_pause: float) -> None:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SPAuse \n
		Snippet: driver.source.afRf.generator.dialing.scal.set_spause(sequence_pause = 1.0) \n
		Defines the duration of a pause between two repetitions of a SELCAL sequence. \n
			:param sequence_pause: Range: 0.1 s to 10 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(sequence_pause)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:SPAuse {param}')

	def get_tpause(self) -> float:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:TPAuse \n
		Snippet: value: float = driver.source.afRf.generator.dialing.scal.get_tpause() \n
		Defines the duration of the pause between the two dual tones of a SELCAL sequence. \n
			:return: tpause: Range: 0.1 s to 3 s, Unit: s
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:TPAuse?')
		return Conversions.str_to_float(response)

	def set_tpause(self, tpause: float) -> None:
		"""SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:TPAuse \n
		Snippet: driver.source.afRf.generator.dialing.scal.set_tpause(tpause = 1.0) \n
		Defines the duration of the pause between the two dual tones of a SELCAL sequence. \n
			:param tpause: Range: 0.1 s to 3 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(tpause)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:DIALing:SCAL:TPAuse {param}')

	def clone(self) -> 'ScalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
