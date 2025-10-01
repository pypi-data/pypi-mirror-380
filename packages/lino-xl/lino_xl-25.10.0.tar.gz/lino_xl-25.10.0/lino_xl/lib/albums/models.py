# -*- coding: UTF-8 -*-
# Copyright 2008-2025 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)


from lino.api import dd, rt, _
from lino.core import constants
from lino.modlib.office.roles import OfficeStaff
from lino.mixins import Hierarchical
from lino.utils.mldbc.mixins import BabelDesignated
# from lino.modlib.uploads.mixins import UploadBase, safe_filename, FileUsable, GalleryViewable
# from lino.modlib.uploads.mixins import UploadBase, safe_filename, GalleryViewable
from lino.modlib.uploads.ui import Uploads


def filename_leaf(name):
    i = name.rfind('/')
    if i != -1:
        return name[i + 1:]
    return name


class Album(BabelDesignated, Hierarchical):

    class Meta:
        abstract = dd.is_abstract_model(__name__, 'Album')
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")


dd.inject_field('uploads.Upload', 'album',
                dd.ForeignKey("albums.Album", blank=True, null=True))


class AlbumDetail(dd.DetailLayout):
    main = """
    treeview_panel general
    """

    general = """
    designation id parent
    FilesByAlbum #AlbumsByAlbum
    """


class Albums(dd.Table):
    model = 'albums.Album'
    required_roles = dd.login_required(OfficeStaff)

    column_names = "designation parent *"
    detail_layout = "albums.AlbumDetail"
    insert_layout = "designation parent"


class FilesByAlbum(Uploads):
    master_key = "album"
    default_display_modes = {None: constants.DISPLAY_MODE_GALLERY}
    column_names = "file description thumbnail *"


class AlbumsByAlbum(Albums):
    label = "Albums"
    master_key = "parent"
