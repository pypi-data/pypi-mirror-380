# -*- coding: utf-8 -*-
"""
Module with functions for iteratively attempting segmentation of DZ images from
ALC/mosaic and single shot-per-image ('gen') datasets.
"""

import numpy as np
import skimage

from skimage import measure
from skimage import filters
from skimage import exposure
from skimage.morphology import binary_closing

from .. import mos_proc

__all__ = ['otsu_masks',
           'segment',
           'gen_segment',
           'segment_given_imgs']

# Get regionated masks from an image via Otsu threshholding
def otsu_masks(input_image):
    """Use Otsu threshholding to segment an image.

    Parameters
    ----------
    input_image : image array
        An input image array. Will be threshholded in grayscale.

    Returns
    -------
    output_masks_list : list[arr]
        A list of mask arrays (one for each region) from Otsu thresholding.

    """
    gray_img = skimage.color.rgb2gray(input_image)
    thresh_val = filters.threshold_otsu(gray_img)
    thresh_img = binary_closing(gray_img > thresh_val)
    label_mask = measure.label(thresh_img.astype(int))
    region_vals = list(np.unique(label_mask))

    #removes very small regions, background class
    larger_region_vals = [val for val in region_vals
                          if np.count_nonzero(label_mask == val) > 30
                          and val > 0]

    output_masks_list = []
    for each_region in larger_region_vals:
        each_mask = label_mask == each_region
        output_masks_list.append(each_mask)

    return output_masks_list


def segment(curr_mosaic_img, curr_predictor,
            try_bools = [False, False, False, False],
            out_trk = None):
    """Apply different methods (see try_bools) iteratively to try to segment
       an ALC image.

    Parameters
    ----------
    curr_mosaic_img : MosImg class instance
        A MosImg class instance w/ desired subimage coords already set.
    curr_predictor : Detectron2 Predictor class instance
        A predictor to apply to the subimage extracted.
    try_bools : list[bool], optional
        A list of bools determining what alternate segmentation methods will be
        applied if Detectron2 segmentation of the original image is unsuccesful.
        In order, these are:
        [apply predictor to 0.9x zoomed-out subimg,
         apply predictor to 1.1x zoomed-in subimg,
         apply predictor to histogram-equalized (contrast-enhanced) subimg,
         Otsu threshholding]
        The default is [False, False, False, False].
    out_trk : colab_zirc_dims.eta.OutputTracker instance
        Optionally (depending on initialization params) refreshes text output
        for every scan instead of streaming all print() data to output box.
        The default is None, in which case text will be streamed normally.

    Returns
    -------
    mask_found_bool : Boolean
        True or False, depending on whether a central mask was found.
    array or list
        np array for the central mask found. Empty list if none found.

    """
    #original subimage size; used for size manipulations
    orig_subimg_size = curr_mosaic_img.sub_img_size_input

    #apply predictor to given subimg
    central_mask = mos_proc.get_central_mask(curr_predictor(curr_mosaic_img.sub_img[:,:,::-1]))

    # try zooming out slightly
    if try_bools[0] and not central_mask[0]:
        if out_trk is not None:
            out_trk.print_txt('Trying segementation of zoomed-out subimage')
        else:
            print('Trying segementation of zoomed-out subimage')
        curr_mosaic_img.set_sub_img_size(round(orig_subimg_size * 1.1))
        central_mask = mos_proc.get_central_mask(curr_predictor(curr_mosaic_img.sub_img[:,:,::-1]))
        curr_mosaic_img.set_sub_img_size(orig_subimg_size)
    #try zooming in slightly
    if try_bools[1] and not central_mask[0]:
        if out_trk is not None:
            out_trk.print_txt('Trying segementation of zoomed-in subimage')
        else:
            print('Trying segementation of zoomed-in subimage')
        curr_mosaic_img.set_sub_img_size(round(orig_subimg_size * 0.9))
        central_mask = mos_proc.get_central_mask(curr_predictor(curr_mosaic_img.sub_img[:,:,::-1]))
        curr_mosaic_img.set_sub_img_size(orig_subimg_size)
    #try increasing contrast
    if try_bools[2] and not central_mask[0]:
        if out_trk is not None:
            out_trk.print_txt('Trying segmentation of contrast-enhanced subimage')
        else:
            print('Trying segmentation of contrast-enhanced subimage')
        cont_enhanced = exposure.equalize_hist(curr_mosaic_img.sub_img)
        central_mask = mos_proc.get_central_mask(curr_predictor(cont_enhanced[:,:,::-1]))
    #try otsu threshholding
    if try_bools[3] and not central_mask[0]:
        if out_trk is not None:
            out_trk.print_txt('Trying Otsu threshholding')
        else:
            print('Trying Otsu threshholding')
        central_mask = mos_proc.get_central_mask(otsu_masks(curr_mosaic_img.sub_img))
    return central_mask

def gen_segment(curr_img, curr_predictor,
                try_bools = [False, False],
                out_trk = None):
    """Apply different methods (see try_bools) iteratively to try to segment
       a single shot (non-ALC) image. Because image source is not a mosaic,
       extent jittering (zooming in and out) is not available.

    Parameters
    ----------
    curr_img : np array
        An array representing an image for segmentation.
    curr_predictor : Detectron2 Predictor class instance
        A predictor to apply to the subimage extracted.
    try_bools : list[bool], optional
        A list of bools determining what alternate segmentation methods will be
        applied if Detectron2 segmentation of the original image is unsuccesful.
        In order, these are:
        [apply predictor to histogram-equalized (contrast-enhanced) subimg,
         Otsu threshholding]
        The default is [False, False].
    out_trk : colab_zirc_dims.eta.OutputTracker instance
        Optionally (depending on initialization params) refreshes text output
        for every scan instead of streaming all print() data to output box.
        The default is None, in which case text will be streamed normally.

    Returns
    -------
    mask_found_bool : Boolean
        True or False, depending on whether a central mask was found.
    array or list
        np array for the central mask found. Empty list if none found.

    """

    #apply predictor to given subimg
    central_mask = mos_proc.get_central_mask(curr_predictor(curr_img[:,:,::-1]))

    #try increasing contrast
    if try_bools[0] and not central_mask[0]:
        if out_trk is not None:
            out_trk.print_txt('Trying segmentation of contrast-enhanced subimage')
        else:
            print('Trying segmentation of contrast-enhanced subimage')
        cont_enhanced = exposure.equalize_hist(curr_img)
        central_mask = mos_proc.get_central_mask(curr_predictor(cont_enhanced[:,:,::-1]))
    #try otsu threshholding
    if try_bools[1] and not central_mask[0]:
        if out_trk is not None:
            out_trk.print_txt('Trying Otsu threshholding')
        else:
            print('Trying Otsu threshholding')
        central_mask = mos_proc.get_central_mask(otsu_masks(curr_img))
    return central_mask


def segment_given_imgs(imgs, curr_predictor,
                       try_bools=[False, False, False, False], **kwargs):
    """Try to segment a series of images (or single image) using the given
    predictor. Does not rely on changing variables in an outer MosaicImage
    instance, and runs silently, thus fixing some problems with using the
    older segmentation function in parallel.

    Parameters
    ----------
    imgs : list[np.ndarray] or np.ndarray
        List of 3 channel images (as np ndarrays) to attempt to segment, in
        order, or a single 3-channel image alone.
    curr_predictor : Detectron2 Predictor class instance
        A predictor to apply to the given images extracted.
    try_bools : list[bool], optional
        A list of bools determining what alternate segmentation methods will be
        applied if Detectron2 segmentation of the first image is unsuccesful.
        In order, these are:
        [apply predictor to 0.9x zoomed-out subimg,
         apply predictor to 1.1x zoomed-in subimg,
         apply predictor to histogram-equalized (contrast-enhanced) subimg,
         Otsu threshholding]
        Only the last two bools are actually parsed here, so only two bools are
        required.
    **kwargs : dict, optional
        If 'only_otsu'=True in kwargs, only try Otsu thresholding of the first
        image in imgs, then return the result (used for benchmarking Otsu
        accuracy).

    Returns
    -------
    mask_found_bool : bool
        True or False, depending on whether a central mask was found.
    array or list
        np array for the central mask found. Empty list if none found.

    """
    assert isinstance(imgs, (list, tuple, np.ndarray, np.generic))
    if isinstance(imgs, (np.ndarray, np.generic)):
        imgs = [imgs]
    #hidden kwarg for benchmarking accuracy
    if 'only_otsu' in kwargs:
        if kwargs['only_otsu'] is True:
            return mos_proc.get_central_mask(otsu_masks(imgs[0]))
    try_otsu = try_bools[-1] #Otsu thresholding bool will always be last
    try_cont_enh = try_bools[-2]#contrast enhancement will always be 2nd to last

    #iterate through images, trying to predict on each. Return first success.
    for each_img in imgs:
        central_mask_ret = mos_proc.get_central_mask(curr_predictor(each_img[:,:,::-1]),
                                                     verbose=False)
        #return vals if central mask found
        if central_mask_ret[0]:
            return central_mask_ret
    if try_cont_enh is True: #contrast enhancement will always be 2nd to last
        red = skimage.exposure.equalize_hist(imgs[0][:, :, 0])
        green = skimage.exposure.equalize_hist(imgs[0][:, :, 1])
        blue = skimage.exposure.equalize_hist(imgs[0][:, :, 2])
        cont_enhanced = np.stack([red, green, blue], axis=2)
        central_mask_ret=mos_proc.get_central_mask(curr_predictor(cont_enhanced[:,:,::-1]),
                                                   verbose=False)
    if try_otsu:
        return mos_proc.get_central_mask(otsu_masks(imgs[0]), verbose=False)
    #finally, return nothing except a failure indicator if nothing worked
    return False, []