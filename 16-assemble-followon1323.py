from pathlib import Path
import hashlib,json,re
parts={}
for p in Path('.').iterdir():
 m=re.fullmatch(r'(?:\d+-)?followon1323\.apk\.part(\d\d)',p.name)
 if m:
  n=int(m[1]);assert n not in parts,'Duplicate part';parts[n]=p
assert set(parts)==set(range(13)),'Missing/unexpected parts'
content=b''.join(parts[n].read_bytes() for n in range(13))
assert len(content)==26211281,'Size mismatch'
assert hashlib.sha256(content).hexdigest()=='69c523cebcc5c65f67357cc25b5eb64eff69bab98376042649e7acb2ef223ad7','Hash mismatch'
out=Path('release');out.mkdir(exist_ok=True)
(out/'one-world-beta-1.3.23.apk').write_bytes(content)
manifest={'schema': 1, 'package': 'com.oneword.forest.beta', 'versionCode': 45, 'versionName': '1.3.23', 'apk': 'one-world-beta-1.3.23.apk', 'size': 26211281, 'sha256': '69c523cebcc5c65f67357cc25b5eb64eff69bab98376042649e7acb2ef223ad7', 'signingCertificateSha256': '02db85e55056e12097dcf84daa5739dac0d1a3551ba8bdc4b257a58408c4c744', 'notes': 'Update check on the first loading screen before lobby or world, with minimal game-themed update controls. Android settings and installer remain system screens. Retains beta 1.3.22 graphics, crafting and pregame music changes. Phone update/download/install, graphics, audio and performance still require testing. Install over existing beta, do not uninstall or clear data.'}
(out/'beta-update.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Verified',manifest['sha256'],manifest['size'])
