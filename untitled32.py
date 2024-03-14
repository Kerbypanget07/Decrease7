def sort_observations(observations):
    for i in range(1, len(observations)):
        current = observations[i]
        j = i - 1
        while j >= 0 and observations[j] > current:
            observations[j + 1] = observations[j]
            j -= 1
        observations[j + 1] = current


observations = {
    "Stars": ["StarObs_6.file", "StarObs_4.file", "StarObs_9.file", "StarObs_2.file",
              "StarObs_8.file", "StarObs_10.file", "StarObs_3.file", "StarObs_5.file",
              "StarObs_7.file", "StarObs_1.file"],
    
    "Galaxies": ["GalaxyObs_4.file", "GalaxyObs_10.file", "GalaxyObs_2.file", "GalaxyObs_8.file",
                 "GalaxyObs_3.file", "GalaxyObs_7.file", "GalaxyObs_1.file", "GalaxyObs_9.file",
                 "GalaxyObs_6.file", "GalaxyObs_5.file"],
    
    "Exoplanets": ["ExoObs_3.file", "ExoObs_5.file", "ExoObs_10.file",
                   "ExoObs_6.file", "ExoObs_9.file", "ExoObs_8.file",
                   "ExoObs_4.file", "ExoObs_7.file", "ExoObs_2.file",
                   "ExoObs_1.file"]
}

print("UNSORTED OBSERVATIONS:")
for category, obs_list in observations.items():
    print(f"UNSORTED {category.upper()} OBSERVATIONS:")
    for index, observation in enumerate(obs_list):
        print(f"{index + 1}. {observation}")
    print("\n")

print("\nSORTED OBSERVATIONS:")
for category, obs_list in observations.items():
    sort_observations(obs_list)
    print(f"SORTED {category.upper()} OBSERVATIONS:")
    for index, sorted_observation in enumerate(obs_list):
        print(f"{index + 1}. {sorted_observation}")
    print("\n")
