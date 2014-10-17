#!/usr/bin/python

from Foundation import NSMutableArray, NSMutableDictionary
from Foundation import CFPreferencesSynchronize, CFPreferencesCopyValue, CFPreferencesCopyKeyList, CFPreferencesSetValue, CFPreferencesCopyMultiple, CFPreferencesSetMultiple, kCFPreferencesCurrentUser, kCFPreferencesAnyHost
import os, sys

# We only handle Yosemite's spotlight for now
majorRelease = int(os.uname()[2].split(".")[0])
if majorRelease < 14:
  print "Good news! This version of Mac OS X's Spotlight is not known to invade your privacy."
  sys.exit(0)

def fixSpotlight ():
  DISABLED_ITEMS=set(["MENU_WEBSEARCH", "MENU_SPOTLIGHT_SUGGESTIONS"])
  REQUIRED_ITEM_KEYS=set(["enabled", "name"])
  BUNDLE_ID="com.apple.Spotlight"
  PREF_NAME="orderedItems"

  items = CFPreferencesCopyValue(PREF_NAME, BUNDLE_ID, kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
  if items is None:
    print "Could not fetch Spotlight preferences!"
    return

  newItems = NSMutableArray.new()
  for item in items:
    missing_keys = []
    for key in REQUIRED_ITEM_KEYS:
      if not item.has_key(key):
        missing_keys.append(key)

    if len(missing_keys) is not 0:
      print "Preference item %s is missing expected keys (%s), skipping" % (item, missing_keys)
      newItems.append(item)
      continue

    if not item["name"] in DISABLED_ITEMS:
      newItems.append(item)
      continue

    newItem = NSMutableDictionary.dictionaryWithDictionary_(item)
    newItem.setObject_forKey_(0, "enabled")
    newItems.append(newItem)

  CFPreferencesSetValue(PREF_NAME, newItems, BUNDLE_ID, kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
  CFPreferencesSynchronize(BUNDLE_ID, kCFPreferencesCurrentUser, kCFPreferencesAnyHost)

fixSpotlight()
print "All done. Please log out for the new settings to take effect."
