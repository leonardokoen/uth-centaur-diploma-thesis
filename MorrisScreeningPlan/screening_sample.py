from modify_input_template import *
from settings import *
from SALib.sample import morris

#Fix broken -> 5.2, quantity -> 2500, loadingOrder -> 1

#   The function is used to filter plans that have big frequency differences.
def max_difference(counts):
    diff = []
    for i in range(0, len(counts)):
        for j in range(0, len(counts)):
            if i == j :
                continue
            else:
                diff.append(abs(counts[i] - counts[j]))
    return max(diff)

# The function is used to filter plans that favor bigger middle values.
def middle_values_minimum(counts):
    tmp = min(counts)
    index = np.where(counts == tmp)[0]
    # if len(index) > 1:
    if (int(len(counts)/2) in index) or ((int(len(counts)/2) - 1) in index):
        return False
    else:
        return True

# Search for a plan that satisfies my filters.
def filtered_plan(num_of_iterations, problem, filter_distance, N, num_levels, optimal_trajectories):
    print("Trying to find a uniform plan...")
    for i in range(0, num_of_iterations):

        screening_plan = morris.sample(problem = problem, N = N, num_levels = num_levels, optimal_trajectories=optimal_trajectories)
        temp_values , temp_counts = np.unique(screening_plan[:,0], return_counts=True)
        mc_values , mc_counts = np.unique(screening_plan[:,1], return_counts=True)
        damage_values , damage_counts = np.unique(screening_plan[:,2], return_counts=True)
        fermented_values , fermented_counts = np.unique(screening_plan[:,3], return_counts=True)


        max_temp = max_difference(temp_counts)
        max_mc = max_difference(mc_counts)
        max_damage = max_difference(damage_counts)
        max_fermented = max_difference(fermented_counts)

        

        if middle_values_minimum(temp_counts) and middle_values_minimum(mc_counts) and middle_values_minimum(damage_counts) and middle_values_minimum(fermented_counts):
            if max_temp <= filter_distance and max_mc <= filter_distance and max_damage <= filter_distance and max_fermented <= filter_distance:

                print("Found a plan")
                temp_array = np.column_stack((np.ones(screening_plan.shape[0]),2500*np.ones(screening_plan.shape[0])))
                screening_plan = np.column_stack((temp_array, screening_plan))
                screening_plan = np.column_stack((screening_plan, 68.9*np.ones(screening_plan.shape[0])))
                screening_plan = np.hstack((screening_plan[:,:4], 5.2*np.ones(screening_plan.shape[0]).reshape(screening_plan.shape[0],1), screening_plan[:,4:]))
                return screening_plan
                 
    print("Did not find a plan. Try again or Change Restrictions.")
    return np.zeros(screening_plan.shape)


def main():

    plan = filtered_plan(NUM_OF_ITERATIONS, PROBLEM, filter_distance = FILTER_DISTANCE, N = NUM_OF_TRAJECTORIES +1 , num_levels = LEVEL_OF_DESCRITIZATION, optimal_trajectories = NUM_OF_TRAJECTORIES)
    if plan.all() == 0:
        return
    else: 
        #Save plan to json files and csv format.
        screening_to_json(plan, TEMPLATE_FILE, JSON_FOLDER_PATH, WIPE)
        screening_to_csv(plan, CSV_FILE)
        return


if __name__ == "__main__":
    main()

