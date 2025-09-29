from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NxdnCls:
	"""Nxdn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nxdn", core, parent)

	# noinspection PyTypeChecker
	def get_transmission(self) -> enums.Transmission:
		"""CONFigure:GPRF:MEASurement<Instance>:ACP:NXDN:TRANsmission \n
		Snippet: value: enums.Transmission = driver.configure.gprfMeasurement.acp.nxdn.get_transmission() \n
		Queries the data rate in bits/s for enhanced full rate (EFR) or enhanced half rate (EHR) . \n
			:return: transmission: EHR4800 | EHR9600 | EFR9600
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:ACP:NXDN:TRANsmission?')
		return Conversions.str_to_scalar_enum(response, enums.Transmission)

	def set_transmission(self, transmission: enums.Transmission) -> None:
		"""CONFigure:GPRF:MEASurement<Instance>:ACP:NXDN:TRANsmission \n
		Snippet: driver.configure.gprfMeasurement.acp.nxdn.set_transmission(transmission = enums.Transmission.EFR9600) \n
		Queries the data rate in bits/s for enhanced full rate (EFR) or enhanced half rate (EHR) . \n
			:param transmission: EHR4800 | EHR9600 | EFR9600
		"""
		param = Conversions.enum_scalar_to_str(transmission, enums.Transmission)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:ACP:NXDN:TRANsmission {param}')
