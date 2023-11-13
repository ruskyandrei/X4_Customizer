'''
Change Log:
 * 0.9
   - Initial version, quick adaption of X3_Customizer for X4.
   - Added first transform, Adjust_Job_Count.
 * 0.9.1
   - Major framework development.
   - Settings overhauled for X4.
   - Source_Reader overhauled, now finds and pulls from extensions.
   - Xml diff patch support added for common operations, merging extensions
     and base files prior to transforms. Pending further debug.
 * 0.9.2
   - Fix for when the user content.xml isn't present.
 * 0.9.3
   - Major development of diff patch generation, now using close to
     minimal patch size instead of full tree replacement, plus
     related debug of the patch application code.
   - Framework largely feature complete, except for further debug.
 * 0.9.4
   - Applied various polish: documentation touchup, gathered misc
     file_manager functions into a class, etc.
   - Added dependency nodes to the output extension.
 * 0.10
   - Major reorganization, moving transforms into a separate Plugins
     package that holds runtime script imports.
   - Added utilities for simple cat operations.
   - Added Print_Weapon_Stats.
 * 0.10.1
   - Added workaround for a bug in x4 catalogs that sometimes use
     an incorrect empty file hash; also added an optional setting to
     allow hash mismatches to support otherwise problematic catalogs.
 * 0.10.2
   - Bug fix in cat unpacker.
 * 0.11
   - Added plugins Check_Extension, Check_All_Extensions.
   - Added passthrough argparse support, along with command line callable
     scripts for extension check and cat pack/unpack.
   - Swapped the default script from User_Transforms to Default_Script.
 * 0.11.1
   - Added support for case insensitive path matching, instead of
     requiring a match to the catalogs.
 * 1.0
   - Scattered framework refinements.
   - Added Adjust_Weapon_Damage.
   - Added Adjust_Weapon_Fire_Rate.
   - Added Adjust_Weapon_Range.
   - Added Adjust_Weapon_Shot_Speed.
   - Refined Print_Weapon_Stats further.
   - Refined matching rule format for Adjust_Job_Count.
 * 1.1
   - Worked around lxml performance issue with index based xpaths, to
     speed up diff patch verification.
   - Added Print_Ware_Stats.
   - Added Adjust_Ware_Prices.
   - Added Adjust_Ware_Price_Spread.
   - Added Adjust_Mission_Rewards.
 * 1.1.1
   - Bugfix for ambiguous xpaths that still require indexes, and cleaned
     up quotes to avoid nesting double quotes.
 * 1.2
   - Added the initial Gui, featuring: python syntax and plugin highlighter,
     documentation viewer, settings editor, script launcher, preliminary
     weapon info viewer; plus niceties like changing font, remembering
     layout, and processing on a background thread.
   - Some unfortunate file size bloat in the compiled version.
 * 1.3
   - Added the Live_Editor, an extension for supporting gui based hand
     editing of game files.
   - Gui refined further, and live editor support added.
   - Weapon tables updated for the live editor.
   - Swapped the release exe to run without a console, and fixed
     a bug when running from outside the main directory.
 * 1.3.1
   - Fix a couple small bugs that crept in.
 * 1.4
   - Added wares to the GUI live editor.
   - Support added in the GUI for changing a laser's bullet.
   - Used several tricks to accelerate wares.xml parsing (multithreading,
     xpath bypassing, etc.) to accelerate Print_Ware_Stats and GUI display.
   - Background work to reorganize gui code for easy tab expansion,
     and tab thread requests will now queue up for service.
   - Further development of the Live_Editor, supporting object tree
     views and dynamically updating inter-object references.
   - Various debugging.
 * 1.4.1
   - Fixed bug when changing paths in the gui.
   - Added Shields and Bullets tabs to the gui.
 * 1.5
   - Redesign of the gui Live_Editor tabs.
   - Added dynamic tab support: create, move, remove, restore.
   - Tabs will load game information automatically if paths are set up.
   - Added editing support for engines, scanners, storage, dockingbays.
   - Various other polish, mostly in the gui.
 * 1.6
   - Added support for basic ship editing.
   - Added a virtual file system tab to the gui.
   - Added file viewing tabs to the gui, with xml syntax highlighting
     and diff comparison output.
 * 1.6.1
   - Bug fixes for hidden tabs and a threading conflicts.
 * 1.6.2
   - Added coloring to the VFS tree view.
   - Added more fields for missile editing.
   - Bug fix for tabs forgetting order between sessions.
   - Swapped around inter-tab signalling and added more threading safety.
 * 1.7
   - Added multi-object table views to the gui object editor tabs.
 * 1.7.1
   - Fixed an issue with lxml find/findall not properly handling xpaths
     using indexes after predicates.
 * 1.8
   - Tested with the top 100 Nexus mods to guide various debug and
     refinement.
   - Added the Extensions tab to the gui, allowing viewing, enabling,
     disabling, and testing of extensions.
   - Added the Color_Text transform.
 * 1.8.1
   - Fixed a couple crash bugs when script or configuration tabs are hidden.
 * 1.9
   - Added Adjust_Ship_Speed.
   - Added Adjust_Mission_Reward_Mod_Chance.
   - Fixed a couple crash bugs.
 * 1.9.1
   - Replaced excess commas in csv files with semicolons.
   - Added a missing comma that cause index and extension folders to
     be ignored when looking for loose files.
   - Gui script window will now check for external changes to the script.
   - Script editor swapped to using tab and shift-tab for indentation.
 * 1.10
   - Added Gui option to save xml files from the VFS tab.
 * 1.11
   - Support all file types in the VFS viewer, with extract support.
 * 1.12
   - Fixed an xml diff bug and reduced warnings, so that the Split dlc
     loads cleanly.
   - Improved catalog unpack plugin's support for extensions.
   - Adjusted newline encoding of packed dat files to better match
     the egosoft tools.
 * 1.13
   - Added Scale_Sector_Size transform.
   - Added path_to_output_folder setting.
   - Added symlink resolution when determining if an extension is the current
     output target.
   - Removes empty folders when cleaning up files from a prior run.
   - Added safety check for a file already existing on an output path.
   - Minor bug fixes.
 * 1.14
   - Added wildcards to capture extension objects when listing weapons,
     shields, etc. in the gui editor.
   - Fixed bug in weapon rate of fire calc for burst weapons in the editor.
 * 1.15
   - Added Generate_Diff support, for auto diff generation between two files.
   - Improved diff patch support for comment nodes.
 * 1.15.1
   - Removed dependency on Settings paths when using Generate_Diff.
 * 1.15.2
   - Diff patcher now ignores namespaced attribute changes due to lack
     of support or necessity on x4 side.
   - Extension checker now better supports mods patching other mods.
 * 1.15.3
   - Tweaked Adjust_Job_Count to generally ignore subordinate counts, to avoid
     ship counts multiplying to very large numbers.
 * 1.16
   - Tweaked xpath generation to select more human pleasing attributes.
   - Added support for generating dummy sig files.
   - Added Remove_Sig_Errors exe transform.
 * 1.16.1
   - Improved handling of extensions with no defined id.
 * 1.17
   - Added High_Precision_Systemtime transform for code profiling.
   - Various refinements to Scale_Sector_Size.
   - Fixed gui crash bug when saving files before Settings path polishing.
 * 1.17.1
   - Fixed bug in generate_diffs that could miss files with just
     attribute changes.
 * 1.17.2
   - Performance optimizations for XML_Diff.Make_Patch, Find_Files, and gui VFS.
   - Improved quality of generate_diff output patches.
 * 1.18
   - Added support for forcing xpath attributes in generated diff patches.
   - Added transforms: Increase_AI_Script_Waits, Adjust_OOS_Damage, 
     Adjust_Ship_Turning, Adjust_Ship_Hull, Adjust_Ship_Crew_Capacity,
     Adjust_Ship_Drone_Storage, Adjust_Ship_Missile_Storage.
 * 1.18.1
   - Bug fix when forced xpath attributes not specified.
   - Bug fixed when copying files at the path_to_source_folder.
 * 1.18.2
   - Changed user folder check to look for uidata.xml instead of config.xml.
   - Added support for 0001.xml language files. Text lookups should now
     be done through File_System.Read_Text.
   - Added better support for XR ship pack file naming and quirks.
   - Refinements to Scale_Sector_Size size estimation of sectors.
 * 1.18.3
   - Improved support for extensions patching other extensions.
   - Added better support for VRO quirks.
 * 1.18.4
   - Tweaked Generate_Diffs script mixed file/folder error check.
 * 1.18.5
   - Teaked Cat_Pack to include "extensions" subfolder files.
 * 1.19
   - Added forced xpath attribute support for matching child nodes and
     attributes.
   - New parameters for Scale_Sector_Size.
   - Changed parameters for Increase_AI_Script_Waits to support also scaling
     in-vision waits.
   - Added transforms: Rescale_Ship_Speeds, Remove_Engine_Travel_Bonus,
     Rebalance_Engines, Adjust_Engine_Boost_Duration, Adjust_Engine_Boost_Speed.
   - Added several example scripts.
 * 1.20
   - Added automatic packing of replacement files into subst cat/dats.
   - Scale_Sector_Size includes split start locations.
   - Switched Rescale_Ship_Speeds to handle multiple groups in one call.
   - Added Adjust_Ship_Cargo_Capacity.
   - Switched weapon transforms to new style match rule args.
   - Changed engine scaline transforms to adjust additional boost/thrust
     speed over normal speed, instead of total boost/thrust speed.
 * 1.21
   - Added gui tab close button. Can be disabled in settings.
   - Set shader files to go into a subst catalog.
   - Added automatic ship storage capacity adjustment to Rescale_Ship_Speeds
     and Rebalance_Engines for traders and miners.
 * 1.22
   - Added Settings.root_file_tag.
   - Adjusted cat unpacker to no longer treat egosoft's bad empty file hashes
     as changed files.
   - Updates to content.xml generation, and support for updating an existing
     content file with new dependencies.
 * 1.23
   - Added extension_whitelist and extension_blacklist settings to control
     which extensions are loaded by the customizer.
   - Fixed content.xml not being generated, introduced by 1.22.
 * 1.23.1
   - Added python configparser module to the packaged customizer.
 * 1.24
   - Added Enable_Windows_File_Cache exe transform (experimental).
   - Refinements to Check_Extensions and extension error handling.
   - Added basic diff patch support for xpaths in parentheses.
 * 1.24.1
   - More consistent lowercasing of file paths for better linux support.
 * 1.24.2
   - Stopped content.xml being packed in a catalog when output_to_catalog
     is enabled.
 * 1.24.3
   - Suppressed error check on SV/CoH dlcs for duplicate background jpgs.
   - Added shader files to default Cat_Unpack.
 * 1.24.4
   - Updated Remove_Sig_Errors for x4 4.0.
   - Removed Enable_Windows_File_Cache, no longer applies to x4 4.0.
   - Various minor fixes for CoH.
 * 1.24.5
   - Bug fix for transforms ignoring other extension diff changes.
 * 1.24.6
   - Bug fix for Get_Ship_Macros only returning drones.
 * 1.24.7
   - Updated Make_Extension_Content_XML list of language t file ids.
 * 1.24.8
   - Ignore error when a ship's loadout engine macro is not found (occurs for
     base game ships that use dlc engine loadouts).
   - Fixed error in Rescale_Ship_Speeds when adjusting variation in
     a ship group with only one ship.
 * 1.24.9
   - Added the "shorten_xpaths" setting, allowing generated xpaths to use
     a // prefix.
 * 1.24.10
   - Removed warning for duplicate xac file paths (common in dlcs).
   - Removed warnings on classless macros (common in dlcs).
   - Check_Extension will only check xml files.
'''
# Note: changes moved here for organization, and to make them easier to
# break out during documentation generation.
# TODO: convert this change_log to a standalone md file.

def Get_Version():
    '''
    Returns the highest version number in the change log,
    as a string, eg. '3.4.1'.
    '''
    # Traverse the docstring, looking for ' *' lines, and keep recording
    #  strings as they are seen.
    version = ''
    for line in __doc__.splitlines():
        if not line.startswith(' *'):
            continue
        version = line.split('*')[1].strip()
    return version
