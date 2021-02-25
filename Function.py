def my_function() :
    print("Hallo semua")

my_function()

# function with parameter
def halo(first_name, last_name) :
    print("halo "+ first_name + " " + last_name)

halo("Nana", "Karima")
halo('Raditya', 'Dika')
halo("Salamah", "Aqidah")

# function with default parameter
def hai(first_name, last_name='') :
    print('halo ' + first_name +' '+last_name)

hai('nana')

# function keyword parameter
def my_function2(child3, child2, child1) :
    print("the youngest child is " +child2)

#my_function2(child1 = "Emil", child2 = "Tobias", child3 = "linus")
my_function2("Emil", "Tobias", "linus")