from pathlib import Path
import re,hashlib,zipfile,json,shutil
parts={}
for p in Path('.').iterdir():
 m=re.fullmatch(r'(?:\d+-)?release1326\.bundle\.part(\d\d)',p.name)
 if m:
  n=int(m[1]);assert n not in parts;parts[n]=p
assert set(parts)==set(range(27))
b=b''.join(parts[n].read_bytes()for n in sorted(parts));assert hashlib.sha256(b).hexdigest()=='90a4435525a62bda7429134739691db02b1d822505927f43be9491ed0aec159a'
Path('release1326.zip').write_bytes(b);release=Path('release');release.mkdir(exist_ok=True)
with zipfile.ZipFile('release1326.zip')as z:
 assert set(z.namelist())==set({'one-world-beta-1.3.26.apk': '25708013d1da77007401895446d603a2dce1df6f02485d98e9afa4833301337c', 'beta-update.json': '43f6bac881847c921919b19087d5d8bd72330690b8c54118b208e9d568957f2f', 'one-world-project-source-1.3.26.zip': '9e3f3583f45f2fe1c942f209e57a0238f6a6c3c7923ff995cce6465d7654aaf0', 'release-notes.md': 'ff4fdaa3398aa44675483a0738f21c92d9f89dd4b3d88e4ec9f03b9f72f0269e'})
 z.extractall(release)
for n,h in {'one-world-beta-1.3.26.apk': '25708013d1da77007401895446d603a2dce1df6f02485d98e9afa4833301337c', 'beta-update.json': '43f6bac881847c921919b19087d5d8bd72330690b8c54118b208e9d568957f2f', 'one-world-project-source-1.3.26.zip': '9e3f3583f45f2fe1c942f209e57a0238f6a6c3c7923ff995cce6465d7654aaf0', 'release-notes.md': 'ff4fdaa3398aa44675483a0738f21c92d9f89dd4b3d88e4ec9f03b9f72f0269e'}.items():assert hashlib.sha256((release/n).read_bytes()).hexdigest()==h
source=release/'one-world-project-source-1.3.26.zip'
with zipfile.ZipFile(source)as z:
 for n in z.namelist():assert not n.startswith('/')and '..'not in Path(n).parts and not n.endswith(('.jks','.keystore','.idsig'))
 z.extractall('.')
for a in json.loads(Path('SOURCE-INVENTORY.json').read_text())['files']:
 p=Path(a['path']);assert p.stat().st_size==a['size'];assert hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256']
print('Verified exact signed APK, manifest and complete editable source')
