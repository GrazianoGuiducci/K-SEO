from pathlib import Path
import json
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_manifest_entry_and_bodies_exist(self):
        m = json.loads((ROOT / "KERNEL_MANIFEST.json").read_text())
        for path in [m[x] for x in ["entry", "kernel", "competence_field", "current", "presence_method"]] + m["competences"]:
            self.assertTrue((ROOT / path).is_file(), path)

    def test_skills_have_distinct_discoverable_names(self):
        names = []
        for p in (ROOT / "skills").glob("*/SKILL.md"):
            text = p.read_text()
            self.assertTrue(text.startswith("---\n"))
            names.append(re.search(r"^name: (.+)$", text, re.M).group(1))
            self.assertRegex(text, r"(?m)^description: .+")
        self.assertEqual(len(names), len(set(names)))
        self.assertGreater(len(names), 0)

    def test_relative_links_reach_their_body(self):
        for p in ROOT.rglob("*.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", p.read_text()):
                if ":" in target or target.startswith("#"):
                    continue
                target = unquote(target.split("#", 1)[0])
                self.assertTrue((p.parent / target).resolve().exists(), f"{p.name}: {target}")

    def test_package_has_no_instance_database(self):
        self.assertEqual(list(ROOT.rglob("*.sqlite3")), [])
        self.assertEqual(list(ROOT.rglob(".env")), [])

    def test_receiver_capabilities_are_qualified(self):
        m = json.loads((ROOT / "KERNEL_MANIFEST.json").read_text())
        for key in ["network", "scheduler", "model_api"]:
            self.assertFalse(m["runtime"][key])
        self.assertTrue(m["private_instance_is_separate"])


if __name__ == "__main__":
    unittest.main()
