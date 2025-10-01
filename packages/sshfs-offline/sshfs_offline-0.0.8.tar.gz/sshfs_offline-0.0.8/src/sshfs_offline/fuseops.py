import errno
from logging import getLogger
import os
from pathlib import Path

from sshfs_offline import metrics
from sshfs_offline import sftp

from fuse import FUSE, FuseOSError, Operations

from sshfs_offline.cache import data
from sshfs_offline.cache import metadata
from sshfs_offline import log

class FuseOps(Operations):
    '''
    SSH File System with offline access to cached files.
    '''    
                        
    def __init__(self, args): 
        self.debug = args.debug       
        host = args.host
        user = args.user
        if args.remotedir == None:
            remotedir = os.path.join('/home', user)
        else:
            remotedir = args.remotedir
        port = args.port
               
        self.log = getLogger(log.MAIN)
       
        metrics.counts = metrics.Metrics()
        sftp.manager = sftp.SFTPManager(host, user, remotedir, port) 
        metadata.cache = metadata.Metadata(host, remotedir, args.cachetimeout)
        data.cache = data.Data(host, remotedir)

        sftp.manager.sftp() # verify connection to host

        try:
            fuse = FUSE(
                self,
                args.mountpoint,
                foreground=args.debug,
                nothreads=False,
                allow_other=True,
                big_writes=True,
                max_read=sftp.BLOCK_SIZE, # Set max read size (e.g., 128KB)
                max_write=sftp.BLOCK_SIZE, # Set max write size (e.g., 128KB)
            )
        except Exception as e:
            pass

    def init(self, path):
        metrics.counts.incr('init')
        metrics.counts.start()
        log.Log().setupConfig(self.debug)
        sftp.manager.startKeepalive()        
         
    def chmod(self, path, mode): 
        try: 
            self.log.debug('-> chmod: %s %s', path, mode)   
            metrics.counts.incr('chmod')     
            metadata.cache.deleteMetadata(path)
            sftp.manager.sftp().chmod(sftp.fixPath(path), mode)
            self.log.debug('<- chmod: %s', path) 
        except Exception as e:
            self.log.error('<- chmod: %s %s', path, mode) 
            metrics.counts.incr('chmod_except') 
            raise e

    def chown(self, path, uid, gid):
        try:
            self.log.debug('-> chown: %s %s %s', path, uid, gid) 
            metrics.counts.incr('chown') 
            metadata.cache.deleteMetadata(path)
            sftp.manager.sftp().chown(sftp.fixPath(path), uid, gid)  
            self.log.debug('<- chown: %s', path)  
        except Exception as e:
            self.log.error('<- chown: %s %s %s', path, uid, gid) 
            metrics.counts.incr('chown_except') 
            raise e
        
    def create(self, path, mode):  
        try:
            self.log.debug('-> create: %s %s', path, mode)  
            metrics.counts.incr('create')     
            metadata.cache.deleteMetadata(path)
            metadata.cache.deleteParentMetadata(path)
            f = sftp.manager.sftp().open(sftp.fixPath(path), 'w')
            f.chmod(mode)
            f.close()
            self.log.debug('<- create: %s', path)             
            return 0
        except Exception as e:
            self.log.error('<- create: %s %s', path, mode) 
            metrics.counts.incr('create_except')  
            raise e       

    def destroy(self, path):  
        try:
            self.log.debug('-> destroy: %s', path)  
            metrics.counts.incr('destroy')     
            sftp.manager.sftp().close()        
            self.log.debug('<- destroy: %s', path) 
        except Exception as e:
            self.log.error('<- destroy: %s', path)  
            metrics.counts.incr('destroy_except') 
            raise e
        finally:
            metrics.counts.stop()
            sftp.manager.stop()

    def getattr(self, path, fh=None):
        try:
            self.log.debug('-> getattr: %s', path)
            metrics.counts.incr('getattr')
            d = metadata.cache.getattr(path)
            if d != None:
                if d == {}:
                    raise FuseOSError(errno.ENOENT)
                else:
                    self.log.debug('<- getattr: %s', path)
                    return d # cache hit
            
            try:
                st = sftp.manager.sftp().lstat(sftp.fixPath(path))            
            except IOError as e: 
                metadata.cache.getattr_save(path, {}) # negative cache entry          
                raise FuseOSError(errno.ENOENT)

            d = dict((key, getattr(st, key)) for key in (
                'st_atime', 'st_gid', 'st_mode', 'st_mtime', 'st_size', 'st_uid'))
            metadata.cache.getattr_save(path, d)
            self.log.debug('<- getattr: %s %s', path, d)
            return d
        except Exception as e:
            if not isinstance(e,  OSError) and OSError(e).errno != errno.ENOENT:                
                self.log.error('<- getattr: %s %s', path, e)
                metrics.counts.incr('getattr_except') 
            raise e        
        
    def statfs(self, path): 
        try:
            self.log.debug('-> statfs: %s', path) 
            metrics.counts.incr('statfs')      
            stv = data.cache.statvfs(path)        
            dic = dict((key, getattr(stv, key)) for key in ('f_bavail', 'f_bfree',
                'f_blocks', 'f_bsize', 'f_favail', 'f_ffree', 'f_files', 'f_flag',
                'f_frsize', 'f_namemax'))
            self.log.debug('<- statfs: %s %s', path, dic)
            return dic
        except Exception as e:
            self.log.error('<- statfs: %s', path) 
            metrics.counts.incr('statfs_except')       
            raise e

    def mkdir(self, path, mode): 
        try: 
            self.log.debug('-> mkdir: %s %s', path, mode) 
            metrics.counts.incr('mkdir')      
            metadata.cache.deleteMetadata(path)
            metadata.cache.deleteParentMetadata(path)
            sftp.manager.sftp().mkdir(sftp.fixPath(path), mode)
            self.log.debug('<- mkdir: %s', path)
        except Exception as e:
            self.log.error('<- mkdir: %s %s', path, mode) 
            metrics.counts.incr('mkdir_except')  
            raise e

    def read(self, path, size, offset, fh):  
        try:
            self.log.debug('-> read: %s size=%d offset=%d', path, size, offset)
            metrics.counts.incr('read')

            buf = data.cache.read(path, size, offset, fh)

            self.log.debug('<- read: %s %d', path, len(buf))
            return buf
        except Exception as e:
            self.log.error('<- read: %s %s %d', path, size, offset) 
            metrics.counts.incr('read_except') 
            raise e
        
    def readdir(self, path, fh):
        try:
            self.log.debug('-> readdir: %s', path)
            metrics.counts.incr('readdir')
            s = metadata.cache.readdir(path)
            if s != None:
                self.log.debug('<- readdir: %s %d', path, len(s))
                return s
            s = ['.', '..'] + [name
                                for name in sftp.manager.sftp().listdir(sftp.fixPath(path))]
            metadata.cache.readdir_save(path, s)        
            s = metadata.cache.readdir(path)
            self.log.debug('<- readdir: %s %d', path, len(s))
            return s
        except Exception as e:
            self.log.error('<- readdir: %s', path)
            metrics.counts.incr('readdir_except') 
            raise e

    def readlink(self, path):
        try:
            self.log.debug('-> readlink: %s', path)
            metrics.counts.incr('readlink')
            link = metadata.cache.readlink(path)
            if link == None:        
                link = sftp.manager.sftp().readlink(sftp.fixPath(path))
                metadata.cache.readlink_save(path, link)
            
            self.log.debug('<- readlink: %s %s', path, link)
            return link
        except Exception as e:
            self.log.error('<- readlink: %s', path)
            metrics.counts.incr('readlink_except') 
            raise e

    def rename(self, old, new):
        try:
            self.log.debug('-> rename: %s %s', old, new) 
            metrics.counts.incr('rename')       
            metadata.cache.deleteMetadata(old)
            sftp.manager.sftp().rename(sftp.fixPath(old), sftp.fixPath(new))
            self.log.debug('<- rename: %s %s', old, new)
        except Exception as e:
            self.log.error('<- rename: %s %s', old, new) 
            metrics.counts.incr('rename_except')   
            raise e

    def rmdir(self, path):  
        try:
            self.log.debug('-> rmdir: %s', path)   
            metrics.counts.incr('rmdir')  
            metadata.cache.deleteMetadata(path)
            metadata.cache.deleteParentMetadata(path)
            sftp.manager.sftp().rmdir(sftp.fixPath(path))
            self.log.debug('<- rmdir: %s', path)    
        except Exception as e:
            self.log.error('<- rmdir: %s', path)  
            metrics.counts.incr('rmdir_except') 
            raise e

    def symlink(self, target, source): 
        try:
            self.log.debug('-> symlink: %s %s', target, source)   
            metrics.counts.incr('symlink')        
            sftp.manager.sftp().symlink(sftp.fixPath(source), sftp.fixPath(target))
            self.log.debug('<- symlink: %s %s', target, source)     
        except Exception as e:
            self.log.error('<- symlink: %s %s', target, source) 
            metrics.counts.incr('symlink_except')   
            raise e

    def truncate(self, path, length, fh=None):  
        try:
            self.log.debug('-> truncate: %s %d', path, length)  
            metrics.counts.incr('truncate')         
            metadata.cache.deleteMetadata(path)
            data.cache.deleteStaleFile(path)
            sftp.manager.sftp().truncate(sftp.fixPath(path), length)
            self.log.debug('<- truncate: %s', path)   
        except Exception as e:
            self.log.error('<- truncate: %s %d', path, length)  
            metrics.counts.incr('truncate_except') 
            raise e  

    def unlink(self, path):  
        try: 
            self.log.debug('-> unlink: %s', path)    
            metrics.counts.incr('unlink')     
            metadata.cache.deleteMetadata(path)
            metadata.cache.deleteParentMetadata(path)
            data.cache.deleteStaleFile(path)
            sftp.manager.sftp().unlink(sftp.fixPath(path))
            self.log.debug('<- unlink: %s', path)    
        except Exception as e:
            self.log.error('<- unlink: %s', path)   
            metrics.counts.incr('unlink_except') 
            raise e

    def utimens(self, path, times=None):
        try:
            self.log.debug('-> utimens: %s', path) 
            metrics.counts.incr('utimens')   
            metadata.cache.deleteMetadata(path)
            data.cache.deleteStaleFile(path)
            sftp.manager.sftp().utime(sftp.fixPath(path), times)
            self.log.debug('<- utimens: %s', path)   
        except Exception as e:
            self.log.error('<- utimens: %s', path) 
            metrics.counts.incr('utimens_except') 
            raise e 

    def write(self, path, buf, offset, fh): 
        try:       
            self.log.debug('-> write: %s size=%d offset=%d', path, len(buf), offset)
            metrics.counts.incr('write')
            metadata.cache.deleteMetadata(path)  
            data.cache.deleteStaleFile(path)
            #self.log.debug('write: write to remote file %s %d', path, offset)
            with sftp.manager.sftp().open(sftp.fixPath(path), 'r+') as file:
                file.seek(offset, 0)
                file.write(buf)                
                file.close()
            self.log.debug('<- write: %s %d', path, len(buf))
            return len(buf)
        except Exception as e:
            self.log.error('<- write: %s %d', path, offset)
            metrics.counts.incr('write_except') 
            raise e     