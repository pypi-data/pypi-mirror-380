from __future__ import annotations

from langcheck.metrics.metric_inputs import (
    get_metric_inputs_with_required_lists,
)
from langcheck.metrics.metric_value import (
    MetricValue,
)
from langcheck.utils.progress_bar import tqdm_wrapper


def exact_match(
    generated_outputs: list[str] | str,
    reference_outputs: list[str] | str,
    prompts: list[str] | str | None = None,
) -> MetricValue[int]:
    """Checks if the generated outputs exact matches with the reference outputs.
    This metric takes on binary 0 or 1 values.

    Args:
        generated_outputs: The model generated output(s) to evaluate
        reference_outputs: The reference output(s)
        prompts: The prompts used to generate the output(s). Prompts are
            optional metadata and not used to calculate the metric.

    Returns:
        An :class:`~langcheck.metrics.metric_value.MetricValue` object
    """
    metric_inputs, [generated_outputs, reference_outputs] = (
        get_metric_inputs_with_required_lists(
            generated_outputs=generated_outputs,
            reference_outputs=reference_outputs,
            prompts=prompts,
            required_params=["generated_outputs", "reference_outputs"],
        )
    )

    # The values are binary: 1 if it's an exact match and 0 if not
    metric_values = []
    for gen, ref in tqdm_wrapper(
        zip(generated_outputs, reference_outputs), total=len(generated_outputs)
    ):
        if gen == ref:
            metric_values.append(1)
        else:
            metric_values.append(0)

    return MetricValue(
        metric_name="exact_match",
        metric_inputs=metric_inputs,
        explanations=None,
        metric_values=metric_values,
        language=None,
    )
