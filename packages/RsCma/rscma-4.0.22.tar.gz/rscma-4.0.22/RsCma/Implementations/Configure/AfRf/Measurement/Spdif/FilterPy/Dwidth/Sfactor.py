from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfactorCls:
	"""Sfactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfactor", core, parent)

	def set(self, factor_left: float, factor_right: float) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:SIN:FILTer:DWIDth:SFACtor \n
		Snippet: driver.configure.afRf.measurement.spdif.filterPy.dwidth.sfactor.set(factor_left = 1.0, factor_right = 1.0) \n
		Sets the distortion filter width factor for a user-defined distortion filter width. CONF:AFRF:MEAS:SIN:FILT:DWID UDEF \n
			:param factor_left: Range: 0.001 to 0.005
			:param factor_right: Range: 0.001 to 0.005
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('factor_left', factor_left, DataType.Float), ArgSingle('factor_right', factor_right, DataType.Float))
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SIN:FILTer:DWIDth:SFACtor {param}'.rstrip())

	# noinspection PyTypeChecker
	class SfactorStruct(StructBase):
		"""Response structure. Fields: \n
			- 1 Factor_Left: float: Range: 0.001 to 0.005
			- 2 Factor_Right: float: Range: 0.001 to 0.005"""
		__meta_args_list = [
			ArgStruct.scalar_float('Factor_Left'),
			ArgStruct.scalar_float('Factor_Right')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Factor_Left: float = None
			self.Factor_Right: float = None

	def get(self) -> SfactorStruct:
		"""CONFigure:AFRF:MEASurement<Instance>:SIN:FILTer:DWIDth:SFACtor \n
		Snippet: value: SfactorStruct = driver.configure.afRf.measurement.spdif.filterPy.dwidth.sfactor.get() \n
		Sets the distortion filter width factor for a user-defined distortion filter width. CONF:AFRF:MEAS:SIN:FILT:DWID UDEF \n
			:return: structure: for return value, see the help for SfactorStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:AFRF:MEASurement<Instance>:SIN:FILTer:DWIDth:SFACtor?', self.__class__.SfactorStruct())
