[app]
# (str) Title of your application
title = ElderCare AI

# (str) Package name
package.name = eldercare

# (str) Package domain (needed for android/ios packaging)
package.domain = org.shehta.ahmed

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,json,ttf,java

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,kivymd,plyer,firebase-admin,bcrypt,cryptography

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/logo.png

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/logo.png

# (list) Supported orientations
orientation = portrait

# (list) List of service to declare for background notifications
services = AlarmReceiver:src/main/java/org/eldercare/singularity/AlarmReceiver.java


[android]
# (list) Permissions
android.permissions = INTERNET,VIBRATE,WAKE_LOCK

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (list) The Android archs to build for.
android.archs = arm64-v8a

# (str) Path to the Java source code for services
p4a.source_dir = src

# (list) Put the serviceAccountKey.json file in the apk assets directory
# The '.' means copy everything from the root that isn't ignored by .gitignore
android.add_assets = .

# (bool) Enable AndroidX support, required by many modern libraries
android.enable_androidx = True

# (list) Gradle dependencies for Firebase
# We will leave these commented out for the first successful build,
# but you will likely need them for Firebase to work.
# android.gradle_dependencies = com.google.firebase:firebase-analytics:17.2.1,com.google.firebase:firebase-auth:19.2.0
# android.add_build_gradle_line = apply plugin: 'com.google.gms.google-services'


[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1