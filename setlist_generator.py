import random
from models import Song

def generate_setlist(num_sets, songs_per_set):
    """
    Generate setlists based on rules and frequency weights.

    Args:
        num_sets: Number of sets to generate (1-3)
        songs_per_set: List of integers indicating songs per set

    Returns:
        Tuple of (setlists, warnings)
        - setlists: List of lists, each containing Song objects
        - warnings: List of warning messages
    """
    warnings = []
    setlists = []

    # Validate inputs
    if num_sets < 1 or num_sets > 3:
        raise ValueError("Number of sets must be between 1 and 3")

    if len(songs_per_set) != num_sets:
        raise ValueError("Number of songs per set must match number of sets")

    total_songs_needed = sum(songs_per_set)

    # Get all songs from database
    all_songs = Song.query.all()
    available_songs = list(all_songs)

    if len(available_songs) < total_songs_needed:
        raise ValueError(
            f"Not enough songs in database. Need {total_songs_needed}, but only {len(available_songs)} available."
        )

    # Track used songs to avoid repetition
    used_song_ids = set()

    for set_num in range(1, num_sets + 1):
        songs_needed = songs_per_set[set_num - 1]

        if songs_needed < 1:
            setlists.append([])
            continue

        set_songs = []

        # Filter available songs based on set constraints
        eligible_songs = []
        for song in available_songs:
            if song.id in used_song_ids:
                continue

            # Check set-specific constraints
            if set_num == 1 and song.second_set_only:
                continue
            if set_num == 2 and song.first_set_only:
                continue
            if set_num >= 2 and song.first_set_only:
                continue

            eligible_songs.append(song)

        if len(eligible_songs) < songs_needed:
            warnings.append(
                f"Set {set_num}: Not enough eligible songs. Needed {songs_needed}, found {len(eligible_songs)}. "
                "Relaxing constraints..."
            )
            # Relax constraints and try again
            eligible_songs = [s for s in available_songs if s.id not in used_song_ids]

        # 1. Select starting song if needed
        if songs_needed >= 1:
            starting_candidates = [s for s in eligible_songs if s.potential_starting_song]

            if starting_candidates:
                starting_song = weighted_random_choice(starting_candidates)
            else:
                # No designated starting songs, pick one randomly with weights
                starting_song = weighted_random_choice(eligible_songs)

            set_songs.append(starting_song)
            used_song_ids.add(starting_song.id)
            eligible_songs = [s for s in eligible_songs if s.id != starting_song.id]

        # 2. Select ending song if needed (and we need more than 1 song)
        ending_song = None
        if songs_needed >= 2:
            ending_candidates = [s for s in eligible_songs if s.potential_final_song]

            if ending_candidates:
                ending_song = weighted_random_choice(ending_candidates)
            else:
                # Reserve a random song for ending
                ending_song = weighted_random_choice(eligible_songs)

            used_song_ids.add(ending_song.id)
            eligible_songs = [s for s in eligible_songs if s.id != ending_song.id]

        # 3. Fill middle songs
        middle_songs_needed = songs_needed - len(set_songs) - (1 if ending_song else 0)

        for _ in range(middle_songs_needed):
            if not eligible_songs:
                warnings.append(f"Set {set_num}: Ran out of eligible songs after {len(set_songs)} songs")
                break

            song = weighted_random_choice(eligible_songs)
            set_songs.append(song)
            used_song_ids.add(song.id)
            eligible_songs = [s for s in eligible_songs if s.id != song.id]

        # 4. Add ending song
        if ending_song:
            set_songs.append(ending_song)

        setlists.append(set_songs)

    return setlists, warnings

def weighted_random_choice(songs):
    """
    Select a song using weighted random selection based on frequency_weight.
    Higher frequency_weight = more likely to be selected.

    Args:
        songs: List of Song objects

    Returns:
        Selected Song object
    """
    if not songs:
        raise ValueError("Cannot choose from empty song list")

    # Get weights, ensuring minimum weight of 1 to allow all songs a chance
    weights = [max(song.frequency_weight, 1.0) for song in songs]

    # Use random.choices with weights
    selected = random.choices(songs, weights=weights, k=1)[0]
    return selected
