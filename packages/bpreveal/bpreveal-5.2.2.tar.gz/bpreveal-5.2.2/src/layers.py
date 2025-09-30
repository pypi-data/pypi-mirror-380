"""Custom layers that are needed for the various models."""
from collections.abc import Callable
from typing import Any
from bpreveal.internal import disableTensorflowLogging  # pylint: disable=unused-import # noqa
from keras.layers import Conv1D, Reshape, Layer  # type: ignore
from keras.ops import convert_to_tensor
import keras.saving
import tensorflow as tf
from bpreveal import logUtils


def linearRegression(**kwargs) -> Callable:
    """A linear regression layer that's compatible with shap.

    .. highlight:: none

    Implements the following formula::

        out = input * slope + offset

    where slope and offset are two (scalar) parameters.

    .. highlight:: python

    Note that although this is a function, it behaves like a normal Keras layer class
    and you create it like this::

        regression = bpreveal.layers.LinearRegression(name="oct4_regression")(regressionInput)


    :param kwargs: Passed to the keras Layer initializer.
    :return: A function that you can call with a Keras layer as input, like a normal
        Keras Layer class.
    :rtype: A function taking a tensor and returning a tensor.
    """
    def layer(inputs):  # noqa
        """The function that will be run to build the layer.

        :param inputs: The input data
        :type inputs: Tensor
        :return: The data shifted by a linear function.
        :rtype: Tensor
        """
        regName = kwargs.get("name", "linReg")
        # Make the layer a (none, length, 1) shape tensor. # noqa
        reshaped = Reshape((-1, 1), name=regName + "_r1")(inputs)
        # A convolution is a multiplication if you think about it wrong enough.
        # x ★ y = x * y if y ∈ R¹
        # and the Conv1D layer includes bias, so that's where the +b comes from.
        convolved = Conv1D(filters=1,
                           kernel_size=1,
                           kernel_initializer="Ones",
                           name=regName + "_conv")(reshaped)
        # Restore the original shape.
        unreshaped = Reshape(inputs.shape[1:], name=regName + "_r2")(convolved)
        logUtils.debug(f"Built regression layer '{regName}' with output shape {inputs.shape[1:]}.")
        return unreshaped
    return layer


try:
    import sphinx
    SPHINX_BUILD = hasattr(sphinx, "application")
except ImportError:
    SPHINX_BUILD = False
# pylint: disable=abstract-method,too-many-ancestors,arguments-differ
if SPHINX_BUILD:
    class CountsLogSumExp(Layer):  # noqa
        """A simple layer that wraps keras.ops.logaddexp."""

        def call(self, inp1, inp2) -> Any:  # noqa  # pylint: disable=unused-argument
            """Calculate logsumexp.

            :param inp1: The first value
            :type inp1: Tensor
            :param inp2: The second value
            :type inp2: Tensor
            :return: log(exp(inp1) + exp(inp2)).
            :rtype: Tensor

            """
            return -1

        def get_config(self) -> dict:  # pylint: disable=invalid-name
            """Used to make this class deserializable.

            :return: A configuration dictionary. There is no custom data in it.
            """
            base = super().get_config()
            config = {}
            return {**base, **config}

else:
    @keras.saving.register_keras_serializable(package="bpreveal", name="CountsLogSumExp")
    class CountsLogSumExp(Layer):
        """A simple layer that wraps keras.ops.logaddexp."""

        def call(self, inp1, inp2):  # noqa
            """Calculate logsumexp.

            :param inp1: The first value
            :type inp1: Tensor
            :param inp2: The second value
            :type inp2: Tensor
            :return: log(exp(inp1) + exp(inp2)).
            :rtype: Tensor

            """
            # I would just return ops.logaddexp(inp1, inp2)
            # but that introduces a SelectV2 call in the graph which Shap
            # (rightly) explodes on.
            # So I do it manually, with the possibility of numerical error.
            # However, we are saved here by the nature of the numbers we are adding
            # these are log counts, and therefore they will be normal numbers that
            # are not extremely large or small. Numerical error will therefore
            # be acceptable. If your sequencing depth is 10^280-fold coverage,
            # you have other problems.
            x1 = convert_to_tensor(inp1)
            x2 = convert_to_tensor(inp2)
            x1 = tf.cast(x1, tf.float64)
            x2 = tf.cast(x2, tf.float64)
            # Here is where the NaN check is deleted.
            expx1 = tf.math.exp(x1)
            expx2 = tf.math.exp(x2)
            sumexp = expx1 + expx2
            logsumexp = tf.math.log(sumexp)
            return tf.cast(logsumexp, inp1.dtype)

        def get_config(self) -> dict:  # pylint: disable=invalid-name
            """Used to make this serializable.

            :return: A configuration dictionary. There is no custom data in it.
            """
            base = super().get_config()
            config = {}
            return {**base, **config}
# pylint: enable=abstract-method,too-many-ancestors,arguments-differ

# Copyright 2022-2025 Charles McAnany. This file is part of BPReveal. BPReveal is free software: You can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version. BPReveal is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with BPReveal. If not, see <https://www.gnu.org/licenses/>.  # noqa
