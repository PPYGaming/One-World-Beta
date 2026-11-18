from pathlib import Path
import re,json,hashlib,zipfile
c=json.loads(next(Path('.').glob('*assembly-config.json')).read_text())
for a in c['expected']:
 p=Path(a['path']);assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256'],'baseline changed '+str(p)
parts={}
for p in Path('.').iterdir():
 m=re.search(r'release1345\.bundle\.part(\d\d)$',p.name)
 if m:parts[int(m[1])]=p
assert set(parts)==set(range(c['parts']))
b=b''.join(parts[n].read_bytes() for n in sorted(parts));assert hashlib.sha256(b).hexdigest()==c['bundle_sha']
Path('/tmp/release1345.zip').write_bytes(b);Path('release').mkdir(exist_ok=True)
with zipfile.ZipFile('/tmp/release1345.zip') as z:
 assert set(z.namelist())==set(c['artifacts']);z.extractall('release')
for n,h in c['artifacts'].items():assert hashlib.sha256((Path('release')/n).read_bytes()).hexdigest()==h
with zipfile.ZipFile('release/one-world-project-source-1.3.45.zip') as z:
 for n in z.namelist():assert not n.startswith('/') and '..' not in Path(n).parts and not n.endswith(('.jks','.keystore','.idsig'))
 z.extractall('.')
for a in json.loads(Path('SOURCE-INVENTORY.json').read_text())['files']:
 p=Path(a['path']);assert p.stat().st_size==a['size'] and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256']
print('Verified original baseline and exact signed artifacts/source')
