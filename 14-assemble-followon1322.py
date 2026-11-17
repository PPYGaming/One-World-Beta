from pathlib import Path
import hashlib,json,re
parts={}
for p in Path('.').iterdir():
 m=re.fullmatch(r'(?:\d+-)?followon1322\.apk\.part(\d\d)',p.name)
 if m:
  n=int(m[1]);assert n not in parts,'Duplicate part';parts[n]=p
assert set(parts)==set(range(13)),'Missing/unexpected parts'
content=b''.join(parts[n].read_bytes() for n in range(13))
assert len(content)==26211281,'Size mismatch'
assert hashlib.sha256(content).hexdigest()=='04c51388be047111606ef4bf26cb23b2d12a021a42d112022dbbeb8cf7088bd6','Hash mismatch'
out=Path('release');out.mkdir(exist_ok=True)
(out/'one-world-beta-1.3.22.apk').write_bytes(content)
manifest={'schema': 1, 'package': 'com.oneword.forest.beta', 'versionCode': 44, 'versionName': '1.3.22', 'apk': 'one-world-beta-1.3.22.apk', 'size': 26211281, 'sha256': '04c51388be047111606ef4bf26cb23b2d12a021a42d112022dbbeb8cf7088bd6', 'signingCertificateSha256': '02db85e55056e12097dcf84daa5739dac0d1a3551ba8bdc4b257a58408c4c744', 'notes': 'Pregame-only looping menu music; High-only sun shadows and shadow-size repair; original tree geometry with painted Low foliage and lower particle budgets; separate Crafting button and static glass controls. Phone graphics/performance/update flow still require testing. Install over existing beta, do not uninstall or clear data.'}
(out/'beta-update.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Verified',manifest['sha256'],manifest['size'])
