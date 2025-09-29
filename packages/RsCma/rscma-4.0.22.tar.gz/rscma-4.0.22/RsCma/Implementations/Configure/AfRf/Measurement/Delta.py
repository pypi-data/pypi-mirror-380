from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeltaCls:
	"""Delta commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delta", core, parent)

	def get_enable(self) -> bool:
		"""CONFigure:AFRF:MEASurement<Instance>:DELTa:ENABle \n
		Snippet: value: bool = driver.configure.afRf.measurement.delta.get_enable() \n
		Enables or disables delta measurements and delta measurement results. If disabled, delta measurement result views are
		hidden. For delta measurements in 'Repetition Mode' > 'SingleShot', the results for 'Standard Deviation' are marked
		'NCAP', since they refer only to one measurement value. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DELTa:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""CONFigure:AFRF:MEASurement<Instance>:DELTa:ENABle \n
		Snippet: driver.configure.afRf.measurement.delta.set_enable(enable = False) \n
		Enables or disables delta measurements and delta measurement results. If disabled, delta measurement result views are
		hidden. For delta measurements in 'Repetition Mode' > 'SingleShot', the results for 'Standard Deviation' are marked
		'NCAP', since they refer only to one measurement value. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DELTa:ENABle {param}')
