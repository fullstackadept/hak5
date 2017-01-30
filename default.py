# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Hak5 addon by fullstackadept
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon and infosecflix addon
#
# Author: fullstackadept
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.hak5'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

# menu / playlist config
def hak5_list():
    menu = [
        {
            'title' : 'Hak5 - Weekly dose of Technolust',
            'id' : 'PLW5y1tjAOzI0w_GbtiEbYS5PGJ2pmxAIX',
            'thumbnail' : 'https://www.hak5.org/wp-content/uploads/2016/04/hak5.png'
        },
        {
            'title' : 'Threat Wire - Security, Privacy, and Internet Freedom News!',
            'id' : 'PLW5y1tjAOzI0Sx4UU2fncEwQ9BQLr5Vlu',
            'thumbnail' : 'https://www.hak5.org/wp-content/uploads/2016/04/threatwire.png'
        },
        {
            'title' : 'TekThing - We make technology behave',
            'id' : 'PLee9VmSvXgvSfmS_R12CFbOGA9zxU14Ri',
            'thumbnail' : 'https://www.hak5.org/wp-content/uploads/2016/04/tekthing.png'
        },
        {
            'title' : 'HakTip with Shannon Morse - Easy Tutorial Series!',
            'id' : 'PLA2578BDE9CB9AAB3',
            'thumbnail' : 'https://www.hak5.org/wp-content/uploads/2016/04/haktip.png'
        },
        {
            'title' : 'Best Of Hak5 - Trusting Our Technolust Since 2005',
            'id' : 'PLW5y1tjAOzI2bHS8jo_QkiWFvAgOV9B7k',
            'thumbnail' : 'https://www.hak5.org/wp-content/uploads/2016/04/hak5.png'
        },
        {
            'title' : 'Metasploit Minute - Mondays with Mubix',
            'id' : 'PLW5y1tjAOzI3n4KRN_ic8N8Qv_ss_dh_F',
            'thumbnail' : 'https://www.hak5.org/wp-content/uploads/2016/04/metasploit-minute.png'
        },
        {
            'title' : 'Hak5: SSH Inside and Out - Secure Shell Cryptographic Networks',
            'id' : 'PLW5y1tjAOzI3IjZWkI4Qh0GP2bPTTF83a',
            'thumbnail' : 'https://i.ytimg.com/vi/mh7oTjV73fI/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=KFctha87E8QSb3TdPpIQETHViaA'
        },
        {
            'title' : 'Hak5: Virtualization',
            'id' : 'PLW5y1tjAOzI38EPlT56d-ZoAqvOMw5xai',
            'thumbnail' : 'https://i.ytimg.com/vi/6YwiBdgOwUI/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=fTAk_R3HU10DmgOsCn0biRfT5i8'
        },
        {
            'title' : 'Hak5: VPNs - Everything You Need to Know',
            'id' : 'PLW5y1tjAOzI3YEamgvUlLvtiiQwMsTj3H',
            'thumbnail' : 'https://i.ytimg.com/vi/04EmeXSZo_0/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=4zP_6Jzm15rZVJlUGWqKy02u8PE'
        },
        {
            'title' : 'HakTip: Linux Terminal - Getting Started!',
            'id' : 'PLW5y1tjAOzI2ZYTlMdGzCV8AJuoqW5lKB',
            'thumbnail' : 'https://i.ytimg.com/vi/b5NmtmNwMgU/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=saLY0xKe6aERbleE7Vj63zaD3rY'
        },
        {
            'title' : 'HakTip: Maltego - Open Source Intelligence and Forensics',
            'id' : 'PLW5y1tjAOzI1SRsVRHeWbAz7tBE-cBgIJ',
            'thumbnail' : 'https://i.ytimg.com/vi/wx4mEQZM_0s/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=MANUNTORFsmtQxKdHvET1DtsuAo'
        },
        {
            'title' : 'HakTip: NMap - The Network Mapper for Gurus',
            'id' : 'PLW5y1tjAOzI0ZLv7YfQtToQmc0yVDfkKO',
            'thumbnail' : 'https://i.ytimg.com/vi/iUZ6nTMO8K0/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=1FCLw_v_rKe_V8Cx4NQp1OZIZXw'
        },
        {
            'title' : 'HakTip: Netcat - Network Port Scanning, File Transfers, and More!',
            'id' : 'PLW5y1tjAOzI1v-RQ8rAftvqKawXQR87eL',
            'thumbnail' : 'https://i.ytimg.com/vi/xjB2nBwzzTk/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=l70g8EhRxIDkzSu64EAMt2YJQG8'
        },
        {
            'title' : 'HakTip: Wireshark - Packet Capturing and Analysis',
            'id' : 'PLW5y1tjAOzI30OkWG_rhUstdJTk1FgU2W',
            'thumbnail' : 'https://i.ytimg.com/vi/6X5TwvGXHP0/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=E8ezncbBuk_gr13KBwQK8lRNzHw'
        },
        {
            'title' : 'Hak5: Arduino, Raspberry Pi, and Microcontrollers',
            'id' : 'PLW5y1tjAOzI0hfWzMldhCXQlgv90cn3rb',
            'thumbnail' : 'https://i.ytimg.com/vi/KKhhBttwUpI/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=6dHhur_L6z_-V_RdRv3Ny2XOHhU'
        },
        {
            'title' : 'Hak5: Video Game Hacks and Mods',
            'id' : 'PLW5y1tjAOzI0oeiDgXBMErEhGoGXrJrRW',
            'thumbnail' : 'https://i.ytimg.com/vi/SUEXCCWMfXg/hqdefault.jpg?custom=true&w=246&h=138&stc=true&jpg444=true&jpgq=90&sp=68&sigh=iJ3pMhRz-ASqKAjQsJia-1TM1vY'
        }
    ]

    return menu

# Entry point
def run():
    plugintools.log("docu.run")

    # Get params
    params = plugintools.get_params()

    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"

    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    for item in hak5_list():
        plugintools.add_item(
            #action="",
            title=item['title'],
            url="plugin://plugin.video.youtube/playlist/" + item['id'] + "/",
            thumbnail=item['thumbnail'],
            fanart=item['thumbnail'].replace('w=246&h=138', 'w=492&h=276'),
            folder=True )
run()
