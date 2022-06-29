import Cabal_Logic as CL
from PySide2.QtCore import SIGNAL, QObject


class GUI_Logic:
    def connect_signals(self):
        QObject.connect(self.window_handle.pb_compute,
                        SIGNAL ('clicked()'), self.__pb_compute_slot)


    def __init__(self, window):
        self.window_handle = window
        self.connect_signals()


    def __get_price_in_gems(self):
        return self.window_handle.le_gems.text()


    def __get_voucher_price(self):
        return self.window_handle.le_voucher_price.text()


    def __set_alz_cost(self, new_text):
        self.window_handle.le_result.setText(new_text)


    def __pb_compute_slot(self):
        gems = int(self.__get_price_in_gems())
        voucher_price = float(self.__get_voucher_price())

        alz_equivalent = str(CL.gem2alz(gems, voucher_price))

        self.__set_alz_cost(alz_equivalent)
