#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2023-03-17 15:50:54 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
import dbus

bus = dbus.SessionBus()
kdeconnect = bus.get_object("org.kde.kdeconnect", "/modules/kdeconnect")
notifications = kdeconnect.notifications()

# Send a custom notification to your phone
notifications.notify("phone_device_id", "Notification Title", "Notification Message", "default", {}, 5000)
