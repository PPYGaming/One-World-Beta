from pathlib import Path
import re,hashlib,zipfile,json,shutil
parts={}
for p in Path('.').iterdir():
 m=re.fullmatch(r'(?:\d+-)?release1325\.bundle\.part(\d\d)',p.name)
 if m:
  n=int(m[1]);assert n not in parts;parts[n]=p
assert set(parts)==set(range(27))
b=b''.join(parts[n].read_bytes()for n in sorted(parts));assert hashlib.sha256(b).hexdigest()=='6b223e691f11b13aed4f1a34a82c5dd3deec2b84fca6aac31a265c78b4788ec3'
Path('release1325.zip').write_bytes(b);release=Path('release');release.mkdir(exist_ok=True)
with zipfile.ZipFile('release1325.zip')as z:
 assert set(z.namelist())==set({'one-world-beta-1.3.25.apk': 'f8a402147c7acc559c2eec23b69a166ec603a990a80cae9903f26a7f704aca25', 'beta-update.json': 'e85c476b48f5b57999ca00066c919849a83e98f04ea11640aa91cee3e529c02e', 'one-world-project-source-1.3.25.zip': '9585e26e5741d3e0373b6251fe0109ade25ca385740218f63a70a956ce584327', 'release-notes.md': 'd7b64a3ecc96ce74d754985b1dc8508faeb004856fbbdbf5fa917929ea845f4c'})
 z.extractall(release)
for n,h in {'one-world-beta-1.3.25.apk': 'f8a402147c7acc559c2eec23b69a166ec603a990a80cae9903f26a7f704aca25', 'beta-update.json': 'e85c476b48f5b57999ca00066c919849a83e98f04ea11640aa91cee3e529c02e', 'one-world-project-source-1.3.25.zip': '9585e26e5741d3e0373b6251fe0109ade25ca385740218f63a70a956ce584327', 'release-notes.md': 'd7b64a3ecc96ce74d754985b1dc8508faeb004856fbbdbf5fa917929ea845f4c'}.items():assert hashlib.sha256((release/n).read_bytes()).hexdigest()==h
source=release/'one-world-project-source-1.3.25.zip'
with zipfile.ZipFile(source)as z:
 for n in z.namelist():assert not n.startswith('/')and '..'not in Path(n).parts and not n.endswith(('.jks','.keystore','.idsig'))
 z.extractall('.')
for a in json.loads(Path('SOURCE-INVENTORY.json').read_text())['files']:
 p=Path(a['path']);assert p.stat().st_size==a['size'];assert hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256']
print('Verified exact signed APK, manifest and complete editable source')
