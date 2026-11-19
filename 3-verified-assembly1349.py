import runpy
from pathlib import Path
runpy.run_path(str(next(Path('.').glob('*verified-assembly1348.py'))))
from pathlib import Path
import re,json,hashlib,zipfile,bz2,struct
cfg=json.loads(next(Path('.').glob('*delta49-guard.json')).read_text())
for a in cfg['expected']:
 p=Path(a['path']);assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256'],'baseline changed '+str(p)
old=Path('/tmp/release1348.zip').read_bytes();assert hashlib.sha256(old).hexdigest()==cfg['old']
patch=next(Path('.').glob('*release1349.delta')).read_bytes();assert hashlib.sha256(patch).hexdigest()==cfg['patch']
def num(b):
 v=int.from_bytes(b,'little');return -(v&((1<<63)-1)) if v>>63 else v
assert patch[:8]==b'BSDIFF40';cl,dl,size=[num(patch[i:i+8]) for i in [8,16,24]]
ctrl=bz2.decompress(patch[32:32+cl]);diff=bz2.decompress(patch[32+cl:32+cl+dl]);extra=bz2.decompress(patch[32+cl+dl:]);new=bytearray();pos=cp=dp=ep=0
while len(new)<size:
 x,y,z=[num(ctrl[cp+i:cp+i+8]) for i in [0,8,16]];cp+=24;assert x>=0 and y>=0
 for i in range(x):new.append((diff[dp+i]+(old[pos+i] if 0<=pos+i<len(old) else 0))%256)
 dp+=x;pos+=x;new.extend(extra[ep:ep+y]);ep+=y;pos+=z
assert len(new)==size and hashlib.sha256(new).hexdigest()==cfg['new']
Path('/tmp/release1349.zip').write_bytes(new);Path('release').mkdir(exist_ok=True)
with zipfile.ZipFile('/tmp/release1349.zip') as z:
 assert set(z.namelist())==set(cfg['artifacts']);z.extractall('release')
for n,h in cfg['artifacts'].items():assert hashlib.sha256((Path('release')/n).read_bytes()).hexdigest()==h
with zipfile.ZipFile('release/one-world-project-source-1.3.49.zip')as z:
 for n in z.namelist():assert not n.startswith('/') and '..'not in Path(n).parts and not n.endswith(('.jks','.keystore','.idsig'))
 z.extractall('.')
for a in json.loads(Path('SOURCE-INVENTORY.json').read_text())['files']:
 p=Path(a['path']);assert p.stat().st_size==a['size'] and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256']
print('Exact signed49 delta assembly and fullsource verified')
