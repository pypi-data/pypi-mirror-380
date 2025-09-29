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
			- 2 Color_Code: int: Color code as part of the PDU content
			- 3 Source_Address: int: Source address as part of the PDU content
			- 4 Target_Address: int: Target address as part of the PDU content
			- 5 Pi: int: No parameter help available
			- 6 Pflag: int: Protect flag as part of the PDU content
			- 7 Flco: int: No parameter help available
			- 8 Fid: int: Feature set ID as part of the PDU content
			- 9 Data_Type: int: Data type as part of the PDU content
			- 10 Broadcast: int: Broadcast operation as part of the service options
			- 11 Privacy: int: Privacy operation as part of the service options
			- 12 Pl: int: Priority level as part of the service options
			- 13 Emergency: int: Emergency operation as part of the service options
			- 14 Ovcm: int: Open voice call mode as part of the service options Range: 0 to 15"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Color_Code'),
			ArgStruct.scalar_int('Source_Address'),
			ArgStruct.scalar_int('Target_Address'),
			ArgStruct.scalar_int('Pi'),
			ArgStruct.scalar_int('Pflag'),
			ArgStruct.scalar_int('Flco'),
			ArgStruct.scalar_int('Fid'),
			ArgStruct.scalar_int('Data_Type'),
			ArgStruct.scalar_int('Broadcast'),
			ArgStruct.scalar_int('Privacy'),
			ArgStruct.scalar_int('Pl'),
			ArgStruct.scalar_int('Emergency'),
			ArgStruct.scalar_int('Ovcm')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Color_Code: int = None
			self.Source_Address: int = None
			self.Target_Address: int = None
			self.Pi: int = None
			self.Pflag: int = None
			self.Flco: int = None
			self.Fid: int = None
			self.Data_Type: int = None
			self.Broadcast: int = None
			self.Privacy: int = None
			self.Pl: int = None
			self.Emergency: int = None
			self.Ovcm: int = None

	def fetch(self) -> ResultData:
		"""FETCh:AFRF:MEASurement<Instance>:DIGital:DMR:SINFo \n
		Snippet: value: ResultData = driver.afRf.measurement.digital.dmr.sinfo.fetch() \n
		Queries signal information parameters for the DMR standard. SIgnal information includes the PDU content and service
		options. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:AFRF:MEASurement<Instance>:DIGital:DMR:SINFo?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""READ:AFRF:MEASurement<Instance>:DIGital:DMR:SINFo \n
		Snippet: value: ResultData = driver.afRf.measurement.digital.dmr.sinfo.read() \n
		Queries signal information parameters for the DMR standard. SIgnal information includes the PDU content and service
		options. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:AFRF:MEASurement<Instance>:DIGital:DMR:SINFo?', self.__class__.ResultData())
