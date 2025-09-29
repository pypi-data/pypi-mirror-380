# Routines related to ownCloud

import time
import zipfile
import collections
import logging
import base64
import sys
from . import webdav
from urllib.parse import urlparse


import ufload3

def _splitCloudName(x):
    spl = x.split(":", 1)
    # no :, so use the default cloud hostname
    if len(spl) == 1:
        return ('cloud.msf.org', x)
    return (spl[0], spl[1])

#Simple enough: we just delete the first four characters and then base64-decode the remaining string
def _decrypt(pwd):
    pwd = pwd.strip()
    x = pwd[4:]
    try:
        x = str(base64.b64decode(x), 'utf8')
        return x
    except:
        ufload3.progress('Unable to decode password')
        print(sys.exc_info()[0])


def instance_to_dir(instance):
    #instance name ends with "_OCA"
    if instance.endswith('_OCA'):
        return '/personal/UF_OCA_msf_geneva_msf_org/'
    #instance name starts with "OCB"
    if instance.startswith('OCB'):
        return '/personal/UF_OCB_msf_geneva_msf_org/'
    # instance name starts with "OCB"
    if instance.startswith('OCP'):
        return '/personal/UF_OCP_msf_geneva_msf_org/'
    #instance name starts with "OCG_"
    if instance.startswith('OCG_'):
        return '/personal/UF_OCG_msf_geneva_msf_org/'

    return ''

def get_cloud_info(args, sub_dir=''):

    #Cloud path depends on the OC
    if args.oc:
        dir = '/personal/UF_' + args.oc.upper() + '_msf_geneva_msf_org/'
    else:
        dir = ''    #No OC specified, let's use only the path

    sub = args.cloud_path

    try:
        #if the argument patchcloud is set, we're downloading the upgrade patch, go to the right directory (MUST be under the main dir)
        if (sub_dir is not None):
            sub = sub + sub_dir
    except:
        #The argument cloudpath is not defined, forget about it (this is not the upgrade process)
        pass
    
    if args.cert_path:
        with open(args.cert_path, 'r') as c:
            args.cert_content = c.read()

    ret = {
        'url': args.cloud_url,
        'dir': dir + sub,
        'site': dir,
        'path': args.cloud_path,
        'tenant': args.tenant,
        'client_id': args.client_id,
        'cert_content': args.cert_content,
    }

    return ret


def get_onedrive_connection(args):
    info = get_cloud_info(args)
    if not info.get('url'):
        ufload3.progress('URL is not set!')
    if not info.get('tenant'):
        ufload3.progress('Tenant is not set!')
    if not info.get('client_id'):
        ufload3.progress('Client_id is not set!')
    if not info.get('cert_content'):
        ufload3.progress('Cert is not set!')

    url = urlparse(info['url'])
    if not url.netloc:
        ufload3.progress('Unable to parse url: %s') % (info['url'])

    path = info.get('site') + url.path

    try:
        dav = webdav.Client(url.netloc, tenant=info['tenant'], client_id= info['client_id'], cert_content=info['cert_content'], path=path)
        return dav
    except webdav.ConnectionFailed as e:
        ufload3.progress('Unable to connect: {}'.format(e))
        ufload3.progress('Cannot proceed without connection, exiting program.')
        exit(1)




def _get_all_files_and_timestamp(dav, d):
    ufload3.progress('Browsing files from dir %s' % d)
    try:
        #all_zip = dav.ls(d)
        all_zip = dav.list(d)
    except Exception as e:
        ufload3.progress("Cloud Exception 88")
        logging.warn(str(e))
        return []

    ret = []
    for f in all_zip:
        #if not f['Name'] or f['Name'][-1] == '/':
        if not f.name:
            continue

        # We don't take into consideration backups that are too recent.
        # Otherwise they could be half uploaded (=> corrupted)
        if abs(time.time() - f.time_last_modified.timestamp()) < 900:
            continue

        # ufload3.progress('File found: %s' % f['Name'])

        if f.name.split(".")[-1] != "zip":
            logging.warn("Ignoring non-zipfile: %s" % f.name)
            continue
        ret.append((f.time_last_modified, f.name, f.serverRelativeUrl))
    return ret

# returns True if x has instance as a substring
def _match_instance_name(instance, x):
    for pat in instance.split(','):
        if pat in x:
            return True
    return False

# returns True is any of the instances match x
# (returns True for all if instances is empty)
def _match_any_wildcard(instances, x):
    if not instances:
        return True

    for i in instances:
        if _match_instance_name(i, x):
            return True
    return False

def _group_files_to_download(files):
    files.sort()
    files.reverse()
    ret = collections.defaultdict(lambda : [])

    for a in files:
        t, f, u = a
        #if '/' not in f:
        #   raise Exception("no slash in %s" % f)

        #isplit = f.rindex('/')
        #filename = f[isplit+1:]
        if '-' not in f:
            ufload3.progress("filename is missing expected dash: "+ f)
            continue

        instance = '-'.join(f.split('-')[:-1])
        ret[instance].append((u, f))

    return ret

# list_files returns a dictionary of instances
# and for each instance, a list of (path,file) tuples
# in order from new to old.
def list_files(**kwargs):
    directory = kwargs['where']

    #all = _get_all_files_and_timestamp(dav, "/remote.php/webdav/"+directory)
    all = _get_all_files_and_timestamp(kwargs['dav'], directory)

    all = _group_files_to_download(all)

    inst = []
    if kwargs['instances'] is not None:
        inst = [x.lower() for x in kwargs['instances']]

    ret = {}
    for i in all:
        if _match_any_wildcard(inst, i.lower()):
            ret[i] = all[i]
    return ret

# list_files returns a dictionary of instances
# and for each instance, a list of (path,file) tuples
# in order from new to old.
def list_patches(**kwargs):
    directory = kwargs['where']

    all = _get_all_files_and_timestamp(kwargs['dav'], directory)

    return all



def peek_inside_local_file(path, fn):
    try:
        z = zipfile.ZipFile(fn)
    except Exception as e:
        ufload3.progress("Zipfile %s: could not read: %s" % (fn, e))
        return None

    names = z.namelist()
    if len(names) == 0:
        ufload3.progress("Zipfile %s has no files in it." % fn)
        return None
    if len(names) != 1:
        ufload3.progress("Zipfile %s has unexpected files in it: %s" % (fn, names))
        return None
    n = names[0]
    z.close()
    del z
    return n


def dlProgress(pct):
    ufload3.progress("Downloaded %d%%" % pct)

# Returns a file-like-object
#def openDumpInZip(path, fn, **kwargs):
def openDumpInZip(fn):
    #file = open(fn, 'r')
    z = zipfile.ZipFile(fn)
    names = z.namelist()
    if len(names) == 0:
        logging.warn("Zipfile %s has no files in it." % fn)
        return None, 0
    if len(names) != 1:
        logging.warn("Zipfile %s has unexpected files in it: %s" % (fn, names))
        return None, 0
    try:
        file = z.open(names[0])
    except:
        logging.warn("Zipfile %s is probably corrupted" % fn)
        return None, 0

    filename = file.name
    size = z.getinfo(names[0]).file_size
    file.close()
    z.close()
    del file
    del z

    #return z.open(names[0]), z.getinfo(names[0]).file_size
    return filename, size


# An object that copies input to output, calling
# the progress callback along the way.
class StatusFile(object):
    def __init__(self, fout, progress):
        self.fout = fout
        self.progress = progress
        self.tot = None
        self.next = 10
        self.n = 0
        
    def setSize(self, sz):
        self.tot = float(sz)
        
    def write(self, data):
        self.n += len(data)
        if self.tot is not None:
            pct = int(self.n/self.tot*100)
            if pct > self.__next__:
                self.next = (pct/10)*10+10
                self.progress(pct)
        self.fout.write(data)

