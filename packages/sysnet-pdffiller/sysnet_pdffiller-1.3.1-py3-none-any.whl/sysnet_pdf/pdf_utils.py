#  Copyright (c) 2022, 2023. SYSNET s.r.o.
#  All rights reserved.
#
#
from __future__ import annotations

import os
import shutil
from datetime import datetime
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError

from fillpdf.fillpdfs import write_fillable_pdf
from pypdf import PdfWriter, PdfReader
from pypdf.generic import NameObject, IndirectObject, BooleanObject, NumberObject
from sysnet_pyutils.utils import Singleton, who_am_i, LoggedObject

from init import (
    PDF_OUTPUT_DIR, PDF_TEMP_FILE, PDF_OWNER_PASSWORD, PDF_TEMPLATES_DIR, LOG, CC, EXTENSION_PDF, EXTENSION_JASPER,
    TEMPLATE_TYPE_PDF, TEMPLATE_TYPE_JASPER, TEMPLATE_TYPE_OTHER,
    KEY_TEMPLATES_PDF, KEY_TEMPLATES_JASPER, KEY_TEMPLATES)
from sysnet_pdf.config import PdfError


def fdf_date(date_str):
    date_time_obj = datetime.strptime(date_str, 'D:%Y%m%d')
    return '{}.{}.{}'.format(date_time_obj.day, date_time_obj.month, date_time_obj.year)


def set_need_appearances_writer(writer_object):
    """

    :type writer_object: PdfFileWriter
    """
    # basically used to ensure there are not
    # overlapping form fields, which makes printing hard
    try:
        catalog = writer_object._root_object
        if "/AcroForm" not in catalog:
            writer_object._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer_object._objects), 0, writer_object)})
        need_appearances = NameObject("/NeedAppearances")
        writer_object._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
    return writer_object


def parse_template_type(source_path=None):
    if source_path is None:
        return ''
    filename = os.path.split(source_path)[-1]
    ext = filename.split('.')[-1]
    if ext.lower() == EXTENSION_PDF:
        return TEMPLATE_TYPE_PDF
    elif ext.lower() == EXTENSION_JASPER:
        return TEMPLATE_TYPE_JASPER
    else:
        return TEMPLATE_TYPE_OTHER


class PdfFactory(LoggedObject, metaclass=Singleton):
    """
    Továrna na plnění PDF a správu souborů se šablonami
    """

    def __init__(self, object_name='PDF_FACTORY'):
        super().__init__(object_name)
        self.config_factory = CC
        self.pdf_templates = self.config_factory.config['templates']['pdf']
        self.jasper_templates = self.config_factory.config['templates']['jasper']
        self.merger = None
        self.log.info(f"{self.name} created")

    class PdfFactoryError(PdfError):
        def __init__(self, status=500, message="PDF Factory exception", module=None):
            self.status = status
            self.message = message
            self.module = module
            super().__init__(self.status, self.message, self.module)

    def _identify_template_type(self, source_path=None):
        template_type = parse_template_type(source_path=source_path)  # PDF/JASPER
        if template_type == TEMPLATE_TYPE_PDF:
            templates = self.pdf_templates
            templates_key = KEY_TEMPLATES_PDF
        elif template_type == TEMPLATE_TYPE_JASPER:
            templates = self.jasper_templates
            templates_key = KEY_TEMPLATES_JASPER
        else:
            self.log.error(f"{self.name}._identify_template_type - Invalid template type {template_type}.")
            raise self.PdfFactoryError(message=f"{self.name}._identify_template_type - Invalid template type {template_type}.", module=self.name)
        return template_type, templates, templates_key

    def init_template_lists(self, template_list_pdf, template_list_jasper):
        out0 = self.init_template_list(template_list_pdf, TEMPLATE_TYPE_PDF)
        out1 = self.init_template_list(template_list_jasper, TEMPLATE_TYPE_JASPER)
        if out0 or out1:
            return True
        return False

    def init_template_list(self, template_list, template_type=None):
        if template_list is None or not template_list: 
            return False
        if template_type not in [TEMPLATE_TYPE_PDF, TEMPLATE_TYPE_JASPER]:
            self.log.error(f"{self.name}.init_template_list - Illegal template type: {template_type}")
            raise self.PdfFactoryError(message=f"{self.name}.init_template_list - Illegal template type: {template_type}", module=self.name)
        self.config_factory.config[KEY_TEMPLATES][template_type] = []
        for item in template_list:
            self.config_factory.config[KEY_TEMPLATES][template_type].append(item)
        self.config_factory.store()
        return True
        
    def add_template(self, source_path=None, remove_source=False):
        if not os.path.exists(path=source_path):
            self.log.error(f"{self.name}.add_template - Template source not found: {source_path}")
            raise self.PdfFactoryError(message=f"{self.name}.add_template - Template source not found: {source_path}", module=self.name)
        if not os.path.isfile(path=source_path):
            self.log.error(f"{self.name}.add_template - Template source is not file: {source_path}")
            raise self.PdfFactoryError(message=f"{self.name}.add_template - Template source is not file: {source_path}", module=self.name)
        template_type, templates, templates_key = self._identify_template_type(source_path=source_path)
        filename = os.path.split(source_path)[-1]
        if filename in templates:
            self.log.error(f"{self.name}.add_template - Template filename {filename} already exists.")
            raise self.PdfFactoryError(message=f"{self.name}.add_template - Template filename {filename} already exists.", module=self.name)
        if source_path is None:
            raise self.PdfFactoryError(message=f"{self.name}.add_template - Template source path is missing", module=self.name)
        target_path = os.path.join(PDF_TEMPLATES_DIR, filename)
        if not os.path.exists(path=target_path):
            target_path = shutil.copy2(source_path, PDF_TEMPLATES_DIR)
        else:
            remove_source = False
        if filename not in self.config_factory.config['templates'][template_type]:
            self.config_factory.config['templates'][template_type].append(filename)
            self.config_factory.store()
        if filename not in templates:
            templates.append(filename)
        if remove_source:
            os.remove(source_path)
        self.log.info(f"{self.name}.add_template - Added {template_type.upper()} template {filename}: {target_path}")

    def replace_template(self, source_path=None, remove_source=False):
        if source_path is None:
            self.log.error(f"{self.name}.replace_template - Template source path is missing")
            raise self.PdfFactoryError(message=f"{self.name}.replace_template - Template source path is missing", module=self.name)
        if not os.path.exists(path=source_path):
            self.log.error(f"{self.name}.replace_template - Template source not found: {source_path}")
            raise self.PdfFactoryError(message=f"{self.name}.replace_template - Template source not found: {source_path}", module=self.name)
        if not os.path.isfile(path=source_path):
            self.log.error(f"{self.name}.replace_template - Template source is not file: {source_path}")
            raise self.PdfFactoryError(message=f"{self.name}.replace_template - Template source is not file: {source_path}", module=self.name)
        template_type, templates, templates_key = self._identify_template_type(source_path=source_path)
        filename = os.path.split(source_path)[-1]
        if filename not in templates:
            self.log.error(f"{self.name}.replace_template - Template {filename} does not exist.")
            raise self.PdfFactoryError(message=f"{self.name}.replace_template - Template {filename} does not exist.", module=self.name)
        target_path = os.path.join(PDF_TEMPLATES_DIR, filename)
        orig_path = target_path
        if os.path.exists(path=orig_path):
            os.remove(path=orig_path)
        if os.path.exists(path=target_path):
            os.remove(path=target_path)
        target_path = shutil.copy2(source_path, PDF_TEMPLATES_DIR)
        if remove_source:
            os.remove(source_path)
        self.log.info(f"{self.name}.replace_template - Replaced {template_type.upper()} template {filename}: {target_path}")

    def remove_template(self, filename=None):
        if filename is None:
            self.log.error(f'{self.name}.remove_template - Template filename is missing')
            raise self.PdfFactoryError(message=f'{self.name}.remove_template - Template filename is missing', module=self.name)
        template_path = os.path.join(PDF_TEMPLATES_DIR, filename)
        template_type, templates, templates_key = self._identify_template_type(source_path=template_path)
        if not os.path.exists(path=template_path):
            self.log.error(f"{self.name}.remove_template - Template not found: {template_path}")
            raise self.PdfFactoryError(message=f"{self.name}.remove_template - Template not found: {template_path}", module=self.name)
        if not os.path.isfile(path=template_path):
            self.log.error(f"{self.name}.remove_template - Template is not file: {template_path}")
            raise self.PdfFactoryError(message=f"{self.name}.remove_template - Template is not file: {template_path}", module=self.name)
        if filename in templates:
            templates.remove(filename)
        if filename in self.config_factory.config['templates'][template_type]:
            self.config_factory.config['templates'][template_type].remove(filename)
            self.config_factory.store()
        orig_path = template_path
        if os.path.exists(path=orig_path):
            os.remove(path=orig_path)
        self.log.info(f'{self.name}.remove_template - Deleted {template_type.upper()} template: {filename}')

    def fill_pdf_form(self, template_filename, data=None, out_filename=PDF_TEMP_FILE, templates=None):
        __name__ = who_am_i()
        if templates is None or not bool(templates):
            templates = self.pdf_templates
        if data is None:
            self.log.error(f"{self.name}.fill_pdf_form - Data is missing")
            raise self.PdfFactoryError(module=self.name, message=f"{self.name}.fill_pdf_form - Data is missing")
        if template_filename is None:
            self.log.error(f"{self.name}.fill_pdf_form - PDF template filename missing")
            raise self.PdfFactoryError(module=self.name, message=f"{self.name}.fill_pdf_form - PDF template filename missing")
        if template_filename not in templates:
            self.log.error(f"{self.name}.fill_pdf_form - PDF template {template_filename} not found")
            raise self.PdfFactoryError(module=self.name, message=f"{self.name}.fill_pdf_form - PDF template {template_filename} not found")
        if out_filename is None:
            out_filename = PDF_TEMP_FILE
        if out_filename == os.path.basename(out_filename):
            out_filename = os.path.join(PDF_OUTPUT_DIR, os.path.basename(out_filename))
        try:
            if os.path.exists(out_filename):
                os.remove(out_filename)
            write_fillable_pdf(str(os.path.join(PDF_TEMPLATES_DIR, template_filename)), str(out_filename), data)
            return out_filename
        except KeyError as e:
            LOG.logger.error(f"{self.name}.fill_pdf_form - {str(e)}")
            return None

    def create_pdf_from_xfdf(self, template_filename=None, xfdf_file_path=None, pdf_file_name=None, templates=None, flatten=False):
        """
        Creates read and print only PDF form XFDF data and PDF template. Main function.
        :param flatten: Flatten PDF
        :param templates: template list
        :param template_filename:    PDF template filename
        :param xfdf_file_path:   XFDF file full path
        :param pdf_file_name:    Output PDF file name. File is stored to PDF_OUTPUT_DIR
        :return:    Created PDF file full path
        """

        pdf_file_path = os.path.join(PDF_OUTPUT_DIR, pdf_file_name)
        data = self.xfdf_to_dict(filename=xfdf_file_path)
        pdf_form = self.fill_pdf_form(template_filename=template_filename, data=data, templates=templates)
        if pdf_form is None:
            return None
        if flatten:
            out = self.flatten_pdf(data_dict=data, output_pdf=pdf_file_path)
        else:
            out = shutil.move(str(pdf_form), str(pdf_file_path))
        return out

    def check_templates(self):
        out = {'pdf': [], 'jasper': []}
        for item in self.pdf_templates:
            fname = item
            fpath = os.path.join(PDF_TEMPLATES_DIR, fname)
            exists = os.path.exists(fpath)
            t = (fname, fpath, exists)
            out['pdf'].append(t)
        for item in self.jasper_templates:
            fname = item
            fpath = os.path.join(PDF_TEMPLATES_DIR, fname)
            exists = os.path.exists(fpath)
            t = (fname, fpath, exists)
            out['jasper'].append(t)
        return out

    def merge_pdf(self, pdf_list, delete_parts=False):
        if pdf_list is None:
            return None
        if not bool(pdf_list):
            return None
        if len(pdf_list) == 1:
            return pdf_list[0]
        dirname = os.path.dirname(pdf_list[0])
        basename = os.path.basename(pdf_list[0])
        out_filename = f"{basename.split('.')[0]}_merged.pdf"
        out_filepath = os.path.join(dirname, out_filename)
        self.merger = PdfWriter()
        for item in pdf_list:
            self.merger.append(item)
        self.merger.write(out_filepath)
        self.merger.close()
        if delete_parts:
            for item in pdf_list:
                if os.path.exists(item):
                    os.remove(item)
        return out_filepath

    def xfdf_to_dict(self, filename=None):
        if filename is None:
            self.log.error(f"{self.name}.xfdf_to_dict - Data filename is missing")
            raise PdfError(module=self.name, message=f"{self.name}.xfdf_to_dict - Data filename is missing")
        if not os.path.exists(filename):
            self.log.error(f"{self.name}.xfdf_to_dict - Data file not found: {filename}")
            raise PdfError(module=self.name, message=f"{self.name}.xfdf_to_dict - Data file not found: {filename}")
        try:
            tree = ElementTree.parse(filename)
            root = tree.getroot()
            fields = None
            for child in root:
                if 'fields' in child.tag:
                    fields = child
            field_list = []
            data = {}
            for child in fields:
                if 'field' in child.tag:
                    field_list.append(child)
                    key = child.attrib['name']
                    for child2 in child:
                        val = child2.text
                        if val is None:
                            val = ''
                        elif val.startswith('D:'):
                            val = fdf_date(val)
                        data[key] = val
            return data
        except ParseError as e:
            self.log.error(f"{self.name}.xfdf_to_dict - {str(e)}")
            raise self.PdfFactoryError(message=f"{self.name}.xfdf_to_dict - {str(e)}", module=self.name)

    def flatten_pdf(self, input_pdf=PDF_TEMP_FILE, data_dict=None, output_pdf=None, user_password=None):
        try:
            input_stream = open(input_pdf, "rb")
            pdf_reader = PdfReader(input_stream, strict=False)
            if "/AcroForm" in pdf_reader.trailer["/Root"]:
                pdf_reader.trailer["/Root"]["/AcroForm"].update(
                    {NameObject("/NeedAppearances"): BooleanObject(True)})
            pdf_writer: PdfWriter = PdfWriter()
            set_need_appearances_writer(pdf_writer)
            if "/AcroForm" in pdf_writer._root_object:
                # Acro form is a form field, set needs appearances to fix printing issues
                pdf_writer._root_object["/AcroForm"].update(
                    {NameObject("/NeedAppearances"): BooleanObject(True)})
            page0 = pdf_reader.pages[0]
            pdf_writer.add_page(page0)
            # page: PageObject = pdf_writer.getPage(0)
            page = pdf_writer.pages[0]
            # update form fields
            # pdf_writer.updatePageFormFieldValues(page, data_dict)
            annots = page['/Annots'].get_object()
            annots_items = annots.items()
            for item in annots_items:
                writer_annot = item[1].get_object()
                if data_dict:
                    for field in data_dict:
                        if writer_annot.get('/T') == field:
                            writer_annot.update({NameObject("/Ff"): NumberObject(1)})  # make ReadOnly
            if user_password is None:
                user_password = ''
            pdf_writer.encrypt(user_password=user_password, owner_password=PDF_OWNER_PASSWORD)
            path = os.path.dirname(output_pdf)
            if not os.path.exists(path=path):
                os.makedirs(path)
            if os.path.exists(output_pdf):
                os.remove(output_pdf)
            output_stream = open(output_pdf, 'wb')
            pdf_writer.write(output_stream)
            output_stream.close()
            input_stream.close()
            return output_pdf
        except Exception as e:
            self.log.error(f"{self.name}.flatten_pdf - {str(e)}")
            raise self.PdfFactoryError(message=f"{self.name}.flatten_pdf - {str(e)}", module=self.name)


PDF_FACTORY = PdfFactory()
