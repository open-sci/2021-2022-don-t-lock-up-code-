from src.OC import csv_manager
import pandas as pd
import os
from glob import glob

pd.options.mode.chained_assignment = None

'''
|--------------------------------------------------------------------------
| DESCRIPTION
|--------------------------------------------------------------------------

REQUIRED SCRIPT: /

'''

if __name__ == '__main__':
    '''
    |--------------------------------------------------------------------------
    | INPUT VARIABLES
    |--------------------------------------------------------------------------
    '''

    path_to_I_O_repo = os.path.join('..', os.getenv('output_directory'), 'OC', 'group_by_year')
    path_to_journals_description_file = os.path.join('..', os.getenv('output_directory'), 'DOAJ', 'doi.json')
    all_csv_normal = glob(os.path.join(path_to_I_O_repo, 'normal', '*.csv'))
    all_csv_byJournal = glob(os.path.join(path_to_I_O_repo, 'by_journal', '*.csv'))
    all_csv_null = glob(os.path.join('..', os.getenv('output_directory'), 'errors', 'null', '*.csv'))
    all_csv_wrong = glob(os.path.join('..', os.getenv('output_directory'), 'errors', 'wrong', '*.csv'))

    '''
    |--------------------------------------------------------------------------
    | LOAD
    |--------------------------------------------------------------------------
    '''

    df_journals_description = pd.read_json(path_to_journals_description_file, orient="index")

    '''
    |--------------------------------------------------------------------------
    | EXECUTION
    |--------------------------------------------------------------------------
    '''
    # concat normal csv
    df_normal = csv_manager.concat_csv_normal(all_csv_normal)
    # concat by_journal csv
    df_by_journal = csv_manager.concat_csv_journal(all_csv_byJournal)

    # add journal information
    df_by_journal = csv_manager.add_to_journals_DOAJ_descriptions(df_by_journal, df_journals_description)

    # concat errors csv
    df_null = csv_manager.concat_csv(all_csv_null)

    df_wrong = csv_manager.concat_csv(all_csv_wrong)

    '''
    |--------------------------------------------------------------------------
    | SAVE
    |--------------------------------------------------------------------------
    '''

    df_normal = df_normal.to_json(os.path.join(path_to_I_O_repo, 'normal.json'), orient="records")

    df_by_journal.to_json(os.path.join(path_to_I_O_repo, 'by_journal.json'), orient="records")

    df_null.to_json(os.path.join('..', os.getenv('output_directory'), 'errors', 'null.json'), orient="records")

    df_wrong.to_json(os.path.join('..', os.getenv('output_directory'), 'errors', 'wrong.json'), orient="records")