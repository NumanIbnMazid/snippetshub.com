
# possible categories of files
# text = ['textFiles', 'doc', 'docx', 'docm', 'odt', 'pdf', 'txt', 'rtf', 'pages', 'pfb', 'mobi', 'chm', 'tex', 'bib', 'dvi',
#         'abw', 'text', 'epub', 'nfo', 'log', 'log1', 'log2', 'wks', 'wps', 'wpd', 'emlx', 'utf8', 'ichat', 'asc', 'ott', 'fra', 'opf']
# image = ['imageFiles', 'img', 'jpg', 'jpeg', 'png', 'png0', 'ai', 'cr2', 'ico', 'icon', 'jfif', 'tiff', 'tif', 'gif', 'bmp', 'odg', 'djvu', 'odg', 'ai', 'fla', 'pic', 'ps',
#          'psb', 'svg', 'dds', 'hdr', 'ithmb', 'rds', 'heic', 'aae', 'apalbum', 'apfolder', 'xmp', 'dng', 'px', 'catalog', 'ita', 'photoscachefile', 'visual', 'shape', 'appicon', 'icns']
# development = ['devFiles', 'py', 'h', 'm', 'jar', 'cs', 'c', 'c#', 'cpp', 'c++', 'class', 'java', 'php', 'phps', 'php5', 'htm', 'html', 'css', 'xml', '3mf', 'o', 'obj', 'json', 'jsonp', 'blg', 'bbl', 'j', 'jav', 'bash', 'bsh', 'sh', 'rb', 'vb', 'vbscript', 'vbs', 'vhd', 'vmwarevm', 'js', 'jsp', 'xhtml', 'md5', 'nib', 'strings', 'frm', 'myd', 'myi', 'props', 'vcxproj', 'vs', 'lst', 'sol', 'vbox', 'vbox-prev', 'pch',
#                'pdb', 'lib', 'nas', 'assets', 'sql', 'sqlite-wal', 'rss', 'swift', 'xsl', 'manifest', 'up_meta', 'down_meta', 'woff', 'dist', 'sublime-snippet', 'd', 'ashx', 'tpm', 'dsw', 'hpp', 'tga', 'kf', 'rq', 'rdf', 'ttl', 'pyc', 'pyo', 's', 'lua', 'vim', 'p', 'dashtoc', 'org%2f2000%2fsvg%22%20width%3d%2232%22', 'md', 'mo', 'make', 'cmake', 'makefile', 'options', 'def', 'cc', 'f90', 'dcp', 'cxx', 'seto', 'f', 'simt']
# spreadsheet = ['spreadsheetFiles', 'csv', 'odf',
#                'ods', 'xlr', 'xls', 'xlsx', 'numbers', 'xlk']
# system = ['systemFiles', 'bif', 'shs', 'ds_store', 'gadget', 'so', 'idx', 'ipmeta', 'sys', 'dll', 'dylib', 'etl', 'regtrans-ms', 'key', 'lock', 'man', 'inf', 'x86', 'dev', 'config', 'cfg', 'cpl', 'cur', 'dmp', 'drv', 'mot', 'ko', 'supported', 'pxe', 'cgz', '0', 'file', 'install', 'desktop', 'ttc', 'ttf', 'fnt', 'fon', 'otf', 'download', 'acsm', 'ini', 'opt', 'dat', 'sav', 'save', 'aux', 'raw', 'temp', 'tmp', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'cache', 'ipsw', 'stt', 'part', 'appcache', 'sbstore', 'gpd', 'sqm', 'emf',
#           'jrs', 'pri', 'vcrd', 'mui', 'localstorage', 'localstorage-journal', 'data', 'crash', 'webhistory', 'settingcontent-ms', 'itc', 'atx', 'apversion', 'apmaster', 'apdetected', 'pos', 'glk', 'blob', 'cat', 'sns', 'adv', 'asd', 'lrprev', 'csl', 'rdl', 'sthlp', 'tm2', 'mcdb', 'fragment', 'nif', 'blockdata', 'continuousdata', 'upk', 'znb', 'xnb', 'idrc', 'model', 'primitives', 'ovl', 'sid', 'stringtable', 'foliage', 'civ4savedgame', 'cgs', 'thewitchersave', 'pssg', 'pac', 'unity3d', 'ifi', 'vmt', 'vtf', 'pfm', 'deu', 'map', 'simss']
# executable = ['executableFiles', 'exe', 'bat', 'dmg',
#               'msi', 'bin', 'pak', 'app', 'com', 'application']
# archive = ['archiveFiles', 'zip', 'gz', 'rar', 'cab', 'iso', 'tar', 'lzma', 'bz2', 'pkg', 'xz', '7z', 'vdi', 'ova', 'rpm', 'z',
#            'tgz', 'deb', 'vcd', 'ost', 'vmdk', '001', '002', '003', '004', '005', '006', '007', '008', '009', 'arj', 'package', 'ims']
# backup = ['backupFiles', 'bak', 'backup', 'back']
# database = ['databaseFiles', 'accdb', 'accde', 'mdb', 'mde', 'odb', 'db', 'gdbtable', 'gdbtablx', 'gdbindexes', 'sqlite', 'enz',
#             'enl', 'sdf', 'hdb', 'cdb', 'gdb', 'cif', 'xyz', 'mat', 'bgl', 'r', 'exp', 'asy', 'info', 'meta', 'adf', 'appinfo', 'xg0', 'yg0']
# presentation = ['presentationFiles', 'ppt',
#                 'pptx', 'pps', 'ppsx', 'odp', 'key']
# bookmark = ['bookmarkFiles', 'torrent', 'url']
# pim = ['PIMFiles', 'dbx', 'eml', 'msg', 'ics', 'pst', 'vcf', 'gdb', 'ofx', 'qif', 'rem', 'tax', 'qbmb', 'one', 'note', 'olk14message', 'olk14msgattach',
#        'olk14folder', 'olkmsgsource', 'olk14msgsource', 'olk15message', 'olk15messageattachment', 'olk14event', 'olk15msgattachment', 'olk15msgsource', 'vcs', 'hbk']
# shortcut = ['shortcutFiles', 'lnk']
# unidentifiable = 'unidentifiableFiles'


audio = ['audioFiles', 'mp3', 'm3u', 'm4a', 'wav', 'ogg', 'flac', 'midi', 'oct', 'aac', 'aiff', 'aif', 'wma',
         'pcm', 'cda', 'mid', 'mpa', 'ens', 'adg', 'dmpatch', 'sngw', 'seq', 'wem', 'mtp', 'l6t', 'lng', 'adx', 'link']
video = ['videoFiles', 'mpg', 'mpeg', 'mpeg4', 'mpegps', 'avi', 'mp4', 'flv', 'h264', 'mov',
         'mk4', 'swf', 'wmv', 'mkv', 'plist', 'm4v', 'trec', '3g2', '3gp', '3gpp', 'rm', 'vob', 'webm', 'dnxhr', 'prores', 'cineform', 'hevc(h265)']


def categorize_audio_video_files(extension):
    if extension.lower() in audio:
        return 'audio'
    elif extension.lower() in video:
        return 'video'
    else:
        return "uncategorized"