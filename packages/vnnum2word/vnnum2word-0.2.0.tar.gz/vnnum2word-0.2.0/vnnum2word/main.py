
from __future__ import unicode_literals
from decimal import Decimal

to_19 = (u'không', u'một', u'hai', u'ba', u'bốn', u'năm', u'sáu',
         u'bảy', u'tám', u'chín', u'mười', u'mười một', u'mười hai',
         u'mười ba', u'mười bốn', u'mười lăm', u'mười sáu', u'mười bảy',
         u'mười tám', u'mười chín')
tens = (u'hai mươi', u'ba mươi', u'bốn mươi', u'năm mươi',
        u'sáu mươi', u'bảy mươi', u'tám mươi', u'chín mươi')
denom = ('',
         u'nghìn', u'triệu', u'tỷ', u'nghìn tỷ', u'trăm nghìn tỷ',
         'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion',
         'Decillion', 'Undecillion', 'Duodecillion', 'Tredecillion',
         'Quattuordecillion', 'Sexdecillion', 'Septendecillion',
         'Octodecillion', 'Novemdecillion', 'Vigintillion')


class WordConverter(object):

    def _convert_nn(self, val):
        if val < 20:
            return to_19[val]
        for (dcap, dval) in ((k, 20 + (10 * v)) for (v, k) in enumerate(tens)):
            if dval + 10 > val:
                if val % 10:
                    a = u'lăm'
                    if to_19[val % 10] == u'một':
                        a = u'mốt'
                    else:
                        a = to_19[val % 10]
                    if to_19[val % 10] == u'năm':
                        a = u'lăm'
                    return dcap + ' ' + a
                return dcap

    def _convert_nnn(self, val):
        word = ''
        (mod, rem) = (val % 100, val // 100)
        if rem > 0:
            word = to_19[rem] + u' trăm'
            if mod > 0:
                word = word + ' '
        if mod > 0 and mod < 10:
            if mod == 5:
                word = word != '' and word + u'lẻ năm' or word + u'năm'
            else:
                word = word != '' and word + u'lẻ ' \
                    + self._convert_nn(mod) or word + self._convert_nn(mod)
        if mod >= 10:
            word = word + self._convert_nn(mod)
        return word

    def vietnam_number(self, val):
        if val < 100:
            return self._convert_nn(val)
        if val < 1000:
            return self._convert_nnn(val)
        for (didx, dval) in ((v - 1, 1000 ** v) for v in range(len(denom))):
            if dval > val:
                mod = 1000 ** didx
                lval = val // mod
                r = val - (lval * mod)

                ret = self._convert_nnn(lval) + u' ' + denom[didx]
                if 99 >= r > 0:
                    ret = self._convert_nnn(lval) + u' ' + denom[didx] + u' lẻ'
                if r > 0:
                    ret = ret + ' ' + self.vietnam_number(r)
                return ret

    def __call__(self, number: int | float | Decimal):
        # Parse number into integer and fractional parts without forcing 2 decimals
        # Support int, float, or Decimal inputs only
        text = str(number)

        parts = text.split('.')

        # Integer part
        start_word = self.vietnam_number(int(parts[0]))
        final_result = start_word

        # Fractional part handling
        if len(parts) > 1:
            frac_raw = parts[1]
            # Trim trailing zeros to avoid reading them when not meaningful
            frac = frac_raw.rstrip('0')
            if frac:
                if len(frac) <= 2:
                    # Read as a 1- or 2-digit number using standard rules
                    end_word = self.vietnam_number(int(frac))
                else:
                    # Read each digit individually when more than two digits
                    digit_words = [to_19[int(ch)] for ch in frac]
                    end_word = ' '.join(digit_words)
                final_result = final_result + ' phẩy ' + end_word

        return final_result

    def to_cardinal(self, number):
        return self.__call__(number)

    def to_ordinal(self, number):
        return self.to_cardinal(number)