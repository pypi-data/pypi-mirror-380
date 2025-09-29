from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SinfoCls:
	"""Sinfo commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinfo", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- 1 Reliability: int: See 'Reliability indicator values'
			- 2 Network_Access_Code: str: Network access code in hexadecimal representation of the network identifier
			- 3 Link_Control_Format: int: Link control format of the link control word
			- 4 Mf_Id: int: Manufacture ID of the link control word
			- 5 Emergency: int: Emergency field of the link control word
			- 6 Reserved: int: Reserved field of the link control word
			- 7 Target_Id: str: Target ID in hexadecimal representation of the link control word
			- 8 Source_Id: str: Source ID in hexadecimal representation of the link control word
			- 9 Message_Indicator: int: Message indicator of the encryption sync word
			- 10 Alg_Id: int: Algorithm ID of the encryption sync word
			- 11 Key_Id: int: Key ID of the encryption sync word"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_raw_str('Network_Access_Code'),
			ArgStruct.scalar_int('Link_Control_Format'),
			ArgStruct.scalar_int('Mf_Id'),
			ArgStruct.scalar_int('Emergency'),
			ArgStruct.scalar_int('Reserved'),
			ArgStruct.scalar_raw_str('Target_Id'),
			ArgStruct.scalar_raw_str('Source_Id'),
			ArgStruct.scalar_int('Message_Indicator'),
			ArgStruct.scalar_int('Alg_Id'),
			ArgStruct.scalar_int('Key_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Network_Access_Code: str = None
			self.Link_Control_Format: int = None
			self.Mf_Id: int = None
			self.Emergency: int = None
			self.Reserved: int = None
			self.Target_Id: str = None
			self.Source_Id: str = None
			self.Message_Indicator: int = None
			self.Alg_Id: int = None
			self.Key_Id: int = None

	def fetch(self) -> ResultData:
		"""FETCh:AFRF:MEASurement<Instance>:DIGital:PTFive:SINFo \n
		Snippet: value: ResultData = driver.afRf.measurement.digital.ptFive.sinfo.fetch() \n
		Queries signal information parameters for the P25 standard. Signal information includes the network identifier, the link
		control word and the encryption sync word. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:DIGital:PTFive:SINFo?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:AFRF:MEASurement<Instance>:DIGital:PTFive:SINFo \n
		Snippet: value: ResultData = driver.afRf.measurement.digital.ptFive.sinfo.read() \n
		Queries signal information parameters for the P25 standard. Signal information includes the network identifier, the link
		control word and the encryption sync word. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:AFRF:MEASurement<Instance>:DIGital:PTFive:SINFo?', self.__class__.ResultData())
