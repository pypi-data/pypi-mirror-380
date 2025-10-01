import numpy as np
from typing import Union, List, Dict

import pymodaq_plugins_holoeye  # mandatory if not imported from somewhere else to load holeye module from local install
from holoeye import slmdisplaysdk


from pymodaq.control_modules.move_utility_classes import DAQ_Move_base, comon_parameters_fun, main
from pymodaq.utils.data import DataActuator
from pymodaq_plugins_holoeye import Config as HoloConfig
from pymodaq_utils.logger import set_logger, get_module_name
from pymodaq_plugins_holoeye.resources.daq_move_HoloeyeBase import DAQ_Move_HoloeyeBase


logger = set_logger(get_module_name(__file__))
config = HoloConfig()


class DAQ_Move_HoloeyeSplitScreen(DAQ_Move_HoloeyeBase):

    shaping_type: str = 'SplitScreen'
    shaping_settings = [
        {'title': 'Splitting (%):', 'name': 'split_value', 'type': 'int', 'value': 50, 'min': 0, 'max': 100},
        {'title': 'Grey A value:', 'name': 'greyA_value', 'type': 'int', 'value': 0, 'min': 0, 'max': 255},
        {'title': 'Grey B value:', 'name': 'greyB_value', 'type': 'int', 'value': 255, 'min': 0, 'max': 255},
        {'title': 'Splitting direction:', 'name': 'split_dir', 'type': 'list',
         'limits': ['Horizontal', 'Vertical']},
        {'title': 'Flipped?:', 'name': 'split_flip', 'type': 'bool', 'value': False},]
    is_multiaxes = True
    axes_name = ['Screen spliting', 'GreyA', 'GreyB']
    _controller_units = ['', '', '']

    def move_abs(self, value: DataActuator):
        """ Move the actuator to the absolute target defined by value

        Parameters
        ----------
        value: (DataActuator) value of the absolute target positioning
        """

        if self.settings['multiaxes', 'axis'] == 'Screen spliting':  # ,'GreyA','GreyB']
            screen_divider = value
            self.settings.child('options', 'split_value').setValue(value.value())
        else:
            screen_divider = self.settings['options', 'split_value']

        if self.settings['multiaxes', 'axis'] == 'GreyA':
            a_gray_value = int(value.value())
            self.settings.child('options', 'greyA_value').setValue(a_gray_value)
        else:
            a_gray_value = self.settings['options', 'greyA_value']
        if self.settings['multiaxes', 'axis'] == 'GreyB':
            b_gray_value = int(value.value())
            self.settings.child('options', 'greyB_value').setValue(b_gray_value)
        else:
            b_gray_value = self.settings['options', 'greyB_value']

        flipped = self.settings['options', 'split_flip']

        data_array = np.ones(self.shape) * a_gray_value
        if self.settings['options', 'split_dir'] == 'Vertical':
            split_index = int(self.shape[1] * screen_divider / 100)
            data_array[:, split_index:] = b_gray_value
        else:
            split_index = int(self.shape[0] * screen_divider / 100)
            data_array[split_index:, :] = b_gray_value

        super().move_abs(DataActuator(data=data_array))

    def commit_settings(self, param):
        super().commit_settings(param)

        if self.settings['multiaxes', 'axis'] == 'Screen spliting':
            self.settings.child('bounds', 'max_bound').setValue(100)
        else:
            self.settings.child('bounds', 'max_bound').setValue(255)


if __name__ == '__main__':
    main(__file__, init=True)
