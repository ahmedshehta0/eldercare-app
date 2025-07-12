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
android.permissions = INTERNET
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
# We don't need to specify service here if it's not a background service
# that needs to run on boot. pyjnius handles it.

[buildozer]
# Set the global buildozer directory to be inside the project folder
# This forces buildozer to use the SDKs we control.
build_dir = ./.buildozer

log_level = 2
warn_on_root = 1