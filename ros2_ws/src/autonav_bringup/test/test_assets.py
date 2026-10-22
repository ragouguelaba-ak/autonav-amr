from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

def test_sdf_files_parse():
    for relative in ('models/amr.sdf', 'worlds/warehouse.sdf'):
        root = ET.parse(ROOT / relative).getroot()
        assert root.tag == 'sdf'

def test_robot_has_drive_and_lidar():
    model = ET.parse(ROOT / 'models/amr.sdf').getroot()
    assert model.find('.//sensor[@name="lidar"]') is not None
    assert model.find('.//plugin[@name="gz::sim::systems::DiffDrive"]') is not None
    assert len(model.findall('.//joint')) == 2
