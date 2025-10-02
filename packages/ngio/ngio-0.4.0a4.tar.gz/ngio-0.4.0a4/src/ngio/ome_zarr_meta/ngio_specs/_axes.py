"""Fractal internal module for axes handling."""

from collections.abc import Sequence
from enum import Enum
from typing import Literal, TypeAlias, TypeVar

import numpy as np
from pydantic import BaseModel, ConfigDict, Field

from ngio.utils import NgioValidationError, NgioValueError

T = TypeVar("T")
SlicingType: TypeAlias = slice | tuple[int, ...] | int

################################################################################################
#
# Axis Types and Units
# We define a small set of axis types and units that can be used in the metadata.
# This axis types are more restrictive than the OME standard.
# We do that to simplify the data processing.
#
#################################################################################################


class AxisType(str, Enum):
    """Allowed axis types."""

    channel = "channel"
    time = "time"
    space = "space"


SpaceUnits = Literal[
    "micrometer",
    "nanometer",
    "angstrom",
    "picometer",
    "millimeter",
    "centimeter",
    "decimeter",
    "meter",
    "inch",
    "foot",
    "yard",
    "mile",
    "kilometer",
    "hectometer",
    "megameter",
    "gigameter",
    "terameter",
    "petameter",
    "exameter",
    "parsec",
    "femtometer",
    "attometer",
    "zeptometer",
    "yoctometer",
    "zettameter",
    "yottameter",
]
DefaultSpaceUnit = "micrometer"

TimeUnits = Literal[
    "attosecond",
    "centisecond",
    "day",
    "decisecond",
    "exasecond",
    "femtosecond",
    "gigasecond",
    "hectosecond",
    "hour",
    "kilosecond",
    "megasecond",
    "microsecond",
    "millisecond",
    "minute",
    "nanosecond",
    "petasecond",
    "picosecond",
    "second",
    "terasecond",
    "yoctosecond",
    "yottasecond",
    "zeptosecond",
    "zettasecond",
]
DefaultTimeUnit = "second"


class Axis(BaseModel):
    """Axis infos model."""

    name: str
    unit: str | None = None
    axis_type: AxisType | None = None

    model_config = ConfigDict(extra="forbid", frozen=True)

    def implicit_type_cast(self, cast_type: AxisType) -> "Axis":
        unit = self.unit
        if cast_type == AxisType.time and unit is None:
            unit = DefaultTimeUnit

        if cast_type == AxisType.space and unit is None:
            unit = DefaultSpaceUnit

        return Axis(name=self.name, axis_type=cast_type, unit=unit)

    def canonical_axis_cast(self, canonical_name: str) -> "Axis":
        """Cast the implicit axis to the correct type."""
        match canonical_name:
            case "t":
                if self.axis_type != AxisType.time or self.unit is None:
                    return self.implicit_type_cast(AxisType.time)
            case "c":
                if self.axis_type != AxisType.channel:
                    return self.implicit_type_cast(AxisType.channel)
            case "z" | "y" | "x":
                if self.axis_type != AxisType.space or self.unit is None:
                    return self.implicit_type_cast(AxisType.space)
        return self


################################################################################################
#
# Axes Handling
# We define a unique mapping to match the axes on disk to the canonical axes.
# The canonical axes are the ones that are used consistently in the NGIO internal API.
# The canonical axes ordered are: t, c, z, y, x.
#
#################################################################################################


def canonical_axes_order() -> tuple[str, str, str, str, str]:
    """Get the canonical axes order."""
    return "t", "c", "z", "y", "x"


def canonical_label_axes_order() -> tuple[str, str, str, str]:
    """Get the canonical axes order."""
    return "t", "z", "y", "x"


class AxesSetup(BaseModel):
    """Axes setup model.

    This model is used to map the on disk axes to the canonical OME-Zarr axes.
    """

    x: str = "x"
    y: str = "y"
    z: str = "z"
    c: str = "c"
    t: str = "t"
    others: list[str] = Field(default_factory=list)

    model_config = ConfigDict(extra="forbid", frozen=True)

    def canonical_map(self) -> dict[str, str]:
        """Get the canonical map of axes."""
        return {
            "t": self.t,
            "c": self.c,
            "z": self.z,
            "y": self.y,
            "x": self.x,
        }

    def get_on_disk_name(self, canonical_name: str) -> str | None:
        """Get the on disk name of the axis by its canonical name."""
        canonical_map = self.canonical_map()
        return canonical_map.get(canonical_name, None)

    def inverse_canonical_map(self) -> dict[str, str]:
        """Get the on disk map of axes."""
        return {
            self.t: "t",
            self.c: "c",
            self.z: "z",
            self.y: "y",
            self.x: "x",
        }

    def get_canonical_name(self, on_disk_name: str) -> str | None:
        """Get the canonical name of the axis by its on disk name."""
        inv_map = self.inverse_canonical_map()
        return inv_map.get(on_disk_name, None)


def _check_unique_names(axes: Sequence[Axis]):
    """Check if all axes on disk have unique names."""
    names = [ax.name for ax in axes]
    if len(set(names)) != len(names):
        duplicates = {item for item in names if names.count(item) > 1}
        raise NgioValidationError(
            f"All axes must be unique. But found duplicates axes {duplicates}"
        )


def _check_non_canonical_axes(axes_setup: AxesSetup, allow_non_canonical_axes: bool):
    """Check if all axes are known."""
    if not allow_non_canonical_axes and len(axes_setup.others) > 0:
        raise NgioValidationError(
            f"Unknown axes {axes_setup.others}. Please set "
            "`allow_non_canonical_axes=True` to ignore them"
        )


def _check_axes_validity(axes: Sequence[Axis], axes_setup: AxesSetup):
    """Check if all axes are valid."""
    _axes_setup = axes_setup.model_dump(exclude={"others"})
    _all_known_axes = [*_axes_setup.values(), *axes_setup.others]
    for ax in axes:
        if ax.name not in _all_known_axes:
            raise NgioValidationError(
                f"Invalid axis name '{ax.name}'. "
                f"Please correct map `{ax.name}` "
                f"using the AxesSetup model {axes_setup}"
            )


def _check_canonical_order(
    axes: Sequence[Axis], axes_setup: AxesSetup, strict_canonical_order: bool
):
    """Check if the axes are in the canonical order."""
    if not strict_canonical_order:
        return
    _names = [ax.name for ax in axes]
    _canonical_order = []
    for name in canonical_axes_order():
        mapped_name = getattr(axes_setup, name)
        if mapped_name in _names:
            _canonical_order.append(mapped_name)

    if _names != _canonical_order:
        raise NgioValidationError(
            f"Invalid axes order. The axes must be in the canonical order. "
            f"Expected {_canonical_order}, but found {_names}"
        )


def validate_axes(
    axes: Sequence[Axis],
    axes_setup: AxesSetup,
    allow_non_canonical_axes: bool = False,
    strict_canonical_order: bool = False,
) -> None:
    """Validate the axes."""
    if allow_non_canonical_axes and strict_canonical_order:
        raise NgioValidationError(
            "`allow_non_canonical_axes` and"
            "`strict_canonical_order` cannot be true at the same time."
            "If non canonical axes are allowed, the order cannot be checked."
        )
    _check_unique_names(axes=axes)
    _check_non_canonical_axes(
        axes_setup=axes_setup, allow_non_canonical_axes=allow_non_canonical_axes
    )
    _check_axes_validity(axes=axes, axes_setup=axes_setup)
    _check_canonical_order(
        axes=axes, axes_setup=axes_setup, strict_canonical_order=strict_canonical_order
    )


class AxesOps(BaseModel):
    """Model to represent axes operations.

    This model will be used to transform objects from on disk axes to in memory axes.
    """

    on_disk_axes: tuple[str, ...]
    in_memory_axes: tuple[str, ...]
    transpose_op: tuple[int, ...] | None = None
    expand_op: tuple[int, ...] | None = None
    squeeze_op: tuple[int, ...] | None = None
    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    @property
    def is_no_op(self) -> bool:
        """Check if all operations are no ops."""
        if (
            self.transpose_op is None
            and self.expand_op is None
            and self.squeeze_op is None
        ):
            return True
        return False

    @property
    def get_transpose_op(self) -> tuple[int, ...] | None:
        """Get the transpose axes."""
        return self.transpose_op

    @property
    def get_expand_op(self) -> tuple[int, ...] | None:
        """Get the expand axes."""
        return self.expand_op

    @property
    def get_squeeze_op(self) -> tuple[int, ...] | None:
        """Get the squeeze axes."""
        return self.squeeze_op

    @property
    def set_transpose_op(self) -> tuple[int, ...] | None:
        """Set the transpose axes."""
        if self.transpose_op is None:
            return None
        return tuple(np.argsort(self.transpose_op))

    @property
    def set_expand_op(self) -> tuple[int, ...] | None:
        """Set the expand axes."""
        return self.squeeze_op

    @property
    def set_squeeze_op(self) -> tuple[int, ...] | None:
        """Set the squeeze axes."""
        return self.expand_op


class AxesHandler:
    """This class is used to handle and operate on OME-Zarr axes.

    The class also provides:
        - methods to reorder, squeeze and expand axes.
        - methods to validate the axes.
        - methods to get axis by name or index.
        - methods to operate on the axes.
    """

    def __init__(
        self,
        # spec dictated args
        axes: Sequence[Axis],
        # user defined args
        axes_setup: AxesSetup | None = None,
        allow_non_canonical_axes: bool = False,
        strict_canonical_order: bool = False,
    ):
        """Create a new AxesMapper object.

        Args:
            axes (list[Axis]): The axes on disk.
            axes_setup (AxesSetup, optional): The axis setup. Defaults to None.
            allow_non_canonical_axes (bool, optional): Allow non canonical axes.
            strict_canonical_order (bool, optional): Check if the axes are in the
                canonical order. Defaults to False.
        """
        axes_setup = axes_setup if axes_setup is not None else AxesSetup()

        validate_axes(
            axes=axes,
            axes_setup=axes_setup,
            allow_non_canonical_axes=allow_non_canonical_axes,
            strict_canonical_order=strict_canonical_order,
        )

        self._allow_non_canonical_axes = allow_non_canonical_axes
        self._strict_canonical_order = strict_canonical_order

        self._canonical_order = canonical_axes_order()

        self._axes = axes
        self._axes_setup = axes_setup

        self._index_mapping = self._compute_index_mapping()

        # Validate the axes type and cast them if necessary
        # This needs to be done after the name mapping is computed
        self.validate_axes_type()

    def _compute_index_mapping(self):
        """Compute the index mapping.

        The index mapping is a dictionary with keys the canonical axes names
        and values the on disk axes index.

        Example:
            If the on disk axes are ['channel', 't', 'z', 'y', 'x'],
            the index mapping will be:
            {
                'c': 0,
                'channel': 0,
                't': 1,
                'z': 2,
                'y': 3,
                'x': 4,
            }
        """
        _index_mapping = {}
        for i, ax in enumerate(self.axes_names):
            _index_mapping[ax] = i
        # If the axis is not in the canonical order we also set it.
        canonical_map = self._axes_setup.canonical_map()
        for canonical_name, on_disk_name in canonical_map.items():
            if on_disk_name in _index_mapping.keys():
                _index_mapping[canonical_name] = _index_mapping[on_disk_name]
        return _index_mapping

    @property
    def axes_setup(self) -> AxesSetup:
        """Return the axes setup."""
        return self._axes_setup

    @property
    def axes(self) -> tuple[Axis, ...]:
        return tuple(self._axes)

    @property
    def axes_names(self) -> tuple[str, ...]:
        return tuple(ax.name for ax in self._axes)

    @property
    def allow_non_canonical_axes(self) -> bool:
        """Return if non canonical axes are allowed."""
        return self._allow_non_canonical_axes

    @property
    def strict_canonical_order(self) -> bool:
        """Return if strict canonical order is enforced."""
        return self._strict_canonical_order

    @property
    def space_unit(self) -> str | None:
        """Return the space unit for a given axis."""
        x_axis = self.get_axis("x")
        y_axis = self.get_axis("y")

        if x_axis is None or y_axis is None:
            raise NgioValidationError(
                "The dataset must have x and y axes to determine the space unit."
            )

        if x_axis.unit == y_axis.unit:
            return x_axis.unit
        else:
            raise NgioValidationError(
                "Inconsistent space units. "
                f"x={x_axis.unit} and y={y_axis.unit} should have the same unit."
            )

    @property
    def time_unit(self) -> str | None:
        """Return the time unit for a given axis."""
        t_axis = self.get_axis("t")
        if t_axis is None:
            return None
        return t_axis.unit

    def to_units(
        self,
        *,
        space_unit: SpaceUnits = DefaultSpaceUnit,
        time_unit: TimeUnits = DefaultTimeUnit,
    ) -> "AxesHandler":
        """Convert the pixel size to the given units.

        Args:
            space_unit(str): The space unit to convert to.
            time_unit(str): The time unit to convert to.
        """
        new_axes = []
        for ax in self.axes:
            if ax.axis_type == AxisType.space:
                new_ax = Axis(
                    name=ax.name,
                    axis_type=ax.axis_type,
                    unit=space_unit,
                )
                new_axes.append(new_ax)
            elif ax.axis_type == AxisType.time:
                new_ax = Axis(name=ax.name, axis_type=ax.axis_type, unit=time_unit)
                new_axes.append(new_ax)
            else:
                new_axes.append(ax)

        return AxesHandler(
            axes=new_axes,
            axes_setup=self.axes_setup,
            allow_non_canonical_axes=self.allow_non_canonical_axes,
            strict_canonical_order=self.strict_canonical_order,
        )

    def get_index(self, name: str) -> int | None:
        """Get the index of the axis by name."""
        return self._index_mapping.get(name, None)

    def get_canonical_name(self, name: str) -> str | None:
        """Get the canonical name of the axis by name."""
        return self._axes_setup.get_canonical_name(name)

    def get_axis(self, name: str) -> Axis | None:
        """Get the axis object by name."""
        index = self.get_index(name)
        if index is None:
            return None
        return self.axes[index]

    def validate_axes_type(self):
        """Validate the axes type.

        If the axes type is not correct, a warning is issued.
        and the axis is implicitly cast to the correct type.
        """
        new_axes = []
        for axes in self.axes:
            for name in self._canonical_order:
                if axes == self.get_axis(name):
                    new_axes.append(axes.canonical_axis_cast(name))
                    break
            else:
                new_axes.append(axes)
        self._axes = new_axes

    def _reorder_axes(
        self, names: Sequence[str]
    ) -> tuple[tuple[int, ...] | None, tuple[int, ...] | None, tuple[int, ...] | None]:
        """Change the order of the axes."""
        # Validate the names
        unique_names = set(names)
        if len(unique_names) != len(names):
            raise NgioValueError(
                "Duplicate axis names found. Please provide unique names for each axis."
            )
        for name in names:
            if not isinstance(name, str):
                raise NgioValueError(
                    f"Invalid axis name '{name}'. Axis names must be strings."
                )
        inv_canonical_map = self.axes_setup.inverse_canonical_map()

        # Step 1: Check find squeeze axes
        _axes_to_squeeze: list[int] = []
        axes_names_after_squeeze = []
        for i, ax in enumerate(self.axes_names):
            # If the axis is not in the names, it means we need to squeeze it
            ax_canonical = inv_canonical_map.get(ax, None)
            if ax not in names and ax_canonical not in names:
                _axes_to_squeeze.append(i)
            elif ax in names:
                axes_names_after_squeeze.append(ax)
            elif ax_canonical in names:
                # If the axis is in the canonical map, we add it to the names
                axes_names_after_squeeze.append(ax_canonical)

        axes_to_squeeze = tuple(_axes_to_squeeze) if len(_axes_to_squeeze) > 0 else None

        # Step 2: Find the transposition order
        _transposition_order: list[int] = []
        axes_names_after_transpose = []
        for ax in names:
            if ax in axes_names_after_squeeze:
                _transposition_order.append(axes_names_after_squeeze.index(ax))
                axes_names_after_transpose.append(ax)

        if np.allclose(_transposition_order, range(len(_transposition_order))):
            # If the transposition order is the identity, we don't need to transpose
            transposition_order = None
        else:
            transposition_order = tuple(_transposition_order)

        # Step 3: Find axes to expand
        _axes_to_expand: list[int] = []
        for i, name in enumerate(names):
            if name not in axes_names_after_transpose:
                # If the axis is not in the mapping, it means we need to expand it
                _axes_to_expand.append(i)

        axes_to_expand = tuple(_axes_to_expand) if len(_axes_to_expand) > 0 else None
        return axes_to_squeeze, transposition_order, axes_to_expand

    def get_axes_ops(self, names: Sequence[str]) -> AxesOps:
        """Get the axes operations to go from on-disk to in-memory axes."""
        axes_to_squeeze, transposition_order, axes_to_expand = self._reorder_axes(names)
        return AxesOps(
            on_disk_axes=self.axes_names,
            in_memory_axes=tuple(names),
            transpose_op=transposition_order,
            expand_op=axes_to_expand,
            squeeze_op=axes_to_squeeze,
        )

    def get_canonical_axes_ops(self) -> AxesOps:
        """Get the axes operations to go from on-disk to canonical in-memory axes."""
        other = self._axes_setup.others
        return self.get_axes_ops(list(self._canonical_order) + other)


def build_canonical_axes_handler(
    axes_names: Sequence[str],
    space_units: SpaceUnits | str | None = DefaultSpaceUnit,
    time_units: TimeUnits | str | None = DefaultTimeUnit,
    # user defined args
    axes_setup: AxesSetup | None = None,
    allow_non_canonical_axes: bool = False,
    strict_canonical_order: bool = False,
) -> AxesHandler:
    """Create a new canonical axes mapper.

    Args:
        axes_names (Sequence[str] | int): The axes names on disk.
            - The axes should be in ['t', 'c', 'z', 'y', 'x']
            - The axes should be in strict canonical order.
            - If an integer is provided, the axes are created from the last axis
              to the first
                e.g. 3 -> ["z", "y", "x"]
        space_units (SpaceUnits, optional): The space units. Defaults to None.
        time_units (TimeUnits, optional): The time units. Defaults to None.
        axes_setup (AxesSetup, optional): The axis setup. Defaults to None.
        allow_non_canonical_axes (bool, optional): Allow non canonical axes.
            Defaults to False.
        strict_canonical_order (bool, optional): Check if the axes are in the
            canonical order. Defaults to False.

    """
    axes = []
    for name in axes_names:
        match name:
            case "t":
                axes.append(Axis(name=name, axis_type=AxisType.time, unit=time_units))
            case "c":
                axes.append(Axis(name=name, axis_type=AxisType.channel))
            case "z" | "y" | "x":
                axes.append(Axis(name=name, axis_type=AxisType.space, unit=space_units))
            case _:
                raise NgioValueError(
                    f"Invalid axis name '{name}'. "
                    "Only 't', 'c', 'z', 'y', 'x' are allowed."
                )

    return AxesHandler(
        axes=axes,
        axes_setup=axes_setup,
        allow_non_canonical_axes=allow_non_canonical_axes,
        strict_canonical_order=strict_canonical_order,
    )
