#!/usr/bin/env python

#
# Copyright 2025 Chris Josephes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

'''
Write out XML data for an album.
'''

import datetime
import os.path
from musicscan.xml.builder import (CompleteCompactDiscXML,
                                   SplitCompactDiscXML, Index, AlbumElementXML)


class XMLFileWriter():
    '''
    Class to write out XML files.

    Handles opening files, writing data, and closing the handle.
    '''
    def __init__(self, in_path=None):
        self._path = in_path
        self._debug = False
        self._overwrite = False
        self._split_xml = False
        self._manifest = False
        self.files_written = 0
        self.files_out = []

    def debug(self):
        '''
        Return the debug value.
        '''
        return self._debug

    def set_debug(self, in_debug):
        '''
        Set the debug value.
        '''
        self._debug = in_debug

    def overwrite(self):
        '''
        Return the overwrite value.
        '''
        return self._overwrite

    def set_overwrite(self, in_overwrite):
        '''
        Set the overwrite value.
        '''
        self._overwrite = in_overwrite

    def split_xml(self):
        '''
        Return the split_xml value.
        '''
        return self._split_xml

    def set_split_xml(self, in_split_xml):
        '''
        Set the split_xml value.
        '''
        self._split_xml = in_split_xml

    def manifest(self):
        '''
        Return the manifest value.
        '''
        return self._manifest

    def set_manifest(self, in_manifest):
        '''
        Set the manifest value.
        '''
        self._manifest = in_manifest

    def identify_files(self, in_album, in_type='audiocd'):
        '''
        Identify all possible files from an passed album.
        '''
        file_list = []
        file_list.append(self._path + '/' + in_album.filename(in_type))
        if self._split_xml:
            file_list.append(self._path + '/' + in_album.filename('album'))
            for dsc in sorted(in_album.discs):
                dsc_o = in_album.discs[dsc]
                f_str = f"cd{dsc_o.disc_no:02}-index"
                file_list.append(self._path + '/' + in_album.filename(f_str))
        return file_list

    def write_xml(self, in_album):
        '''
        Write out the XML data.
        '''
        if self._split_xml:
            self.write_split_xml(in_album)
        else:
            self.write_single_xml(in_album)
        if self._manifest and len(self.files_out) > 0:
            self.write_manifest_file()

    def write_single_xml(self, in_album):
        '''
        Write all the XML data in a single file.
        '''
        f_name = in_album.filename('audiocd')
        complete = self._path + '/' + f_name
        audiocd = CompleteCompactDiscXML(self._debug)
        if not os.path.isfile(complete) or self._overwrite:
            with open(complete, mode='w', encoding='utf-8') as f_handle:
                f_handle.write(audiocd.build(in_album))
                f_handle.close()
                self.files_written += 1
                self.files_out.append(f_name)

    def write_split_xml(self, in_album):
        '''
        Write multiple XML files.
        '''
        self.write_split_xml_audiocd(in_album)
        self.write_split_xml_index(in_album)
        self.write_split_xml_album(in_album)

    def write_split_xml_audiocd(self, in_album):
        '''
        Write the XML data pertaining to the audio CD.
        '''
        f_name = in_album.filename('audiocd')
        complete = self._path + '/' + f_name
        audiocd = SplitCompactDiscXML(self._debug)
        if not os.path.isfile(complete) or self._overwrite:
            with open(complete, mode='w', encoding='utf-8') as f_handle:
                f_handle.write(audiocd.build(in_album))
                f_handle.close()
                self.files_written += 1
                self.files_out.append(f_name)

    def write_split_xml_index(self, in_album):
        '''
        Write the XML data pertaining to the CD index.
        '''
        index = Index(self._debug)
        for dsc in sorted(in_album.discs):
            dsc_o = in_album.discs[dsc]
            f_str = f"cd{dsc_o.disc_no:02}-index"
            f_name = in_album.filename(f_str)
            complete = self._path + '/' + f_name
            if not os.path.isfile(complete) or self._overwrite:
                with open(complete, mode='w', encoding='utf-8') as f_handle:
                    f_handle.write(index.build_index_per_cd(dsc_o, True))
                    f_handle.close()
                    self.files_written += 1
                    self.files_out.append(f_name)

    def write_split_xml_album(self, in_album):
        '''
        Write out the XML data pertaining to the album contents.
        '''
        f_name = in_album.filename('album')
        complete = self._path + '/' + f_name
        album = AlbumElementXML(self._debug)
        if not os.path.isfile(complete) or self._overwrite:
            with open(complete, mode='w', encoding='utf-8') as f_handle:
                f_handle.write(album.build_standalone_album(in_album))
                f_handle.close()
                self.files_written += 1
                self.files_out.append(f_name)

    def write_manifest_file(self):
        '''
        Create a file listing all files that have been output.
        '''
        t_stamp = datetime.datetime.now()
        f_name = 'FILES_WRITTEN-'
        f_name += t_stamp.strftime("%Y%m%dT%H%M%S")
        f_name += '.txt'
        complete = self._path + '/' + f_name
        with open(complete, mode='w', encoding='utf-8') as f_handle:
            for xml_file in self.files_out:
                f_handle.write(xml_file+'\n')
            f_handle.close()
