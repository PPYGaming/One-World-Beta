from pathlib import Path
import hashlib,json,re
parts={}
for p in Path('.').iterdir():
 m=re.fullmatch(r'(?:\d+-)?bootstrap1321\.apk\.part(\d\d)',p.name)
 if m:
  n=int(m[1]);assert n not in parts,'Duplicate part';parts[n]=p
assert set(parts)==set(range(12)),'Missing or unexpected parts'
content=b''.join(parts[n].read_bytes() for n in range(12))
assert len(content)==22696506,'Size mismatch'
assert hashlib.sha256(content).hexdigest()=='f20f2793875dab94c5476ed37e3a965bd66afd4d3ca632fa292e56406b8104f8','APK hash mismatch'
out=Path('release');out.mkdir(exist_ok=True)
(out/'one-world-beta-1.3.21.apk').write_bytes(content)
manifest={'schema':1,'package':'com.oneword.forest.beta','versionCode':43,'versionName':'1.3.21','apk':'one-world-beta-1.3.21.apk','size':22696506,'sha256':hashlib.sha256(content).hexdigest(),'signingCertificateSha256':'02db85e55056e12097dcf84daa5739dac0d1a3551ba8bdc4b257a58408c4c744','notes':'Updater bootstrap beta, without new background music. Includes joystick target correction. Install over the existing beta to retain its saved world. Android installation and update flow still require phone testing.'}
(out/'beta-update.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Verified APK hash and size:',manifest['sha256'],manifest['size'])
