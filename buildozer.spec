[app]
title = Moses Robot
package.name = mosesrobot
package.domain = com.moses.robot
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.ant_path = /usr/bin/ant
p4a.branch = master

[buildozer:android]
android.allow_backup = False
