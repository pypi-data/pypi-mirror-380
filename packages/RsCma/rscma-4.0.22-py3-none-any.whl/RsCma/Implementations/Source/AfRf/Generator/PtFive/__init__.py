from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtFiveCls:
	"""PtFive commands group definition. 10 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptFive", core, parent)

	@property
	def cfFm(self):
		"""cfFm commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_cfFm'):
			from .CfFm import CfFmCls
			self._cfFm = CfFmCls(self._core, self._cmd_group)
		return self._cfFm

	def get_emergency(self) -> bool:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:EMERgency \n
		Snippet: value: bool = driver.source.afRf.generator.ptFive.get_emergency() \n
		Configures the emergency bit to be signaled to the DUT, for P25. \n
			:return: emergency: OFF | ON
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:PTFive:EMERgency?')
		return Conversions.str_to_bool(response)

	def set_emergency(self, emergency: bool) -> None:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:EMERgency \n
		Snippet: driver.source.afRf.generator.ptFive.set_emergency(emergency = False) \n
		Configures the emergency bit to be signaled to the DUT, for P25. \n
			:param emergency: OFF | ON
		"""
		param = Conversions.bool_to_str(emergency)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:PTFive:EMERgency {param}')

	def get_sid(self) -> str:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:SID \n
		Snippet: value: str = driver.source.afRf.generator.ptFive.get_sid() \n
		Configures the source ID to be signaled to the DUT. \n
			:return: source_id: Range: #H0 to #HFFFFFF
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:PTFive:SID?')
		return trim_str_response(response)

	def set_sid(self, source_id: str) -> None:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:SID \n
		Snippet: driver.source.afRf.generator.ptFive.set_sid(source_id = rawAbc) \n
		Configures the source ID to be signaled to the DUT. \n
			:param source_id: Range: #H0 to #HFFFFFF
		"""
		param = Conversions.value_to_str(source_id)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:PTFive:SID {param}')

	def get_tgid(self) -> str:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:TGID \n
		Snippet: value: str = driver.source.afRf.generator.ptFive.get_tgid() \n
		Configures the talk group ID to be signaled to the DUT. \n
			:return: tgroup_id: Range: #H0 to #HFFFF
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:PTFive:TGID?')
		return trim_str_response(response)

	def set_tgid(self, tgroup_id: str) -> None:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:TGID \n
		Snippet: driver.source.afRf.generator.ptFive.set_tgid(tgroup_id = rawAbc) \n
		Configures the talk group ID to be signaled to the DUT. \n
			:param tgroup_id: Range: #H0 to #HFFFF
		"""
		param = Conversions.value_to_str(tgroup_id)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:PTFive:TGID {param}')

	def get_nac(self) -> str:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:NAC \n
		Snippet: value: str = driver.source.afRf.generator.ptFive.get_nac() \n
		Configures the network access code to be signaled to the DUT. \n
			:return: nac: Range: #H0 to #HFFF
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:PTFive:NAC?')
		return trim_str_response(response)

	def set_nac(self, nac: str) -> None:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:NAC \n
		Snippet: driver.source.afRf.generator.ptFive.set_nac(nac = rawAbc) \n
		Configures the network access code to be signaled to the DUT. \n
			:param nac: Range: #H0 to #HFFF
		"""
		param = Conversions.value_to_str(nac)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:PTFive:NAC {param}')

	# noinspection PyTypeChecker
	def get_pattern(self) -> enums.P25Pattern:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:PATTern \n
		Snippet: value: enums.P25Pattern = driver.source.afRf.generator.ptFive.get_pattern() \n
		Selects the bit pattern to be transmitted as payload for P25. \n
			:return: pattern: P1011 | SILence | INTerference | BUSY | IDLE | CALibration | RSYR | RLD | C4FM | RAW1 | RA1 | RA0 | R10A | RPRB9 | RPRB15
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:PTFive:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.P25Pattern)

	def set_pattern(self, pattern: enums.P25Pattern) -> None:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:PATTern \n
		Snippet: driver.source.afRf.generator.ptFive.set_pattern(pattern = enums.P25Pattern.BUSY) \n
		Selects the bit pattern to be transmitted as payload for P25. \n
			:param pattern: P1011 | SILence | INTerference | BUSY | IDLE | CALibration | RSYR | RLD | C4FM | RAW1 | RA1 | RA0 | R10A | RPRB9 | RPRB15
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.P25Pattern)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:PTFive:PATTern {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.P25Mode:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:MODE \n
		Snippet: value: enums.P25Mode = driver.source.afRf.generator.ptFive.get_mode() \n
		Specifies the modulation type used for P25 phase 1 modulation. \n
			:return: mode: C4FM
		"""
		response = self._core.io.query_str_with_opc('SOURce:AFRF:GENerator<Instance>:PTFive:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.P25Mode)

	def set_mode(self, mode: enums.P25Mode) -> None:
		"""SOURce:AFRF:GENerator<Instance>:PTFive:MODE \n
		Snippet: driver.source.afRf.generator.ptFive.set_mode(mode = enums.P25Mode.C4FM) \n
		Specifies the modulation type used for P25 phase 1 modulation. \n
			:param mode: C4FM
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.P25Mode)
		self._core.io.write_with_opc(f'SOURce:AFRF:GENerator<Instance>:PTFive:MODE {param}')

	def clone(self) -> 'PtFiveCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PtFiveCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
