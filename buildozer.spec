[app]
title = Moses Robot
package.name = mosesrobot
package.domain = com.moses.robot
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.0,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.ant_options = -Dfile.encoding=UTF-8
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
