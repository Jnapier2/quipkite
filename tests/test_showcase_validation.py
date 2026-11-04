"""Checks reject changed evidence and unsupported promotion claims."""
from contextlib import redirect_stdout, redirect_stderr
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT=Path(__file__).absolute().parents[1]
spec=importlib.util.spec_from_file_location('showcase_validation',ROOT/'scripts/validate_showcase.py')
review=importlib.util.module_from_spec(spec);spec.loader.exec_module(review)

class ShowcaseEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for path in review.REQUIRED_FILES:
            target=self.root/path.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(path,target)
        self.original={key:getattr(review,key) for key in ('ROOT','README','METADATA','ASSET','REQUIRED_FILES')}
        review.ROOT=self.root;review.README=self.root/'README.md';review.METADATA=self.root/'PROJECT_METADATA.json'
        review.ASSET=self.root/'assets/quipkite-solo-0.36.0.png'
        review.REQUIRED_FILES=tuple(self.root/path.relative_to(ROOT) for path in self.original['REQUIRED_FILES'])
        self.addCleanup(self.restore)
    def restore(self):
        for key,value in self.original.items():setattr(review,key,value)
    def run_review(self):
        output=io.StringIO()
        with redirect_stdout(output),redirect_stderr(output):code=review.main()
        return code,output.getvalue()
    def mutate(self,change):
        data=json.loads(review.METADATA.read_bytes());change(data)
        review.METADATA.write_text(json.dumps(data),encoding='utf-8')
    def test_reviewed_proposal_passes(self):
        code,text=self.run_review();self.assertEqual(0,code,text)
    def test_wrong_artifact_is_rejected(self):
        self.mutate(lambda d:d['publicBuild'].update(playerZipSha256='0'*64))
        self.assertNotEqual(0,self.run_review()[0])
    def test_unverified_host_cannot_be_declared_published(self):
        self.mutate(lambda d:d['publicBuild'].update(publicationStatus='published'))
        self.assertNotEqual(0,self.run_review()[0])
    def test_real_person_and_online_scope_cannot_be_conflated(self):
        self.mutate(lambda d:d['publicBoundary']['separateOnlineExperience'].update(twoPlayerPlayVerified=True))
        self.assertNotEqual(0,self.run_review()[0])
    def test_changed_screenshot_is_rejected(self):
        review.ASSET.write_bytes(review.ASSET.read_bytes()+b'changed')
        self.assertNotEqual(0,self.run_review()[0])
    def test_missing_qualification_is_rejected(self):
        review.README.write_text(review.README.read_text(encoding='utf-8').replace('awaits comparison with the final hosted artifact','is fully published'),encoding='utf-8')
        self.assertNotEqual(0,self.run_review()[0])
if __name__=='__main__':unittest.main(verbosity=2)
