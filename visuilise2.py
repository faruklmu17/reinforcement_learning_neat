"""Minimal visualization stubs for Neatprogram.py.
These provide lightweight no-op implementations so training can run
when the original visualization modules are missing.
"""

import sys


def draw_net(config, genome, view=False, fmt='png', show_disabled=False, prune_unused=False, node_names=None):
    # Safe no-op: the original function likely produced a graphviz image.
    # We keep this lightweight and side-effect free.
    try:
        print(f"visuilise2.draw_net called for genome id={getattr(genome, 'key', str(genome))} view={view}")
    except Exception:
        print("visuilise2.draw_net called")


def plot_stats(stats_obj, ylog=False, view=True):
    # Try a minimal plot if matplotlib is available and stats_obj exposes data.
    try:
        import matplotlib.pyplot as plt
    except Exception:
        print('matplotlib not available - skipping plot_stats')
        return

    # Attempt to extract generation statistics (best fitness per generation)
    gens = []
    best = []
    try:
        # common StatisticsReporter fields vary; be defensive
        if hasattr(stats_obj, 'best_fitness'):
            # single value
            gens = [0]
            best = [stats_obj.best_fitness]
        elif hasattr(stats_obj, 'generation_statistics'):
            # might be a list of strings
            gens = list(range(len(stats_obj.generation_statistics)))
            best = [0] * len(gens)
        else:
            print('plot_stats: no compatible stats data found')
            return
    except Exception:
        print('plot_stats: error reading stats object')
        return

    plt.figure()
    plt.plot(gens, best)
    plt.title('Training stats (placeholder)')
    if view:
        plt.show()
    else:
        plt.close()


def plot_species(stats_obj, view=True):
    # Lightweight placeholder: print species counts if available
    try:
        if hasattr(stats_obj, 'species_sizes'):
            print('Species sizes:', stats_obj.species_sizes)
        else:
            print('plot_species: no species data available; placeholder')
    except Exception:
        print('plot_species: failed')
