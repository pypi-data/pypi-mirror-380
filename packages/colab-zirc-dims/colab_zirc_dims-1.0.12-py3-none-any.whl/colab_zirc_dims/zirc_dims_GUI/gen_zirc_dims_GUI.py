# -*- coding: utf-8 -*-
"""
Module with a simple GUI function for non-ALC datasets.
"""

import base64
import io
import json
import uuid
import os
import copy
import datetime

from typing import List
from typing import Union
from IPython.display import display
import numpy as np
from PIL import Image
import pandas as pd
import skimage.io as skio

colab_import_success_bool = True
try:
    from google.colab import output
    from google.colab.output import eval_js
except ModuleNotFoundError:
    from ..jupyter_colab_compat import output_local as output
    colab_import_success_bool = False

from .gui_js import js
from .. import czd_utils
from .. import mos_proc
from .. import poly_utils
from .. import save_load

# NOTE: Despite strong points of Google Colab as a platform for a deep-learning-\
# based image processing toolset (e.g., free high-end hardware), it is not an \
# optimal platform for a Python-based GUI. The embedded javascript, numerous \
# callbacks, and neccesarily nonlocal/global variables in the GUI function \
# below are an (un-Pythonic) testament to this. Said function (extended from \
# code in tensorflow.models) does work, though, and at present seems like the \
# best way to implement the colab_zirc_dims project entirely in Google Colab \
# Notebooks.

__all__ = ['run_gen_GUI']

def run_gen_GUI(sample_data_dict, sample_list, root_dir_path, Predictor,
                load_dir = None, id_string = '',
                is_colab = colab_import_success_bool):
    """Run a colab-based GUI for automated / manual zircon segmentation and
       segmentation inspection of non-ALC (one image/shot) datasets.

    Parameters
    ----------
    sample_data_dict : dict
        A dict of dicts (single image/shot format) containing data from
        project folder w/ format:
                {EACH_SAMPLE: {EACH_SPOT: {'img_file': FULL_IMG_PATH,
                               'Align_file': FULL_ALIGN_PATH or '',
                               'rel_file': IMG_FILENAME
                               'scale_factor': float(scale factor for each scan),
                               'scale_from': str(method used get scale factor)},
                               ...},
                 ...}.

    sample_list : list of str
        A list of sample names (selected by user while running Colab notebook)
        indicating which samples they will actually be working with.
    root_dir_path : str
        Full path to project directory.
    Predictor : Detectron2 Predictor class instance
        A Detectron2 Predictor; should be initialized before running this fxn.
    load_dir : str, optional
        User-selected directory with .json files for loading polygons.
        The default is None.
    id_string : str, optional
        A string to add to front of default (date-time) output folder name.
        The default is ''.
    is_colab : bool, optional
        A bool telling the GUI function whether to use Google Colab (if True)
        or local IPython >= 7.0 (if False) functions and callbacks, both in the
        GUI javascript function and in its Python wrapper. Users should not
        need to set this argument manually. Its default value is determined
        automatically based on whether trying to import 'google.colab.outputs'
        module throws a ModuleNotFoundError (this package is installed) in
        all Colab virtual environments.

    Raises
    ------
    TypeError
        Raised if image type is not supported (np array or array-like).

    Returns
    -------
    None

    """

    if len(sample_list) == 0:
        print('ERROR: NO SAMPLES SELECTED')
        return

    ### CODE FOR FUNCTIONS BELOW (SIGNIFICANTLY) MODIFIED FROM tensorflow.models FOR POLYGON ANNOTATION ###
    # Lint as: python3
    # Copyright 2020 The TensorFlow Authors. All Rights Reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    # ==============================================================================

    def image_from_numpy(image):
        """Open an image at the specified path and encode it in Base64.
        Args:
          image: np.ndarray
            Image represented as a numpy array
        Returns:
          An encoded Base64 representation of the image
        """

        with io.BytesIO() as img_output:
            Image.fromarray(image).save(img_output, format='JPEG')
            data = img_output.getvalue()
        data = str(base64.b64encode(data))[2:-1]
        return data


    def draw_polygons(image_urls, spot_names, track_list, sample_scale_factors,
                      original_polys, auto_human_list_input, tag_list_input1,
                      sample_name, callbackId1,
                      callbackId2, callbackId3, callbackId4):  # pylint: disable=invalid-name
        """Open polygon annotation UI and send the results to a set of callback functions.
        """

        # load the images as a byte array
        bytearrays = []
        for image in image_urls:
            if isinstance(image, np.ndarray):
                bytearrays.append(image_from_numpy(image))
            else:
                raise TypeError('Image has unsupported type {}.'.format(type(image)))

        # format arrays for input
        image_data = json.dumps(bytearrays)
        del bytearrays
        # call java script function pass string byte array(image_data) as input
        if is_colab:
            display(js)
            eval_js('load_image(true, {}, {}, {}, {}, {}, {}, {}, \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(image_data, spot_names, track_list,
                                                                                                             sample_scale_factors,
                                                                                                             original_polys,
                                                                                                             auto_human_list_input, tag_list_input1,
                                                                                                             sample_name,
                                                                                                             callbackId1, callbackId2, callbackId3,
                                                                                                             callbackId4))
        else:
            output.alt_eval_js(js,
                               'load_image(false, {}, {}, {}, {}, {}, {}, {}, \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(image_data, spot_names, track_list,
                                                                                                                                sample_scale_factors,
                                                                                                                                original_polys,
                                                                                                                                auto_human_list_input, tag_list_input1,
                                                                                                                                sample_name,
                                                                                                                                callbackId1, callbackId2, callbackId3,
                                                                                                                                callbackId4))

        return


    def annotate(imgs: List[Union[str, np.ndarray]],  # pylint: disable=invalid-name
                  poly_storage_pointer: List[np.ndarray],
                  auto_polygons: List[List[dict]],
                  spot_names: List[str],
                  track_list: List[int],
                  sample_scale_factors: List[float],
                  scales_from: List[str],
                  img_filenames: List[str],
                  outputs_path: str,
                  predictor_input,
                  auto_human_list_input: List[str],
                  tag_list_input: List[str],
                  sample_name: str = None):
        """Open the polygon annotation UI and prompt the user for input.
        """
        # Set random IDs for the callback functions
        callbackId1 = str(uuid.uuid1()).replace('-', '')
        callbackId2 = str(uuid.uuid1()).replace('-', '')
        callbackId3 = str(uuid.uuid1()).replace('-', '')
        callbackId4 = str(uuid.uuid1()).replace('-', '')


        def savecallbackFunction(annotations, human_auto_list, tags_list):
            #print('callback started')
            """Callback function to save polygons for current sample and measure
               actual grain dimensions, exporting results to a linked Google Drive
               folder.
            """
            tags_for_export = []
            for tag in tags_list:
                if str(tag) == 'True':
                    tags_for_export.append('True')
                else:
                    tags_for_export.append('')
            #tags_for_export = [tag if tag == 'True' else '' for tag in tags_list ]
            #print('poly conversion started')
            # reset the poly list
            nonlocal poly_storage_pointer
            #print(box_storage_pointer)
            polys: List[np.ndarray] = poly_storage_pointer
            polys.clear()

            # load the new annotations into the polygon list
            for annotations_per_img in annotations:
                polys_as_arrays = [poly_utils.vertex_dict_to_list(annotation)
                                   for annotation in annotations_per_img]
                if polys_as_arrays:
                    polys.append(np.stack(polys_as_arrays))
                else:
                    polys.append(None)

            ###exports data

            output_data_list = []
            #paths for saving
            img_save_root_dir = os.path.join(outputs_path, 'mask_images')
            each_img_save_dir = os.path.join(img_save_root_dir, str(sample_name))
            csv_save_dir = os.path.join(outputs_path, 'grain_dimensions')
            #poly_save_dir = os.path.join(outputs_path, 'saved_polys')

            #directory for saving images for each sample
            os.makedirs(each_img_save_dir, exist_ok=True)
            #os.makedirs(csv_save_dir, exist_ok=True)

            ##directory for saving polygons for current sample
            #os.makedirs(poly_save_dir, exist_ok=True)

            for eachindex, eachpoly in enumerate(poly_storage_pointer):

                poly_mask = poly_utils.poly_to_mask(eachpoly, imgs[eachindex])

                tag_Bool = False
                if tags_for_export[eachindex] == 'True':
                    tag_Bool = True

                #if polygon sucessfully converted into a mask w/ area >0:
                if poly_mask[0] is True:
                    each_props = mos_proc.overlay_mask_and_get_props(poly_mask[1],
                                                                     imgs[eachindex],
                                                                     spot_names[eachindex],
                                                                     display_bool = False,
                                                                     save_dir=each_img_save_dir,
                                                                     tag_bool = tag_Bool,
                                                                     scale_factor=sample_scale_factors[eachindex])

                    #properties to save for each scan/image
                    each_props_list = mos_proc.parse_properties(each_props,
                                                                sample_scale_factors[eachindex],
                                                                spot_names[eachindex],
                                                                False,
                                                                [scales_from[eachindex],
                                                                 img_filenames[eachindex],
                                                                 human_auto_list[eachindex],
                                                                 tags_for_export[eachindex]]
                                                                )

                    output_data_list.append(each_props_list)
                else:
                    #properties to save for each scan/image (null values)
                    null_properties = mos_proc.parse_properties([],
                                                                sample_scale_factors[eachindex],
                                                                spot_names[eachindex],
                                                                False,
                                                                [scales_from[eachindex],
                                                                 img_filenames[eachindex],
                                                                 human_auto_list[eachindex],
                                                                 tags_for_export[eachindex]]
                                                                )

                    output_data_list.append(null_properties)
                    mos_proc.save_show_results_img(imgs[eachindex],
                                                   spot_names[eachindex],
                                                   display_bool=False,
                                                   save_dir=each_img_save_dir,
                                                   tag_bool=tag_Bool,
                                                   scale_factor=sample_scale_factors[eachindex])


            #converts collected data to pandas DataFrame, saves as .csv
            output_dataframe = pd.DataFrame(output_data_list,
                                            columns=czd_utils.get_save_fields(proj_type='general',
                                                                              save_type='GUI',
                                                                              addit_fields=[]))
            csv_filename = str(sample_name) + '_grain_dimensions.csv'
            output_csv_filepath = os.path.join(csv_save_dir, csv_filename)
            czd_utils.save_csv(output_csv_filepath, output_dataframe)

            save_load.save_sample_json(outputs_path, str(sample_name), spot_names,
                                       annotations, human_auto_list, tags_for_export)


            # output message to the errorlog
            with output.redirect_to_element('#errorlog'):
                display('Measurement and export for current sample complete')


        #a callback function to change samples; saves polygons before moving samples
        def changesamplecallbackFunction(next_prev_str, annotations,
                                         human_auto_list, tags_list):

            nonlocal index_tracker
            nonlocal predictor_input

            proceed_bool = False

            if str(next_prev_str) == 'next':
                if index_tracker.at_end is False:
                    index_tracker.next_sample()
                    proceed_bool = True

            if str(next_prev_str) == 'prev':
                if index_tracker.at_begin is False:
                    index_tracker.prev_sample()
                    proceed_bool = True

            if proceed_bool:
                #output.clear()
                #eval_js(remove_prev_GUI_js) #should clear previous GUI
                save_polys_callbackFunction(annotations, human_auto_list,
                                            tags_list, disp_bool=False)
                load_and_annotate(Predictor)

        def save_polys_callbackFunction(annotations, human_auto_list, tags_list,
                                        disp_bool=True):
            """Callback function to export poly annotations for the current sample
               to .json files in a linked Google Drive folder. ALlows persistance
               of user changes to polygons between samples.
            """
            tags_for_export = []
            for tag in tags_list:
                if str(tag) == 'True':
                    tags_for_export.append('True')
                else:
                    tags_for_export.append('')
            save_load.save_sample_json(outputs_path, str(sample_name), spot_names,
                                       annotations, human_auto_list, tags_for_export)

            if disp_bool:
                # output message to the errorlog
                with output.redirect_to_element('#errorlog'):
                    display('Polygon export complete')

        def analyze_all_polys_callbackFunction(annotations, human_auto_list, tags_list):
            """Callback to analyze, export dimensions, etc. from polygons for
               all selected samples. Restarts annotation GUI when done.
            """
            save_polys_callbackFunction(annotations, human_auto_list,
                                        tags_list, disp_bool=False)
            dataset_dimensions_from_polys()
            load_and_annotate(Predictor)

        #register all callbacks
        output.register_callback(callbackId1, savecallbackFunction)
        output.register_callback(callbackId2, changesamplecallbackFunction)
        output.register_callback(callbackId3, save_polys_callbackFunction)
        output.register_callback(callbackId4, analyze_all_polys_callbackFunction)

        #convert scale factors to strings for display in GUI
        sample_scale_factors_str = [str(round(sf, 5)) for sf in sample_scale_factors]

        #send data for drawing
        draw_polygons(imgs, spot_names, track_list, sample_scale_factors_str,
                      auto_polygons, auto_human_list_input,
                      tag_list_input, sample_name, callbackId1,
                      callbackId2, callbackId3, callbackId4)

### END MODIFIED CODE
# =================================================================================

    ### Code for looping through datasets, loading data for each, etc. below\

    # a class for storing index and name of a samples from a list of sample names.\
    # An instance of this class is made nonlocal and used to track position within \
    # a dataset while using the GUI function.
    class sample_index:

        def __init__(self, input_sample_list):
            self.sample_list = input_sample_list
            self.curr_index = 0
            self.max_index = len(input_sample_list) - 1
            self.at_begin = True
            self.at_end = False
            self.track_list = [self.curr_index, self.max_index]
            if self.curr_index == self.max_index:
                self.at_end = True

            #self.curr_sample = current sample name
            self.curr_sample = self.sample_list[self.curr_index]

        #moves to next sample, unless at end of sample list
        def next_sample(self):
            if self.at_end is True:
                return
            self.curr_index += 1
            self.track_list = [self.curr_index, self.max_index]
            self.curr_sample = self.sample_list[self.curr_index]
            if self.curr_index == self.max_index:
                self.at_end = True
            if self.curr_index > 0:
                self.at_begin = False

        #moves to prev sample, unless at beginning of sample list
        def prev_sample(self):
            if self.at_begin is True:
                return
            self.curr_index -= 1
            self.track_list = [self.curr_index, self.max_index]
            self.curr_sample = self.sample_list[self.curr_index]
            if self.curr_index < self.max_index:
                self.at_end = False
            if self.curr_index == 0:
                self.at_begin = True



    # segments all zircons in a sample automatically and opens annotation GUI to \
    # inspect, modify, and/or save segmentations.
    def load_and_annotate(Predictor):

        nonlocal index_tracker
        nonlocal sample_data_dict
        nonlocal run_dir
        nonlocal run_load_dir

        #lists, variables that will be called in function for loading new samples
        curr_auto_polys = [] #list polygons from automatically generated masks (as np (N, 2) arrs)
        curr_poly_pointer = [] #pointer for polygons from GUI, automatically updated in save fxns
        curr_subimage_list = [] #list of subimages (as np arrays) for loading into GUI
        #curr_scan_name_list = [] #list of spot names corresponding to each subimage
        curr_auto_human_list = [] #list of strings indicating whether segmentation \
                                  # (or lack therof) of spot was done automatically or by a human
        curr_spot_tags = [] #list of strings indicating whether user has 'tagged' each spot
        curr_scale_factors = [] #scale factors the each shot in the current sample


        curr_dict_copy = copy.deepcopy(sample_data_dict[index_tracker.curr_sample])

        #loads sample mosaic

        curr_scan_names = list(curr_dict_copy.keys())
        print('Sample:', index_tracker.curr_sample)
        print(2 * "\n")
        curr_scale_factors = [scan['scale_factor'] for scan in curr_dict_copy.values()]
        curr_scale_froms = [scan['scale_from'] for scan in curr_dict_copy.values()]
        curr_filenames = [scan['img_file'] for scan in curr_dict_copy.values()]
        load_outputs = [False]
        if run_load_dir is not None:
            load_outputs = save_load.find_load_json_polys(run_load_dir,
                                                          index_tracker.curr_sample,
                                                          curr_scan_names)
        if load_outputs[0] is False:
            #use predictor to automatically segment images if loadable polys unavailable
            print('Auto-processing:', index_tracker.curr_sample)
            for eachscan_idx, eachscan in enumerate(curr_scan_names):
                #gets subimage, processes it, and appends subimage and results \
                # (or empty values if unsuccessful) to various lists
                each_img = skio.imread(curr_dict_copy[eachscan]['img_file'])
                curr_subimage_list.append(each_img)
                print(str(eachscan) + ':')
                outputs = Predictor(each_img)
                central_mask = mos_proc.get_central_mask(outputs)
                curr_auto_human_list.append('auto')
                curr_spot_tags.append('')

                #if a central zircon is found, does initial processing and adds polygon
                if central_mask[0] is True:
                    print('Successful')

                    curr_auto_polys.append(poly_utils.mask_to_poly(central_mask[1], 1,
                                                                   curr_scale_factors[eachscan_idx]))
                else:
                    curr_auto_polys.append([])
            #saves polygons on initial processing so that processing \
            # does not have to repeat if navigating back to sample
            run_load_dir = os.path.join(run_dir, 'saved_polygons')
            save_load.save_sample_json(run_dir, index_tracker.curr_sample,
                                       curr_scan_names, curr_auto_polys)
        else:
            #simply load polygons from .json if possible
            curr_auto_polys, curr_auto_human_list, curr_spot_tags = load_outputs[1:]
            print('Preparing grain subimages')
            for eachscan in curr_scan_names:
                #gets subimage, processes it, and appends subimage and results \
                # (or empty values if unsuccessful) to various lists
                each_img = skio.imread(curr_dict_copy[eachscan]['img_file'])
                curr_subimage_list.append(each_img)

        print('')

        #starts annotator GUI for current sample
        output.clear()
        annotate(curr_subimage_list, curr_poly_pointer, curr_auto_polys,
                 curr_scan_names, index_tracker.track_list,
                 curr_scale_factors, curr_scale_froms, curr_filenames,
                 run_dir, Predictor,
                 curr_auto_human_list, curr_spot_tags,
                 str(index_tracker.curr_sample))

    def dataset_dimensions_from_polys():
        nonlocal run_dir
        nonlocal sample_data_dict
        nonlocal run_load_dir
        nonlocal sample_list
        nonlocal img_save_root_dir
        nonlocal csv_save_dir

        # Get dimensions from saved polygons for an individual sample
        def sample_dimensions_from_polys(indiv_sample_dict,
                                         indiv_sample_json_data,
                                         sample_scan_names,
                                         sample_name):

            #unpack saved .json polygon data
            sample_auto_human, sample_tags = indiv_sample_json_data[2:]
            sample_polys = poly_utils.poly_dicts_to_arrays(indiv_sample_json_data[1])

            #convert tags to export format
            tags_for_export = []
            for tag in sample_tags:
                if str(tag) == 'True':
                    tags_for_export.append('True')
                else:
                    tags_for_export.append('')

            #empty list for output data
            output_data_list = []
            #path for saving
            each_img_save_dir = os.path.join(img_save_root_dir, str(sample_name))
            os.makedirs(each_img_save_dir, exist_ok=True)

            #loop through scans, saving
            for each_scan_idx, each_scan in enumerate(sample_scan_names):
                scale_fact = indiv_sample_dict[each_scan]['scale_factor']
                scale_from = indiv_sample_dict[each_scan]['scale_from']
                file_name = indiv_sample_dict[each_scan]['rel_file']
                eachpoly = sample_polys[each_scan_idx]
                each_img = skio.imread(indiv_sample_dict[each_scan]['img_file'])
                poly_mask = poly_utils.poly_to_mask(eachpoly, each_img)

                #tag bool needs to persist into saved img filename; hence tag_Bool
                tag_Bool = False
                if sample_tags[each_scan_idx] == 'True':
                    tag_Bool = True

                #if polygon sucessfully converted into a mask w/ area >0:
                if poly_mask[0] is True:
                    each_props = mos_proc.overlay_mask_and_get_props(poly_mask[1],
                                                                     each_img,
                                                                     each_scan,
                                                                     display_bool = False,
                                                                     save_dir=each_img_save_dir,
                                                                     tag_bool = tag_Bool,
                                                                     scale_factor=scale_fact)

                    each_props_list = mos_proc.parse_properties(each_props,
                                                                scale_fact,
                                                                sample_scan_names[each_scan_idx],
                                                                False,
                                                                [scale_from,
                                                                 file_name,
                                                                 sample_auto_human[each_scan_idx],
                                                                 tags_for_export[each_scan_idx]]
                                                                )
                    output_data_list.append(each_props_list)
                else:
                    null_properties = mos_proc.parse_properties([], scale_fact,
                                                                each_scan,
                                                                False,
                                                                [scale_from,
                                                                 file_name,
                                                                 sample_auto_human[each_scan_idx],
                                                                 tags_for_export[each_scan_idx]]
                                                                )

                    output_data_list.append(null_properties)

                    mos_proc.save_show_results_img(each_img,
                                                   each_scan,
                                                   display_bool=False,
                                                   save_dir=each_img_save_dir,
                                                   tag_bool=tag_Bool,
                                                   scale_factor=scale_fact)

            output_dataframe = pd.DataFrame(output_data_list,
                                columns=czd_utils.get_save_fields(proj_type='general',
                                                                  save_type='GUI',
                                                                  addit_fields=[]))
            csv_filename = str(sample_name) + '_grain_dimensions.csv'
            output_csv_filepath = os.path.join(csv_save_dir, csv_filename)
            czd_utils.save_csv(output_csv_filepath, output_dataframe)
            print('Analysis & export complete')

        #start loop through samples
        for each_sample in sample_list:
            each_dict_copy = copy.deepcopy(sample_data_dict[each_sample])
            sample_scan_names = list(each_dict_copy.keys())
            loadable_polys = save_load.find_load_json_polys(run_load_dir,
                                                            str(each_sample),
                                                            sample_scan_names)
            #only analyze if loadable polygons presents
            if loadable_polys[0]:
                print('Analyzing dimensions from saved polygons:', each_sample)
                sample_dimensions_from_polys(each_dict_copy,
                                             loadable_polys,
                                             sample_scan_names,
                                             each_sample)
        output.clear()


    ##code below runs upon initial startup
    index_tracker = sample_index(sample_list) #initializes sample/index tracker class instance

    #directory initialization

    #main output directory path, can be modified if necessary
    root_output_dir = os.path.join(root_dir_path, 'outputs')

    #creates output directory if it does not already exist
    if not os.path.exists(root_output_dir):
        os.makedirs(root_output_dir)

    #creates a main directory for this processing run
    run_dir_name_str = 'semi-auto_proccessing_run_' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    if str(id_string):
        run_dir_name_str = id_string + '_' + run_dir_name_str
    run_dir = os.path.join(root_output_dir, run_dir_name_str)
    os.makedirs(run_dir)

    #copy mosaic info csv (for reloading at later point in case original changed)
    save_load.save_mosaic_info_copy(root_dir_path, run_dir, run_dir_name_str)

    #creates a root directory for saved images
    img_save_root_dir = os.path.join(run_dir, 'mask_images')
    os.makedirs(img_save_root_dir)

    #creates a directory for zircon dimension .csv files
    csv_save_dir = os.path.join(run_dir, 'grain_dimensions')
    os.makedirs(csv_save_dir)

    if load_dir is not None:
        run_load_dir = save_load.transfer_json_files(sample_list, run_dir, load_dir,
                                           verbose=True)
    else:
        run_load_dir = None

    #starts annotator for first time/sample
    load_and_annotate(Predictor)
    
    #return run dir for use in exploratory plotting
    return run_dir
