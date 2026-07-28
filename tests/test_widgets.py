import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).parent.parent))

from widgets.roundButton import RoundedButton

def test_rounded_button_collision():
    button = RoundedButton(corner_radius=20)
    button.pos = (0, 0)
    button.size = (100, 100)
    
    # จุดตรงกลางปุ่ม -> ควรคลิกติด (True)
    assert button.collide_point(50, 50) == True
    
    # จุดอยู่นอกพื้นที่ปุ่ม -> ควรคลิกไม่ติด (False)
    assert button.collide_point(150, 150) == False
    
    # จุดตรงมุมเว้า (มุมขวาบน 100, 100) -> ควรคืนค่า False เพราะอยู่นอกส่วนมน
    assert button.collide_point(99, 99) == False
