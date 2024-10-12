import pandas as pd
# Extract the order of categories from the mappings DataFrame
def set_categorical_order(df, mappings, variables=[
        'Class', 'Frequency_of_Consuming_Vegetables', 'Number_of_Main_Meals_Daily',
        'Food_Intake_Between_Meals', 'Liquid_Intake_Daily', 
        'Schedule_Dedicated_to_Technology'
    ]):
        """
        Sets the categorical order for specified variables in a DataFrame based on a provided mapping DataFrame.

        Args:
            df (pandas.DataFrame): The DataFrame containing the variables to be ordered.
            mappings (pandas.DataFrame): A DataFrame containing the mapping information.
                                         It should have columns 'Variable', 'Value', 'Mapping', and 'Order'.
            variables (list): A list of variable names to set the categorical order for.

        Returns:
            None: The function modifies the input DataFrame `df` in place, setting the categorical order for specified variables.
        """
        def extract_order(mappings, variable):
            """
            Extracts the order of categories for a specified variable from the mappings DataFrame.

            Args:
                mappings (pandas.DataFrame): A DataFrame containing the mapping information.
                                             It should have columns 'Variable', 'Value', 'Mapping', and 'Order'.
                variable (str): The name of the variable to extract the order for.

            Returns:
                list: A list of categories in the specified order.
            """
            return mappings[mappings['Variable'] == variable].sort_values(by='Value')['Mapping'].tolist()

        for variable in variables:
            if variable + '_mapped' in df.columns:
                ordered_categories = extract_order(mappings, variable)
                df[variable + '_mapped'] = pd.Categorical(
                    df[variable + '_mapped'], 
                    categories=ordered_categories, 
                    ordered=True
                )

        return(df)
