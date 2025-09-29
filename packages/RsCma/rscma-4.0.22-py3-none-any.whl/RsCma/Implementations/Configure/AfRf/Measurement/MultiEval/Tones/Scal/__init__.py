from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScalCls:
	"""Scal commands group definition. 5 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scal", core, parent)

	@property
	def userDefined(self):
		"""userDefined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_userDefined'):
			from .UserDefined import UserDefinedCls
			self._userDefined = UserDefinedCls(self._core, self._cmd_group)
		return self._userDefined

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	# noinspection PyTypeChecker
	def get_standard(self) -> enums.SelCalStandard:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:SCAL:STANdard \n
		Snippet: value: enums.SelCalStandard = driver.configure.afRf.measurement.multiEval.tones.scal.get_standard() \n
		Selects the SELCAL standard. Selecting the standard also determines the dual-tone frequencies that the CMA expects during
		a SELCAL measurement. \n
			:return: standard: SCAL16 | SCAL32 | UDEFind SCAL16 SELCAL16 standard and corresponding frequencies SCAL32 SELCAL32 standard and corresponding frequencies UDEFinde User-defined dual-tone frequencies
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:SCAL:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.SelCalStandard)

	def set_standard(self, standard: enums.SelCalStandard) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:SCAL:STANdard \n
		Snippet: driver.configure.afRf.measurement.multiEval.tones.scal.set_standard(standard = enums.SelCalStandard.SCAL16) \n
		Selects the SELCAL standard. Selecting the standard also determines the dual-tone frequencies that the CMA expects during
		a SELCAL measurement. \n
			:param standard: SCAL16 | SCAL32 | UDEFind SCAL16 SELCAL16 standard and corresponding frequencies SCAL32 SELCAL32 standard and corresponding frequencies UDEFinde User-defined dual-tone frequencies
		"""
		param = Conversions.enum_scalar_to_str(standard, enums.SelCalStandard)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:SCAL:STANdard {param}')

	def get_cfgenerator(self) -> bool:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:SCAL:CFGenerator \n
		Snippet: value: bool = driver.configure.afRf.measurement.multiEval.tones.scal.get_cfgenerator() \n
		Couples the SELCAL tone settings of the analyzer to the corresponding generator settings. \n
			:return: conf_from_gen: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:SCAL:CFGenerator?')
		return Conversions.str_to_bool(response)

	def set_cfgenerator(self, conf_from_gen: bool) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:SCAL:CFGenerator \n
		Snippet: driver.configure.afRf.measurement.multiEval.tones.scal.set_cfgenerator(conf_from_gen = False) \n
		Couples the SELCAL tone settings of the analyzer to the corresponding generator settings. \n
			:param conf_from_gen: OFF | ON
		"""
		param = Conversions.bool_to_str(conf_from_gen)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:MEValuation:TONes:SCAL:CFGenerator {param}')

	def clone(self) -> 'ScalCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ScalCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
