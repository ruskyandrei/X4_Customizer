X4 Customizer 0.9.3
-----------------

Current status: functional, most features in place, but still in beta testing.

This tool will programatically apply a variety of user selected transforms to X4 game files, optionally pre-modded. Features include:

 * Integrated catalog read/write support.
 * Basic XML diff patch support.
 * Automatic detection and loading of enabled extensions.
 * Framework for developing modular, customizable transforms of varying complexity.
 * Transforms can dynamically read and alter game files, instead of being limited to static changes like standard extensions.
 * Transforms operate on a user's unique mixture of mods, and can easily be rerun after game patches or mod updates.
 * Changes are written to a new or specified extension.

This tool is available as platform portable Python source code (tested on 3.7 with the lxml package) or as a compiled executable for 64-bit Windows.

The control script:

  * This tool works by executing a user supplied python script specifying any system paths, settings, and desired transforms to run.

  * The key control script sections are:
    - "from X4_Customizer import *" to make all transform functions available.
    - Call Settings() to change paths and set non-default options.
    - Call a series of transforms.
    
  * The quickest way to set up the control script is to copy and edit the "input_scripts/User_Transforms_template.py" file, renaming it to "User_Transforms.py" for recognition by Launch_X4_Customizer.bat.

Usage for compiled releases:

  * "Launch_X4_Customizer.bat <optional path to control script>"
    - Call from the command line for full options (-h for help), or run directly to execute the default script at "input_scripts/User_Transforms.py".
  * "Clean_X4_Customizer.bat <optional path to control script>"
    - Removes files generated in a prior run of the given or default3 control script.

Usage for Python source code:

  * "python X4_Customizer\Main.py <optional path to control script>"
    - This is the primary entry function for the python source code.
    - Add the "-default_script" option to behave like the bat launcher.
    - Control scripts may freely use any python packages, instead of being limited to those included with the release.
  * "python X4_Customizer\Make_Documentation.py"
    - Generates updated documentation for this project, as markdown formatted files README.md and Documentation.md.
  * "python X4_Customizer\Make_Executable.py"
    - Generates a standalone executable and support files, placed in the bin folder. Requires the PyInstaller package be available. The executable will be created for the system it was generated on.
  * "python X4_Customizer\Make_Release.py"
    - Generates a zip file with all necessary binaries, source files, and example scripts for general release.


***

Example input file:

    '''
    Example for using the Customizer, setting a path to
    the X4 directory and running some simple transforms.
    '''
    
    # Import all transform functions.
    from X4_Customizer import *
    
    Settings(
        # Set the path to the X4 installation folder.
        path_to_x4_folder   = r'C:\Steam\SteamApps\common\X4 Foundations',
        # Set the path to the user documents folder.
        path_to_user_folder = r'C:\Users\charname\Documents\Egosoft\X4\12345678',
        # Switch output to be in the user documents folder.
        output_to_user_extensions = True,
        )
    
    # Reduce mass traffic and increase military jobs.
    Adjust_Job_Count(
        ('id','masstraffic', 0.5),
        ('tag','military', 2)
        )

***

Settings:


       This holds general settings and paths to control the customizer. Adjust these settings as needed prior to running the first transform, using direct writes to attributes.
   
       Settings may be updated directly individually, or as arguments to a call of the Settings object. Examples: Settings.path_to_x4_folder   = 'C:\...' Settings.path_to_user_folder = 'C:\...' Settings( path_to_x4_folder = 'C:\...', path_to_user_folder = 'C:\...')
   
       Attributes:
       * path_to_x4_folder
         - Path to the main x4 folder.
         - Defaults to HOMEDRIVE/"Steam/steamapps/common/X4 Foundations"
       * path_to_user_folder
         - Path to the folder where user files are located.
         - Should include config.xml, content.xml, etc.
         - Defaults to HOMEPATH/"Documents/Egosoft/X4" or a subfolder with an 8-digit name.
       * extension_name
         - String, name of the extension being generated.
         - Defaults to 'X4_Customizer'
       * output_to_user_extensions
         - Bool, if True then the generated extension holding output files will be under <path_to_user_folder/extensions>.
         - Defaults to False, writing to <path_to_x4_folder/extensions>
       * path_to_source_folder
         - Optional path to a source folder that holds high priority source files, which will be used instead of reading the x4 cat/dat files.
         - For use when running transforms on manually edited files.
         - Defaults to None
       * prefer_single_files
         - Bool, if True then loose files will be used before those in cat/dat files, otherwise cat/dat takes precedence.
         - Only applies within a single search location, eg. within an extension, within the source folder, or within the base X4 folder; a loose file in the source folder will still be used over those in the X4 folder regardless of setting.
         - Defaults to False
       * ignore_extensions
         - Bool, if True then extensions will be ignored, and files are only sourced from the source_folder or x4_folder.
         - Defaults to False
       * make_maximal_diffs
         - Bool, if True then generated xml diff patches will do the maximum full tree replacement instead of using the algorithm to find and patch only edited nodes.
         - Turn on to more easily view xml changes.
         - Defaults to False.
       * transform_log_file_name
         - String, name a text file to write transform output messages to; content depends on transforms run.
         - File is located in the output extension folder.
         - Defaults to 'transform_log.txt'
       * customizer_log_file_name
         - String, name a json file to write customizer log information to, including a list of files written.
         - File is located in the output extension folder.
         - Defaults to 'customizer_log.json'
       * disable_cleanup_and_writeback
         - Bool, if True then cleanup from a prior run and any final writes will be skipped.
         - For use when testing transforms without modifying files.
         - Defaults to False
       * log_source_paths
         - Bool, if True then the path for any source files read will be printed in the transform log.
         - Defaults to False
       * skip_all_transforms
         - Bool, if True all transforms will be skipped.
         - For use during cleaning mode.
         - Defaults to False
       * use_scipy_for_scaling_equations
         - Bool, if True then scipy will be used to optimize scaling equations, for smoother curves between the boundaries.
         - If False or scipy is not found, then a simple linear scaling will be used instead.
         - Defaults to True
       * show_scaling_plots
         - Bool, if True and matplotlib and numpy are available, any generated scaling equations will be plotted (and their x and y vectors printed for reference). Close the plot window manually to continue transform processing.
         - Primarily for development use.
         - Defaults to False
       * developer
         - Bool, if True then enable some behavior meant just for development, such as leaving exceptions uncaught.
         - Defaults to False
       * verbose
         - Bool, if True some extra status messages may be printed to the console.
         - Defaults to False
       * allow_path_error
         - Bool, if True and the x4 or user folder path looks wrong, the customizer will still attempt to run (with a warning).
         - Defaults to False
       * output_to_catalog
         - Bool, if True then the modified files will be written to a single cat/dat pair, otherwise they are written as loose files.
         - Defaults to False
       


***

Job Transforms:

 * Adjust_Job_Count

      Adjusts job ship counts using a multiplier, affecting all quota fields. Caller provided matching rules determine which jobs get adjusted. Resulting non-integer job counts are rounded, with a minimum of 1 unless the multiplier or original count were 0.
  
      * job_factors:
        - Tuples holding the matching rules and job count  multipliers, (match_key, match_value, multiplier).
        - The match_key is one of a select few fields from the job nodes, against which the match_value will be compared.
        - Multiplier is an int or float, how much to adjust the job count by.
        - If a job matches multiple entries, the first match is used.
        - Supported keys:
          - 'faction': The name of the category/faction.
          - 'tag'    : A possible value in the category/tags list.
          - 'id'     : Name of the job entry, partial matches supported.
          - '*'      : Wildcard, always matches, takes no match_value.
          - 'masstraffic' : Mass traffic ship, takes no match_value.
  
      Example: Adjust_Job_Count( ('id','masstraffic', 0.5), ('tag','military', 2), ('tag','miner', 1.5), ('faction','argon', 1.2), ('*', 1.1) )
      


***

Change Log:
 * 0.9
   - Initial version, after a long evening of adapting X3_Customizer for X4.
   - Added first transform, Adjust_Job_Count.
 * 0.9.1
   - Major framework development.
   - Settings overhauled for X4.
   - Source_Reader overhauled, now finds and pulls from extensions.
   - Xml diff patch support added for common operations, merging extensions and base files prior to transforms. Pending further debug.
 * 0.9.2
   - Fix for when the user content.xml isn't present.
 * 0.9.3
   - Major development of diff patch generation, now using close to minimal patch size instead of full tree replacement, plus related debug of the patch application code.
   - Framework largely feature complete, except for further debug.