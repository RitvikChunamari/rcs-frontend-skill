"""Smoke test for the bundled style taxonomy and relative reference links."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class StyleAtlasContract(unittest.TestCase):
    def test_all_twelve_profiles_exist(self):
        atlas = (ROOT / 'references/style-atlas.md').read_text()
        headers = re.findall(r'^## (\d+)\. ', atlas, re.M)
        self.assertEqual(headers, [str(i) for i in range(1, 13)])
        for term in ('Bento', 'Editorial', 'Brutalism', 'Retro', 'Aurora', 'Immersive', 'Glassmorphism', 'Maximalism', 'Skeuomorphism', 'Cyberpunk', 'Claymorphism', 'Swiss'):
            with self.subTest(term=term):
                self.assertIn(term, atlas)

    def test_main_skill_has_navigation_and_gates(self):
        content = (ROOT / 'SKILL.md').read_text()
        for path in ('references/style-atlas.md', 'references/style-composition.md'):
            self.assertIn(path, content)
            self.assertTrue((ROOT / path).is_file())
        self.assertIn('style-specific test matrix', content)

    def test_all_local_markdown_paths_exist(self):
        docs = [ROOT / 'SKILL.md', *list((ROOT/'references').glob('*.md'))]
        for doc in docs:
            for link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', doc.read_text()):
                if '://' in link or link.startswith('mailto:'):
                    continue
                with self.subTest(document=doc.name, link=link):
                    self.assertTrue((doc.parent / link).exists(), f'{doc}: missing {link}')

if __name__ == '__main__':
    unittest.main()
