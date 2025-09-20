[app]
title = ElderCare AI
package.name = eldercare
package.domain = org.shehta.ahmed
source.dir = .
source.include_exts = py,png,jpg,kv,json,ttf,java
version = 1.0
requirements = python3,kivy,kivymd,plyer,firebase-admin,bcrypt,cryptography
orientation = portrait
icon.filename = %(source.dir)s/assets/logo.png
android.add_assets = .

[android]
android.permissions = INTERNET,VIBRATE,WAKE_LOCK
android.api = 31
android.minapi = 21
android.archs = arm64-v8a
android.enable_androidx = True
p4a.source_dir = src
services = AlarmReceiver:src/main/java/org/eldercare/singularity/AlarmReceiver.java

# --- Point to the SDK we built in the workflow ---
android.sdk_path = /github/workspace/android-sdk

[buildozer]
log_level = 2
warn_on_root = 1
# Let's use the develop branch for better compatibility
p4a.branch = develop