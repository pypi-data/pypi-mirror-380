from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnableCls:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, audioInput=repcap.AudioInput.Default) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:AIN<nr>:SDECay:ENABle \n
		Snippet: driver.configure.afRf.measurement.audioInput.sdecay.enable.set(enable = False, audioInput = repcap.AudioInput.Default) \n
		No command help available \n
			:param enable: No help available
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
		"""
		param = Conversions.bool_to_str(enable)
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:AIN{audioInput_cmd_val}:SDECay:ENABle {param}')

	def get(self, audioInput=repcap.AudioInput.Default) -> bool:
		"""CONFigure:AFRF:MEASurement<Instance>:AIN<nr>:SDECay:ENABle \n
		Snippet: value: bool = driver.configure.afRf.measurement.audioInput.sdecay.enable.get(audioInput = repcap.AudioInput.Default) \n
		No command help available \n
			:param audioInput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioInput')
			:return: enable: No help available"""
		audioInput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioInput, repcap.AudioInput)
		response = self._core.io.query_str(f'CONFigure:AFRF:MEASurement<Instance>:AIN{audioInput_cmd_val}:SDECay:ENABle?')
		return Conversions.str_to_bool(response)
