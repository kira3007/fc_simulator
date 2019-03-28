from fc_cpu import (
    Cpu,
    load_nes,
    sign,
)
from fc_ppu import (
    PPU,
    PpuSpace,
)
from utils import (
    log,
    bytes_to_int,
)


def test_sign():
    input = 255
    output = -1
    result = sign(input)
    assert output == result

    input = 0
    output = 0
    result = sign(input)
    assert output == result

    input = 256
    output = 256
    result = sign(input, length=2)
    assert output == result

    input = 128
    output = -128
    result = sign(input)
    assert output == result


def test_mirror():
    space = PpuSpace()
    # set
    space[0x3000] = 123
    assert space[0x2000] == 123

    space[0x3EFF] = 111
    assert space[0x2EFF] == 111

    space[0x3123:0x3125] = [1, 2]
    assert space[0x2123:0x2125] == [1, 2]

    # 0x3F20-0x3FFF	大小0x00E0	0x3F00-0x3F1F 镜像
    space[0x3FFF - 32] = 233
    assert space[0x3F1F] == 233

    space[0x3FFF - 30: 0x3FFF - 28] = [3, 9]
    assert space[0x3F1F - 30:0x3F1F - 28] == [3, 9]
    # assert 1==3


def test_ppu_PPUADDR_write():
    ppu = PPU()
    ppu.set_PPUADDR(0x20)
    ppu.set_PPUADDR(0x20)
    assert ppu.registers['PPUADDR'] == 0x2020

    ppu.set_PPUADDR(0xff)
    ppu.set_PPUADDR(0x10)
    assert ppu.registers['PPUADDR'] == 0xff10


def test_ppu_pattern_block():
    pattern = [
        # low_8
        0b00010000,
        0b00000000,
        0b01000100,
        0b00000000,
        0b11111110,
        0b00000000,
        0b10000010,
        0b00000000,
        # high8
        0b00000000,
        0b00101000,
        0b01000100,
        0b10000010,
        0b00000000,
        0b10000010,
        0b10000010,
        0b00000000,
    ]
    ppu = PPU()
    block = ppu.pattern_block(pattern)
    assert block[3] == 1
    assert block[10] == 2
    assert block[17] == 3


def test_NMI():
    cpu = Cpu()
    nes = load_nes()
    prg_rom = nes['prg_rom']
    cpu.load_prg_rom(prg_rom)
    cpu.load_chr_rom(nes['chr_rom'])
    NMI_AD = 0xFFFA
    save_p = 0b11111111
    cpu.registers['P'].flag = save_p
    right_pc = bytes_to_int(cpu.space[NMI_AD: NMI_AD+2])
    log(cpu.registers)
    cpu.NMI()
    log(cpu.registers)
    assert cpu.PC == right_pc
    # P 4位置0后压入stack
    s = cpu.registers['S']
    pushed_p = cpu.space[s+256+1]
    assert pushed_p == 0b11101111

def test1():
    # CPU 汇编测试
    cpu = Cpu()
    nes = load_nes()
    prg_rom = nes['prg_rom']
    cpu.load_prg_rom(prg_rom)
    cpu.load_chr_rom(nes['chr_rom'])
    cpu.loop_logs()



def test2():
    # PPU log测试
    cpu = Cpu()
    nes = load_nes()
    cpu.load_prg_rom(nes['prg_rom'])
    cpu.load_chr_rom(nes['chr_rom'])
    cpu.loop_20000()
    # print(cpu.space.ppu.space.space[0x0000:0x1FFF])

    # assert 1== 3
    right = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32,
             82, 117, 110, 32, 97, 108, 108, 32, 116, 101, 115, 116, 115, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 45, 45, 32, 66, 114, 97, 110, 99, 104, 32, 116, 101, 115, 116, 115, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32, 70, 108, 97, 103, 32, 116, 101, 115, 116, 115,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32, 73, 109, 109, 101,
             100, 105, 97, 116, 101, 32, 116, 101, 115, 116, 115, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 45, 45, 32, 73, 109, 112, 108, 105, 101, 100, 32, 116, 101, 115, 116, 115, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32, 83, 116, 97, 99, 107, 32, 116, 101, 115, 116, 115, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32, 65, 99, 99, 117, 109, 117, 108,
             97, 116, 111, 114, 32, 116, 101, 115, 116, 115, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32,
             40, 73, 110, 100, 105, 114, 101, 99, 116, 44, 88, 41, 32, 116, 101, 115, 116, 115, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 45, 45, 32, 90, 101, 114, 111, 112, 97, 103, 101, 32, 116, 101, 115, 116, 115, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32, 65, 98, 115, 111, 108, 117, 116, 101, 32,
             116, 101, 115, 116, 115, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32, 40, 73,
             110, 100, 105, 114, 101, 99, 116, 41, 44, 89, 32, 116, 101, 115, 116, 115, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 45, 45, 32, 65, 98, 115, 111, 108, 117, 116, 101, 44, 89, 32, 116, 101, 115, 116, 115, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32, 90, 101, 114, 111, 112, 97, 103, 101, 44, 88, 32,
             116, 101, 115, 116, 115, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 45, 45, 32, 65, 98, 115, 111,
             108, 117, 116, 101, 44, 88, 32, 116, 101, 115, 116, 115, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 85, 112, 47, 68, 111, 119, 110, 58, 32, 115, 101, 108, 101, 99,
             116, 32, 116, 101, 115, 116, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 83, 116, 97, 114, 116,
             58, 32, 114, 117, 110, 32, 116, 101, 115, 116, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 83, 101, 108, 101, 99, 116, 58, 32, 73, 110, 118, 97, 108, 105, 100, 32, 111, 112, 115, 33, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
             32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0]
    # assert len(cpu.space.ppu.space.space[0x2000:0x2400]) == len(right)
    assert cpu.space.ppu.space.space[0x2000:0x2400] == right