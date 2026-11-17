from pathlib import Path
import hashlib,json,re
parts={}
for p in Path('.').iterdir():
 m=re.fullmatch(r'(?:\d+-)?followon1324\.apk\.part(\d\d)',p.name)
 if m:
  n=int(m[1]);assert n not in parts,'Duplicate part';parts[n]=p
assert set(parts)==set(range(13)),'Missing/unexpected parts'
content=b''.join(parts[n].read_bytes() for n in range(13))
assert len(content)==26215377,'Size mismatch'
assert hashlib.sha256(content).hexdigest()=='e52f0c48f327444a281f3713ffbeb685a3a087db0df59322ea076a6d10f814d7','Hash mismatch'
out=Path('release');out.mkdir(exist_ok=True)
(out/'one-world-beta-1.3.24.apk').write_bytes(content)
manifest={'schema': 1, 'package': 'com.oneword.forest.beta', 'versionCode': 46, 'versionName': '1.3.24', 'apk': 'one-world-beta-1.3.24.apk', 'size': 26215377, 'sha256': 'e52f0c48f327444a281f3713ffbeb685a3a087db0df59322ea076a6d10f814d7', 'signingCertificateSha256': '02db85e55056e12097dcf84daa5739dac0d1a3551ba8bdc4b257a58408c4c744', 'notes': 'Fullscreen game-style settings with left categories, right scrolling options and top close. Existing preferences and controls retained. Startup updater from 1.3.23 unchanged. Phone layout, touch scroll and update/download/install still require testing. Install over existing beta, do not uninstall or clear data.'}
(out/'beta-update.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Verified',manifest['sha256'],manifest['size'])
