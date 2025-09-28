import matplotlib.pyplot as plt
from .styles import EventStyle

def plot_events(ax, profile_events, plot_type='normal', event_alpha=0.6):
    """
    Plots the hline or vline for each event on a plot
    Args:
        ax: matplotlib.Axes to add horizontal or vertical lines to
        start: Array index to represent start of motion
        surface: Array index to represent snow surface
        stop: Array index to represent stop of motion
        nir_stop: Array index to represent stop estimated by nir
        plot_type: string indicating whether the index is on the y (vertical) or the x (normal)
    """
    # PLotting sensor data on the x axis and time/or depth on y axis
    if plot_type == 'vertical':
        line_fn = ax.axhline

    # Normal time series data with y = values, x = time
    elif plot_type == 'normal':
        line_fn = ax.axvline

    else:
        raise ValueError(f'Unrecognized plot type {plot_type}, options are vertical or normal!')

    for event in profile_events:
        if event.time is not None:
            style = EventStyle.from_name(event.name)
            line_fn(event.time, linestyle=style.linestyle, color=style.color,
                    label=style.label, alpha=event_alpha,  linewidth=style.linewidth)


def plot_ts(data, data_label=None, time_data=None, events=None, thresholds=None, features=None, show=True, ax=None, alpha=1.0, color=None):
    if ax is None:
        fig, ax = plt.subplots(1)
        ax.grid(True)
    n_samples = len(data)
    if n_samples < 100:
        mark = 'o--'
    else:
        mark = '-'

    if time_data is not None:
        ax.plot(time_data, data, mark, alpha=alpha, label=data_label, color=color)
    else:
        ax.plot(data, mark, alpha=alpha, label=data_label, color=color)

    if data_label is not None:
        ax.legend()

    if events is not None:
        for name, event_idx in events:
            s = EventStyle.from_name(name)
            if time_data is not None:
                v = time_data[event_idx]
            else:
                v = event_idx
            ax.axvline(v, color=s.color, linestyle=s.linestyle, label=name)
    if thresholds is not None:
        for name, tr in thresholds:
            ax.axhline(tr, label=name, alpha=0.8, linestyle='--')

    if features is not None:
        ydata = [data[f] for f in features]
        if time_data is not None:
            ax.plot([time_data[f] for f in features], ydata, '.')
        else:
            ax.plot(features, ydata, '.')

    if show:
        plt.show()

    return ax


def plot_constrained_baro(orig, partial, full, acc_pos, top, bottom, start, stop,
                          baro='filtereddepth', acc_axis='Y-Axis'):

    # zero it out
    partial[baro] = partial[baro] - partial[baro].iloc[0]
    # partial = partial.reset_index('time')
    # orig = orig.set_index('time')

    mid = int((start+stop)/2)

    orig[baro] = orig[baro] - orig[baro].iloc[0]
    ax = plot_ts(orig[baro], time_data=orig['time'], color='steelblue', alpha=0.2,
                 data_label='Orig.', show=False, features=[top, bottom])
    ax = plot_ts(acc_pos[acc_axis], time_data=acc_pos['time'], color='black', alpha=0.5,
                 ax=ax, data_label='Acc.', show=False,
                 events=[('start', start), ('stop', stop), ('mid', mid)])
    ax = plot_ts(partial[baro], time_data=partial['time'], color='blue',
                 ax=ax, show=False, data_label='Part. Const.', alpha=0.3)
    ax = plot_ts(full, time_data=partial['time'], color='magenta', alpha=1,
                 ax=ax, show=True, data_label='Constr.')

def plot_fused_depth(acc_depth, baro_depth, avg, scaled_baro=None, error=None):
    """
    Diagnostic plot to show the inner workings of the fusing technique
    """
    events = None
    if error is not None:
        events=[('error',error)]
    ax = plot_ts(avg, events=events, show=False)
    ax = plot_ts(acc_depth, ax=ax, data_label='Acc', show=False)
    ax = plot_ts(baro_depth, ax=ax, data_label='Baro', show=False)
    if scaled_baro is not None:
        ax = plot_ts(scaled_baro, ax=ax, data_label='Scaled Baro', show=False)

    ax.legend()
    plt.show()


def plot_ground_strike(signal, impact_series, long_press_series, search_start, stop_idx, impact, long_press, ground):
    events = [('stop', stop_idx)]
    impact_events = [('stop', stop_idx - search_start)]

    if long_press is not None:
        events.append(('long_press', long_press))
        impact_events.append(('long_press', long_press-search_start))

    if impact is not None:
        events.append(('impact', impact))
        impact_events.append(('impact', impact-search_start))

    if ground is not None:
        events.append(('ground', ground))

    fig, (ax1, ax2, ax3) = plt.subplots(3,1)
    ax1 = plot_ts(signal, events=events,show=False, ax=ax1)
    ax1.set_title('Full series and events')
    ax1.legend()

    plot_ts(impact_series, events=impact_events, ax=ax2, show=False)
    ax2.set_title('impact')
    ax2.legend()

    plot_ts(long_press_series, events=impact_events, ax=ax3, show=False)
    ax3.set_title('Long Press')
    ax3.legend()
    plt.tight_layout()
    plt.show()

def plot_nir_cleaning(active, ambient, norm_active, norm_ambient, diff, clean):

    fig,axes = plt.subplots(2,1)
    # Plot normalized
    plot_ts(norm_ambient, ax=axes[0], data_label='norm amb.', show=False)
    plot_ts(norm_active, ax=axes[0], data_label='norm act.', show=False)
    plot_ts(diff, ax=axes[0], data_label='norm diff', show=False)

    plot_ts(ambient, ax=axes[1], data_label='ambient', show=False)
    plot_ts(active, ax=axes[1], data_label='active', show=False)

    plot_ts(clean, ax=axes[1], data_label='clean.', show=False)
    plt.show()

def plot_nir_surface(clean_active, diff, surface):
    events = []
    if surface is not None:
        events.append(('surface', surface))

    fig,axes = plt.subplots(2, 1)
    plot_ts(clean_active,events=events, ax=axes[0], show=False)
    plot_ts(diff, events=events, ax=axes[1])