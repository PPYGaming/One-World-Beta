import runpy,json,hashlib
from pathlib import Path
preflight=json.loads(next(Path('.').glob('*delta51-guard.json')).read_text())
for a in preflight['expected']:
 p=Path(a['path']);assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256'],'Current source changed before assembly: '+str(p)
import urllib.request,base64,zipfile
metadata=[{'name': 'one-world-beta-1.3.50.apk', 'date': (2026, 11, 19, 17, 18, 44), 'compress': 0, 'create_system': 3, 'external_attr': 2175008768, 'internal_attr': 0, 'extra': '', 'comment': '', 'sha': 'd97bda369cd116ca5fb7e5d3b8e1ca24594ab77a88e1ca0e189220017409142b', 'inline': None}, {'name': 'beta-update.json', 'date': (2026, 11, 19, 17, 18, 44), 'compress': 0, 'create_system': 3, 'external_attr': 2175008768, 'internal_attr': 0, 'extra': '', 'comment': '', 'sha': 'c375b0d440213bb6aa2b9e39faf9d7d69e3b37d7302ed5cd29a2b89727c90577', 'inline': None}, {'name': 'one-world-project-source-1.3.50.zip', 'date': (2026, 11, 19, 17, 21, 36), 'compress': 0, 'create_system': 3, 'external_attr': 2175008768, 'internal_attr': 0, 'extra': '', 'comment': '', 'sha': 'a47331474e9ed302bbe1cb542ca36b5b568a6f601f7ab95a1238260835a99ab5', 'inline': None}, {'name': 'release-notes.md', 'date': (2026, 11, 19, 17, 18, 42), 'compress': 0, 'create_system': 3, 'external_attr': 2175008768, 'internal_attr': 0, 'extra': '', 'comment': '', 'sha': '18cc37de5ab9324646e2a92d82692a86b6d2b8c56c4d728e26aec8428f49485f', 'inline': 'IyBPbmUgV29ybGQgQmV0YSAxLjMuNTAKClRlc3RpbmcgcmVsZWFzZSwgdmVyc2lvbkNvZGUgNzIuIEluc3RhbGwgb3ZlciB0aGUgZXhpc3RpbmcgYmV0YS4gRG8gbm90IHVuaW5zdGFsbCBvciBjbGVhciBhcHAgZGF0YS4KCi0gQ29ubmVjdGVkIHNub3cgcmFuZ2VzLCBicm9hZCB0ZXJyYWNlZCBkZXNlcnQgaGlnaGxhbmQsIGNlbnRyYWwgd29vZGVkIHN0b25lIHJpZGdlcywgYW5kIHNjYXR0ZXJlZCBzd2FtcCBjcmFncyBhcmUgaW50ZWdyYXRlZCBpbnRvIHRoZSBjdW11bGF0aXZlIFNlY29uZCBNYXAuIEV4aXN0aW5nIGhhcnZlc3RhYmxlIHRyZWUgbW9kZWxzIGFyZSByZXRhaW5lZDsgbGlnaHR3ZWlnaHQgZGlzdGFudCBjYW5vcHkgZmlsbHMgdGhlIHdpZGVyIGxhbmRzY2FwZS4gQWxsIGhpZGRlbiBzbG9wZXMgYW5kIG1ldHJpYyBkaW1lbnNpb25zIGFyZSBpbnRlcnByZXRhdGlvbnMgb2YgdGhlIHN1cHBsaWVkIGlsbHVzdHJhdGlvbiwgbm90IGFuIGV4YWN0IHJlY29uc3RydWN0aW9uLgotIFNldHRpbmdzID4gSGVscCAmIEJldGEgPiBCZXRhIGluc3BlY3Rpb24gZmxpZ2h0LiBKb3lzdGljay9XQVNEIHRyYXZlbHMsIHRvdWNoIFVQL0RPV04gb3Iga2V5Ym9hcmQgRS9RIGNoYW5nZXMgaGVpZ2h0LCBSRVRVUk4gcmVzdG9yZXMgeW91ciBvcmlnaW5hbCBncm91bmQgbG9jYXRpb24uIEZsaWdodCBkb2VzIG5vdCBvdmVyd3JpdGUgdGhhdCBzYXZlZCBsb2NhdGlvbiwgc3BlbmQgc3Vydml2YWwgc3RhdHMsIG9yIHBlcm1pdCBhdHRhY2tzLgotIEV4aXN0aW5nIGxvY2FsIHNhdmVzIGFuZCBwcm9maWxlcyBhcmUgYXJjaGl2ZWQgb25jZSBiZWZvcmUgdGhpcyB0ZXJyYWluIHVwZGF0ZS4gTm8gd29ybGQsIGludmVudG9yeSwgY3JhZnRpbmcgc3RhdGlvbiwgcmVzb3VyY2VzIG9yIHByb2ZpbGUgcHJvZ3Jlc3MgaXMgaW50ZW50aW9uYWxseSByZXNldC4gU2F2aW5nIGlzIHBhdXNlZCBpZiB0aGUgcHJvdGVjdGl2ZSBhcmNoaXZlIGNhbm5vdCBiZSBzdG9yZWQuCi0gTmV3IHByb2ZpbGVzIGRlZmF1bHQgdG8gQm95IGFuZCByZXF1aXJlIGEgbmFtZS4gVHdvLXByb2ZpbGUgY3JlYXRpb24gY2FwLiBFeGlzdGluZyBsYXJnZXIgcmVnaXN0cmllcyByZW1haW4gYWNjZXNzaWJsZS4gVGhlIG90aGVyIHN1cnZpdm9yJ3MgbmFtZSByZXBsYWNlcyB0aGUgcGx1cyBidXR0b24gZm9yIGRpcmVjdCBzd2l0Y2hpbmcsIHdpdGhvdXQgYSBwb3B1cC4KCkxvY2FsIGNoZWNrczogYWN0dWFsIHBhY2thZ2VkIGVudHJ5L3JlYWRpbmVzcy9tZW51L3NldHRpbmdzL2NhbXBmaXJlLCBmbGlnaHQgbW92ZW1lbnQgYW5kIG9yaWdpbmFsLWxvY2F0aW9uIHNhdmUvcmV0dXJuLCBwcm9maWxlIHN3aXRjaGluZy9jcmVhdGlvbiBjYXAvc2F2ZSByZXRlbnRpb24sIHNvdXJjZS9BUEsgcGF5bG9hZCBjaGVja3MsIG9yaWdpbmFsIHNpZ25pbmcgY2VydGlmaWNhdGUuCgpOb3QgdmVyaWZpZWQ6IHBoeXNpY2FsIEFuZHJvaWQgRlBTL3RoZXJtYWwvbG9uZy1zZXNzaW9uIGJlaGF2aW9yLCB0aGUgZWFybGllciBhcHAgZXhpdCBjYXVzZSwgYW5kIGZ1bGwgb24tZGV2aWNlIGNvbGxpc2lvbiB0cmF2ZXJzYWwgYWNyb3NzIHRoZSB3b3JsZC4gVGhpcyBiZXRhIGlzIGZvciB0aGUgb3duZXIncyBpbnN0YWxsYXRpb24gcmV2aWV3OyBpdCBkb2VzIG5vdCBjbGFpbSB0aGUgZWFybGllciBsYWcvY3Jhc2ggaXMgZml4ZWQgb3IgdGhlIGlsbHVzdHJhdGlvbidzIGRldGFpbGVkIG1vZGVsIHF1YWxpdHkgaXMgbWF0Y2hlZC4KCk9yaWdpbmFsIGdhbWU6IFNtaWxleSwgbW9kaWZpZWQgYW5kIHJlZGlzdHJpYnV0ZWQgd2l0aCBwZXJtaXNzaW9uLiBCdW5kbGVkIHRoaXJkLXBhcnR5IG5vdGljZXMgcmV0YWluZWQuIEFJIHNlcnZpY2VzIHN1cHBsaWVkIHByb2NlZHVyYWwgZHJhZnQgaWRlYXMsIG5vdCBmaW5pc2hlZCBoaWdoLXF1YWxpdHkgbW9kZWwgYXNzZXRzLiBDbGF1ZGUgY291bGQgbm90IHNlZSBpdHMgYXR0YWNobWVudDsgaXRzIGRyYWZ0IHdhcyBkZXNjcmlwdGlvbi1iYXNlZCBhbmQgdGhlIHNoaXBwZWQgdGVycmFpbiB3YXMgaW5kZXBlbmRlbnRseSByZXZpc2VkLiBObyBwYWlkIHNlcnZpY2Ugb3IgZ2VuZXJhdGlvbiBjcmVkaXRzIHVzZWQuCg=='}]
with zipfile.ZipFile('/tmp/release1350.zip','w')as bundle:
 for item in metadata:
  data=base64.b64decode(item['inline'])if item['inline']else urllib.request.urlopen('https://github.com/PPYGaming/One-World-Beta/releases/download/v1.3.50/'+item['name'],timeout=120).read()
  assert hashlib.sha256(data).hexdigest()==item['sha'],'Published50 baseline asset mismatch'
  info=zipfile.ZipInfo(item['name'],tuple(item['date']));info.compress_type=item['compress'];info.create_system=item['create_system'];info.external_attr=item['external_attr'];info.internal_attr=item['internal_attr'];info.extra=bytes.fromhex(item['extra']);info.comment=bytes.fromhex(item['comment']);bundle.writestr(info,data)

from pathlib import Path
import re,json,hashlib,zipfile,bz2,struct
cfg=json.loads(next(Path('.').glob('*delta51-guard.json')).read_text())
for a in cfg['expected']:
 p=Path(a['path']);assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256'],'baseline changed '+str(p)
old=Path('/tmp/release1350.zip').read_bytes();assert hashlib.sha256(old).hexdigest()==cfg['old']
patch=next(Path('.').glob('*release1351.delta')).read_bytes();assert hashlib.sha256(patch).hexdigest()==cfg['patch']
def num(b):
 v=int.from_bytes(b,'little');return -(v&((1<<63)-1)) if v>>63 else v
assert patch[:8]==b'BSDIFF40';cl,dl,size=[num(patch[i:i+8]) for i in [8,16,24]]
ctrl=bz2.decompress(patch[32:32+cl]);diff=bz2.decompress(patch[32+cl:32+cl+dl]);extra=bz2.decompress(patch[32+cl+dl:]);new=bytearray();pos=cp=dp=ep=0
while len(new)<size:
 x,y,z=[num(ctrl[cp+i:cp+i+8]) for i in [0,8,16]];cp+=24;assert x>=0 and y>=0
 for i in range(x):new.append((diff[dp+i]+(old[pos+i] if 0<=pos+i<len(old) else 0))%256)
 dp+=x;pos+=x;new.extend(extra[ep:ep+y]);ep+=y;pos+=z
assert len(new)==size and hashlib.sha256(new).hexdigest()==cfg['new']
Path('/tmp/release1351.zip').write_bytes(new);Path('release').mkdir(exist_ok=True)
with zipfile.ZipFile('/tmp/release1351.zip') as z:
 assert set(z.namelist())==set(cfg['artifacts']);z.extractall('release')
for n,h in cfg['artifacts'].items():assert hashlib.sha256((Path('release')/n).read_bytes()).hexdigest()==h
with zipfile.ZipFile('release/one-world-project-source-1.3.51.zip')as z:
 for n in z.namelist():assert not n.startswith('/') and '..'not in Path(n).parts and not n.endswith(('.jks','.keystore','.idsig'))
 z.extractall('.')
for a in json.loads(Path('SOURCE-INVENTORY.json').read_text())['files']:
 p=Path(a['path']);assert p.stat().st_size==a['size'] and hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256']
print('Exact signed51 delta assembly and fullsource verified')

for n in ['android/src/com/oneword/forest/BetaUpdateProvider.java', 'android/src/com/oneword/forest/BetaUpdater.java', 'android/src/com/oneword/forest/GithubUpdatePolicy.java']: Path(n).unlink(missing_ok=True)
