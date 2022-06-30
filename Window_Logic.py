import Cabal_Logic as CL
from PySide2.QtCore import SIGNAL, QObject


class GUI_Logic:
    def connect_signals(self):
        QObject.connect(self.window_handle.pb_compute,
                        SIGNAL('clicked()'), self.__pb_compute_slot)

    def __init__(self, window):
        self.window_handle = window
        self.connect_signals()

    def __get_le_text(self, le):
        return le.text()

    def __get_price_in_gems(self):
        gems = self.__get_le_text(self.window_handle.le_gems)
        self.__log_msg(f'Cost in gems: {gems}')
        return int(gems)

    def __get_voucher_price(self):
        vp = self.__get_le_text(self.window_handle.le_voucher_price)
        self.__log_msg(f'Cost of voucher in alz: {vp}')
        return float(vp)

    def __set_line_edit(self, le, inText):
        le.setText(inText)

    def __set_alz_cost(self, new_text):
        self.__set_line_edit(self.window_handle.le_result, new_text)

    def __log_msg(self, msg):
        self.window_handle.tb_console.append(msg)

    def __pb_compute_slot(self):
        gems = int(self.__get_price_in_gems())
        voucher_price = float(self.__get_voucher_price())

        alz_equivalent = str(CL.gem2alz(gems, voucher_price))
        self.__log_msg(f'Gems calculated in alz: {alz_equivalent}')
        self.__set_alz_cost(alz_equivalent)
