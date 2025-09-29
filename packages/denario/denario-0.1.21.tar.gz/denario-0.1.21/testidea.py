from denario import Denario

den = Denario()

data_description = r"""
Generate your own data for studying harmonic oscillators
Constraints: 
- We are running only computational experiments in Python on a laptop. 
- The data should not take more than 3 minutes to generate. 
- The research project should not be on the data generation itself, but on some harmonic oscillator physics.  
"""

den.set_data_description(data_description = data_description)
den.show_data_description()

den.get_idea_fast()
