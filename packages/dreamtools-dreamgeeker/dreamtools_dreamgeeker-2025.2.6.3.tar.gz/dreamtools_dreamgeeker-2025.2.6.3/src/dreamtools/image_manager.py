# -*- coding: utf-8 -*-
# project/dreamtools-dreamgeeker/image_manager.py
_all_ = ['ImageManager', 'TYPE_IMG_JPEG', 'TYPE_IMG_PNG', 'TYPE_IMG_GIF', 'TYPE_IMG_WEBP', 'TYPE_IMG_SVG']

import copy
import os
from io import BytesIO

from PIL import Image, ImageFile, ImageDraw
from PIL.ExifTags import TAGS
from PIL.TiffImagePlugin import ImageFileDirectory_v2

from . import file_manager
from .controller_manager import ControllerEngine
from .tracking_manager import TrackingManager

TYPE_IMG_JPEG = 'JPEG'
TYPE_IMG_PNG = 'PNG'
TYPE_IMG_GIF = 'GIF'
TYPE_IMG_WEBP = 'WEBP'
TYPE_IMG_SVG = "SVG"

"""
Class CImagine
=============================

Class permettant le traitement d'une image png convertit en jpg avec prise en charge de la transparence (fond blanc)


pathfile : dreamtools-dreamgeeker/pyimaging

"""

MAX_SIZE = 640
MIN_SIZE = 200


class ImageManager(object):
    size_max: int
    size_thumb_max: int

    def __init__(self, src, dest, size_max=MAX_SIZE, size_thumb_max=MIN_SIZE):
        """
        Preparation image  pour traitement
        ==================================
        Les images sont convertit au format JPEG

        :param int size_max: taille maximum d'une image
        :param int size_thumb_max: taille miniature et minimum

        """
        self.extension = file_manager.file_extension(src).upper()

        if self.extension == "JPG":
            self.extension = TYPE_IMG_JPEG

        if self.extension not in [TYPE_IMG_JPEG, TYPE_IMG_PNG, TYPE_IMG_GIF, TYPE_IMG_WEBP]:
            raise ValueError("Format image non supporté")

        self.size_max = size_max
        self.size_thumb_max = size_thumb_max

        self.img = Image.open(src)
        self.exif = None

        self._size = self.img.size
        self._format = self.img.format.lower()

        self.file = file_manager.file_extension_less(dest)  # on s'assure de retirer l'extension

        self.resize()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.img.close()
        except:
            pass

    @property
    def _size(self):
        return self.w, self.h

    @_size.setter
    def _size(self, s):
        self.w, self.h = s

    def image_to_rgb(self):
        if self.img.mode != 'RGB':
            self.img = self.img.convert('RGB')
            self.extension = TYPE_IMG_JPEG

    def white_background(self):
        """
        Retourne l'image avec un fond blanc appliqué si l'image comporte de la transparence.
        :return: PIL.Image avec fond blanc
        """

        # Si l'image a un canal alpha (RGBA), on l’utilise comme masque
        if self.img.mode in ("RGBA", "LA"):
            bg = Image.new("RGB", self._size, (255, 255, 255))
            bg.paste(self.img, (0, 0), self.img)
            return bg
        return self.img

    def redraw_border(self, shape="rect", wc=False):
        """
            fs = '/home/dreamgeeker/Images/2151910934.jpg'
            fs_out = '/home/dreamgeeker/Images/tests.jpg'

            imager = ImageManager(fs, fs_out.format('circ'))
            imager.img = imager.redraw_border('circ')
            imager.save('png')
            imager = ImageManager(fs, fs_out.format('circ_border'))
            imager.img = imager.redraw_border('circ', True)
            imager.save('png')"""

        padding = 5 if wc else 0
        diameter = 2 * padding
        box = (self.img.width + diameter, self.img.height + diameter)

        if shape == "rect":
            bg = Image.new("RGB", box, (255, 255, 255))
            bg.paste(self.white_background(), (padding, padding))
        else:  # shape == "circ":
            self.img.convert("RGBA")
            bg = Image.new("RGBA", box, (0, 0, 0, 0))
            if wc:
                draw = ImageDraw.Draw(bg)
                draw.ellipse((0, 0, box[0], box[1]), fill=(255, 255, 255, 255))

            # Masque circulaire
            mask = Image.new("L", self.img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, self.img.width, self.img.height), fill=255)

            pos_x = padding
            pos_y = padding

            # Coller l'image sur le cercle blanc au centre
            bg.paste(self.img, (pos_x, pos_y), mask)

        return bg

    def resize(self):
        """ Redimensionnement de l'image au format jpg


        :return:
        """
        if self.h < self.size_thumb_max or self.w < self.size_thumb_max:
            raise Exception("Image trop petite")
        elif self.h < self.size_max and self.w < self.size_max:
            return

        if self.w >= self.h:
            coeff = self.w / self.size_max
        else:
            coeff = self.h / self.size_max

        h = int(self.h / coeff)
        w = int(self.w / coeff)


        self.img = self.img.resize((w, h))

    def recadre(self, w, h):
        """"""
        for coeff in range(11):
            if w % coeff == 0 and h % coeff == 0:
                w //= coeff
                h //= coeff
                w, h = self.recadre(w, h)
                break

        return w, h

    def rationalize(self, r_w: int, r_h: int):
        """ Redimensionnement de l'image au format jpg

        :return:
        """
        w = self.w
        h = w * r_h // r_w

        self.img = self.img.resize((w, h))

    def save(self, frm: str | None = None):
        """ Thumb Image
        :param frm:
        """

        frm = frm.lower() if frm else self._format
        file_name = self.file + '.' + frm
        frm = frm.upper()

        # certaines conversions nécessitent convert()
        if frm == 'JPEG' and self.img.mode in ('RGBA', 'LA'):
            # JPEG ne supporte pas alpha → convertir en RGB
            background = Image.new("RGB", self.img.size, (255, 255, 255))
            background.paste(self.img, mask=self.img.split()[-1])  # utiliser l'alpha comme masque
            self.img = background

        file_manager.makedirs(file_manager.parent_directory(file_name))

        if frm == TYPE_IMG_PNG and self.exif:
            self.img.save(file_name, exif=self.exif, quality=90, optimize=True)
        else:
            self.img.save(file_name, format=frm, quality=90, optimize=True)

    def generate_thumb(self):
        """ Thumb Image       """
        thumb = copy.deepcopy(self)
        thumb.img.thumbnail((self.size_thumb_max, self.size_thumb_max))
        thumb.file += "_thumb"
        return thumb

    def save_thumb_image(self, frm: str = TYPE_IMG_JPEG):
        """ Thumb Image
        """
        thumb = self.generate_thumb()
        thumb.save(frm=frm)

    def to_badge(self):
        """Redimensionnement de l'image

        :return:
        """
        thumb = copy.deepcopy(self)
        thumb.img = thumb.redraw_border('circ', wc=True)
        thumb.img.thumbnail((64, 64))
        thumb.file += "_ico"

        return thumb

    def save_image_jpeg(self):
        self.image_to_rgb()
        self.save(frm=TYPE_IMG_JPEG)

    def protected(self, artist, description):
        """Ajoute un nom d'artist et le copyright d'une image"""

        _TAGS_r = dict(((v, k) for k, v in TAGS.items()))

        # Image File Directory
        ifd = ImageFileDirectory_v2()
        ifd[_TAGS_r["Artist"]] = artist
        ifd[_TAGS_r["Copyright"]] = 'Tous droits réservés'
        ifd[_TAGS_r["Description"]] = description

        out = BytesIO()
        ifd.save(out)

        self.exif = b"Exif\x00\x00" + out.getvalue()
        self.img.save(self.file, TYPE_IMG_JPEG, exif=self.exif)

    @staticmethod
    def directory_parsing(main_directory: str):
        """
        Redimensionne toutes les images contenu dans un répertoire donné + thumb
        :param main_directory:
        """
        for f in os.listdir(main_directory):
            f_path = os.path.join(main_directory, f)
            if os.path.isfile(f_path):
                imager = ImageManager(f_path, f_path)
                imager.save()
                imager.save_thumb_image()

    @staticmethod
    def treat_uploading(fs, fp):
        """
        Enregistrement d'une image uploaded (byte)

        :param file fs: filestream from flask request
        :param str fp: filepath d'enregistrement
        :return:
        """
        import uuid

        tmp = uuid.uuid1().int >> 64
        tmp_image = file_manager.path_build(ControllerEngine.TMP_DIR, str(tmp))

        try:
            TrackingManager.flag(f'[imgrecorder] Image temp recording : {tmp}')
            fs.save(tmp_image)

            TrackingManager.flag(f'[imgrecorder] Image treatment: {tmp} | {fp}')
            o = ImageManager(tmp_image, fp)
            o.save()

            TrackingManager.flag('[imgrecorder] Image thumbing')
            o.save_thumb_image()

            file_manager.remove_file(tmp_image)

            return True
        except Exception as e:
            TrackingManager.exception_tracking(e, '[imgrecorder] Aïe')
            return False

    @staticmethod
    def get_file_size(i_p):
        """

        :param i_p: image_path
        :return:
        """
        size_bytes = None
        try:
            # Obtenir la taille du fichier image en octets
            size_bytes = os.path.getsize(i_p)
        finally:
            return size_bytes  # Retourne None si la taille ne peut pas être obtenue
