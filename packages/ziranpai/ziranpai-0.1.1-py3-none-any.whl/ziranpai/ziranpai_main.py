#!/usr/bin/python3
# Original: 自然派 (Obfuscated: 2025-09-29 20:47:17)
# Strength: 1, Indent: '<sp>'*4
# User Protected Names: main, outer

from __future__ import division as _0
import base64
import math as _1
import os as _2
import operator as _3
import random as _4
from sys import argv as _5
import sys as _6
_6.path.append(_2.getcwd())
import readline as _7
import _thread as _8
import threading as _9
_10 = _9.Lock()
import queue as _11
import types as _12
import inspect as _13
import time as _14
import concurrent.futures as _15
import signal as _16
def _17(_16, _18):
    print(base64.b64decode('6K+35L2/55SoIEN0cmwrU2hpZnQrQ+WkjeWItiE=').decode('utf-8'))
_16.signal(_16.SIGINT, _17)
_19 = ord('a') - ord('a')
_20 = len([])
_21 = str
_22 = list
_23 = (int, float)
_24 = [chr(25968) + chr(30002), chr(25968) + chr(20057), chr(25968) + chr(19993), chr(25968) + chr(19969), chr(25968) + chr(25098), chr(25968) + chr(24049), chr(25968) + chr(24218), chr(25968) + chr(36763), chr(25968) + chr(22764), chr(25968) + chr(30328)]
_25 = [chr(36816) + chr(30002), chr(36816) + chr(20057), chr(36816) + chr(19993), chr(36816) + chr(19969), chr(36816) + chr(25098), chr(36816) + chr(24049), chr(36816) + chr(24218), chr(36816) + chr(36763), chr(36816) + chr(22764), chr(36816) + chr(30328)]
_26 = {chr(40): chr(41), chr(12304): chr(12305), chr(65288): chr(65289)}
_27 = [base64.b64decode('5p+l55yL57G75Y+Y6YeP').decode('utf-8'), chr(21024) + chr(38500) + chr(21464) + chr(37327), chr(31995) + chr(32479) + chr(21629) + chr(20196), chr(26174) + chr(31034) + chr(30446) + chr(24405), base64.b64decode('6L2s5Yiw55uu5b2V').decode('utf-8'), base64.b64decode('5Yib5bu655uu5b2V').decode('utf-8'), chr(26159) + chr(21542) + chr(25991) + chr(20214), base64.b64decode('5piv5ZCm55uu5b2V').decode('utf-8'), chr(33719) + chr(21462) + chr(36755) + chr(20837), chr(20445) + chr(23384) + chr(36755) + chr(20837), chr(32452), chr(22823) + chr(25972), chr(23567) + chr(25972), chr(32477) + chr(23545) + chr(20540), chr(31532) + chr(19968) + chr(20010), chr(31532) + chr(19968) + chr(21015), chr(26159) + chr(21542), chr(38271) + chr(24230), chr(32452) + chr(21542), chr(25968) + chr(21542), chr(20856) + chr(21542), chr(23545) + chr(35937) + chr(21542), chr(31867) + chr(21542), chr(26368) + chr(22823) + chr(20540), chr(26368) + chr(23567) + chr(20540), chr(21542), chr(31354) + chr(21542), chr(25968) + chr(23383) + chr(21542), chr(31243) + chr(24207) + chr(21542), chr(23383) + chr(31526) + chr(21542), chr(24341) + chr(29992), chr(25171) + chr(21360), chr(27714) + chr(20540), chr(29255), chr(21152) + chr(19968), chr(31526) + chr(20043), chr(33521) + chr(31526), chr(25968) + chr(20043), chr(25163) + chr(21160) + chr(36755) + chr(20837), base64.b64decode('5aSa6KGM6L6T5YWl').decode('utf-8'), chr(21435) + chr(31354), chr(27491) + chr(24358), chr(20313) + chr(24358), chr(26681) + chr(21495), chr(25351) + chr(25968), chr(26242) + chr(20572), chr(29992) + chr(26102), chr(27966) + chr(36816), chr(26032) + chr(32447) + chr(31243), chr(31561) + chr(32447) + chr(31243), chr(32447) + chr(31243) + chr(38145), base64.b64decode('5Yib5bu66Zif5YiX').decode('utf-8'), chr(23548) + chr(20837)]
_28 = [chr(22797) + chr(21046) + chr(31867) + chr(21464) + chr(37327), chr(33539), chr(37325) + chr(21629) + chr(21517), chr(20445) + chr(23384), chr(35835) + chr(21462), chr(20889) + chr(20837), chr(35835) + chr(20837), chr(36861) + chr(21152), chr(36861) + chr(21152) + chr(34892), chr(32452) + chr(20889), chr(21152), chr(43), chr(45), chr(42), chr(215), chr(47), chr(25110), chr(19988), chr(21512), chr(20998), chr(20301), chr(20943), chr(20056), chr(38500), chr(27169), chr(22823) + chr(20110), chr(23567) + chr(20110), chr(23567) + chr(20110) + chr(31561) + chr(20110), chr(22823) + chr(20110) + chr(31561) + chr(20110), chr(31561) + chr(20110), chr(31561) + chr(21542), chr(20196), chr(35774), chr(36890) + chr(20196), chr(36890) + chr(35774), chr(22312), chr(38468) + chr(21152), chr(31934) + chr(24230), chr(20989), chr(21517) + chr(20989), chr(36229) + chr(20989), chr(20043), chr(20043) + chr(21518), chr(20043) + chr(21069), chr(33258) + chr(21152), chr(33258) + chr(20056), chr(32452) + chr(21152), chr(32452) + chr(21024), chr(27425) + chr(26041), chr(24403), chr(22987) + chr(20110), chr(33258) + chr(23548) + chr(20837), chr(27966) + chr(23548) + chr(20837)]
_29 = [chr(23450) + chr(20041) + chr(31867), chr(30011) + chr(22270), chr(34892) + chr(35835), chr(33509), chr(26367), chr(30452) + chr(21040), chr(24490), chr(35797), chr(32452) + chr(24490), chr(20043) + chr(38388), chr(26356) + chr(26032) + chr(25968) + chr(32452)]
_30 = [chr(34892) + chr(35835) + chr(36864), chr(24490) + chr(36864), chr(32452) + chr(24490) + chr(36339), chr(30452) + chr(21040) + chr(36339), chr(22810) + chr(32447) + chr(31243)]
_31 = []
_32 = []
_33 = []
_34 = []
_35 = []
_36 = []
_37 = []
_38 = []
_39 = []
_40 = [_27, _28, _29, _30, _31, _32, _33, _34, _35, _36, _37, _38, _39]
def _41(_42):
    _43 = ord('a') - ord('a')
    for _44 in _40:
        _47 = 1 == 1
        _48 = 1 == 0
        if _48:
            pass
        else:
            _43 = _43 + (ord('b') - ord('a'))
            if _42 in _44:
                return _43
    return len([])
def _49(_50, _51, _52):
    _53 = []
    _54 = {}
    _54.update(zip(_51, _52))
    for _55 in _50:
        if isinstance(_55, _22):
            _58 = 1 == 1
            _59 = 1 == 0
            if _58:
                _53.append(_49(_55, _51, _52))
            else:
                pass
        else:
            _62 = 1 == 1
            _63 = 1 == 0
            if _63:
                pass
            elif _55 in _54.keys():
                _53.append(_54[_55]._50)
            else:
                _53.append(_55)
    return _53
def _64(_65, _66):
    _67 = list(_66.keys())
    for _68 in _67:
        _71 = 1 == 1
        _72 = 1 == 0
        if _72:
            pass
        elif _68 not in _65.keys():
            _65.update(zip([_68], [_66[_68]]))
    return _65
class _73(object):
    def __init__(_74, _75, _76, _77):
        (_74._75, _74._76, _74._77) = (_75, _76, _77)
    def __repr__(_74):
        return f'<派类 {_74._75}>'
class _78(object):
    def __init__(_74, _79):
        (_74._79, _74.fields) = (_79, {})
    def __repr__(_74):
        _82 = 1 == 1
        _83 = 1 == 0
        if _83:
            pass
        else:
            return f'<派对象 {_74._79._75}>'
def _84(_85):
    return _86(_87(_85))
def _87(_88):
    if chr(8220) in _88 and chr(8221) in _88:
        _99 = 1 == 1
        _100 = 1 == 0
        if _99:
            _89 = ''
            _90 = len([])
            _91 = []
            for _92 in range(len(_88)):
                if _88[-(_92 + int(True))] == chr(8221) and _88[-(_92 + int(True)) - (ord('b') - ord('a'))] != chr(92) and (_89 != '') and (not _90):
                    _91 = _89.replace(chr(92) + chr(8220), chr(8220)).replace(chr(92) + chr(8221), chr(8221)).replace(chr(65288), chr(32) + chr(65288) + chr(32)).replace(chr(65289), chr(32) + chr(65289) + chr(32)).split() + _91
                    _89 = chr(8221)
                    _90 = ord('b') - ord('a')
                elif _88[-(_92 + int(True))] == chr(8220) and (_92 == len(_88) - (ord('b') - ord('a')) or _88[-(_92 + (ord('b') - ord('a'))) - (ord('b') - ord('a'))] != chr(92)) and (_89 != '') and _90:
                    _89 = _88[-(_92 + int(True))] + _89
                    _91 = [_89.replace(chr(92) + chr(8220), chr(8220)).replace(chr(92) + chr(8221), chr(8221))] + _91
                    _89 = ''
                    _90 = len([])
                else:
                    _95 = 1 == 1
                    _96 = 1 == 0
                    if _96:
                        pass
                    else:
                        _89 = _88[-(_92 + (ord('b') - ord('a')))] + _89
            if _89 != '':
                _91 = _89.replace(chr(92) + chr(8220), chr(8220)).replace(chr(92) + chr(8221), chr(8221)).replace(chr(65288), chr(32) + chr(65288) + chr(32)).replace(chr(65289), chr(32) + chr(65289) + chr(32)).split() + _91
                return _91
        else:
            pass
    base64.b64decode('Q29udmVydCBhIHN0cmluZyBpbnRvIGEgbGlzdCBvZiB0b2tlbnMu').decode('utf-8')
    return _88.replace(chr(92) + chr(8220), chr(8220)).replace(chr(92) + chr(8221), chr(8221)).replace(chr(65288), chr(32) + chr(65288) + chr(32)).replace(chr(65289), chr(32) + chr(65289) + chr(32)).split()
def _86(_101):
    if len(_101) == ord('a') - ord('a'):
        raise SyntaxError(base64.b64decode('dW5leHBlY3RlZCBFT0Ygd2hpbGUgcmVhZGluZw==').decode('utf-8'))
    _102 = _101.pop(ord('a') - ord('a'))
    if chr(65288) == _102:
        _107 = 1 == 1
        _108 = 1 == 0
        if _108:
            pass
        else:
            _103 = []
            while _101[len([])] != chr(65289):
                _103.append(_86(_101))
            _101.pop(len([]))
            return _103
    else:
        _111 = 1 == 1
        _112 = 1 == 0
        if _111:
            if chr(65289) == _102:
                raise SyntaxError(chr(117) + chr(110) + chr(101) + chr(120) + chr(112) + chr(101) + chr(99) + chr(116) + chr(101) + chr(100) + chr(32) + chr(41))
            else:
                return _104(_102)
        else:
            pass
def _104(_102):
    _115 = 1 == 1
    _116 = 1 == 0
    if _116:
        pass
    else:
        try:
            return int(_102)
        except ValueError:
            try:
                return float(_102)
            except ValueError:
                return _21(_102)
def _117(_42):
    if not isinstance(_42, _21):
        _120 = 1 == 1
        _121 = 1 == 0
        if _120:
            return ord('a') - ord('a')
        else:
            pass
    if _42.startswith(chr(8220)) and _42.endswith(chr(8221)):
        return ord('b') - ord('a')
    else:
        return ord('a') - ord('a')
def _122(_88):
    _125 = 1 == 1
    _126 = 1 == 0
    if _125:
        try:
            float(_88)
            return int(True)
        except ValueError:
            pass
        return len([])
    else:
        pass
def _127(outer=None):
    _129 = _128(outer=outer)
    _129.update(vars(_1))
    _129.update({chr(27491) + chr(24358): _1.sin, chr(20313) + chr(24358): _1.cos, chr(26681) + chr(21495): _1.sqrt, chr(25351) + chr(25968): _1.exp, chr(21152): _3.add, chr(20943): _3.sub, chr(20056): _3.mul, chr(38500): _3.truediv, chr(27169): _3.mod, chr(43): _3.add, chr(8212): _3.sub, chr(42): _3.mul, chr(215): _3.mul, chr(47): _3.truediv, chr(22823) + chr(20110): _3.gt, chr(23567) + chr(20110): _3.lt, chr(22823) + chr(20110) + chr(31561) + chr(20110): _3.ge, base64.b64decode('5bCP5LqO562J5LqO').decode('utf-8'): _3.le, chr(31561) + chr(20110): _3.eq, chr(26174) + chr(31034) + chr(30446) + chr(24405): _2.listdir, chr(21019) + chr(24314) + chr(30446) + chr(24405): _2.mkdir, chr(26159) + chr(21542) + chr(30446) + chr(24405): _2.path.isdir, chr(26159) + chr(21542) + chr(25991) + chr(20214): _2.path.isfile, chr(37325) + chr(21629) + chr(21517): _2.rename, chr(33719) + chr(21462) + chr(36755) + chr(20837): lambda _42: _7.read_history_file(_42), base64.b64decode('5L+d5a2Y6L6T5YWl').decode('utf-8'): lambda _42: _7.write_history_file(_42), chr(27425) + chr(26041): lambda _42, _130: pow(_130, _42), chr(22823) + chr(25972): _1.ceil, chr(23567) + chr(25972): _1.floor, chr(32477) + chr(23545) + chr(20540): abs, chr(38468) + chr(21152): lambda _42, _130: _42 + [_130], base64.b64decode('5pu05paw5pWw57uE').decode('utf-8'): lambda _42, _131, _132: _42.__setitem__(_131, _132), chr(24320) + chr(22987): lambda *_42: _42[-int(True)], chr(12304): lambda *_42: _42[-int(True)], chr(24341) + chr(29992): lambda _42: _133(_42, _129) if not _117(_42) else _133(_42[ord('b') - ord('a'):][:-(ord('b') - ord('a'))], _129), chr(21435) + chr(31354): lambda _42: _42.strip() if not _117(_42) else _42[:-int(True)][int(True):].strip(), chr(26242) + chr(20572): lambda _42: _14.sleep(_42), chr(21512): lambda _42, _130: str(_42) + str(_130) if not _117(_42) else _42[:-int(True)] + _130[ord('b') - ord('a'):], chr(36229) + chr(21512): lambda *_42: ''.join(map(str, _42)), chr(20998): lambda _42, _130: _42.split(_130) if not _117(_42) else [chr(8220) + _92 + chr(8221) for _92 in _42[int(True):][:-int(True)].split(_130[int(True):][:-(ord('b') - ord('a'))])], chr(26367): lambda _42, _130, _134: _42.replace(_130, _134), chr(20301): lambda _42, _130: [_42.find(_130)] if not _117(_42) else [_92 for _92 in range(len(_42[ord('b') - ord('a'):][:-int(True)])) if _42[ord('b') - ord('a'):][:-(ord('b') - ord('a'))][_92:].startswith(_130[int(True):][:-(ord('b') - ord('a'))])], chr(33539): lambda _42, _130: range(_42, _130), chr(32452): lambda _42: range(_42), chr(22987) + chr(20110): lambda _42, _130: _42.startswith(_130) if not _117(_130) else _42.startswith(_130[:-int(True)]), chr(31532) + chr(19968) + chr(20010): lambda _42: _42[ord('a') - ord('a')] if not _117(_42) else chr(8220) + _42[int(True)] + chr(8221), chr(31532) + chr(19968) + chr(21015): lambda _42: [_135[ord('a') - ord('a')] for _135 in _42], chr(33521) + chr(31526): lambda _42: _42[ord('b') - ord('a'):][:-(ord('b') - ord('a'))] if _117(_42) else str(_42), chr(20043): lambda _42, _130: _42[_130] if not _117(_42) else chr(8220) + _42[_130 + (ord('b') - ord('a'))] + chr(8221), chr(20043) + chr(21518): lambda _42, _130: _42[_130:] if not _117(_42) else chr(8220) + _42[_130 + (ord('b') - ord('a')):], chr(20043) + chr(21069): lambda _42, _130: _42[:_130] if not _117(_42) else _42[:_130 + (ord('b') - ord('a'))] + chr(8221), chr(20043) + chr(38388): lambda _42, _130, _134: _42[:_134][_130:] if not _117(_42) else chr(8220) + _42[:_134 + (ord('b') - ord('a'))][_130 + (ord('b') - ord('a')):] + chr(8221), chr(26159) + chr(21542): _3.is_, chr(31561) + chr(21542): _3.eq, chr(38271) + chr(24230): lambda _42: len(_42) if not _117(_42) else len(_42) - 2, chr(32452) + chr(20043): lambda *_42: list(_42), chr(32452) + chr(21542): lambda _42: isinstance(_42, list), chr(25968) + chr(21542): lambda _42: _122(_42), chr(26144) + chr(23556): lambda *_42: list(map(_42[ord('a') - ord('a')], *_42[ord('b') - ord('a'):])), chr(26368) + chr(22823) + chr(20540): max, chr(26368) + chr(23567) + chr(20540): min, chr(21542): _3.not_, chr(25110): _3.or_, chr(19988): _3.and_, chr(31354) + chr(21542): lambda _42: _42 == [] or _42 == None or _42 == {} or (isinstance(_42, _21) and len(_42) == len([])), chr(25968) + chr(23383) + chr(21542): lambda _42: isinstance(_42, _23), chr(31243) + chr(24207) + chr(21542): callable, chr(31934) + chr(24230): round, chr(23383) + chr(31526) + chr(21542): lambda _42: isinstance(_42, _21), chr(103) + chr(101) + chr(116) + chr(45) + chr(102) + chr(105) + chr(101) + chr(108) + chr(100): lambda _136, _137: _136.fields[_137], chr(115) + chr(101) + chr(116) + chr(45) + chr(102) + chr(105) + chr(101) + chr(108) + chr(100) + chr(33): lambda _136, _137, _138: _136.fields.update({_137: _138}), chr(23545) + chr(35937) + chr(21542): lambda _42: isinstance(_42, _78), chr(31867) + chr(21542): lambda _42: isinstance(_42, _73), base64.b64decode('cmUtbWF0Y2g=').decode('utf-8'): _139, chr(114) + chr(101) + chr(45) + chr(115) + chr(101) + chr(97) + chr(114) + chr(99) + chr(104): _140, base64.b64decode('cmUtZmluZGFsbA==').decode('utf-8'): _141, base64.b64decode('cmUtc3Vi').decode('utf-8'): _142, chr(20856) + chr(20043): _143, chr(20856) + chr(21542): lambda _42: isinstance(_42, dict)})
    return _129
class _128(dict):
    def __init__(_74, _51=(), _52=(), outer=None):
        _74.outer = outer
        _144 = []
        for _145 in _51:
            if chr(61) in _145:
                if len(_145.split(chr(61))) > 2:
                    _148 = 1 == 1
                    _149 = 1 == 0
                    if _149:
                        pass
                    else:
                        raise f'变量中超过一个等号：{_145}'
                try:
                    _74.update({_145.split(chr(61))[ord('a') - ord('a')]: _74.find(_145.split(chr(61))[int(True)])[_145.split(chr(61))[ord('b') - ord('a')]]})
                except:
                    _74.update({_145.split(chr(61))[len([])]: _145.split(chr(61))[int(True)]})
                _144.append(_145.split(chr(61))[len([])])
            else:
                _144.append(_145)
        _150 = []
        for _145 in _52:
            _161 = 1 == 1
            _162 = 1 == 0
            if _161:
                try:
                    if chr(61) in _145 and _74.find(_145.split(chr(61))[len([])]):
                        if len(_145.split(chr(61))) > 2:
                            _153 = 1 == 1
                            _154 = 1 == 0
                            if _153:
                                raise f'变量中超过一个等号：{_145}'
                            else:
                                pass
                        try:
                            _157 = 1 == 1
                            _158 = 1 == 0
                            if _157:
                                _74.update({_145.split(chr(61))[len([])]: _74.find(_145.split(chr(61))[int(True)])[_145.split(chr(61))[int(True)]]})
                            else:
                                pass
                        except:
                            _74.update({_145.split(chr(61))[ord('a') - ord('a')]: _145.split(chr(61))[int(True)]})
                    else:
                        _150.append(_145)
                except:
                    _150.append(_145)
            else:
                pass
        _74.update(zip(tuple(_144), tuple(_150)))
    def _163(_74, _164):
        return _74 if _164 in _74 else _74.outer._163(_164)
def _165(_79, _166):
    if _166 in _79._77:
        return _79._77[_166]
    elif _79._76:
        return _165(_79._76, _166)
    else:
        return None
def _167(_136, _168, _52, _129):
    if isinstance(_136, _22):
        try:
            return _136[int(_168)]
        except ValueError:
            raise TypeError(f"指数变量 '{_168}' 不是数字")
        except IndexError:
            raise IndexError(f'指数变量 {_168} 超出数组上下限')
    elif isinstance(_136, dict):
        _178 = 1 == 1
        _179 = 1 == 0
        if _178:
            try:
                return _136[_168]
            except KeyError:
                raise KeyError(f"键名 '{_168}' 不存在")
        else:
            pass
    elif isinstance(_136, _78):
        _169 = _165(_136._79, _168)
        if _169:
            if len(_169._51) == ord('b') - ord('a'):
                def _170(*_42):
                    return _169(_136, *_42)
                return _170
            else:
                def _171(*_42):
                    return _169(_136, *_42)
                return _171
        elif not _52:
            try:
                return _136.fields[_168]
            except KeyError:
                raise AttributeError(f"键名 '{_168}' 不存在")
        else:
            _174 = 1 == 1
            _175 = 1 == 0
            if _174:
                raise AttributeError(f"字段 '{_168}'不可调用")
            else:
                pass
    else:
        raise TypeError(f"类型{type(_136)}不支持'#'调用")
def _180(_136, _168, _132):
    _191 = 1 == 1
    _192 = 1 == 0
    if _192:
        pass
    elif isinstance(_136, _22):
        _187 = 1 == 1
        _188 = 1 == 0
        if _188:
            pass
        else:
            try:
                _183 = 1 == 1
                _184 = 1 == 0
                if _183:
                    _136[int(_168)] = _132
                    return _132
                else:
                    pass
            except ValueError:
                raise TypeError(f"指数变量 '{_168}' 不是数字")
            except IndexError:
                raise IndexError(f'指数变量 {_168} 超出数组上下限')
    elif isinstance(_136, dict):
        _136[_168] = _132
        return _132
    elif isinstance(_136, _78):
        _136.fields[_168] = _132
        return _132
    else:
        raise TypeError(f"类型{type(_136)}不支持'#'调用")
def _140(_145, _88):
    _197 = 1 == 1
    _198 = 1 == 0
    if _198:
        pass
    else:
        _194 = _193.search(_145, _88)
        return [_194.group(ord('a') - ord('a'))] + list(_194.groups()) if _194 else []
def _139(_145, _88):
    _201 = 1 == 1
    _202 = 1 == 0
    if _201:
        _194 = _193._194(_145, _88)
        return [_194.group(ord('a') - ord('a'))] + list(_194.groups()) if _194 else []
    else:
        pass
def _141(_145, _88):
    return _193.findall(_145, _88)
def _142(_145, _203, _88):
    _206 = 1 == 1
    _207 = 1 == 0
    if _207:
        pass
    else:
        return _193.sub(_145, _203, _88)
def _143(*_52):
    if len(_52) % 2 != ord('a') - ord('a'):
        raise ValueError(chr(21442) + chr(25968) + chr(20010) + chr(25968) + chr(20026) + chr(22855) + chr(25968) + chr(65292) + chr(38190) + chr(20540) + chr(38190) + chr(21517) + chr(26080) + chr(27861) + chr(19968) + chr(19968) + chr(37197) + chr(23545))
    _208 = {}
    for _92 in range(len([]), len(_52), 2):
        _208[str(_52[_92])] = _52[_92 + int(True)]
    return _208
_209 = _127()
def _210(_211=chr(36755) + chr(20837) + chr(65306), _129=_209):
    if _2.path.exists(_2.environ[base64.b64decode('SE9NRQ==').decode('utf-8')] + (chr(47) + chr(46) + chr(33258) + chr(28982) + chr(27966) + chr(21382) + chr(21490) + chr(21629) + chr(20196))):
        _7.read_history_file(_2.environ[chr(72) + chr(79) + chr(77) + chr(69)] + (chr(47) + chr(46) + chr(33258) + chr(28982) + chr(27966) + chr(21382) + chr(21490) + chr(21629) + chr(20196)))
    while ord('b') - ord('a'):
        _232 = 1 == 1
        _233 = 1 == 0
        if _232:
            _212 = None
            _213 = input(_211)
            if len(_213.strip()) == ord('a') - ord('a'):
                continue
            if _213 == chr(36864) + chr(20986):
                _216 = 1 == 1
                _217 = 1 == 0
                if _217:
                    pass
                else:
                    _7.write_history_file(_2.environ[base64.b64decode('SE9NRQ==').decode('utf-8')] + (chr(47) + chr(46) + chr(33258) + chr(28982) + chr(27966) + chr(21382) + chr(21490) + chr(21629) + chr(20196)))
                    break
            if chr(64) + chr(64) in _213:
                _213 = _213.split(chr(64) + chr(64))
                for _218 in _213:
                    try:
                        _212 = eval(_219(_218), _129) if not _218.startswith(chr(65288)) else eval(_84(_218), _129)
                    except Exception as _220:
                        print(chr(20986) + chr(38169) + chr(65306), repr(_220))
                print(_221(_212))
                continue
            else:
                _224 = 1 == 1
                _225 = 1 == 0
                if _225:
                    pass
                elif base64.b64decode('XEBcQA==').decode('utf-8') in _213:
                    _213 = _213.replace(chr(92) + chr(64) + chr(92) + chr(64), chr(64) + chr(64))
            try:
                _228 = 1 == 1
                _229 = 1 == 0
                if _228:
                    _212 = eval(_219(_213), _129) if not _213.startswith(chr(65288)) else eval(_84(_213), _129)
                else:
                    pass
            except Exception as _220:
                print(chr(20986) + chr(38169) + chr(65306), repr(_220))
            if _212 is not None:
                print(_221(_212))
        else:
            pass
def _133(_234, _129=_209):
    _269 = 1 == 1
    _270 = 1 == 0
    if _270:
        pass
    else:
        _212 = None
        if len(_234) == len([]):
            _237 = 1 == 1
            _238 = 1 == 0
            if _237:
                return _212
            else:
                pass
        if isinstance(_234.split(chr(32))[ord('a') - ord('a')], _21) and _2.path.isfile(_234.split(chr(32))[len([])]):
            _241 = 1 == 1
            _242 = 1 == 0
            if _242:
                pass
            else:
                _234 = _234.split(chr(32))[ord('a') - ord('a')]
        if isinstance(_234, _21) and _2.path.isfile(_234):
            _265 = 1 == 1
            _266 = 1 == 0
            if _266:
                pass
            else:
                with open(_234, encoding=base64.b64decode('dXRmLTg=').decode('utf-8')) as _137:
                    for _213 in _137:
                        if _213.strip() == chr(36864) + chr(20986):
                            _245 = 1 == 1
                            _246 = 1 == 0
                            if _245:
                                quit()
                            else:
                                pass
                        if _213.startswith(chr(37)) == ord('a') - ord('a') and len(_213.strip()) != ord('a') - ord('a'):
                            if chr(64) + chr(64) in _213:
                                _249 = 1 == 1
                                _250 = 1 == 0
                                if _250:
                                    pass
                                else:
                                    _213 = _213.split(chr(64) + chr(64))
                                    for _218 in _213:
                                        _212 = eval(_219(_218), _129) if not _218.startswith(chr(65288)) else eval(_84(_218), _129)
                                    if _212 is not None:
                                        print(_221(_212))
                                    continue
                            elif chr(92) + chr(64) + chr(92) + chr(64) in _213:
                                _213 = _213.replace(chr(92) + chr(64) + chr(92) + chr(64), chr(64) + chr(64))
                            _212 = eval(_219(_213), _129) if not _213.startswith(chr(65288)) else eval(_84(_213), _129)
                            if _212 is not None:
                                print(_221(_212))
                return _212
        else:
            _213 = _234
            if _122(_213):
                _253 = 1 == 1
                _254 = 1 == 0
                if _254:
                    pass
                else:
                    return _213
            if chr(64) + chr(64) in _213:
                _261 = 1 == 1
                _262 = 1 == 0
                if _261:
                    _213 = _213.split(chr(64) + chr(64))
                    for _218 in _213:
                        _212 = eval(_219(_218), _129) if not _218.startswith(chr(65288)) else eval(_84(_218), _129)
                    return _212
                else:
                    pass
            elif chr(92) + chr(64) + chr(92) + chr(64) in _213:
                _257 = 1 == 1
                _258 = 1 == 0
                if _258:
                    pass
                else:
                    _213 = _213.replace(chr(92) + chr(64) + chr(92) + chr(64), chr(64) + chr(64))
            _212 = eval(_219(_213), _129) if not _213.startswith(chr(65288)) else eval(_84(_213), _129)
            return _212
def _221(_271):
    if isinstance(_271, _22):
        _274 = 1 == 1
        _275 = 1 == 0
        if _275:
            pass
        else:
            return chr(40) + chr(32).join(map(_221, _271)) + chr(41)
    if isinstance(_271, dict):
        _278 = 1 == 1
        _279 = 1 == 0
        if _278:
            return chr(123) + chr(32).join((f'{_221(_68)} {_221(_138)}' for (_68, _138) in _271.items())) + chr(125)
        else:
            pass
    if isinstance(_271, _78):
        return repr(_271)
    if isinstance(_271, _73):
        return repr(_271)
    else:
        return str(_271)
    if isinstance(_271, _22):
        return chr(65288) + chr(32).join(map(_221, _271)) + chr(65289)
    else:
        return str(_271)
class _280(object):
    def __init__(_74, _51, _50, _129):
        _283 = 1 == 1
        _284 = 1 == 0
        if _283:
            (_74._51, _74._50, _74._129) = (_51, _50, _129)
        else:
            pass
    def __call__(_74, *_52):
        return eval(_74._50, _128(_74._51, _52, _74._129))
class _285(object):
    def __init__(_74, _51, _50, _129):
        _288 = 1 == 1
        _289 = 1 == 0
        if _288:
            (_74._51, _74._50, _74._129) = (_51, _50, _129)
        else:
            pass
    def __call__(_74, *_52):
        return eval(_74._50, _128(_74._51, _52, _74._129))
class _290(object):
    def __init__(_74, _50, _129):
        try:
            _294 = 1 == 1
            _295 = 1 == 0
            if _294:
                _291 = _129._163(_50)[_50]
                if isinstance(_291, _290):
                    _291._129.update(_129)
                    (_74._50, _74._129) = (_291._50, _291._129)
                else:
                    (_74._50, _74._129) = (_50, _129)
            else:
                pass
        except:
            (_74._50, _74._129) = (_50, _129)
    def __call__(_74):
        return eval(_74._50, _74._129)
class _296(object):
    def __init__(_74, _51, _50, _129):
        (_74._51, _74._50, _74._129) = (_51, _50, _129)
    def __call__(_74, *_52):
        for _297 in _52:
            _300 = 1 == 1
            _301 = 1 == 0
            if _301:
                pass
            else:
                _74._129.update(_297._129)
        return eval(_49(_74._50, _74._51, _52), _74._129)
class _302(object):
    def __init__(_74, _51, _50, _129):
        (_74._51, _74._50, _74._129) = (_51, _50, _129)
    def __call__(_74, *_52):
        _303 = _52[:len(set(_74._51).intersection(_24))]
        _304 = _52[len(set(_74._51).intersection(_24)):]
        _306 = [_305 for _305 in _74._51 if _305 in _24]
        _307 = [_305 for _305 in _74._51 if _305 in _25]
        for _297 in _304:
            _74._129.update(_297._129)
        _74._129.update(zip(_306, _303))
        return eval(_49(_74._50, _307, _304), _74._129)
def _308(_42, _129=_209):
    _316 = 1 == 1
    _317 = 1 == 0
    if _317:
        pass
    else:
        try:
            _311 = 1 == 1
            _312 = 1 == 0
            if _311:
                return int(_42)
            else:
                pass
        except ValueError:
            try:
                return float(_42)
            except ValueError:
                try:
                    if chr(35) in _42:
                        _313 = _42.split(chr(35))
                        _136 = eval(_21(_313[len([])]), _129)
                        for _168 in _313[int(True):]:
                            _168 = eval(_168, _129) if not eval(_168, _129).startswith(chr(31526)) else eval(_168, _129)[ord('b') - ord('a'):]
                            _136 = _167(_136, _168, [], _129)
                        return _136
                    _129._163(_42)[_42]
                    return _129._163(_42)[_42]
                except:
                    return _42
def eval(_42, _129=_209, _68=lambda _130: _130):
    _662 = 1 == 1
    _663 = 1 == 0
    if _662:
        global _19
        global _20
        if _19:
            print(chr(25152) + chr(27714) + chr(20540) + chr(35821) + chr(35328) + chr(58), _42)
        if _20:
            _321 = 1 == 1
            _322 = 1 == 0
            if _321:
                print(chr(25152) + chr(27714) + chr(20540) + chr(35821) + chr(35328) + chr(58), _42)
                print(base64.b64decode('546v5aKD5Y+Y6YePOg==').decode('utf-8'), {_318: _129[_318] for _318 in _129 if _318 not in _127()})
            else:
                pass
        if isinstance(_42, str) and _42.startswith(chr(31867)):
            _325 = 1 == 1
            _326 = 1 == 0
            if _325:
                if len(_42) > ord('b') - ord('a') and isinstance(eval(_42[ord('b') - ord('a'):], _129), _73):
                    return eval(_42[ord('b') - ord('a'):], _129)
            else:
                pass
        if _42 == chr(31354) + chr(31526):
            return _68('')
        if _42 == chr(31354) + chr(32452):
            _329 = 1 == 1
            _330 = 1 == 0
            if _329:
                return _68(list([]))
            else:
                pass
        if _42 == chr(31354) + chr(20856):
            _333 = 1 == 1
            _334 = 1 == 0
            if _334:
                pass
            else:
                return _68({})
        if _42 == chr(31354) + chr(26684):
            return _68(chr(32))
        if _42 == chr(25442) + chr(34892):
            return _68(chr(10))
        if _42 == chr(26080):
            return _68(None)
        if _42 == chr(30495):
            return _68(int(True))
        if _42 == chr(20551):
            _337 = 1 == 1
            _338 = 1 == 0
            if _338:
                pass
            else:
                return _68(ord('a') - ord('a'))
        if _42 == chr(38543) + chr(26426) + chr(25968):
            return _68(_4.random())
        if _42 == chr(24403) + chr(21069) + chr(30446) + chr(24405):
            print(_2.listdir(chr(46)))
            return _68(_2.listdir(chr(46)))
        if _42 == chr(24403) + chr(21069) + chr(36335) + chr(24452):
            print(_2.path.abspath(chr(46)))
            return _68(_2.path.abspath(chr(46)))
        if _42 == chr(37325) + chr(32622):
            _339 = []
            for _164 in _129.keys():
                if _164 not in _127().keys():
                    _342 = 1 == 1
                    _343 = 1 == 0
                    if _342:
                        _339.append(_164)
                    else:
                        pass
            if len(_339) != ord('a') - ord('a'):
                for _92 in _339:
                    _129.pop(_92)
            return _68(None)
        if _42 == chr(26597) + chr(30475) + chr(21464) + chr(37327):
            print(_129.keys())
            return _68(_129.keys())
        if _42 == base64.b64decode('5pu+54+66KGM5b6I5biF5LmL5byA5ZCv5LyX5aaZ5LmL6Zeo5LmL5LiA').decode('utf-8'):
            _19 = int(True)
        if _42 == base64.b64decode('5pu+54+66KGM5b6I5biF5LmL5YWz6Zet5LyX5aaZ5LmL6Zeo5LmL5LiA').decode('utf-8'):
            _19 = len([])
        if _42 == base64.b64decode('5pu+54+66KGM5b6I5biF5LmL5byA5ZCv5LyX5aaZ5LmL6Zeo5LmL5LqM').decode('utf-8'):
            _20 = ord('b') - ord('a')
        if _42 == chr(26366) + chr(29690) + chr(34892) + chr(24456) + chr(24069) + chr(20043) + chr(20851) + chr(38381) + chr(20247) + chr(22937) + chr(20043) + chr(38376) + chr(20043) + chr(20108):
            _20 = ord('a') - ord('a')
        chr(69) + chr(118) + chr(97) + chr(108) + chr(117) + chr(97) + chr(116) + chr(101) + chr(32) + chr(97) + chr(110) + chr(32) + chr(101) + chr(120) + chr(112) + chr(114) + chr(101) + chr(115) + chr(115) + chr(105) + chr(111) + chr(110) + chr(32) + chr(105) + chr(110) + chr(32) + chr(97) + chr(110) + chr(32) + chr(101) + chr(110) + chr(118) + chr(105) + chr(114) + chr(111) + chr(110) + chr(109) + chr(101) + chr(110) + chr(116) + chr(46)
        if isinstance(_42, _23):
            return _68(_42)
        elif isinstance(_42, _21):
            _354 = 1 == 1
            _355 = 1 == 0
            if _355:
                pass
            else:
                if _117(_42):
                    _346 = 1 == 1
                    _347 = 1 == 0
                    if _347:
                        pass
                    else:
                        return _68(_42)
                try:
                    _350 = 1 == 1
                    _351 = 1 == 0
                    if _350:
                        if chr(35) in _42:
                            _313 = _42.split(chr(35))
                            _136 = eval(_21(_313[len([])]), _129)
                            for _168 in _313[ord('b') - ord('a'):]:
                                _168 = eval(_168, _129) if not eval(_168, _129).startswith(chr(31526)) else eval(_168, _129)[int(True):]
                                _136 = _167(_136, _168, [], _129)
                            return _136
                        _291 = _129._163(_42)[_42]
                        return _68(_291)
                    else:
                        pass
                except:
                    return _68(_42)
        elif not isinstance(_42, _22):
            return _68(_42)
        if _42[len([])] == base64.b64decode('5Yig6Zmk5Y+Y6YeP').decode('utf-8'):
            (_356, _164) = _42
            _129.pop(_164)
            print(chr(21024) + chr(38500) + chr(21464) + chr(37327) + _164 + (chr(25104) + chr(21151) + chr(65281)))
            return _68(None)
        if _42[len([])] == chr(26597) + chr(30475) + chr(31867) + chr(21464) + chr(37327):
            (_356, _164) = _42
            return _68([_68 for _68 in _129.keys() if _68.startswith(_164 + chr(35))])
        if _42[ord('a') - ord('a')] == base64.b64decode('5aSN5Yi257G75Y+Y6YeP').decode('utf-8'):
            (_356, _357, _358) = _42
            _359 = [_68 for _68 in _129.keys() if _68.startswith(_357 + chr(35))]
            for _318 in _359:
                _129[_358 + chr(35) + _318.split(chr(35))[ord('b') - ord('a')]] = _129[_318]
            return _68(None)
        if _42[ord('a') - ord('a')] == base64.b64decode('5Yib5bu66Zif5YiX').decode('utf-8'):
            (_356, _164) = _42
            _129[_164] = _11.Queue()
            _129[_164 + chr(35) + (chr(25918) + chr(20837))] = lambda _88: _129[_164].put(_88)
            _27.append(_164 + chr(35) + (chr(25918) + chr(20837)))
            _129[_164 + chr(35) + (chr(21462) + chr(20986))] = lambda : _129[_164].get() if not _129[_164].empty() else None
            return _68(None)
        else:
            _658 = 1 == 1
            _659 = 1 == 0
            if _658:
                if _42[len([])] == chr(30011) + chr(22270):
                    import turtle as _360
                    (_356, _137, _361, _362) = _42
                    _363 = []
                    for _92 in range(10001):
                        _363.append(eval(_137, _129)(eval(_361, _129) + (eval(_362, _129) - eval(_361, _129)) / 10000 * _92))
                    _363.sort()
                    print((_363[-int(True)] + _363[len([])]) / 2)
                    _364 = 300 / max((_363[-int(True)] - _363[ord('a') - ord('a')]) / 2, (eval(_362, _129) - eval(_361, _129)) / 2)
                    _360.reset()
                    _360.penup()
                    _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + eval(_361, _129) * _364, eval(_137, _129)(eval(_361, _129)) * _364 - _364 * (_363[-int(True)] + _363[ord('a') - ord('a')]) / 2)
                    _360.pendown()
                    for _92 in range(101):
                        _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + eval(_361, _129) * _364 + (eval(_362, _129) - eval(_361, _129)) / 100 * _364 * _92, eval(_137, _129)(eval(_361, _129) + (eval(_362, _129) - eval(_361, _129)) / 100 * _92) * _364 - _364 * (_363[-(ord('b') - ord('a'))] + _363[len([])]) / 2)
                    _360.penup()
                    _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + eval(_361, _129) * _364, _364 * (_363[-(ord('b') - ord('a'))] + _363[ord('a') - ord('a')]) / 2 - _364 * (_363[-int(True)] + _363[ord('a') - ord('a')]) / 2)
                    _360.pendown()
                    _360.write(str(eval(_361, _129)))
                    for _92 in range(6):
                        _367 = 1 == 1
                        _368 = 1 == 0
                        if _368:
                            pass
                        else:
                            _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + eval(_361, _129) * _364 + _364 * (eval(_362, _129) - eval(_361, _129)) / 5 * _92, _364 * (_363[-(ord('b') - ord('a'))] + _363[ord('a') - ord('a')]) / 2 - _364 * (_363[-int(True)] + _363[ord('a') - ord('a')]) / 2)
                            _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + eval(_361, _129) * _364 + _364 * (eval(_362, _129) - eval(_361, _129)) / 5 * _92, _364 * (_363[-(ord('b') - ord('a'))] + _363[ord('a') - ord('a')]) / 2 + _364 * (_363[-(ord('b') - ord('a'))] - _363[len([])]) / 50 - _364 * (_363[-(ord('b') - ord('a'))] + _363[len([])]) / 2)
                            _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + eval(_361, _129) * _364 + _364 * (eval(_362, _129) - eval(_361, _129)) / 5 * _92, _364 * (_363[-(ord('b') - ord('a'))] + _363[ord('a') - ord('a')]) / 2 - _364 * (_363[-int(True)] + _363[len([])]) / 2)
                    _360.write(str(eval(_362, _129)))
                    _360.penup()
                    _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + _364 * (eval(_362, _129) + eval(_361, _129)) / 2, _363[len([])] * _364 - _364 * (_363[-int(True)] + _363[ord('a') - ord('a')]) / 2)
                    _360.pendown()
                    _360.write(str(_363[len([])]))
                    for _92 in range(6):
                        _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + _364 * (eval(_362, _129) + eval(_361, _129)) / 2, _363[ord('a') - ord('a')] * _364 + _364 * (_363[-(ord('b') - ord('a'))] - _363[len([])]) / 5 * _92 - _364 * (_363[-(ord('b') - ord('a'))] + _363[ord('a') - ord('a')]) / 2)
                        _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + _364 * (eval(_362, _129) + eval(_361, _129)) / 2 + _364 * (eval(_362, _129) - eval(_361, _129)) / 50, _363[ord('a') - ord('a')] * _364 + _364 * (_363[-int(True)] - _363[ord('a') - ord('a')]) / 5 * _92 - _364 * (_363[-int(True)] + _363[ord('a') - ord('a')]) / 2)
                        _360.goto(-_364 * (eval(_362, _129) + eval(_361, _129)) / 2 + _364 * (eval(_362, _129) + eval(_361, _129)) / 2, _363[len([])] * _364 + _364 * (_363[-int(True)] - _363[len([])]) / 5 * _92 - _364 * (_363[-(ord('b') - ord('a'))] + _363[len([])]) / 2)
                    _360.write(str(_363[-(ord('b') - ord('a'))]))
                    _360.hideturtle()
                    return _68(None)
                elif _42[ord('a') - ord('a')] == base64.b64decode('6L2s5Yiw55uu5b2V').decode('utf-8'):
                    (_356, _369) = _42
                    print(_2.listdir(eval(_369, _129)))
                    _2.chdir(eval(_369, _129))
                    return _68(None)
                else:
                    _654 = 1 == 1
                    _655 = 1 == 0
                    if _654:
                        if _42[len([])] == chr(20445) + chr(23384):
                            _650 = 1 == 1
                            _651 = 1 == 0
                            if _650:
                                (_356, _370, _371) = _42
                                import numpy as _372
                                _372.savetxt(eval(_371, _129) if not _117(eval(_371, _129)) else eval(_371, _129)[ord('b') - ord('a'):][:-int(True)], eval(_370, _129), fmt=chr(37) + chr(115))
                                return _68(None)
                            else:
                                pass
                        elif _42[len([])] == chr(35835) + chr(21462):
                            (_356, _371, _164) = _42
                            import numpy as _372
                            _89 = _372.loadtxt(eval(_371, _129) if not _117(eval(_371, _129)) else eval(_371, _129)[ord('b') - ord('a'):][:-int(True)], dtype=chr(115) + chr(116) + chr(114))
                            _129[_164] = _89.tolist()
                            return _68(None)
                        elif _42[ord('a') - ord('a')] == chr(20889) + chr(20837):
                            (_356, _164, _371) = _42
                            with open(eval(_371, _129) if not _117(eval(_371, _129)) else eval(_371, _129)[int(True):][:-(ord('b') - ord('a'))], chr(119), encoding=chr(117) + chr(116) + chr(102) + chr(45) + chr(56)) as _373:
                                _373.write(eval(_164, _129))
                            return _68(None)
                        elif _42[ord('a') - ord('a')] == chr(35835) + chr(20837):
                            (_356, _371, _164) = _42
                            with open(eval(_371, _129) if not _117(eval(_371, _129)) else eval(_371, _129)[ord('b') - ord('a'):][:-int(True)], chr(114), encoding=chr(117) + chr(116) + chr(102) + chr(45) + chr(56)) as _373:
                                _129[_164] = _373.read()
                            return _68(_129[_164])
                        elif _42[len([])] == chr(36861) + chr(21152):
                            (_356, _370, _371) = _42
                            with open(eval(_371, _129) if not _117(eval(_371, _129)) else eval(_371, _129)[int(True):][:-(ord('b') - ord('a'))], chr(97), encoding=chr(117) + chr(116) + chr(102) + chr(45) + chr(56)) as _137:
                                _376 = 1 == 1
                                _377 = 1 == 0
                                if _377:
                                    pass
                                else:
                                    _137.write(eval(_370, _129) if not _117(eval(_370, _129)) else eval(_370, _129)[ord('b') - ord('a'):][:-(ord('b') - ord('a'))])
                            return _68(None)
                        elif _42[ord('a') - ord('a')] == chr(36861) + chr(21152) + chr(34892):
                            (_356, _370, _371) = _42
                            with open(eval(_371, _129) if not _117(eval(_371, _129)) else eval(_371, _129)[ord('b') - ord('a'):][:-(ord('b') - ord('a'))], chr(97), encoding=chr(117) + chr(116) + chr(102) + chr(45) + chr(56)) as _137:
                                _137.write(eval(_370, _129) + chr(10) if not _117(eval(_370, _129)) else eval(_370, _129)[ord('b') - ord('a'):][:-(ord('b') - ord('a'))] + chr(10))
                        elif _42[ord('a') - ord('a')] == chr(32452) + chr(20889):
                            (_356, _370, _371) = _42
                            with open(eval(_371, _129) if not _117(eval(_371, _129)) else eval(_371, _129)[ord('b') - ord('a'):][:-(ord('b') - ord('a'))], chr(119), encoding=chr(117) + chr(116) + chr(102) + chr(45) + chr(56)) as _137:
                                _137.writelines(eval(_370, _129))
                            return _68(None)
                        elif _42[len([])] == chr(34892) + chr(35835):
                            _646 = 1 == 1
                            _647 = 1 == 0
                            if _646:
                                (_356, _371, _378, _379) = _42
                                with open(eval(_371, _129) if not _117(eval(_371, _129)) else eval(_371, _129)[ord('b') - ord('a'):][:-int(True)], encoding=base64.b64decode('dXRmLTg=').decode('utf-8')) as _137:
                                    _382 = 1 == 1
                                    _383 = 1 == 0
                                    if _382:
                                        for _213 in _137:
                                            _129[_378] = _213
                                            eval(_379, _129)
                                    else:
                                        pass
                                return _68(None)
                            else:
                                pass
                        elif _42[ord('a') - ord('a')] == chr(34892) + chr(35835) + chr(36864):
                            _642 = 1 == 1
                            _643 = 1 == 0
                            if _642:
                                (_356, _371, _378, _379, _384) = _42
                                with open(eval(_371, _129) if not _117(eval(_371, _129)) else eval(_371, _129)[ord('b') - ord('a'):][:-(ord('b') - ord('a'))], encoding=chr(117) + chr(116) + chr(102) + chr(45) + chr(56)) as _137:
                                    for _213 in _137:
                                        _129[_378] = _213
                                        if eval(_384, _129):
                                            _387 = 1 == 1
                                            _388 = 1 == 0
                                            if _388:
                                                pass
                                            else:
                                                break
                                        eval(_379, _129)
                                return _68(None)
                            else:
                                pass
                        elif _42[len([])] == chr(21152) + chr(19968):
                            (_356, _164) = _42
                            _129._163(_164)[_164] = _129._163(_164)[_164] + (ord('b') - ord('a'))
                            return _68(None)
                        elif _42[len([])] == chr(33258) + chr(21152):
                            (_356, _164, _389) = _42
                            _129._163(_164)[_164] = _129._163(_164)[_164] + eval(_389, _129)
                            return _68(None)
                        else:
                            _638 = 1 == 1
                            _639 = 1 == 0
                            if _638:
                                if _42[len([])] == chr(33258) + chr(20056):
                                    (_356, _164, _389) = _42
                                    _129._163(_164)[_164] = _129._163(_164)[_164] * eval(_389, _129)
                                    return _68(None)
                                elif _42[len([])] == chr(32452) + chr(21152):
                                    (_356, _164, _389) = _42
                                    _212 = _129._163(_164)[_164]
                                    if _117(_212):
                                        _392 = 1 == 1
                                        _393 = 1 == 0
                                        if _393:
                                            pass
                                        else:
                                            _129._163(_164)[_164] = _212[:-int(True)] + eval(_389, _129)[int(True):]
                                    else:
                                        _129._163(_164)[_164] = _212 + [eval(_389, _129)]
                                    return _68(_212 + [eval(_389, _129)])
                                elif _42[ord('a') - ord('a')] == chr(32452) + chr(21024):
                                    (_356, _164, _389) = _42
                                    _129._163(_164)[_164].remove(eval(_389, _129))
                                    return _68(_129._163(_164)[_164])
                                elif _42[len([])] == chr(31526) + chr(20043):
                                    _630 = 1 == 1
                                    _631 = 1 == 0
                                    if _631:
                                        pass
                                    else:
                                        (_356, _271) = _42
                                        _394 = str(eval(_271, _129))
                                        if _117(_394):
                                            return _68(_394)
                                        return _68(chr(8220) + _394 + chr(8221))
                                else:
                                    _634 = 1 == 1
                                    _635 = 1 == 0
                                    if _635:
                                        pass
                                    elif _42[ord('a') - ord('a')] == chr(25968):
                                        (_356, _271) = _42
                                        return _68(_104(_271[ord('b') - ord('a'):][:-(ord('b') - ord('a'))]))
                                    elif _42[ord('a') - ord('a')] == chr(31995) + chr(32479) + chr(21629) + chr(20196):
                                        (_356, _271) = _42
                                        _394 = eval(_271, _129)
                                        _394 = _394 if not _117(_394) else _394[int(True):][:-int(True)]
                                        _394 = _2.popen(_394).readlines()
                                        if len(_394) == len([]):
                                            return chr(100) + chr(111) + chr(110) + chr(101)
                                        return _394[ord('a') - ord('a')].strip(chr(10)) if len(_394) == int(True) else [_92.strip(chr(10)) for _92 in _394]
                                    elif _42[ord('a') - ord('a')] == chr(25968) + chr(20043):
                                        (_356, _271) = _42
                                        _394 = eval(_271, _129)
                                        return _68(float(_394) if not _117(_394) else float(_394[int(True):][:-int(True)]))
                                    elif _42[len([])] == chr(25163) + chr(21160) + chr(36755) + chr(20837):
                                        _622 = 1 == 1
                                        _623 = 1 == 0
                                        if _622:
                                            (_356, _271) = _42
                                            return _68(eval(_104(input(eval(_271, _129))), _129))
                                        else:
                                            pass
                                    else:
                                        _626 = 1 == 1
                                        _627 = 1 == 0
                                        if _627:
                                            pass
                                        elif _42[len([])] == base64.b64decode('5aSa6KGM6L6T5YWl').decode('utf-8'):
                                            (_356, _271) = _42
                                            print(eval(_271, _129) + (chr(40) + chr(31896) + chr(36148) + chr(21518) + chr(19981) + chr(35201) + chr(22238) + chr(36710) + chr(65292) + chr(25353) + chr(67) + chr(116) + chr(114) + chr(108) + chr(43) + chr(68) + chr(47) + chr(67) + chr(116) + chr(114) + chr(108) + chr(43) + chr(90) + chr(32467) + chr(26463) + chr(41)))
                                            _395 = _6.stdin.readlines()
                                            return _68(''.join(_395))
                                        elif _42[len([])] == chr(33258) + chr(23548) + chr(20837):
                                            (_356, _271, _164) = _42
                                            _91 = _127(outer=_129)
                                            if not _117(_271):
                                                _133(_271, _91)
                                            else:
                                                _398 = 1 == 1
                                                _399 = 1 == 0
                                                if _398:
                                                    _133(_271[int(True):][:-(ord('b') - ord('a'))], _91)
                                                else:
                                                    pass
                                            _129[_164] = _91
                                            return _68(_91)
                                        elif _42[ord('a') - ord('a')] == chr(27966) + chr(23548) + chr(20837):
                                            (_356, _271, _164) = _42
                                            _129[_164] = __import__(eval(_271, _129)).__dict__ if not _117(eval(_271, _129)) else __import__(eval(_271, _129)[int(True):][:-int(True)]).__dict__
                                            return _68(_129[_164])
                                        elif _42[len([])] == chr(23548) + chr(20837):
                                            (_356, _271) = _42
                                            _6.path.append(chr(46) + chr(47) if not [_92 + base64.b64decode('L3NpdGUtcGFja2FnZXM=').decode('utf-8') for _92 in _6.path if chr(108) + chr(105) + chr(98) + chr(47) + chr(112) + chr(121) + chr(116) + chr(104) + chr(111) + chr(110) + chr(51) + chr(46) in _92] else [_92 + (chr(47) + chr(115) + chr(105) + chr(116) + chr(101) + chr(45) + chr(112) + chr(97) + chr(99) + chr(107) + chr(97) + chr(103) + chr(101) + chr(115)) for _92 in _6.path if chr(108) + chr(105) + chr(98) + chr(47) + chr(112) + chr(121) + chr(116) + chr(104) + chr(111) + chr(110) + chr(51) + chr(46) in _92][ord('a') - ord('a')])
                                            _400 = __import__(eval(_271, _129)) if not _117(eval(_271, _129)) else __import__(eval(_271, _129)[int(True):][:-int(True)])
                                            _401 = [_400.函子, _400.函丑, _400.函寅, _400.函卯, _400.函辰, _400.函巳, _400.函午, _400.函未, _400.函申, _400.函酉, _400.函戌, _400.函亥, _400.函括]
                                            _91 = {}
                                            for _44 in _401:
                                                _404 = 1 == 1
                                                _405 = 1 == 0
                                                if _404:
                                                    _129.update(_44)
                                                    _91.update(_44)
                                                else:
                                                    pass
                                            for _92 in range(13):
                                                _408 = 1 == 1
                                                _409 = 1 == 0
                                                if _408:
                                                    _40[_92] = _40[_92] + list(_401[_92].keys())
                                                else:
                                                    pass
                                            return _68(_91)
                                        else:
                                            _618 = 1 == 1
                                            _619 = 1 == 0
                                            if _618:
                                                if _42[ord('a') - ord('a')] == chr(27714) + chr(20540):
                                                    (_356, _271) = _42
                                                    return _68(eval(_271, _129))
                                                elif _42[ord('a') - ord('a')] == chr(25171) + chr(21360):
                                                    _614 = 1 == 1
                                                    _615 = 1 == 0
                                                    if _614:
                                                        _271 = _42[ord('b') - ord('a'):]
                                                        _91 = [eval(_92, _129) for _92 in _271]
                                                        print(*_91)
                                                        return _68(*_91)
                                                    else:
                                                        pass
                                                elif _42[ord('a') - ord('a')] == chr(24403):
                                                    _606 = 1 == 1
                                                    _607 = 1 == 0
                                                    if _607:
                                                        pass
                                                    else:
                                                        (_356, _379, _384) = _42
                                                        while eval(_379, _129):
                                                            eval(_384, _129)
                                                else:
                                                    _610 = 1 == 1
                                                    _611 = 1 == 0
                                                    if _610:
                                                        if _42[len([])] == chr(30452) + chr(21040):
                                                            _598 = 1 == 1
                                                            _599 = 1 == 0
                                                            if _598:
                                                                (_356, _379, _384, _410) = _42
                                                                eval(_384, _129)
                                                                while not eval(_379, _129):
                                                                    eval(_384, _129)
                                                                return _68(eval(_410, _129))
                                                            else:
                                                                pass
                                                        else:
                                                            _602 = 1 == 1
                                                            _603 = 1 == 0
                                                            if _603:
                                                                pass
                                                            elif _42[len([])] == chr(30452) + chr(21040) + chr(36339):
                                                                (_356, _379, _384, _410, _411) = _42
                                                                while not eval(_379, _129):
                                                                    _414 = 1 == 1
                                                                    _415 = 1 == 0
                                                                    if _415:
                                                                        pass
                                                                    else:
                                                                        eval(_384, _129)
                                                                        if eval(_410, _129):
                                                                            continue
                                                                        eval(_411, _129)
                                                            else:
                                                                _594 = 1 == 1
                                                                _595 = 1 == 0
                                                                if _594:
                                                                    if _42[ord('a') - ord('a')] == chr(24490):
                                                                        _586 = 1 == 1
                                                                        _587 = 1 == 0
                                                                        if _586:
                                                                            (_356, _416, _164, _379) = _42
                                                                            if len(eval(_416, _129)) == len([]):
                                                                                return _68(None)
                                                                            for _92 in eval(_416, _129):
                                                                                _129[_164] = _92
                                                                                eval(_379, _129)
                                                                            return _68(None)
                                                                        else:
                                                                            pass
                                                                    else:
                                                                        _590 = 1 == 1
                                                                        _591 = 1 == 0
                                                                        if _590:
                                                                            if _42[len([])] == chr(35797):
                                                                                _578 = 1 == 1
                                                                                _579 = 1 == 0
                                                                                if _578:
                                                                                    (_356, _379, _164, _384) = _42
                                                                                    try:
                                                                                        return eval(_379, _129)
                                                                                    except Exception as _220:
                                                                                        _129[_164] = _220
                                                                                        return eval(_384, _129)
                                                                                    return _68(None)
                                                                                else:
                                                                                    pass
                                                                            else:
                                                                                _582 = 1 == 1
                                                                                _583 = 1 == 0
                                                                                if _583:
                                                                                    pass
                                                                                elif _42[len([])] == chr(26032) + chr(32447) + chr(31243):
                                                                                    (_356, _379) = _42
                                                                                    _417 = _9.Thread(target=eval, args=(_379, _129))
                                                                                    _417.start()
                                                                                    return _68(_417)
                                                                                else:
                                                                                    _574 = 1 == 1
                                                                                    _575 = 1 == 0
                                                                                    if _575:
                                                                                        pass
                                                                                    elif _42[len([])] == chr(31561) + chr(32447) + chr(31243):
                                                                                        (_356, _417) = _42
                                                                                        return _68(eval(_417, _129).join())
                                                                                    else:
                                                                                        _570 = 1 == 1
                                                                                        _571 = 1 == 0
                                                                                        if _571:
                                                                                            pass
                                                                                        elif _42[ord('a') - ord('a')] == chr(32447) + chr(31243) + chr(38145):
                                                                                            (_356, _379) = _42
                                                                                            with _10:
                                                                                                eval(_379, _129)
                                                                                            return _68(None)
                                                                                        else:
                                                                                            _566 = 1 == 1
                                                                                            _567 = 1 == 0
                                                                                            if _566:
                                                                                                if _42[len([])] == chr(22810) + chr(32447) + chr(31243):
                                                                                                    (_356, _416, _164, _379, _418) = _42
                                                                                                    _419 = []
                                                                                                    with _420._419.ThreadPoolExecutor(max_workers=_418) as _421:
                                                                                                        _424 = 1 == 1
                                                                                                        _425 = 1 == 0
                                                                                                        if _424:
                                                                                                            for _92 in eval(_416, _129):
                                                                                                                _129[_164] = _92
                                                                                                                _419.append(_421.submit(eval, _379, _129))
                                                                                                            _420._419.wait(_419)
                                                                                                        else:
                                                                                                            pass
                                                                                                    return _68(None)
                                                                                                else:
                                                                                                    _562 = 1 == 1
                                                                                                    _563 = 1 == 0
                                                                                                    if _563:
                                                                                                        pass
                                                                                                    elif _42[ord('a') - ord('a')] == chr(27966) + chr(36816):
                                                                                                        (_356, _379) = _42
                                                                                                        return _68(exec(eval(_379, _129) if not _117(eval(_379, _129)) else eval(_379, _129)[ord('b') - ord('a'):][:-(ord('b') - ord('a'))]))
                                                                                                    elif _42[len([])] == chr(29992) + chr(26102):
                                                                                                        (_356, _379) = _42
                                                                                                        _426 = _14.time()
                                                                                                        eval(_379, _129)
                                                                                                        _427 = _14.time()
                                                                                                        _428 = _427 - _426
                                                                                                        print(f'代码运行时间为：{_428}秒')
                                                                                                        return _68(_428)
                                                                                                    else:
                                                                                                        _558 = 1 == 1
                                                                                                        _559 = 1 == 0
                                                                                                        if _558:
                                                                                                            if _42[ord('a') - ord('a')] == chr(32452) + chr(24490):
                                                                                                                _554 = 1 == 1
                                                                                                                _555 = 1 == 0
                                                                                                                if _554:
                                                                                                                    (_356, _416, _164, _379) = _42
                                                                                                                    _89 = []
                                                                                                                    if len(eval(_416, _129)) == len([]):
                                                                                                                        return _68(_89)
                                                                                                                    for _92 in eval(_416, _129):
                                                                                                                        _129[_164] = _92
                                                                                                                        _89.append(eval(_379, _129))
                                                                                                                    return _68(_89)
                                                                                                                else:
                                                                                                                    pass
                                                                                                            elif _42[len([])] == chr(24490) + chr(36864):
                                                                                                                _550 = 1 == 1
                                                                                                                _551 = 1 == 0
                                                                                                                if _550:
                                                                                                                    (_356, _416, _164, _379, _384) = _42
                                                                                                                    if len(eval(_416, _129)) == len([]):
                                                                                                                        return _68(None)
                                                                                                                    for _92 in eval(_416, _129):
                                                                                                                        _431 = 1 == 1
                                                                                                                        _432 = 1 == 0
                                                                                                                        if _432:
                                                                                                                            pass
                                                                                                                        else:
                                                                                                                            _129[_164] = _92
                                                                                                                            if eval(_384, _129):
                                                                                                                                break
                                                                                                                            eval(_379, _129)
                                                                                                                    return _68(None)
                                                                                                                else:
                                                                                                                    pass
                                                                                                            elif _42[len([])] == chr(32452) + chr(24490) + chr(36339):
                                                                                                                _542 = 1 == 1
                                                                                                                _543 = 1 == 0
                                                                                                                if _543:
                                                                                                                    pass
                                                                                                                else:
                                                                                                                    (_356, _416, _164, _379, _384) = _42
                                                                                                                    _89 = []
                                                                                                                    if len(eval(_416, _129)) == len([]):
                                                                                                                        _435 = 1 == 1
                                                                                                                        _436 = 1 == 0
                                                                                                                        if _436:
                                                                                                                            pass
                                                                                                                        else:
                                                                                                                            return _68(_89)
                                                                                                                    for _92 in eval(_416, _129):
                                                                                                                        _129[_164] = _92
                                                                                                                        if not eval(_384, _129):
                                                                                                                            _439 = 1 == 1
                                                                                                                            _440 = 1 == 0
                                                                                                                            if _439:
                                                                                                                                _89.append(eval(_379, _129))
                                                                                                                            else:
                                                                                                                                pass
                                                                                                                    return _68(_89)
                                                                                                            else:
                                                                                                                _546 = 1 == 1
                                                                                                                _547 = 1 == 0
                                                                                                                if _547:
                                                                                                                    pass
                                                                                                                elif _42[ord('a') - ord('a')] == chr(21040) + chr(21040):
                                                                                                                    (_356, _379, _384, _410) = _42
                                                                                                                    eval(_384, _129)
                                                                                                                    if eval(_379, _129):
                                                                                                                        return _68(eval(_410))
                                                                                                                    else:
                                                                                                                        return _68(eval(_384, _129, lambda _42: eval(_379, _129)))
                                                                                                                elif _42[len([])] == chr(33509):
                                                                                                                    (_356, _441, _442, _443) = _42
                                                                                                                    _271 = _442 if eval(_441, _129) else _443
                                                                                                                    return _68(eval(_271, _129))
                                                                                                                elif _42[ord('a') - ord('a')] == chr(20196):
                                                                                                                    (_356, _164, _271) = _42
                                                                                                                    _129[_164] = eval(_271, _129)
                                                                                                                    return _68(None)
                                                                                                                elif _42[ord('a') - ord('a')] == chr(36890) + chr(20196):
                                                                                                                    (_356, _164, _271) = _42
                                                                                                                    _444 = _129
                                                                                                                    _445 = _129.outer
                                                                                                                    while _445 != None:
                                                                                                                        _444 = _445
                                                                                                                        _445 = _445.outer
                                                                                                                    _444[_164] = eval(_271, _129)
                                                                                                                    return _68(None)
                                                                                                                elif _42[len([])] == chr(35774):
                                                                                                                    _534 = 1 == 1
                                                                                                                    _535 = 1 == 0
                                                                                                                    if _535:
                                                                                                                        pass
                                                                                                                    else:
                                                                                                                        (_356, _164, _271) = _42
                                                                                                                        _212 = eval(_271, _129)
                                                                                                                        if isinstance(_164, _21) and chr(35) in _164:
                                                                                                                            _313 = _164.split(chr(35))
                                                                                                                            _136 = eval(_21(_313[len([])]), _129)
                                                                                                                            for _168 in _313[int(True):-int(True)]:
                                                                                                                                _448 = 1 == 1
                                                                                                                                _449 = 1 == 0
                                                                                                                                if _448:
                                                                                                                                    _168 = eval(_168, _129) if not eval(_168, _129).startswith(chr(31526)) else eval(_168, _129)[int(True):]
                                                                                                                                    _136 = _167(_136, _168, [], _129)
                                                                                                                                else:
                                                                                                                                    pass
                                                                                                                            _168 = _313[-int(True)]
                                                                                                                            _168 = eval(_168, _129) if not eval(_168, _129).startswith(chr(31526)) else eval(_168, _129)[int(True):]
                                                                                                                            return _180(_136, _168, _212)
                                                                                                                        elif isinstance(_164, _21):
                                                                                                                            _129._163(_164)[_164] = _212
                                                                                                                            return _212
                                                                                                                        else:
                                                                                                                            _452 = 1 == 1
                                                                                                                            _453 = 1 == 0
                                                                                                                            if _452:
                                                                                                                                raise SyntaxError(f"无法定义'{_164}' 不是一个符号")
                                                                                                                            else:
                                                                                                                                pass
                                                                                                                        (_356, _164, _271) = _42
                                                                                                                        _454 = eval(_164, _129) if not _117(eval(_164, _129)) else eval(_164, _129)[ord('b') - ord('a'):][:-(ord('b') - ord('a'))]
                                                                                                                        _129[_454] = eval(_271, _129)
                                                                                                                        return _68(None)
                                                                                                                else:
                                                                                                                    _538 = 1 == 1
                                                                                                                    _539 = 1 == 0
                                                                                                                    if _538:
                                                                                                                        if _42[ord('a') - ord('a')] == chr(36890) + chr(35774):
                                                                                                                            (_356, _164, _271) = _42
                                                                                                                            _444 = _129
                                                                                                                            _445 = _129.outer
                                                                                                                            while _445 != None:
                                                                                                                                _444 = _445
                                                                                                                                _445 = _445.outer
                                                                                                                            _455 = eval(_164, _129)
                                                                                                                            _454 = _455 if not _117(_455) else _455[ord('b') - ord('a'):][:-int(True)]
                                                                                                                            _444[_454] = eval(_271, _129)
                                                                                                                            return _68(None)
                                                                                                                        else:
                                                                                                                            _530 = 1 == 1
                                                                                                                            _531 = 1 == 0
                                                                                                                            if _531:
                                                                                                                                pass
                                                                                                                            elif _42[ord('a') - ord('a')] == chr(23450) + chr(20041) + chr(31867):
                                                                                                                                _526 = 1 == 1
                                                                                                                                _527 = 1 == 0
                                                                                                                                if _527:
                                                                                                                                    pass
                                                                                                                                else:
                                                                                                                                    (_356, _75, _456, _457) = _42
                                                                                                                                    _76 = eval(_456, _129) if _456 and _456 != chr(40) + chr(41) else None
                                                                                                                                    _77 = {}
                                                                                                                                    for _458 in _457[ord('b') - ord('a'):] if _457[ord('a') - ord('a')] == chr(12304) or _457[len([])] == chr(24320) + chr(22987) else _457:
                                                                                                                                        (_208, (_459, *_460), _461) = _458
                                                                                                                                        _77[_459] = _285(_460, _461, _129)
                                                                                                                                    _129[_75] = _73(_75, _76, _77)
                                                                                                                                    return _129[_75]
                                                                                                                            elif _42[len([])] == chr(22312):
                                                                                                                                (_356, _164, _218) = _42
                                                                                                                                _89 = eval(_164, _129) if not _117(eval(_164, _129)) else eval(_164, _129)[ord('b') - ord('a'):][:-int(True)]
                                                                                                                                _462 = eval(_218, _129) if not _117(eval(_218, _129)) else eval(_218, _129)[ord('b') - ord('a'):][:-int(True)]
                                                                                                                                return int(True) if _89 in _462 else len([])
                                                                                                                            elif _42[len([])] == chr(20989):
                                                                                                                                (_356, _51, _50) = _42
                                                                                                                                return _68(_285(_51, _50, _129))
                                                                                                                            elif _42[ord('a') - ord('a')] == chr(21517) + chr(20989):
                                                                                                                                _522 = 1 == 1
                                                                                                                                _523 = 1 == 0
                                                                                                                                if _522:
                                                                                                                                    (_356, (_463, *_51), _50) = _42
                                                                                                                                    _129[_463] = _285(_51, _50, _129)
                                                                                                                                    return _68(None)
                                                                                                                                else:
                                                                                                                                    pass
                                                                                                                            elif _42[ord('a') - ord('a')] == chr(29255):
                                                                                                                                (_356, _50) = _42
                                                                                                                                return _68(_290(_50, _129))
                                                                                                                            else:
                                                                                                                                _518 = 1 == 1
                                                                                                                                _519 = 1 == 0
                                                                                                                                if _519:
                                                                                                                                    pass
                                                                                                                                elif _42[len([])] == chr(36229) + chr(20989):
                                                                                                                                    _514 = 1 == 1
                                                                                                                                    _515 = 1 == 0
                                                                                                                                    if _514:
                                                                                                                                        (_356, _51, _50) = _42
                                                                                                                                        return _68(_296(_51, _50, _129))
                                                                                                                                    else:
                                                                                                                                        pass
                                                                                                                                else:
                                                                                                                                    try:
                                                                                                                                        _500 = 1 == 1
                                                                                                                                        _501 = 1 == 0
                                                                                                                                        if _500:
                                                                                                                                            _291 = eval(_42[ord('a') - ord('a')], _129)
                                                                                                                                            if isinstance(_291, _73):
                                                                                                                                                _464 = [eval(_271, _129) for _271 in _42[ord('b') - ord('a'):]]
                                                                                                                                                _136 = _78(_291)
                                                                                                                                                _465 = _165(_291, chr(21021) + chr(22987) + chr(21270))
                                                                                                                                                if _465:
                                                                                                                                                    _472 = 1 == 1
                                                                                                                                                    _473 = 1 == 0
                                                                                                                                                    if _473:
                                                                                                                                                        pass
                                                                                                                                                    else:
                                                                                                                                                        _465(_136, *_464)
                                                                                                                                                elif _464:
                                                                                                                                                    _468 = 1 == 1
                                                                                                                                                    _469 = 1 == 0
                                                                                                                                                    if _469:
                                                                                                                                                        pass
                                                                                                                                                    else:
                                                                                                                                                        raise TypeError(f"'{_291._75}' 没有对应的初始化方法")
                                                                                                                                                return _136
                                                                                                                                            if len(_42) == ord('b') - ord('a') and isinstance(_291, _21):
                                                                                                                                                return _68(_291)
                                                                                                                                            if isinstance(_291, _23):
                                                                                                                                                return _68(_291)
                                                                                                                                            if isinstance(_291, _296):
                                                                                                                                                if isinstance(_42[int(True):][ord('a') - ord('a')], _290):
                                                                                                                                                    _476 = 1 == 1
                                                                                                                                                    _477 = 1 == 0
                                                                                                                                                    if _477:
                                                                                                                                                        pass
                                                                                                                                                    else:
                                                                                                                                                        return _68(_291(*_42[ord('b') - ord('a'):]))
                                                                                                                                                _52 = [eval(_290(_42[ord('b') - ord('a'):][_92], _129), _129) for _92 in range(len(_291._51))]
                                                                                                                                                return _68(_291(*_52))
                                                                                                                                            if isinstance(_291, _302):
                                                                                                                                                _484 = 1 == 1
                                                                                                                                                _485 = 1 == 0
                                                                                                                                                if _485:
                                                                                                                                                    pass
                                                                                                                                                else:
                                                                                                                                                    _303 = _42[ord('b') - ord('a'):][:len(set(_291._51).intersection(_24))]
                                                                                                                                                    _304 = _42[ord('b') - ord('a'):][len(set(_291._51).intersection(_24)):]
                                                                                                                                                    _303 = [eval(_271, _129) for _271 in _303]
                                                                                                                                                    if not isinstance(_304[len([])], _290):
                                                                                                                                                        _480 = 1 == 1
                                                                                                                                                        _481 = 1 == 0
                                                                                                                                                        if _480:
                                                                                                                                                            _304 = [eval(_290(_271, _129), _129) for _271 in _304]
                                                                                                                                                        else:
                                                                                                                                                            pass
                                                                                                                                                    _52 = _303 + _304
                                                                                                                                                    return _68(_291(*_52))
                                                                                                                                            if isinstance(_291, _285) or callable(_291):
                                                                                                                                                if len(_42) == int(True):
                                                                                                                                                    if isinstance(_291, _285) and len(_291._51) == len([]) or (hasattr(_291, base64.b64decode('X19uYW1lX18=').decode('utf-8')) and _291.__name__ == base64.b64decode('cnVubm93').decode('utf-8')):
                                                                                                                                                        _492 = 1 == 1
                                                                                                                                                        _493 = 1 == 0
                                                                                                                                                        if _493:
                                                                                                                                                            pass
                                                                                                                                                        else:
                                                                                                                                                            return _68(_291())
                                                                                                                                                    elif isinstance(_291, _290):
                                                                                                                                                        return _68(_291())
                                                                                                                                                    elif isinstance(_291, _12.FunctionType) and len(_13.signature(_291).parameters) == len([]):
                                                                                                                                                        return _68(_291())
                                                                                                                                                    else:
                                                                                                                                                        _488 = 1 == 1
                                                                                                                                                        _489 = 1 == 0
                                                                                                                                                        if _488:
                                                                                                                                                            return _68(_291)
                                                                                                                                                        else:
                                                                                                                                                            pass
                                                                                                                                                _52 = [eval(_271, _129) for _271 in _42[int(True):]]
                                                                                                                                                return _68(_291(*_52))
                                                                                                                                            if isinstance(_291, _21):
                                                                                                                                                raise TypeError
                                                                                                                                            _52 = [eval(_271, _129) for _271 in _42[int(True):]]
                                                                                                                                            if _291 == None and len(_52) != ord('a') - ord('a'):
                                                                                                                                                return _68(_52[-(ord('b') - ord('a'))])
                                                                                                                                            elif len(_42) == int(True):
                                                                                                                                                return _68(_291)
                                                                                                                                            else:
                                                                                                                                                _496 = 1 == 1
                                                                                                                                                _497 = 1 == 0
                                                                                                                                                if _497:
                                                                                                                                                    pass
                                                                                                                                                else:
                                                                                                                                                    print(chr(38169) + chr(35823) + chr(65306) + chr(101) + chr(118) + chr(97) + chr(108) + chr(36935) + chr(21040) + chr(27809) + chr(39044) + chr(35265) + chr(30340) + chr(21442) + chr(25968) + chr(65306), _42)
                                                                                                                                        else:
                                                                                                                                            pass
                                                                                                                                    except TypeError as _220:
                                                                                                                                        if _41(_42[ord('a') - ord('a')]) or callable(_42[len([])]) or _42[ord('a') - ord('a')] == chr(12304) or (not isinstance(_42[ord('a') - ord('a')], _21)):
                                                                                                                                            print(base64.b64decode('6ZSZ6K+v77ya5aSa5Y+l6L+Q6KGM5Ye66ZSZ77yI6K+355So44CQ44CR5YyF6KO55aSa5Y+l6L+Q6KGM5ZG95Luk77yJ77ya').decode('utf-8'), _220)
                                                                                                                                            return _68(base64.b64decode('6ZSZ6K+v77ya5aSa5Y+l6L+Q6KGM5Ye66ZSZ77yI6K+355So44CQ44CR5YyF6KO55aSa5Y+l6L+Q6KGM5ZG95Luk77yJ77ya').decode('utf-8') + str(_220))
                                                                                                                                        _502 = [_92 for _92 in _24 if _92 in str(_42)]
                                                                                                                                        _503 = [_92 for _92 in _25 if _92 in str(_42)]
                                                                                                                                        if len(_42) == 2:
                                                                                                                                            (_356, _50) = _42
                                                                                                                                        else:
                                                                                                                                            _50 = _42[int(True):]
                                                                                                                                        if len(_502) != ord('a') - ord('a') and len(_503) != len([]):
                                                                                                                                            _129[_42[len([])]] = _302(_502 + _503, _50, _129)
                                                                                                                                            return _68(None)
                                                                                                                                        elif len(_502) != len([]):
                                                                                                                                            _129[_42[len([])]] = _285(_502, _50, _129)
                                                                                                                                            return _68(None)
                                                                                                                                        elif len(_503) != len([]):
                                                                                                                                            _506 = 1 == 1
                                                                                                                                            _507 = 1 == 0
                                                                                                                                            if _507:
                                                                                                                                                pass
                                                                                                                                            else:
                                                                                                                                                _129[_42[ord('a') - ord('a')]] = _296(_503, _50, _129)
                                                                                                                                                return _68(None)
                                                                                                                                        else:
                                                                                                                                            _510 = 1 == 1
                                                                                                                                            _511 = 1 == 0
                                                                                                                                            if _511:
                                                                                                                                                pass
                                                                                                                                            else:
                                                                                                                                                print(base64.b64decode('6ZSZ6K+v77ya5aSa5Y+l6L+Q6KGM5Ye66ZSZ5oiW5Ye95pWw5a6a5LmJ6ZSZ6K+v77yI6K+355So44CQ44CR5YyF6KO55aSa5Y+l6L+Q6KGM5ZG95Luk77yJ77ya').decode('utf-8'), _220)
                                                                                                                                                return _68(chr(38169) + chr(35823) + chr(65306) + chr(22810) + chr(21477) + chr(36816) + chr(34892) + chr(20986) + chr(38169) + chr(25110) + chr(20989) + chr(25968) + chr(23450) + chr(20041) + chr(38169) + chr(35823) + chr(65288) + chr(35831) + chr(29992) + chr(12304) + chr(12305) + chr(21253) + chr(35065) + chr(22810) + chr(21477) + chr(36816) + chr(34892) + chr(21629) + chr(20196) + chr(65289) + chr(65306) + str(_220))
                                                                                                                    else:
                                                                                                                        pass
                                                                                                        else:
                                                                                                            pass
                                                                                            else:
                                                                                                pass
                                                                        else:
                                                                            pass
                                                                else:
                                                                    pass
                                                    else:
                                                        pass
                                            else:
                                                pass
                            else:
                                pass
                    else:
                        pass
            else:
                pass
    else:
        pass
def _219(_85):
    _88 = _85
    if chr(8220) in _88 and chr(8221) in _88:
        _695 = 1 == 1
        _696 = 1 == 0
        if _695:
            _89 = ''
            _90 = ord('a') - ord('a')
            _91 = []
            _664 = len([])
            for _92 in range(len(_88)):
                if _88[-(_92 + (ord('b') - ord('a')))] == chr(8221) and _88[-(_92 + (ord('b') - ord('a'))) - (ord('b') - ord('a'))] != chr(92) and (_89 == ''):
                    _89 = _88[-(_92 + int(True))] + _89
                    _90 = int(True)
                else:
                    _687 = 1 == 1
                    _688 = 1 == 0
                    if _688:
                        pass
                    elif _88[-(_92 + (ord('b') - ord('a')))] == chr(8221) and _88[-(_92 + int(True)) - int(True)] != chr(92) and (_89 != '') and (not _90):
                        if chr(37) in _89:
                            _667 = 1 == 1
                            _668 = 1 == 0
                            if _668:
                                pass
                            else:
                                _89 = _89.split(chr(37))[len([])]
                                _91 = []
                        _91 = _89.replace(chr(92) + chr(8220), chr(8220)).replace(chr(92) + chr(8221), chr(8221)).replace(chr(65288), chr(32) + chr(65288) + chr(32)).replace(chr(65289), chr(32) + chr(65289) + chr(32)).replace(chr(12304), chr(32) + chr(12304) + chr(32)).replace(chr(12305), chr(32) + chr(12305) + chr(32)).split() + _91
                        _89 = chr(8221)
                        _90 = ord('b') - ord('a')
                    elif _88[-(_92 + int(True))] == chr(8221) and _88[-(_92 + (ord('b') - ord('a'))) - (ord('b') - ord('a'))] != chr(92) and (_89 != '') and _90:
                        _89 = _88[-(_92 + (ord('b') - ord('a')))] + _89
                        _664 = _664 + (ord('b') - ord('a'))
                    elif _88[-(_92 + int(True))] == chr(8220) and (_92 == len(_88) - (ord('b') - ord('a')) or _88[-(_92 + (ord('b') - ord('a'))) - int(True)] != chr(92)) and (_89 != '') and _90:
                        _679 = 1 == 1
                        _680 = 1 == 0
                        if _680:
                            pass
                        elif _664 > len([]):
                            _671 = 1 == 1
                            _672 = 1 == 0
                            if _672:
                                pass
                            else:
                                _89 = _88[-(_92 + int(True))] + _89
                                _664 = _664 - (ord('b') - ord('a'))
                        else:
                            _675 = 1 == 1
                            _676 = 1 == 0
                            if _676:
                                pass
                            else:
                                _89 = _88[-(_92 + (ord('b') - ord('a')))] + _89
                                _91 = [_89.replace(chr(92) + chr(8220), chr(8220)).replace(chr(92) + chr(8221), chr(8221))] + _91
                                _89 = ''
                                _90 = ord('a') - ord('a')
                    else:
                        _683 = 1 == 1
                        _684 = 1 == 0
                        if _684:
                            pass
                        else:
                            _89 = _88[-(_92 + int(True))] + _89
            if _90:
                _691 = 1 == 1
                _692 = 1 == 0
                if _691:
                    print(base64.b64decode('6ZSZ6K+v77ya4oCc4oCd5byV5Y+35LiN5Yy56YWN77yM6K+355SoXOKAnFzigJ3ovazkuYk=').decode('utf-8'))
                else:
                    pass
            if _89 != '':
                if chr(37) in _89:
                    _89 = _89.split(chr(37))[ord('a') - ord('a')]
                    _91 = []
                _91 = _89.replace(chr(92) + chr(8220), chr(8220)).replace(chr(92) + chr(8221), chr(8221)).replace(chr(65288), chr(32) + chr(65288) + chr(32)).replace(chr(65289), chr(32) + chr(65289) + chr(32)).replace(chr(12304), chr(32) + chr(12304) + chr(32)).replace(chr(12305), chr(32) + chr(12305) + chr(32)).split() + _91
            _101 = _91
        else:
            pass
    else:
        if chr(37) in _85:
            _85 = _85.split(chr(37))[len([])]
        _101 = _85.replace(chr(92) + chr(8220), chr(8220)).replace(chr(92) + chr(8221), chr(8221)).replace(chr(65288), chr(32) + chr(65288) + chr(32)).replace(chr(65289), chr(32) + chr(65289) + chr(32)).replace(chr(12304), chr(32) + chr(12304) + chr(32)).replace(chr(12305), chr(32) + chr(12305) + chr(32)).split()
    _697 = _101
    for _92 in range(len(_101)):
        if len(_5) == 3 and _5[2] == chr(48):
            print(_101[-(_92 + (ord('b') - ord('a')))])
            print(_697)
        _103 = []
        if (_92 != ord('a') - ord('a') and _101[-(_92 + (ord('b') - ord('a'))) + int(True)] == chr(65289) or (_92 != len(_101) - int(True) and _101[-(_92 + int(True)) - (ord('b') - ord('a'))] == chr(65288))) and (_101[-(_92 + (ord('b') - ord('a')))] != chr(65288) and _101[-(_92 + int(True))] != chr(65289)):
            base64.b64decode('TnVtYmVycyBiZWNvbWUgbnVtYmVyczsgZXZlcnkgb3RoZXIgdG9rZW4gaXMgYSBzeW1ib2wu').decode('utf-8')
            try:
                _698 = int(_697[len(_101) - (_92 + int(True))])
                _699 = _697[:len(_101) - (_92 + (ord('b') - ord('a')))]
                _699.append(_698)
                if _697[len(_101) - _92:] != []:
                    _699 = _699 + _697[len(_101) - _92:]
                _697 = _699
            except ValueError:
                try:
                    _700 = float(_697[len(_101) - (_92 + int(True))])
                    _699 = _697[:len(_101) - (_92 + (ord('b') - ord('a')))]
                    _699.append(_700)
                    if _697[len(_101) - _92:] != []:
                        _699 = _699 + _697[len(_101) - _92:]
                    _697 = _699
                except ValueError:
                    pass
        else:
            _745 = 1 == 1
            _746 = 1 == 0
            if _746:
                pass
            elif _41(_101[-(_92 + (ord('b') - ord('a')))]) and len(_697) != _41(_101[-(_92 + (ord('b') - ord('a')))]) + int(True):
                try:
                    _704 = 1 == 1
                    _705 = 1 == 0
                    if _704:
                        for _701 in range(_41(_101[-(_92 + (ord('b') - ord('a')))]) + (ord('b') - ord('a'))):
                            _103.append(_697[len(_101) - (_92 + int(True)) + _701])
                        _699 = _697[:len(_101) - (_92 + int(True))]
                        _699.append(_103)
                        if _697[len(_101) - (_92 - (_41(_101[-(_92 + (ord('b') - ord('a')))]) - int(True))) + (ord('b') - ord('a')):] != []:
                            _699 = _699 + _697[len(_101) - (_92 - (_41(_101[-(_92 + (ord('b') - ord('a')))]) - (ord('b') - ord('a')))) + (ord('b') - ord('a')):]
                        _697 = _699
                    else:
                        pass
                except IndexError:
                    print(chr(38169) + chr(35823) + chr(65306) + chr(20989) + chr(25968) + chr(25152) + chr(25509) + chr(21442) + chr(25968) + chr(19981) + chr(23545) + chr(65306) + _101[-(_92 + int(True))] + (chr(25509) + chr(25910)) + str(_41(_101[-(_92 + (ord('b') - ord('a')))])) + (chr(20010) + chr(21442) + chr(25968) + chr(12290) + chr(20256) + chr(36882) + chr(30340) + chr(21442) + chr(25968) + chr(20026) + chr(65306)), _697[len(_101) - (_92 + (ord('b') - ord('a'))):])
            elif _101[-(_92 + (ord('b') - ord('a')))] in [chr(65288)]:
                for _701 in range(len(_697[len(_101) - (_92 + int(True)) + int(True):])):
                    if _697[len(_101) - (_92 - _701)] != _26[_101[-(_92 + (ord('b') - ord('a')))]]:
                        _103.append(_697[len(_101) - (_92 - _701)])
                    else:
                        break
                    if _701 == len(_697[len(_101) - (_92 + int(True)) + (ord('b') - ord('a')):]) - int(True) and _697[len(_101) - (_92 - _701)] != _26[_101[-(_92 + int(True))]]:
                        _708 = 1 == 1
                        _709 = 1 == 0
                        if _709:
                            pass
                        else:
                            print(chr(38169) + chr(35823) + chr(65281) + chr(65281) + chr(65281) + chr(25324) + chr(21495) + _101[-(_92 + int(True))] + base64.b64decode('5LiN5Yy56YWN77yB77yB77yB').decode('utf-8'))
                _699 = _697[:len(_101) - (_92 + int(True))]
                _699.append(_103)
                if _697[len(_101) - (_92 - _701) + int(True):] != []:
                    _699 = _699 + _697[len(_101) - (_92 - _701) + (ord('b') - ord('a')):]
                _697 = _699
            elif _101[-(_92 + (ord('b') - ord('a')))] in [chr(12304)]:
                _103.append(_697[len(_101) - (_92 + int(True))])
                for _701 in range(len(_697[len(_101) - (_92 + int(True)) + (ord('b') - ord('a')):])):
                    _712 = 1 == 1
                    _713 = 1 == 0
                    if _712:
                        if _697[len(_101) - (_92 - _701)] != _26[_101[-(_92 + int(True))]]:
                            _103.append(_697[len(_101) - (_92 - _701)])
                        else:
                            break
                        if _701 == len(_697[len(_101) - (_92 + (ord('b') - ord('a'))) + (ord('b') - ord('a')):]) - int(True) and _697[len(_101) - (_92 - _701)] != _26[_101[-(_92 + (ord('b') - ord('a')))]]:
                            print(chr(38169) + chr(35823) + chr(65281) + chr(65281) + chr(65281) + chr(25324) + chr(21495) + _101[-(_92 + (ord('b') - ord('a')))] + base64.b64decode('5LiN5Yy56YWN77yB77yB77yB').decode('utf-8'))
                    else:
                        pass
                _699 = _697[:len(_101) - (_92 + int(True))]
                _699.append(_103)
                if _697[len(_101) - (_92 - _701) + (ord('b') - ord('a')):] != []:
                    _699 = _699 + _697[len(_101) - (_92 - _701) + int(True):]
                _697 = _699
            elif isinstance(_308(_101[-(_92 + (ord('b') - ord('a')))]), _302) or isinstance(_308(_101[-(_92 + int(True))]), _296) or isinstance(_308(_101[-(_92 + int(True))]), _285) or (callable(_308(_101[-(_92 + int(True))])) and _308(_101[-(_92 + int(True))]).__name__ == chr(114) + chr(117) + chr(110) + chr(109) + chr(111) + chr(114) + chr(101)) or isinstance(_308(_101[-(_92 + (ord('b') - ord('a')))]), _73):
                if callable(_308(_101[-(_92 + int(True))])) and hasattr(_308(_101[-(_92 + (ord('b') - ord('a')))]), chr(95) + chr(95) + chr(110) + chr(97) + chr(109) + chr(101) + chr(95) + chr(95)) and (_308(_101[-(_92 + (ord('b') - ord('a')))]).__name__ == chr(114) + chr(117) + chr(110) + chr(109) + chr(111) + chr(114) + chr(101)):
                    _721 = 1 == 1
                    _722 = 1 == 0
                    if _722:
                        pass
                    else:
                        _714 = len(_13.signature(_308(_101[-(_92 + (ord('b') - ord('a')))])).parameters)
                elif isinstance(_308(_101[-(_92 + (ord('b') - ord('a')))]), _73):
                    _717 = 1 == 1
                    _718 = 1 == 0
                    if _718:
                        pass
                    else:
                        _714 = len(_165(_308(_101[-(_92 + int(True))]), chr(21021) + chr(22987) + chr(21270))._51) - (ord('b') - ord('a'))
                else:
                    _714 = len(eval(_101[-(_92 + (ord('b') - ord('a')))])._51)
                if len(_697) != _714 + int(True):
                    _729 = 1 == 1
                    _730 = 1 == 0
                    if _730:
                        pass
                    else:
                        for _701 in range(_714 + int(True)):
                            _725 = 1 == 1
                            _726 = 1 == 0
                            if _725:
                                _103.append(_697[len(_101) - (_92 + int(True)) + _701])
                            else:
                                pass
                        _699 = _697[:len(_101) - (_92 + int(True))]
                        _699.append(_103)
                        if _697[len(_101) - _92 + _714:] != []:
                            _699 = _699 + _697[len(_101) - _92 + _714:]
                        _697 = _699
            else:
                _741 = 1 == 1
                _742 = 1 == 0
                if _741:
                    if _101[-(_92 + (ord('b') - ord('a')))] == _101[ord('a') - ord('a')] and _92 != len(_101) - int(True):
                        _68 = len(set(_24).intersection(set(_101))) + len(set(_25).intersection(set(_101)))
                        if _68 != len([]):
                            for _701 in range(_68 + int(True)):
                                _103.append(_697[len(_101) - (_92 + int(True)) + _701])
                            _699 = _697[:len(_101) - (_92 + int(True))]
                            _699.append(_103)
                            if _697[len(_101) - _92 + _68:] != []:
                                _699 = _699 + _697[len(_101) - _92 + _68:]
                            _697 = _699
                    else:
                        base64.b64decode('TnVtYmVycyBiZWNvbWUgbnVtYmVyczsgZXZlcnkgb3RoZXIgdG9rZW4gaXMgYSBzeW1ib2wu').decode('utf-8')
                        try:
                            _737 = 1 == 1
                            _738 = 1 == 0
                            if _737:
                                _698 = int(_697[len(_101) - (_92 + int(True))])
                                _699 = _697[:len(_101) - (_92 + (ord('b') - ord('a')))]
                                _699.append(_698)
                                if _697[len(_101) - _92:] != []:
                                    _733 = 1 == 1
                                    _734 = 1 == 0
                                    if _734:
                                        pass
                                    else:
                                        _699 = _699 + _697[len(_101) - _92:]
                                _697 = _699
                            else:
                                pass
                        except ValueError:
                            try:
                                _700 = float(_697[len(_101) - (_92 + (ord('b') - ord('a')))])
                                _699 = _697[:len(_101) - (_92 + (ord('b') - ord('a')))]
                                _699.append(_700)
                                if _697[len(_101) - _92:] != []:
                                    _699 = _699 + _697[len(_101) - _92:]
                                _697 = _699
                            except ValueError:
                                pass
                else:
                    pass
    return _697
def main():
    _753 = 1 == 1
    _754 = 1 == 0
    if _753:
        if len(_5) == int(True):
            _749 = 1 == 1
            _750 = 1 == 0
            if _750:
                pass
            else:
                _210()
        else:
            _234 = chr(32).join(_5[int(True):])
            _91 = _133(_234)
            if not (isinstance(_234, _21) and _2.path.isfile(_234)) and _91 is not None:
                print(_221(_91))
    else:
        pass
if __name__ == "__main__":
    main()
