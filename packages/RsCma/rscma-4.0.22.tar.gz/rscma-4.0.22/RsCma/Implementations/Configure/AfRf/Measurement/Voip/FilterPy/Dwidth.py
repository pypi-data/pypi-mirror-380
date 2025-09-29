from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DwidthCls:
	"""Dwidth commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dwidth", core, parent)

	def set(self, dwidth: enums.PwrFilterType, relative: enums.Relative) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:VOIP:FILTer:DWIDth \n
		Snippet: driver.configure.afRf.measurement.voip.filterPy.dwidth.set(dwidth = enums.PwrFilterType.NARRow, relative = enums.Relative.CONStant) \n
		Configures the bandwidth of the distortion filter in the VoIP input path. \n
			:param dwidth: WIDE | NARRow | UDEF Wide, narrow or user-defined bandwidth
			:param relative: RELative | CONStant Proportional to reference frequency or constant
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dwidth', dwidth, DataType.Enum, enums.PwrFilterType), ArgSingle('relative', relative, DataType.Enum, enums.Relative))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:VOIP:FILTer:DWIDth {param}'.rstrip())

	# noinspection PyTypeChecker
	class DwidthStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Dwidth: enums.PwrFilterType: WIDE | NARRow | UDEF Wide, narrow or user-defined bandwidth
			- 2 Relative: enums.Relative: RELative | CONStant Proportional to reference frequency or constant"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Dwidth', enums.PwrFilterType),
			ArgStruct.scalar_enum('Relative', enums.Relative)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dwidth: enums.PwrFilterType = None
			self.Relative: enums.Relative = None

	def get(self) -> DwidthStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:VOIP:FILTer:DWIDth \n
		Snippet: value: DwidthStruct = driver.configure.afRf.measurement.voip.filterPy.dwidth.get() \n
		Configures the bandwidth of the distortion filter in the VoIP input path. \n
			:return: structure: for return value, see the help for DwidthStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:VOIP:FILTer:DWIDth?', self.__class__.DwidthStruct())

	def get_sfactor(self) -> float:
		"""CONFigure:AFRF:MEASurement<Instance>:VOIP:FILTer:DWIDth:SFACtor \n
		Snippet: value: float = driver.configure.afRf.measurement.voip.filterPy.dwidth.get_sfactor() \n
		Sets the distortion filter width factor for a user-defined distortion filter width. CONF:AFRF:MEAS:VOIP:FILT:DWID UDEF \n
			:return: factor: Range: 0.001 to 0.005
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:VOIP:FILTer:DWIDth:SFACtor?')
		return Conversions.str_to_float(response)

	def set_sfactor(self, factor: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:VOIP:FILTer:DWIDth:SFACtor \n
		Snippet: driver.configure.afRf.measurement.voip.filterPy.dwidth.set_sfactor(factor = 1.0) \n
		Sets the distortion filter width factor for a user-defined distortion filter width. CONF:AFRF:MEAS:VOIP:FILT:DWID UDEF \n
			:param factor: Range: 0.001 to 0.005
		"""
		param = Conversions.decimal_value_to_str(factor)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:VOIP:FILTer:DWIDth:SFACtor {param}')
