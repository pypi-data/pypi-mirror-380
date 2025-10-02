from collections.abc import Callable, Generator, Sequence

import dask.array as da
import numpy as np

from ngio.common import Roi
from ngio.experimental.iterators._abstract_iterator import AbstractIteratorBuilder
from ngio.images import Image, Label
from ngio.images._image import (
    ChannelSlicingInputType,
    add_channel_selection_to_slicing_dict,
)
from ngio.io_pipes import DaskRoiGetter, NumpyRoiGetter, TransformProtocol


class FeatureExtractorIterator(AbstractIteratorBuilder):
    """Base class for iterators over ROIs."""

    def __init__(
        self,
        input_image: Image,
        input_label: Label,
        channel_selection: ChannelSlicingInputType = None,
        axes_order: Sequence[str] | None = None,
        input_transforms: Sequence[TransformProtocol] | None = None,
        label_transforms: Sequence[TransformProtocol] | None = None,
    ) -> None:
        """Initialize the iterator with a ROI table and input/output images.

        Args:
            input_image (Image): The input image to be used as input for the
                segmentation.
            input_label (Label): The input label with the segmentation masks.
            channel_selection (ChannelSlicingInputType): Optional
                selection of channels to use for the segmentation.
            axes_order (Sequence[str] | None): Optional axes order for the
                segmentation.
            input_transforms (Sequence[TransformProtocol] | None): Optional
                transforms to apply to the input image.
            label_transforms (Sequence[TransformProtocol] | None): Optional
                transforms to apply to the output label.
        """
        self._input = input_image
        self._input_label = input_label
        self._ref_image = input_image
        self._rois = input_image.build_image_roi_table(name=None).rois()

        # Set iteration parameters
        self._input_slicing_kwargs = add_channel_selection_to_slicing_dict(
            image=self._input, channel_selection=channel_selection, slicing_dict={}
        )
        self._channel_selection = channel_selection
        self._axes_order = axes_order
        self._input_transforms = input_transforms
        self._label_transforms = label_transforms

        self._input.require_axes_match(self._input_label)
        self._input.require_can_be_rescaled(self._input_label)

    def get_init_kwargs(self) -> dict:
        """Return the initialization arguments for the iterator."""
        return {
            "input_image": self._input,
            "input_label": self._input_label,
            "channel_selection": self._channel_selection,
            "axes_order": self._axes_order,
            "input_transforms": self._input_transforms,
            "label_transforms": self._label_transforms,
        }

    def build_numpy_getter(self, roi: Roi):
        data_getter = NumpyRoiGetter(
            zarr_array=self._input.zarr_array,
            dimensions=self._input.dimensions,
            axes_order=self._axes_order,
            transforms=self._input_transforms,
            roi=roi,
            slicing_dict=self._input_slicing_kwargs,
        )
        label_getter = NumpyRoiGetter(
            zarr_array=self._input_label.zarr_array,
            dimensions=self._input_label.dimensions,
            axes_order=self._axes_order,
            transforms=self._label_transforms,
            roi=roi,
            remove_channel_selection=True,
        )
        return lambda: (data_getter(), label_getter(), roi)

    def build_numpy_setter(self, roi: Roi):
        return None

    def build_dask_getter(self, roi: Roi):
        data_getter = DaskRoiGetter(
            zarr_array=self._input.zarr_array,
            dimensions=self._input.dimensions,
            axes_order=self._axes_order,
            transforms=self._input_transforms,
            roi=roi,
            slicing_dict=self._input_slicing_kwargs,
        )
        label_getter = DaskRoiGetter(
            zarr_array=self._input_label.zarr_array,
            dimensions=self._input_label.dimensions,
            axes_order=self._axes_order,
            transforms=self._label_transforms,
            roi=roi,
            remove_channel_selection=True,
        )
        return lambda: (data_getter(), label_getter(), roi)

    def build_dask_setter(self, roi: Roi):
        return None

    def post_consolidate(self):
        pass

    def iter_as_numpy(self) -> Generator[tuple[np.ndarray, np.ndarray, Roi]]:  # type: ignore (non compatible override)
        """Create an iterator over the pixels of the ROIs as Dask arrays.

        Returns:
            Generator[tuple[da.Array, DaskWriter]]: An iterator the input
                image as Dask arrays and a writer to write the output
                to the label image.
        """
        for (data, label, roi), _ in super().iter_as_numpy():
            yield data, label, roi

    def map_as_numpy(self, func: Callable[[np.ndarray], np.ndarray]) -> None:
        """Apply a transformation function to the ROI pixels."""
        raise NotImplementedError("Numpy mapping not implemented for this iterator.")

    def iter_as_dask(self) -> Generator[tuple[da.Array, da.Array, Roi]]:  # type: ignore (non compatible override)
        """Create an iterator over the pixels of the ROIs as Dask arrays.

        Returns:
            Generator[tuple[da.Array, DaskWriter]]: An iterator the input
                image as Dask arrays and a writer to write the output
                to the label image.
        """
        for (data, label, roi), _ in super().iter_as_dask():
            yield data, label, roi

    def map_as_dask(self, func: Callable[[da.Array], da.Array]) -> None:
        """Apply a transformation function to the ROI pixels."""
        raise NotImplementedError("Dask mapping not implemented for this iterator.")
