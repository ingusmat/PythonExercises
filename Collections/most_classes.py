__author__ = 'matthewburleson'

# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

def most_classes(class_sets):
    max_count = 0
    current_lead = ''
    for teacher, classlist in class_sets.items():
        if len(classlist) > max_count:
            max_count = len(classlist)
            current_lead = teacher

    return current_lead


def num_teachers(class_sets):
    return len(class_sets)


def stats(class_sets):
    stat_set = []
    for teacher, classlist in class_sets.items():
        stat_set.append([teacher, len(classlist)])
    return stat_set


def courses(class_sets):
    course_list = []
    for teacher, classlist in class_sets.items():
        for course in classlist:
            if course not in course_list:
                course_list.append(course)

    return course_list



class_sets = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
            'Kenneth Love': ['Python Basics', 'Python Collections']}

print(most_classes(class_sets))
print(num_teachers(class_sets))
print(stats(class_sets))
print(courses(class_sets))
