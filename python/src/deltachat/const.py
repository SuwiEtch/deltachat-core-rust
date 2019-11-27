import sys
import re
import os
from os.path import dirname, abspath
from os.path import join as joinpath

# the following const are generated from deltachat.h
# this works well when you in a git-checkout
# run "python deltachat/const.py" to regenerate events
# begin const generated
DC_GCL_ARCHIVED_ONLY = 0x01
DC_GCL_NO_SPECIALS = 0x02
DC_GCL_ADD_ALLDONE_HINT = 0x04
DC_GCL_VERIFIED_ONLY = 0x01
DC_GCL_ADD_SELF = 0x02
DC_QR_ASK_VERIFYCONTACT = 200
DC_QR_ASK_VERIFYGROUP = 202
DC_QR_FPR_OK = 210
DC_QR_FPR_MISMATCH = 220
DC_QR_FPR_WITHOUT_ADDR = 230
DC_QR_ADDR = 320
DC_QR_TEXT = 330
DC_QR_URL = 332
DC_QR_ERROR = 400
DC_CHAT_ID_DEADDROP = 1
DC_CHAT_ID_TRASH = 3
DC_CHAT_ID_MSGS_IN_CREATION = 4
DC_CHAT_ID_STARRED = 5
DC_CHAT_ID_ARCHIVED_LINK = 6
DC_CHAT_ID_ALLDONE_HINT = 7
DC_CHAT_ID_LAST_SPECIAL = 9
DC_CHAT_TYPE_UNDEFINED = 0
DC_CHAT_TYPE_SINGLE = 100
DC_CHAT_TYPE_GROUP = 120
DC_CHAT_TYPE_VERIFIED_GROUP = 130
DC_MSG_ID_MARKER1 = 1
DC_MSG_ID_DAYMARKER = 9
DC_MSG_ID_LAST_SPECIAL = 9
DC_STATE_UNDEFINED = 0
DC_STATE_IN_FRESH = 10
DC_STATE_IN_NOTICED = 13
DC_STATE_IN_SEEN = 16
DC_STATE_OUT_PREPARING = 18
DC_STATE_OUT_DRAFT = 19
DC_STATE_OUT_PENDING = 20
DC_STATE_OUT_FAILED = 24
DC_STATE_OUT_DELIVERED = 26
DC_STATE_OUT_MDN_RCVD = 28
DC_CONTACT_ID_SELF = 1
DC_CONTACT_ID_INFO = 2
DC_CONTACT_ID_DEVICE = 5
DC_CONTACT_ID_LAST_SPECIAL = 9
DC_MSG_TEXT = 10
DC_MSG_IMAGE = 20
DC_MSG_GIF = 21
DC_MSG_STICKER = 23
DC_MSG_AUDIO = 40
DC_MSG_VOICE = 41
DC_MSG_VIDEO = 50
DC_MSG_FILE = 60
DC_LP_AUTH_OAUTH2 = 0x2
DC_LP_AUTH_NORMAL = 0x4
DC_LP_IMAP_SOCKET_STARTTLS = 0x100
DC_LP_IMAP_SOCKET_SSL = 0x200
DC_LP_IMAP_SOCKET_PLAIN = 0x400
DC_LP_SMTP_SOCKET_STARTTLS = 0x10000
DC_LP_SMTP_SOCKET_SSL = 0x20000
DC_LP_SMTP_SOCKET_PLAIN = 0x40000
DC_CERTCK_AUTO = 0
DC_CERTCK_STRICT = 1
DC_CERTCK_ACCEPT_INVALID_HOSTNAMES = 2
DC_CERTCK_ACCEPT_INVALID_CERTIFICATES = 3
DC_EMPTY_MVBOX = 0x01
DC_EMPTY_INBOX = 0x02
DC_EVENT_INFO = 100
DC_EVENT_SMTP_CONNECTED = 101
DC_EVENT_IMAP_CONNECTED = 102
DC_EVENT_SMTP_MESSAGE_SENT = 103
DC_EVENT_IMAP_MESSAGE_DELETED = 104
DC_EVENT_IMAP_MESSAGE_MOVED = 105
DC_EVENT_IMAP_FOLDER_EMPTIED = 106
DC_EVENT_NEW_BLOB_FILE = 150
DC_EVENT_DELETED_BLOB_FILE = 151
DC_EVENT_WARNING = 300
DC_EVENT_ERROR = 400
DC_EVENT_ERROR_NETWORK = 401
DC_EVENT_ERROR_SELF_NOT_IN_GROUP = 410
DC_EVENT_MSGS_CHANGED = 2000
DC_EVENT_INCOMING_MSG = 2005
DC_EVENT_MSG_DELIVERED = 2010
DC_EVENT_MSG_FAILED = 2012
DC_EVENT_MSG_READ = 2015
DC_EVENT_CHAT_MODIFIED = 2020
DC_EVENT_CONTACTS_CHANGED = 2030
DC_EVENT_LOCATION_CHANGED = 2035
DC_EVENT_CONFIGURE_PROGRESS = 2041
DC_EVENT_IMEX_PROGRESS = 2051
DC_EVENT_IMEX_FILE_WRITTEN = 2052
DC_EVENT_SECUREJOIN_INVITER_PROGRESS = 2060
DC_EVENT_SECUREJOIN_JOINER_PROGRESS = 2061
DC_EVENT_SECUREJOIN_MEMBER_ADDED = 2062
DC_EVENT_FILE_COPIED = 2055
DC_EVENT_IS_OFFLINE = 2081
DC_EVENT_GET_STRING = 2091
DC_STR_SELFNOTINGRP = 21
DC_PROVIDER_STATUS_OK = 1
DC_PROVIDER_STATUS_PREPARATION = 2
DC_PROVIDER_STATUS_BROKEN = 3
DC_STR_NOMESSAGES = 1
DC_STR_SELF = 2
DC_STR_DRAFT = 3
DC_STR_MEMBER = 4
DC_STR_CONTACT = 6
DC_STR_VOICEMESSAGE = 7
DC_STR_DEADDROP = 8
DC_STR_IMAGE = 9
DC_STR_VIDEO = 10
DC_STR_AUDIO = 11
DC_STR_FILE = 12
DC_STR_STATUSLINE = 13
DC_STR_NEWGROUPDRAFT = 14
DC_STR_MSGGRPNAME = 15
DC_STR_MSGGRPIMGCHANGED = 16
DC_STR_MSGADDMEMBER = 17
DC_STR_MSGDELMEMBER = 18
DC_STR_MSGGROUPLEFT = 19
DC_STR_GIF = 23
DC_STR_ENCRYPTEDMSG = 24
DC_STR_E2E_AVAILABLE = 25
DC_STR_ENCR_TRANSP = 27
DC_STR_ENCR_NONE = 28
DC_STR_CANTDECRYPT_MSG_BODY = 29
DC_STR_FINGERPRINTS = 30
DC_STR_READRCPT = 31
DC_STR_READRCPT_MAILBODY = 32
DC_STR_MSGGRPIMGDELETED = 33
DC_STR_E2E_PREFERRED = 34
DC_STR_CONTACT_VERIFIED = 35
DC_STR_CONTACT_NOT_VERIFIED = 36
DC_STR_CONTACT_SETUP_CHANGED = 37
DC_STR_ARCHIVEDCHATS = 40
DC_STR_STARREDMSGS = 41
DC_STR_AC_SETUP_MSG_SUBJECT = 42
DC_STR_AC_SETUP_MSG_BODY = 43
DC_STR_SELFTALK_SUBTITLE = 50
DC_STR_CANNOT_LOGIN = 60
DC_STR_SERVER_RESPONSE = 61
DC_STR_MSGACTIONBYUSER = 62
DC_STR_MSGACTIONBYME = 63
DC_STR_MSGLOCATIONENABLED = 64
DC_STR_MSGLOCATIONDISABLED = 65
DC_STR_LOCATION = 66
DC_STR_STICKER = 67
DC_STR_DEVICE_MESSAGES = 68
DC_STR_COUNT = 68
# end const generated


def read_event_defines(f):
    rex = re.compile(r'#define\s+((?:DC_EVENT|DC_QR|DC_MSG|DC_LP|DC_EMPTY|DC_CERTCK|DC_STATE|DC_STR|'
                     r'DC_CONTACT_ID|DC_GCL|DC_CHAT|DC_PROVIDER)_\S+)\s+([x\d]+).*')
    for line in f:
        m = rex.match(line)
        if m:
            yield m.groups()


if __name__ == "__main__":
    here = abspath(__file__).rstrip("oc")
    here_dir = dirname(here)
    if len(sys.argv) >= 2:
        deltah = sys.argv[1]
    else:
        deltah = joinpath(dirname(dirname(dirname(here_dir))), "deltachat-ffi", "deltachat.h")
    assert os.path.exists(deltah)

    lines = []
    skip_to_end = False
    for orig_line in open(here):
        if skip_to_end:
            if not orig_line.startswith("# end const"):
                continue
            skip_to_end = False
        lines.append(orig_line)
        if orig_line.startswith("# begin const"):
            with open(deltah) as f:
                for name, item in read_event_defines(f):
                    lines.append("{} = {}\n".format(name, item))
            skip_to_end = True

    tmpname = here + ".tmp"
    with open(tmpname, "w") as f:
        f.write("".join(lines))
    os.rename(tmpname, here)
