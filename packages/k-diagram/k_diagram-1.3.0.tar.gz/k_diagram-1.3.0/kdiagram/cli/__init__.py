from __future__ import annotations

import argparse

from .. import __version__ as _VERSION

# subcommand registrars
from .plot_anomalies import add_plot_anomalies
from .plot_comparison import add_plot_comparison
from .plot_cond_relationship import add_plot_cond_relationship
from .plot_confusion_matrices import add_confusion_matrices
from .plot_context_corr import add_context_corr
from .plot_context_err import add_context_err
from .plot_coverages import add_plot_coverages
from .plot_credibility import add_plot_credibility
from .plot_drift import add_plot_drift
from .plot_errors import add_plot_errors
from .plot_eval_ext import add_eval_extension
from .plot_eval_performance import add_plot_regression_performance
from .plot_eval_relationship import add_plot_eval_relationship
from .plot_feature_based import add_plot_feature_based
from .plot_fields import add_plot_fields
from .plot_intervals import add_plot_intervals
from .plot_pr_roc import add_pr_roc
from .plot_probs import add_plot_probs
from .plot_reliability import add_plot_reliability
from .plot_sharpness import add_plot_sharpness
from .plot_taylord import add_plot_taylord
from .plot_temporal import add_plot_temporal
from .plot_ts_analyses import add_ts_analyses
from .plot_velocities import add_plot_velocities
from .plot_vs import add_plot_vs

__all__ = ["build_parser", "main"]


def build_parser() -> argparse.ArgumentParser:
    """
    Build the top-level CLI parser and register all
    subcommands from kdiagram/cli/* modules.
    """
    parser = argparse.ArgumentParser(
        prog="k-diagram",
        description=(
            "KDiagram CLI — polar diagnostics for "
            "uncertainty, drift, fields, and more."
        ),
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"kdiagram {_VERSION}",
        help="Show version and exit.",
    )

    sub = parser.add_subparsers(
        dest="command",
        metavar="<command>",
        help="Run 'kdiagram <command> -h' for help.",
    )

    # register all commands (grouped by theme)
    # Uncertainty / coverage
    add_plot_coverages(sub)
    add_plot_intervals(sub)
    add_plot_anomalies(sub)

    # Probabilistic diagnostics (PIT, CRPS, sharpness)
    add_plot_probs(sub)
    add_plot_sharpness(sub)
    add_plot_credibility(sub)

    # Drift & temporal
    add_plot_drift(sub)
    add_plot_temporal(sub)

    # Fields & vectors
    add_plot_fields(sub)
    add_plot_velocities(sub)

    # Ground-truth vs prediction
    add_plot_vs(sub)

    # Relationship views (truth vs preds, conditional bands)
    add_plot_cond_relationship(sub)
    add_plot_eval_relationship(sub)

    # errors plot
    add_plot_errors(sub)

    # comparison plots
    add_plot_reliability(sub)
    add_plot_comparison(sub)

    # feature based plot
    add_plot_feature_based(sub)

    # taylor diagrams
    add_plot_taylord(sub)

    # add contexts
    add_ts_analyses(sub)
    add_context_corr(sub)
    add_context_err(sub)

    # add evaluations plots
    add_confusion_matrices(sub)
    add_pr_roc(sub)
    add_eval_extension(sub)
    add_plot_regression_performance(sub)

    return parser


def main(args: list[str] | None = None) -> None:
    """
    CLI entrypoint. Parse args and dispatch to the
    selected subcommand.
    """
    parser = build_parser()
    ns = parser.parse_args(args=args)
    if hasattr(ns, "func"):
        ns.func(ns)
    else:
        parser.print_help()
