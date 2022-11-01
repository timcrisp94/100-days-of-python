# functions with outputs
def format_name(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name"""
  if f_name == "" or l_name == "":
    return "You did not provide valid input"
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  
  return f"{formatted_f_name} {formatted_l_name}"

format_name()

"""
don't 
do
multi
line
comments
like
this
"""