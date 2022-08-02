import Cabal_Logic as CL
from PySide2.QtCore import SIGNAL, QObject


class GUI_Logic:
    def connect_signals(self):
        QObject.connect(self.window_handle.pb_compute,
                        SIGNAL('clicked()'), self.__pb_compute_gems_slot)
        QObject.connect(self.window_handle.pb_compute_cc,
                        SIGNAL('clicked()'), self.__pb_compute_cc_slot)
        QObject.connect(self.window_handle.pb_compute_rse,
                        SIGNAL('clicked()'), self.__pb_compute_rse_slot)

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

    def __pb_compute_gems_slot(self):
        gems = self.__get_price_in_gems()
        voucher_price = self.__get_voucher_price()

        alz_equivalent = str(CL.gem2alz(gems, voucher_price))
        self.__log_msg(f'Gems calculated in alz: {alz_equivalent}')
        self.__set_alz_cost(alz_equivalent)

    def __get_price_in_cc(self):
        cc = self.__get_le_text(self.window_handle.le_cc)
        self.__log_msg_cc(f'Cost in CC: {cc}')
        return int(cc)

    def __get_voucher_price_cc(self):
        vp = self.__get_le_text(self.window_handle.le_vp)
        self.__log_msg_cc(f'Cost of voucher in alz: {vp}')
        return float(vp)

    def __log_msg_cc(self, msg):
        self.window_handle.tb_console_cc.append(msg)

    def __set_alz_cost_cc(self, new_text):
        self.__set_line_edit(self.window_handle.le_ro_cc2alz_res, new_text)

    def __pb_compute_cc_slot(self):
        cc = self.__get_price_in_cc()
        vp = self.__get_voucher_price_cc()

        alz_equivalent = str(CL.cc2alz(cc, vp))
        self.__log_msg_cc(f'CC calculated in alz: {alz_equivalent}')
        self.__set_alz_cost_cc(alz_equivalent)

    def __log_msg_rse(self, msg):
        self.window_handle.tb_log_console.append(msg)

    def __get_ice_orb_price(self):
        ice_price = self.__get_le_text(self.window_handle.le_ice)
        self.__log_msg_rse(f'Orb of Ice price {ice_price}')
        return float(ice_price)

    def __get_earth_orb_price(self):
        earth_price = self.__get_le_text(self.window_handle.le_earth)
        self.__log_msg_rse(f'Orb of Earth price {earth_price}')
        return float(earth_price)

    def __get_fire_orb_price(self):
        fire_price = self.__get_le_text(self.window_handle.le_fire)
        self.__log_msg_rse(f'Orb of fire price {fire_price}')
        return float(fire_price)

    def __get_wind_orb_price(self):
        wind_price = self.__get_le_text(self.window_handle.le_wind)
        self.__log_msg_rse(f'Orb of Wind price {wind_price}')
        return float(wind_price)

    def __set_rse_price(self, rse_price):
        self.__log_msg_rse(f'Rune Slot Extender craft price: {rse_price}')
        self.__set_line_edit(self.window_handle.le_ro_craft_price, rse_price)

    def __pb_compute_rse_slot(self):
        l_prices = []
        l_prices.append(self.__get_ice_orb_price())
        l_prices.append(self.__get_earth_orb_price())
        l_prices.append(self.__get_fire_orb_price())
        l_prices.append(self.__get_wind_orb_price())

        orbs_needed = 10
        rse_price = str(CL.RSE_craft_price(l_prices, orbs_needed))
        self.__set_rse_price(rse_price)
