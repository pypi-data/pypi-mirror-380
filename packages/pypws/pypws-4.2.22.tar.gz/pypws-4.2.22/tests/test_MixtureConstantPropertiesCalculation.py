import os
import pathlib
import sys

# When running locally the environment variable PYPWS_RUN_LOCALLY needs to be set to True.
# Check if the environment variable is set
PYPWS_RUN_LOCALLY = os.getenv('PYPWS_RUN_LOCALLY')
if PYPWS_RUN_LOCALLY and PYPWS_RUN_LOCALLY.lower() == 'true':
    # Navigate to the PYPWS directory by searching upwards until it is found.
    current_dir = pathlib.Path(__file__).resolve()

    while current_dir.name.lower() != 'package':
        if current_dir.parent == current_dir:  # Check if the current directory is the root directory
            raise FileNotFoundError("The 'pypws' directory was not found in the path hierarchy.")
        current_dir = current_dir.parent

    # Insert the path to the pypws package into sys.path.
    sys.path.insert(0, f'{current_dir}')


from pypws.calculations import MixtureConstantPropertiesCalculation
from pypws.entities import Material, MaterialComponent, State
from pypws.enums import ResultCode


def test():

    # Set the material
    material = Material("NATURAL GAS", [MaterialComponent("METHANE", 0.85), MaterialComponent("ETHANE", 0.1), MaterialComponent("PROPANE", 0.05)], component_count = 3)

    # Create a mixture constant properties calculation using the material.
    mixture_constant_properties_calculation = MixtureConstantPropertiesCalculation(material)

    # Run the calculation
    print('Running mixture_constant_properties_calculation...')
    resultCode = mixture_constant_properties_calculation.run()

    # Print any messages.
    if len(mixture_constant_properties_calculation.messages) > 0:
        print('Messages:')
        for message in mixture_constant_properties_calculation.messages:
            print(message)

    if resultCode == ResultCode.SUCCESS:
        # check whether lower flammability limit is a number and not zero
        if not isinstance(mixture_constant_properties_calculation.mix_constant_prop_result.lower_flammability_limit, (int, float)) or mixture_constant_properties_calculation.mix_constant_prop_result.lower_flammability_limit == 0:
            assert False,f'Regression failed with mixture_constant_properties_calculation.mix_constant_prop_result.lower_flammability_limit = {mixture_constant_properties_calculation.mix_constant_prop_result.lower_flammability_limit}'
        
        # check whether upper flammability limit is a number and not zero
        if not isinstance(mixture_constant_properties_calculation.mix_constant_prop_result.upper_flammability_limit, (int, float)) or mixture_constant_properties_calculation.mix_constant_prop_result.upper_flammability_limit == 0:
            assert False,f'Regression failed with mixture_constant_properties_calculation.mix_constant_prop_result.upper_flammability_limit = {mixture_constant_properties_calculation.mix_constant_prop_result.upper_flammability_limit}'
        
        # check whether critical pressure is a number and not zero
        if not isinstance(mixture_constant_properties_calculation.mix_constant_prop_result.critical_pressure, (int, float)) or mixture_constant_properties_calculation.mix_constant_prop_result.critical_pressure == 0:
            assert False,f'Regression failed with mixture_constant_properties_calculation.mix_constant_prop_result.critical_pressure = {mixture_constant_properties_calculation.mix_constant_prop_result.critical_pressure}'
        
        # check whether critical temperature is a number and not zero
        if not isinstance(mixture_constant_properties_calculation.mix_constant_prop_result.critical_temperature, (int, float)) or mixture_constant_properties_calculation.mix_constant_prop_result.critical_temperature == 0:
            assert False,f'Regression failed with mixture_constant_properties_calculation.mix_constant_prop_result.critical_temperature = {mixture_constant_properties_calculation.mix_constant_prop_result.critical_temperature}'

        # check whether molecular weight is a number and not zero
        if not isinstance(mixture_constant_properties_calculation.mix_constant_prop_result.molecular_weight, (int, float)) or mixture_constant_properties_calculation.mix_constant_prop_result.molecular_weight == 0:
            assert False,f'Regression failed with mixture_constant_properties_calculation.mix_constant_prop_result.molecular_weight = {mixture_constant_properties_calculation.mix_constant_prop_result.molecular_weight}'
        
        # check whether bubble point is a number and not zero
        if not isinstance(mixture_constant_properties_calculation.mix_constant_prop_result.bubble_point, (int, float)) or mixture_constant_properties_calculation.mix_constant_prop_result.bubble_point == 0:
            assert False,f'Regression failed with mixture_constant_properties_calculation.mix_constant_prop_result.bubble_point = {mixture_constant_properties_calculation.mix_constant_prop_result.bubble_point}'

        print(f'SUCCESS: mixture_constant_properties_calculation ({mixture_constant_properties_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED mixture_constant_properties_calculation with result code {resultCode}'