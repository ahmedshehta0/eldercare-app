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
android.add_assets = .

# --- Force Buildozer to use our manually prepared SDK ---
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk-bundle  # A standard sub-path
android.skip_update = True

[buildozer]
log_level = 2
warn_on_root = 1