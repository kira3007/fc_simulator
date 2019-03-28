def order_code():
    code = {
        0x00: ('BRK', 'IMP'),
        0x01: ('ORA', 'INX'),
        0x02: ('KIL', 'IMP'),
        0x03: ('SLO', 'INX'),
        0x04: ('NOP', 'ZPG'),
        0x05: ('ORA', 'ZPG'),
        0x06: ('ASL', 'ZPG'),
        0x07: ('SLO', 'ZPG'),
        0x08: ('PHP', 'IMP'),
        0x09: ('ORA', 'IMM'),
        0x0A: ('ASL', 'IMP'),
        0x0B: ('ANC', 'IMM'),
        0x0C: ('NOP', 'ABS'),
        0x0D: ('ORA', 'ABS'),
        0x0E: ('ASL', 'ABS'),
        0x0F: ('SLO', 'ABS'),
        0x10: ('BPL', 'REL'),
        0x11: ('ORA', 'INY'),
        0x12: ('KIL', 'IMP'),
        0x13: ('SLO', 'INY'),
        0x14: ('NOP', 'ZPX'),
        0x15: ('ORA', 'ZPX'),
        0x16: ('ASL', 'ZPX'),
        0x17: ('SLO', 'ZPX'),
        0x18: ('CLC', 'IMP'),
        0x19: ('ORA', 'ABY'),
        0x1A: ('NOP', 'IMP'),
        0x1B: ('SLO', 'ABY'),
        0x1C: ('NOP', 'ABX'),
        0x1D: ('ORA', 'ABX'),
        0x1E: ('ASL', 'ABX'),
        0x1F: ('SLO', 'ABX'),
        0x20: ('JSR', 'ABS'),
        0x21: ('AND', 'INX'),
        0x22: ('KIL', 'IMP'),
        0x23: ('RLA', 'INX'),
        0x24: ('BIT', 'ZPG'),
        0x25: ('AND', 'ZPG'),
        0x26: ('ROL', 'ZPG'),
        0x27: ('RLA', 'ZPG'),
        0x28: ('PLP', 'IMP'),
        0x29: ('AND', 'IMM'),
        0x2A: ('ROL', 'IMP'),
        0x2B: ('ANC', 'IMM'),
        0x2C: ('BIT', 'ABS'),
        0x2D: ('AND', 'ABS'),
        0x2E: ('ROL', 'ABS'),
        0x2F: ('RLA', 'ABS'),
        0x30: ('BMI', 'REL'),
        0x31: ('AND', 'INY'),
        0x32: ('KIL', 'IMP'),
        0x33: ('RLA', 'INY'),
        0x34: ('NOP', 'ZPX'),
        0x35: ('AND', 'ZPX'),
        0x36: ('ROL', 'ZPX'),
        0x37: ('RLA', 'ZPX'),
        0x38: ('SEC', 'IMP'),
        0x39: ('AND', 'ABY'),
        0x3A: ('NOP', 'IMP'),
        0x3B: ('RLA', 'ABY'),
        0x3C: ('NOP', 'ABX'),
        0x3D: ('AND', 'ABX'),
        0x3E: ('ROL', 'ABX'),
        0x3F: ('RLA', 'ABX'),
        0x40: ('RTI', 'IMP'),
        0x41: ('EOR', 'INX'),
        0x42: ('KIL', 'IMP'),
        0x43: ('SRE', 'INX'),
        0x44: ('NOP', 'ZPG'),
        0x45: ('EOR', 'ZPG'),
        0x46: ('LSR', 'ZPG'),
        0x47: ('SRE', 'ZPG'),
        0x48: ('PHA', 'IMP'),
        0x49: ('EOR', 'IMM'),
        0x4A: ('LSR', 'IMP'),
        0x4B: ('ASR', 'IMM'),
        0x4C: ('JMP', 'ABS'),
        0x4D: ('EOR', 'ABS'),
        0x4E: ('LSR', 'ABS'),
        0x4F: ('SRE', 'ABS'),
        0x50: ('BVC', 'REL'),
        0x51: ('EOR', 'INY'),
        0x52: ('KIL', 'IMP'),
        0x53: ('SRE', 'INY'),
        0x54: ('NOP', 'ZPX'),
        0x55: ('EOR', 'ZPX'),
        0x56: ('LSR', 'ZPX'),
        0x57: ('SRE', 'ZPX'),
        0x58: ('CLI', 'IMP'),
        0x59: ('EOR', 'ABY'),
        0x5A: ('NOP', 'IMP'),
        0x5B: ('SRE', 'ABY'),
        0x5C: ('NOP', 'ABX'),
        0x5D: ('EOR', 'ABX'),
        0x5E: ('LSR', 'ABX'),
        0x5F: ('SRE', 'ABX'),
        0x60: ('RTS', 'IMP'),
        0x61: ('ADC', 'INX'),
        0x62: ('KIL', 'IMP'),
        0x63: ('RRA', 'INX'),
        0x64: ('NOP', 'ZPG'),
        0x65: ('ADC', 'ZPG'),
        0x66: ('ROR', 'ZPG'),
        0x67: ('RRA', 'ZPG'),
        0x68: ('PLA', 'IMP'),
        0x69: ('ADC', 'IMM'),
        0x6A: ('ROR', 'IMP'),
        0x6B: ('ARR', 'IMM'),
        0x6C: ('JMP', 'IND'),
        0x6D: ('ADC', 'ABS'),
        0x6E: ('ROR', 'ABS'),
        0x6F: ('RRA', 'ABS'),
        0x70: ('BVS', 'REL'),
        0x71: ('ADC', 'INY'),
        0x72: ('KIL', 'IMP'),
        0x73: ('RRA', 'INY'),
        0x74: ('NOP', 'ZPX'),
        0x75: ('ADC', 'ZPX'),
        0x76: ('ROR', 'ZPX'),
        0x77: ('RRA', 'ZPX'),
        0x78: ('SEI', 'IMP'),
        0x79: ('ADC', 'ABY'),
        0x7A: ('NOP', 'IMP'),
        0x7B: ('RRA', 'ABY'),
        0x7C: ('NOP', 'ABX'),
        0x7D: ('ADC', 'ABX'),
        0x7E: ('ROR', 'ABX'),
        0x7F: ('RRA', 'ABX'),
        0x80: ('NOP', 'IMM'),
        0x81: ('STA', 'INX'),
        0x82: ('NOP', 'IMM'),
        0x83: ('SAX', 'INX'),
        0x84: ('STY', 'ZPG'),
        0x85: ('STA', 'ZPG'),
        0x86: ('STX', 'ZPG'),
        0x87: ('SAX', 'ZPG'),
        0x88: ('DEY', 'IMP'),
        0x89: ('NOP', 'IMM'),
        0x8A: ('TXA', 'IMP'),
        0x8B: ('XAA', 'IMM'),
        0x8C: ('STY', 'ABS'),
        0x8D: ('STA', 'ABS'),
        0x8E: ('STX', 'ABS'),
        0x8F: ('SAX', 'ABS'),
        0x90: ('BCC', 'REL'),
        0x91: ('STA', 'INY'),
        0x92: ('KIL', 'IMP'),
        0x93: ('AHX', 'INY'),
        0x94: ('STY', 'ZPX'),
        0x95: ('STA', 'ZPX'),
        0x96: ('STX', 'ZPY'),
        0x97: ('SAX', 'ZPY'),
        0x98: ('TYA', 'IMP'),
        0x99: ('STA', 'ABY'),
        0x9A: ('TXS', 'IMP'),
        0x9B: ('TAS', 'ABY'),
        0x9C: ('SHY', 'ABX'),
        0x9D: ('STA', 'ABX'),
        0x9E: ('SHX', 'ABY'),
        0x9F: ('AHX', 'ABY'),
        0xA0: ('LDY', 'IMM'),
        0xA1: ('LDA', 'INX'),
        0xA2: ('LDX', 'IMM'),
        0xA3: ('LAX', 'INX'),
        0xA4: ('LDY', 'ZPG'),
        0xA5: ('LDA', 'ZPG'),
        0xA6: ('LDX', 'ZPG'),
        0xA7: ('LAX', 'ZPG'),
        0xA8: ('TAY', 'IMP'),
        0xA9: ('LDA', 'IMM'),
        0xAA: ('TAX', 'IMP'),
        0xAB: ('LAX', 'IMM'),
        0xAC: ('LDY', 'ABS'),
        0xAD: ('LDA', 'ABS'),
        0xAE: ('LDX', 'ABS'),
        0xAF: ('LAX', 'ABS'),
        0xB0: ('BCS', 'REL'),
        0xB1: ('LDA', 'INY'),
        0xB2: ('KIL', 'IMP'),
        0xB3: ('LAX', 'INY'),
        0xB4: ('LDY', 'ZPX'),
        0xB5: ('LDA', 'ZPX'),
        0xB6: ('LDX', 'ZPY'),
        0xB7: ('LAX', 'ZPY'),
        0xB8: ('CLV', 'IMP'),
        0xB9: ('LDA', 'ABY'),
        0xBA: ('TSX', 'IMP'),
        0xBB: ('LAS', 'ABY'),
        0xBC: ('LDY', 'ABX'),
        0xBD: ('LDA', 'ABX'),
        0xBE: ('LDX', 'ABY'),
        0xBF: ('LAX', 'ABY'),
        0xC0: ('CPY', 'IMM'),
        0xC1: ('CMP', 'INX'),
        0xC2: ('NOP', 'IMM'),
        0xC3: ('DCP', 'INX'),
        0xC4: ('CPY', 'ZPG'),
        0xC5: ('CMP', 'ZPG'),
        0xC6: ('DEC', 'ZPG'),
        0xC7: ('DCP', 'ZPG'),
        0xC8: ('INY', 'IMP'),
        0xC9: ('CMP', 'IMM'),
        0xCA: ('DEX', 'IMP'),
        0xCB: ('AXS', 'IMM'),
        0xCC: ('CPY', 'ABS'),
        0xCD: ('CMP', 'ABS'),
        0xCE: ('DEC', 'ABS'),
        0xCF: ('DCP', 'ABS'),
        0xD0: ('BNE', 'REL'),
        0xD1: ('CMP', 'INY'),
        0xD2: ('KIL', 'IMP'),
        0xD3: ('DCP', 'INY'),
        0xD4: ('NOP', 'ZPX'),
        0xD5: ('CMP', 'ZPX'),
        0xD6: ('DEC', 'ZPX'),
        0xD7: ('DCP', 'ZPX'),
        0xD8: ('CLD', 'IMP'),
        0xD9: ('CMP', 'ABY'),
        0xDA: ('NOP', 'IMP'),
        0xDB: ('DCP', 'ABY'),
        0xDC: ('NOP', 'ABX'),
        0xDD: ('CMP', 'ABX'),
        0xDE: ('DEC', 'ABX'),
        0xDF: ('DCP', 'ABX'),
        0xE0: ('CPX', 'IMM'),
        0xE1: ('SBC', 'INX'),
        0xE2: ('NOP', 'IMM'),
        0xE3: ('ISB', 'INX'),
        0xE4: ('CPX', 'ZPG'),
        0xE5: ('SBC', 'ZPG'),
        0xE6: ('INC', 'ZPG'),
        0xE7: ('ISB', 'ZPG'),
        0xE8: ('INX', 'IMP'),
        0xE9: ('SBC', 'IMM'),
        0xEA: ('NOP', 'IMP'),
        0xEB: ('SBC', 'IMM'),
        0xEC: ('CPX', 'ABS'),
        0xED: ('SBC', 'ABS'),
        0xEE: ('INC', 'ABS'),
        0xEF: ('ISB', 'ABS'),
        0xF0: ('BEQ', 'REL'),
        0xF1: ('SBC', 'INY'),
        0xF2: ('KIL', 'IMP'),
        0xF3: ('ISB', 'INY'),
        0xF4: ('NOP', 'ZPX'),
        0xF5: ('SBC', 'ZPX'),
        0xF6: ('INC', 'ZPX'),
        0xF7: ('ISB', 'ZPX'),
        0xF8: ('SED', 'IMP'),
        0xF9: ('SBC', 'ABY'),
        0xFA: ('NOP', 'IMP'),
        0xFB: ('ISB', 'ABY'),
        0xFC: ('NOP', 'ABX'),
        0xFD: ('SBC', 'ABX'),
        0xFE: ('INC', 'ABX'),
        0xFF: ('ISB', 'ABX'),
    }
    return code

def order_size():
    size = {
        'ABS': 3,
        'IMM': 2,
        'IMP': 1,
        'ZPG': 2,
        'ABX': 3,
        'ABY': 3,
        'INX': 2,
        'INY': 2,
        'ZPX': 2,
        'ZPY': 2,
        'REL': 2,
        'IND': 3,
        'UNK': 1,
    }
    return size

def order_circle():
    d = {
        0x0: '7',
        0x1: '6',
        0x2: '-1',
        0x3: '8',
        0x4: '3',
        0x5: '3',
        0x6: '5',
        0x7: '5',
        0x8: '3',
        0x9: '2',
        0xa: '2',
        0xb: '2',
        0xc: '4',
        0xd: '4',
        0xe: '6',
        0xf: '6',
        0x10: '2*',
        0x11: '5*',
        0x12: '-1',
        0x13: '8',
        0x14: '4',
        0x15: '4',
        0x16: '6',
        0x17: '6',
        0x18: '2',
        0x19: '4*',
        0x1a: '2',
        0x1b: '7',
        0x1c: '4*',
        0x1d: '4*',
        0x1e: '7',
        0x1f: '7',
        0x20: '6',
        0x21: '6',
        0x22: '-1',
        0x23: '8',
        0x24: '3',
        0x25: '3',
        0x26: '5',
        0x27: '5',
        0x28: '4',
        0x29: '2',
        0x2a: '2',
        0x2b: '2',
        0x2c: '4',
        0x2d: '4',
        0x2e: '6',
        0x2f: '6',
        0x30: '2*',
        0x31: '5*',
        0x32: '-1',
        0x33: '8',
        0x34: '4',
        0x35: '4',
        0x36: '6',
        0x37: '6',
        0x38: '2',
        0x39: '4*',
        0x3a: '2',
        0x3b: '7',
        0x3c: '4*',
        0x3d: '4*',
        0x3e: '7',
        0x3f: '7',
        0x40: '6',
        0x41: '6',
        0x42: '-1',
        0x43: '8',
        0x44: '3',
        0x45: '3',
        0x46: '5',
        0x47: '5',
        0x48: '3',
        0x49: '2',
        0x4a: '2',
        0x4b: '2',
        0x4c: '3',
        0x4d: '4',
        0x4e: '6',
        0x4f: '6',
        0x50: '2*',
        0x51: '5*',
        0x52: '-1',
        0x53: '8',
        0x54: '4',
        0x55: '4',
        0x56: '6',
        0x57: '6',
        0x58: '2',
        0x59: '4*',
        0x5a: '2',
        0x5b: '7',
        0x5c: '4*',
        0x5d: '4*',
        0x5e: '7',
        0x5f: '7',
        0x60: '6',
        0x61: '6',
        0x62: '-1',
        0x63: '8',
        0x64: '3',
        0x65: '3',
        0x66: '5',
        0x67: '5',
        0x68: '4',
        0x69: '2',
        0x6a: '2',
        0x6b: '2',
        0x6c: '5',
        0x6d: '4',
        0x6e: '6',
        0x6f: '6',
        0x70: '2*',
        0x71: '5*',
        0x72: '-1',
        0x73: '8',
        0x74: '4',
        0x75: '4',
        0x76: '6',
        0x77: '6',
        0x78: '2',
        0x79: '4*',
        0x7a: '2',
        0x7b: '7',
        0x7c: '4*',
        0x7d: '4*',
        0x7e: '7',
        0x7f: '7',
        0x80: '2',
        0x81: '6',
        0x82: '2',
        0x83: '6',
        0x84: '3',
        0x85: '3',
        0x86: '3',
        0x87: '3',
        0x88: '2',
        0x89: '2',
        0x8a: '2',
        0x8b: '2',
        0x8c: '4',
        0x8d: '4',
        0x8e: '4',
        0x8f: '4',
        0x90: '2*',
        0x91: '6',
        0x92: '-1',
        0x93: '6',
        0x94: '4',
        0x95: '4',
        0x96: '4',
        0x97: '4',
        0x98: '2',
        0x99: '5',
        0x9a: '2',
        0x9b: '5',
        0x9c: '5',
        0x9d: '5',
        0x9e: '5',
        0x9f: '5',
        0xa0: '2',
        0xa1: '6',
        0xa2: '2',
        0xa3: '6',
        0xa4: '3',
        0xa5: '3',
        0xa6: '3',
        0xa7: '3',
        0xa8: '2',
        0xa9: '2',
        0xaa: '2',
        0xab: '2',
        0xac: '4',
        0xad: '4',
        0xae: '4',
        0xaf: '4',
        0xb0: '2*',
        0xb1: '5*',
        0xb2: '-1',
        0xb3: '5*',
        0xb4: '4',
        0xb5: '4',
        0xb6: '4',
        0xb7: '4',
        0xb8: '2',
        0xb9: '4*',
        0xba: '2',
        0xbb: '4*',
        0xbc: '4*',
        0xbd: '4*',
        0xbe: '4*',
        0xbf: '4*',
        0xc0: '2',
        0xc1: '6',
        0xc2: '2',
        0xc3: '8',
        0xc4: '3',
        0xc5: '3',
        0xc6: '5',
        0xc7: '5',
        0xc8: '2',
        0xc9: '2',
        0xca: '2',
        0xcb: '2',
        0xcc: '4',
        0xcd: '4',
        0xce: '6',
        0xcf: '6',
        0xd0: '2*',
        0xd1: '5*',
        0xd2: '-1',
        0xd3: '8',
        0xd4: '4',
        0xd5: '4',
        0xd6: '6',
        0xd7: '6',
        0xd8: '2',
        0xd9: '4*',
        0xda: '2',
        0xdb: '7',
        0xdc: '4*',
        0xdd: '4*',
        0xde: '7',
        0xdf: '7',
        0xe0: '2',
        0xe1: '6',
        0xe2: '2',
        0xe3: '8',
        0xe4: '3',
        0xe5: '3',
        0xe6: '5',
        0xe7: '5',
        0xe8: '2',
        0xe9: '2',
        0xea: '2',
        0xeb: '2',
        0xec: '4',
        0xed: '4',
        0xee: '6',
        0xef: '6',
        0xf0: '2*',
        0xf1: '5*',
        0xf2: '-1',
        0xf3: '8',
        0xf4: '4',
        0xf5: '4',
        0xf6: '6',
        0xf7: '6',
        0xf8: '2',
        0xf9: '4*',
        0xfa: '2',
        0xfb: '7',
        0xfc: '4*',
        0xfd: '4*',
        0xfe: '7',
        0xff: '7',
    }
    return d

def palette_table():
    # r g b a
    palette = [
        (0x7F, 0x7F, 0x7F, 0xFF), (0x20, 0x00, 0xB0, 0xFF), (0x28, 0x00, 0xB8, 0xFF), (0x60, 0x10, 0xA0, 0xFF),
        (0x98, 0x20, 0x78, 0xFF), (0xB0, 0x10, 0x30, 0xFF), (0xA0, 0x30, 0x00, 0xFF), (0x78, 0x40, 0x00, 0xFF),
        (0x48, 0x58, 0x00, 0xFF), (0x38, 0x68, 0x00, 0xFF), (0x38, 0x6C, 0x00, 0xFF), (0x30, 0x60, 0x40, 0xFF),
        (0x30, 0x50, 0x80, 0xFF), (0x00, 0x00, 0x00, 0xFF), (0x00, 0x00, 0x00, 0xFF), (0x00, 0x00, 0x00, 0xFF),

        (0xBC, 0xBC, 0xBC, 0xFF), (0x40, 0x60, 0xF8, 0xFF), (0x40, 0x40, 0xFF, 0xFF), (0x90, 0x40, 0xF0, 0xFF),
        (0xD8, 0x40, 0xC0, 0xFF), (0xD8, 0x40, 0x60, 0xFF), (0xE0, 0x50, 0x00, 0xFF), (0xC0, 0x70, 0x00, 0xFF),
        (0x88, 0x88, 0x00, 0xFF), (0x50, 0xA0, 0x00, 0xFF), (0x48, 0xA8, 0x10, 0xFF), (0x48, 0xA0, 0x68, 0xFF),
        (0x40, 0x90, 0xC0, 0xFF), (0x00, 0x00, 0x00, 0xFF), (0x00, 0x00, 0x00, 0xFF), (0x00, 0x00, 0x00, 0xFF),

        (0xFF, 0xFF, 0xFF, 0xFF), (0x60, 0xA0, 0xFF, 0xFF), (0x50, 0x80, 0xFF, 0xFF), (0xA0, 0x70, 0xFF, 0xFF),
        (0xF0, 0x60, 0xFF, 0xFF), (0xFF, 0x60, 0xB0, 0xFF), (0xFF, 0x78, 0x30, 0xFF), (0xFF, 0xA0, 0x00, 0xFF),
        (0xE8, 0xD0, 0x20, 0xFF), (0x98, 0xE8, 0x00, 0xFF), (0x70, 0xF0, 0x40, 0xFF), (0x70, 0xE0, 0x90, 0xFF),
        (0x60, 0xD0, 0xE0, 0xFF), (0x60, 0x60, 0x60, 0xFF), (0x00, 0x00, 0x00, 0xFF), (0x00, 0x00, 0x00, 0xFF),

        (0xFF, 0xFF, 0xFF, 0xFF), (0x90, 0xD0, 0xFF, 0xFF), (0xA0, 0xB8, 0xFF, 0xFF), (0xC0, 0xB0, 0xFF, 0xFF),
        (0xE0, 0xB0, 0xFF, 0xFF), (0xFF, 0xB8, 0xE8, 0xFF), (0xFF, 0xC8, 0xB8, 0xFF), (0xFF, 0xD8, 0xA0, 0xFF),
        (0xFF, 0xF0, 0x90, 0xFF), (0xC8, 0xF0, 0x80, 0xFF), (0xA0, 0xF0, 0xA0, 0xFF), (0xA0, 0xFF, 0xC8, 0xFF),
        (0xA0, 0xFF, 0xF0, 0xFF), (0xA0, 0xA0, 0xA0, 0xFF), (0x00, 0x00, 0x00, 0xFF), (0x00, 0x00, 0x00, 0xFF),
    ]
    return palette