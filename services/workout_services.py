from models.workout_exercise import Workout_exercise

##########################
# example of howe we might extract code 
###########################
def is_exercise_in_workout(exercise_id, workout_id):
    amount_of_times_in_workout = Workout_exercise.query.filter(Workout_exercise.exercise_id == exercise_id, Workout_exercise.workout_id == workout_id).count() 
    
    return amount_of_times_in_workout == 0

