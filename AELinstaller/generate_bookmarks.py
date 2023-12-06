#! /usr/bin/env python
## ----------------------------------------------------------------------- INFO
## [AELinstaller/generate_firefox_policies.py]
## author        : fantomH @alterEGO Linux
## created       : 2023-12-04 19:57:47 UTC
## updated       : 2023-12-04 19:57:47 UTC
## description   : Generates bookmarks (dev)

# import os
import sqlite3 as sql
import json
import sys
# import subprocess
# import tempfile
# import webbrowser

def add_bookmarks(category):

    mb = firefox_policies["policies"]["ManagedBookmarks"]

    for i, c in enumerate(mb):
        if "name" in c and c["name"] == category:
            position = i
            break

    con = sql.connect('/home/ghost/main/ael-filesystem/usr/local/share/bookmarks.db')
    cur = con.cursor()

    sqlite_select_query = f"""SELECT * from bookmarks WHERE bookmarks.tags LIKE 'ael-{category.lower()}%'"""
    cur.execute(sqlite_select_query)
    records = cur.fetchall()

    new_bookmarks = []

    for record in records:
        r = {}
        if record[2] is not None:
            r["name"] = f"{record[1]} - {record[2]}"
        else:
            r["name"] = f"{record[1]}"
        r["url"] = record[3]
        new_bookmarks.append(r)

    new_bookmarks = sorted(new_bookmarks, key=lambda d: d['name'].lower())

    # new_bookmarks = [{
                        # "name": "ArcoLinux",
                        # "url": "https://www.arcolinux.info/"
                    # },
                    # {
                        # "name": "Kali Linux",
                        # "url": "https://www.kali.org/"
                    # }]


    firefox_policies["policies"]["ManagedBookmarks"][position]["children"].extend(new_bookmarks)

    return firefox_policies


firefox_policies = {
  "policies": {
    "DisableFirefoxStudies": True,
    "DisablePocket": True,
    "DisableTelemetry": True,
    "DisplayBookmarksToolbar": True,
    "FirefoxHome": {
      "Search": True,
      "TopSites": True,
      "SponsoredTopSites": False,
      "Highlights": False,
      "Pocket": False,
      "SponsoredPocket": False,
      "Snippets": False,
      "Locked": False
    },
    "NoDefaultBookmarks": True,
    "Preferences": {
      "ui.context_menus.after_mouseup": {
        "Value": True,
	      "Status": "locked"
      }
    },
    "ExtensionSettings": {
      "tab-stash@condordes.net": {
        "installation_mode": "normal_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/tab-stash/latest.xpi"
      },
      "{d10d0bf8-f5b5-c8b4-a8b2-2b9879e08c5d}": {
        "installation_mode": "normal_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/adblock-plus/latest.xpi"
      },
      "{c3c10168-4186-445c-9c5b-63f12b8e2c87}": {
        "installation_mode": "normal_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/cookie-editor/latest.xpi"
      },
      "CSSViewer@quantum": {
        "installation_mode": "normal_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/cssviewer-quantum/latest.xpi"
      },
      "foxyproxy@eric.h.jung": {
        "installation_mode": "normal_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/foxyproxy-standard/latest.xpi"
      },
      "{2e5ff8c8-32fe-46d0-9fc8-6b8986621f3c}": {
        "installation_mode": "normal_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/search_by_image/latest.xpi"
      },
      "{531906d3-e22f-4a6c-a102-8057b88a1a63}": {
        "installation_mode": "normal_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/single-file/latest.xpi"
      },
      "wappalyzer@crunchlabz.com": {
        "installation_mode": "normal_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/wappalyzer/latest.xpi"
      }
    },
    "ManagedBookmarks": [
      {
        "toplevel_name": "AEL-Bookmarks"
      },
      {
        "url": "https://github.com/alterEGO-Linux",
        "name": "AlterEGO Linux Home"
      },
      { "name": "Converters", "children": [] },
      { "name": "CyberTraining", "children": [] },
      { "name": "References", "children": [] },
      { "name": "Resources", "children": [] },
      { "name": "Search", "children": [] },
      { "name": "Sites", "children": [] },
      { "name": "Tools", "children": [] },
      { "name": "Wikipedia", "children": [] }
    ]
  }
}


for x in ["Converters",
          "CyberTraining", 
          "References",
          "Resources",
          "Search",
          "Sites",
          "Tools",
          "Wikipedia"]:
    firefox_policies = add_bookmarks(x)

print(json.dumps(firefox_policies, indent=2))

# con = sql.connect('/usr/local/share/bookmarks.db')
# cur = con.cursor()

# sqlite_select_query = """SELECT * from bookmarks WHERE bookmarks.tags LIKE 'ael%'"""
# cur.execute(sqlite_select_query)
# records = cur.fetchall()

# for row in records:
    # print(len(row))

# options = set()
# for row in records:
    # try:
        # title = f'{row[1]} - {row[2]}'
    # except:
        # title = f'{row[1]}'

    # bk = f'{title:<100}: {row[3]} : {row[4]} : TAGS: {row[5]}\n'
    # options.add(bk)

# options = ''.join(sorted(list(options)))

# with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    # f.write(options)
    # f.seek(0)
    # dumpfile = f.name

# with open(dumpfile, 'r') as f:
    # data = f.read().encode('UTF-8')

# try:
    # fzf = subprocess.run(["fzf",
                          # "--prompt=Bookmarks ❯ ",
                          # "--header= ",
                          # "--no-hscroll",
                          # "--reverse",
                          # "-i",
                          # "--exact",
                          # "--tiebreak=begin",
                          # "--no-info",
                          # "--pointer=•",
                         # ], input=data, stdout=subprocess.PIPE)

    # selection = fzf.stdout
    # url = selection.decode('ascii').split(': ')[1]

    # webbrowser.open_new_tab(url)
# except:
    # pass

# con.close()
# os.remove(dumpfile)

# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
