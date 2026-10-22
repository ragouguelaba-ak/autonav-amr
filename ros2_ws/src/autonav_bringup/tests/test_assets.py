from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def test_model_xml():
    root = ET.parse(ROOT / 'models/autonav_robot/model.sdf').getroot()
    assert root.find('.//plugin[@name="gz::sim::systems::DiffDrive"]') is not None
    assert root.find('.//sensor[@name="lidar"]') is not None


def test_world_xml():
    root = ET.parse(ROOT / 'worlds/warehouse.sdf').getroot()
    assert root.find('.//include/uri').text == 'model://autonav_robot'
