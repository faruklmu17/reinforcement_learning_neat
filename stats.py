"""Minimal stats utilities used by Neatprogram.py when the original
`stats` module is missing. Provides `generation_stats_str` used by the
custom reporter in the training script.
"""

def generation_stats_str(stats_reporter, population_obj, generation=None):
    try:
        gen = generation if generation is not None else getattr(stats_reporter, 'generation', 'N/A')
        pop_size = len(population_obj) if population_obj is not None else 'N/A'
        return f'Generation {gen} | population={pop_size} | (stats stub)'
    except Exception:
        return f'Generation {generation} | (stats unavailable)'
